import { prisma } from './prisma';

export async function registrarInteracao(whatsapp_number: string, question: string, answer: string) {
  try {
    await prisma.interaction.create({
      data: {
        fan: {
          connect: { whatsapp_number },
        },
        question,
        answer,
      },
    });
  } catch (err) {
    console.error('❌ Erro ao registrar interação:', err);
  }
}