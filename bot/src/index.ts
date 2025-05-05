import { Client, LocalAuth } from 'whatsapp-web.js';
import { handleMessage } from '@app/handleMessage';
import { connectRabbitMQ } from '@queue/rabbitMQ';

const client = new Client({
  authStrategy: new LocalAuth(),
  puppeteer: { headless: false } // Para escanear o QR code no navegador
});

const AUTORIZADO = '5511987365509@c.us';

client.on('qr', (qr) => {
  console.log('📱 Escaneie o QR Code com seu WhatsApp:\n', qr);
});

client.on('ready', () => {
  console.log('🤖 Bot conectado e pronto para uso!');
});

client.on('message', async (message) => {
  console.log('📩 Mensagem recebida:', message.body);

  const isNew = (message as any).isNewMsg ?? true;
  console.log(`[DEBUG] from: ${message.from}`);
  console.log(`[DEBUG] isNewMsg:`, isNew);
  console.log(`[DEBUG] fromMe: ${message.fromMe}`);

  if (
    !message.fromMe &&
    isNew &&
    !message.from.includes('@g.us') &&
    message.from === AUTORIZADO
  ) {
    try {
      await handleMessage(message);
    } catch (err) {
      console.error('❌ Erro ao processar a mensagem:', err);
    }
  }
});

connectRabbitMQ();
client.initialize();
