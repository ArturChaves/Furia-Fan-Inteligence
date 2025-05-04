import { handleMessage } from '@app/handleMessage';
import { connectRabbitMQ, publishToQueue } from '@queue/rabbitMQ';

const numeroFake = '95229107@c.us'; // número do fan fake pra teste

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

// substitui setupFakeFan por envio direto para a fila, simulando a finalização de cadastro
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
  await enviarCadastroFake();  // usado no lugar do setupFakeFan()
  await rodarFluxoFake();
}

main().catch(console.error);