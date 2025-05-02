import amqp from 'amqplib';

let channel: amqp.Channel;

export async function connectRabbitMQ() {
  try {
    const url = process.env.RABBITMQ_URL;
    if (!url) throw new Error('RABBITMQ_URL não definida no .env');
    const connection = await amqp.connect(url);
    channel = await connection.createChannel();
    console.log('📡 Conectado ao RabbitMQ');
  } catch (error) {
    console.error('❌ Erro ao conectar ao RabbitMQ:', error);
  }
}

export async function publishToQueue(queue: string, message: object) {
  try {
    if (!channel) {
      throw new Error('Canal RabbitMQ não inicializado.');
    }
    await channel.assertQueue(queue, { durable: true });
    channel.sendToQueue(queue, Buffer.from(JSON.stringify(message)), {
      persistent: true,
    });
    console.log(`📤 Mensagem publicada na fila "${queue}"`, message);
  } catch (error) {
    console.error('❌ Erro ao publicar mensagem:', error);
  }
}
