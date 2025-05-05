import { Message } from 'whatsapp-web.js';
import { userStates, userData } from '@core/stateManager';
import { isYes, isNo } from '@utils/respostaBooleana';
import { validarCPF } from '@utils/validarCPF';
import { segmentarFan } from '@core/segmentarFan';
import { publishToQueue } from '@queue/rabbitMQ';

async function safeReply(message: Message, text: string) {
  try {
    const chat = await message.getChat();
    await chat.sendMessage(text);
  } catch (err) {
    if (err instanceof Error) {
      console.error('❌ Erro ao enviar mensagem:', err.message);
    } else {
      console.error('❌ Erro desconhecido ao enviar mensagem:', err);
    }
  }
}

export async function handleMessage(message: Message) {
  const userId = message.from;
  const now = Date.now();

  // Timeout removido
  // userLastSeen.set(userId, now);

  const text = message.body.toLowerCase().trim();

  if (text === 'reiniciar') {
    userStates.set(userId, 'inicio');
    userData.delete(userId);
    await safeReply(message, '🔄 Cadastro reiniciado! Envie "oi" para começarmos novamente.');
    return;
  }

  const currentState = userStates.get(userId) || 'inicio';
  console.log(`📨 Estado atual de ${userId}: ${currentState}`);

  switch (currentState) {
    case 'inicio':
      await safeReply(message, '🐺 Olá! Que bom te ver por aqui!\nQuer criar seu perfil de fã da FURIA e ficar por dentro das novidades? (Responda com *Sim* ou *Não*)');
      userStates.set(userId, 'consentimento');
      break;

    case 'consentimento':
      if (isYes(text)) {
        await safeReply(message, '🔐 Antes de continuar, precisamos da sua permissão pra salvar suas informações com segurança, ok?\nVocê concorda com nossa política de dados? (Sim/Não)');
        userStates.set(userId, 'aguardando_consentimento');
      } else if (isNo(text)) {
        await safeReply(message, 'Sem problemas! Até a próxima. 💜');
        userStates.delete(userId);
      }
      break;

    case 'aguardando_consentimento':
      if (isYes(text)) {
        await safeReply(message, '👤 Show! Vamos começar. Qual é o seu nome completo?');
        userStates.set(userId, 'perguntando_nome');
      } else if (isNo(text)) {
        await safeReply(message, 'Tudo certo! Não armazenaremos nada. Até mais! 👋');
        userStates.delete(userId);
      }
      break;

    case 'perguntando_nome':
      if (text.length > 2) {
        userData.set(userId, { nome: text });
        await safeReply(message, '🏙️ Massa! E de qual cidade você fala?');
        await publishToQueue('fan.interacao', {
          whatsapp_number: userId,
          question: 'Qual é o seu nome completo?',
          answer: text
        });
        userStates.set(userId, 'perguntando_cidade');
      } else {
        await safeReply(message, '🤔 Parece que o nome está muito curtinho. Pode mandar seu nome completo?');
      }
      break;

    case 'perguntando_cidade':
      if (text.length > 2) {
        try {
          const response = await fetch('https://servicodados.ibge.gov.br/api/v1/localidades/municipios');
          const cidades = await response.json();
          const lista = cidades.map((c: any) => c.nome.toLowerCase());
          if (lista.includes(text.toLowerCase())) {
            const current = userData.get(userId) || {};
            userData.set(userId, { ...current, cidade: text });
            await safeReply(message, '🔍 Agora, pra liberar benefícios exclusivos no futuro, você gostaria de informar seu CPF?\n(Se preferir não informar, é só digitar *pular*)');
            await publishToQueue('fan.interacao', {
              whatsapp_number: userId,
              question: 'De qual cidade você fala?',
              answer: text
            });
            userStates.set(userId, 'perguntando_cpf');
          } else {
            await safeReply(message, '🤔 Não encontrei essa cidade no Brasil. Pode verificar a grafia e tentar de novo?');
          }
        } catch (error) {
          await safeReply(message, '⚠️ Ocorreu um erro ao validar sua cidade. Tente novamente em instantes.');
        }
      } else {
        await safeReply(message, '🌍 Ops! Preciso do nome completo da sua cidade pra te localizar no mapa da FURIA!');
      }
      break;

    case 'perguntando_cpf':
      if (text === 'pular') {
        const current = userData.get(userId) || {};
        userData.set(userId, { ...current, cpf: null });
        await safeReply(message, 'Sem problemas! 🎮 Quer receber alertas sempre que a FURIA entrar em ação? (Sim/Não)');
        await publishToQueue('fan.interacao', {
          whatsapp_number: userId,
          question: 'Você gostaria de informar seu CPF?',
          answer: 'pular'
        });
        userStates.set(userId, 'optin_jogos');
      } else if (/^\d{11}$/.test(text)) {
        const cpfValido = validarCPF(text);
        if (cpfValido) {
          const current = userData.get(userId) || {};
          userData.set(userId, { ...current, cpf: text });
          await safeReply(message, '✅ CPF ok! Agora vamos pra parte divertida.\n🎮 Quer receber alertas sempre que a FURIA entrar em ação? (Sim/Não)');
          await publishToQueue('fan.interacao', {
            whatsapp_number: userId,
            question: 'Você gostaria de informar seu CPF?',
            answer: text
          });
          userStates.set(userId, 'optin_jogos');
        } else {
          await safeReply(message, '😕 Esse CPF não parece válido. Pode revisar e enviar de novo?\nOu, se quiser seguir sem, digite *pular*.');
        }
      } else {
        await safeReply(message, 'Opa! CPF deve ter 11 dígitos, só números.\nOu escreva *pular* pra continuar sem ele.');
      }
      break;

    case 'optin_jogos':
      if (isYes(text) || isNo(text)) {
        const current = userData.get(userId) || {};
        userData.set(userId, { ...current, optinJogos: isYes(text) });
        await safeReply(message, '💥 E que tal promoções exclusivas e novidades da FURIA? Mando pra você? (Sim/Não)');
        await publishToQueue('fan.interacao', {
          whatsapp_number: userId,
          question: 'Quer receber alertas?',
          answer: text
        });
        userStates.set(userId, 'optin_promocoes');
      } else {
        await safeReply(message, 'Por favor, responda apenas com "Sim" ou "Não". Deseja receber alertas sobre jogos?');
      }
      break;

    case 'optin_promocoes':
      if (isYes(text) || isNo(text)) {
        const current = userData.get(userId) || {};
        userData.set(userId, { ...current, optinPromocoes: isYes(text) });

        const jogosTexto = current.optinJogos ? 'Sim' : 'Não';
        const promocoesTexto = isYes(text) ? 'Sim' : 'Não';
        const resumo = `📋 Confere aí se está tudo certo:\n\n👤 Nome: ${current.nome}\n🏙️ Cidade: ${current.cidade}\n📄 CPF: ${current.cpf ? 'Informado' : 'Não informado'}\n🎮 Alertas de jogos: ${jogosTexto}\n💥 Promoções: ${promocoesTexto}\n\nPosso concluir o cadastro? (Sim/Editar)`;

        await safeReply(message, resumo);
        await publishToQueue('fan.interacao', {
          whatsapp_number: userId,
          question: 'Deseja receber promoções?',
          answer: text
        });
        userStates.set(userId, 'confirmacao_final');
      } else {
        await safeReply(message, 'Por favor, responda apenas com "Sim" ou "Não". Deseja receber promoções?');
      }
      break;

    case 'confirmacao_final':
      await publishToQueue('fan.interacao', {
        whatsapp_number: userId,
        question: 'Confirma os dados e deseja concluir?',
        answer: text
      });
      if (isYes(text)) {
        const current = userData.get(userId);
        if (current) {
          await publishToQueue('fan.cadastro_finalizado', {
            whatsapp_number: userId,
            nome: current.nome,
            cidade: current.cidade,
            cpf: current.cpf,
            optinJogos: current.optinJogos,
            optinPromocoes: current.optinPromocoes
          });
          await segmentarFan(userId, current);
        }

        await safeReply(message, '🏁 Tudo certo! Seu perfil foi criado com sucesso.\nObrigado por fazer parte da matilha, torcedor(a)! 💜🐺');
        userStates.delete(userId);
        userData.delete(userId);
      } else {
        await safeReply(message, '🔄 Tudo bem! Se quiser reiniciar, digite "reiniciar".');
      }
      break;

    default:
      console.log(`❓ Comando não reconhecido. Resetando estado.`);
      await safeReply(message, 'Desculpe, não entendi. Pode repetir?');
      userStates.set(userId, 'inicio');
  }
}
