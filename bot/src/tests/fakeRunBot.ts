import { handleMessage } from '@app/handleMessage';
import { connectRabbitMQ, publishToQueue } from '@queue/rabbitMQ';

const numeroFake = '91219999999@c.us'; // número do fan fake pra teste

async function rodarFluxoFake() {
  const mockMsg = (body: string) =>
    ({
      from: numeroFake,
      body,
      getChat: async () => ({
        sendMessage: (msg: string) => console.log(`💬 Bot responderia: ${msg}`),
      }),
    } as any);

  const mensagens = [
    'sim', // início
    'sim', // consentimento
    'sim', // lgpd
    'teste', // nome
    'são paulo', // cidade
    'pular', // cpf
    'sim', // optin_jogos
    'sim', // optin_promocoes
    'sim'  // confirmação final
  ];

  for (const body of mensagens) {
    await handleMessage(mockMsg(body));
  }
}

async function enviarCadastroFake() {
  await publishToQueue('fan.cadastro_finalizado', {
    whatsapp_number: numeroFake,
    nome: 'Fake Tester',
    cidade: 'Teste',
    cpf: null,
    optinJogos: false,
    optinPromocoes: false
  });
  console.log('✅ Fan fake publicado na fila fan.cadastro_finalizado.');
}

async function main() {
  await connectRabbitMQ();

  // Espera curta para garantir que o canal esteja pronto (evita race condition)
  await new Promise((resolve) => setTimeout(resolve, 300));

  await enviarCadastroFake();
  await rodarFluxoFake();
}

main().catch(console.error);
