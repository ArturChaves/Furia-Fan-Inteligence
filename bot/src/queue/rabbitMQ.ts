import dotenv from 'dotenv';
dotenv.config();

import amqp from 'amqplib';

let channel: amqp.Channel;

export async function connectRabbitMQ() {
  try {
    const host = process.env.RABBITMQ_HOST;
    const port = process.env.RABBITMQ_PORT;
    const user = process.env.RABBITMQ_USER;
    const pass = process.env.RABBITMQ_PASSWORD;

    if (!host || !port || !user || !pass) {
      throw new Error('Variáveis de ambiente do RabbitMQ não definidas corretamente.');
    }

    const url = `amqp://${user}:${pass}@${host}:${port}`;
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