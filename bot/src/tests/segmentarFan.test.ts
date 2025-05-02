import { segmentarFan } from '@core/segmentarFan';
import { prisma } from '@core/prisma';
import { publishToQueue } from '@queue/rabbitMQ';

jest.mock('@core/prisma', () => ({
  prisma: {
    fanSegment: {
      create: jest.fn()
    }
  }
}));

jest.mock('@queue/rabbitMQ', () => ({
  publishToQueue: jest.fn()
}));

describe('segmentarFan', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('segmenta corretamente para cluster 1 (Engajado)', async () => {
    const fanData = {
      nome: 'Artur',
      cidade: 'São Paulo',
      cpf: '12345678900',
      optinJogos: true,
      optinPromocoes: true
    };

    await segmentarFan('user123', fanData);

    expect(prisma.fanSegment.create).toHaveBeenCalledWith({
      data: {
        cluster: 1,
        fan: {
          connect: {
            whatsapp_number: 'user123'
          }
        }
      }
    });

    expect(publishToQueue).toHaveBeenCalledWith('fan.segmentado', {
      whatsapp_number: 'user123',
      cluster: 1,
      label: 'Engajado'
    });
  });

  it('segmenta corretamente para cluster 4 (João - não se encaixa nas regras específicas)', async () => {
    const fanData = {
      nome: 'João',
      cidade: 'Rio de Janeiro',
      cpf: '12345678900',
      optinJogos: false,
      optinPromocoes: true
    };

    await segmentarFan('user456', fanData);

    expect(prisma.fanSegment.create).toHaveBeenCalledWith({
      data: {
        cluster: 4,
        fan: {
          connect: {
            whatsapp_number: 'user456'
          }
        }
      }
    });

    expect(publishToQueue).toHaveBeenCalledWith('fan.segmentado', {
      whatsapp_number: 'user456',
      cluster: 4,
      label: 'Outro'
    });
  });

  it('segmenta corretamente para cluster 4 (Maria - cpf presente)', async () => {
    const fanData = {
      nome: 'Maria',
      cidade: 'Curitiba',
      cpf: '12345678900',
      optinJogos: true,
      optinPromocoes: false
    };

    await segmentarFan('user789', fanData);

    expect(prisma.fanSegment.create).toHaveBeenCalledWith({
      data: {
        cluster: 4,
        fan: {
          connect: {
            whatsapp_number: 'user789'
          }
        }
      }
    });

    expect(publishToQueue).toHaveBeenCalledWith('fan.segmentado', {
      whatsapp_number: 'user789',
      cluster: 4,
      label: 'Outro'
    });
  });

  it('segmenta corretamente para cluster 2 (Lucas - sem cpf, sem opt-ins)', async () => {
    const fanData = {
      nome: 'Lucas',
      cidade: 'Fortaleza',
      cpf: null,
      optinJogos: false,
      optinPromocoes: false
    };

    await segmentarFan('user999', fanData);

    expect(prisma.fanSegment.create).toHaveBeenCalledWith({
      data: {
        cluster: 2,
        fan: {
          connect: {
            whatsapp_number: 'user999'
          }
        }
      }
    });

    expect(publishToQueue).toHaveBeenCalledWith('fan.segmentado', {
      whatsapp_number: 'user999',
      cluster: 2,
      label: 'Casual'
    });
  });
});