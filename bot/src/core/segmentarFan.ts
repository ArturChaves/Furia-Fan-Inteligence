import { prisma } from './prisma';
import { FanData } from '@domain/fanData';
import { publishToQueue } from '@queue/rabbitMQ';

export async function segmentarFan(userId: string, fan: FanData) {
  let cluster = 0;

  if (fan.optinJogos && fan.optinPromocoes) {
    cluster = 1;
  } else if (!fan.cpf && !fan.optinJogos && !fan.optinPromocoes) {
    cluster = 2;
  } else if (!fan.cpf && fan.optinPromocoes) {
    cluster = 3;
  } else {
    cluster = 4;
  }

  await prisma.fanSegment.create({
    data: {
      fan: { connect: { whatsapp_number: userId } },
      cluster,
    },
  });

  let label = '';
  if (cluster === 1) label = 'Engajado';
  else if (cluster === 2) label = 'Casual';
  else if (cluster === 3) label = 'Cuidadoso com marketing';
  else label = 'Outro';

  await publishToQueue('fan.segmentado', {
    whatsapp_number: userId,
    cluster,
    label,
  });
}