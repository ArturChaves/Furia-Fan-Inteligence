import { handleMessage } from '@app/handleMessage';

jest.mock('@core/prisma', () => ({
  prisma: {
    interacao: { create: jest.fn() },
    fan: { upsert: jest.fn() },
    fanSegment: { create: jest.fn() }
  }
}));

jest.mock('@queue/rabbitMQ', () => ({ publishToQueue: jest.fn() }));
jest.mock('@core/segmentarFan', () => ({ segmentarFan: jest.fn() }));

// ✅ Mock adicional obrigatório
jest.mock('@core/registrarInteracao', () => ({
  registrarInteracao: jest.fn()
}));

jest.mock('@core/stateManager', () => {
  const state = new Map();
  const data = new Map();
  const seen = new Map();
  return {
    userStates: state,
    userData: data,
    userLastSeen: seen,
    TIMEOUT_MINUTES: 10,
  };
});

const sendMessage = jest.fn();
const mockMessage = (body: string) =>
  ({
    from: '123456789',
    body,
    getChat: jest.fn().mockResolvedValue({ sendMessage }),
  } as any);

describe('handleMessage - fluxo completo do chatbot', () => {
  let prisma: any;

  beforeEach(() => {
    jest.clearAllMocks();
    prisma = require('@core/prisma').prisma;
    const { userStates, userData, userLastSeen } = require('@core/stateManager');
    userStates.clear();
    userData.clear();
    userLastSeen.clear();
  });

  test('inicia com estado "inicio"', async () => {
    const { userStates } = require('@core/stateManager');
    userStates.set('123456789', 'inicio');
    await handleMessage(mockMessage('sim'));
    expect(sendMessage).toHaveBeenCalledWith(expect.stringContaining('Quer criar seu perfil'));
    expect(userStates.get('123456789')).toBe('consentimento');
  });

  test('consentimento com "sim"', async () => {
    const { userStates } = require('@core/stateManager');
    userStates.set('123456789', 'consentimento');
    await handleMessage(mockMessage('sim'));
    expect(sendMessage).toHaveBeenCalledWith(expect.stringContaining('Você concorda'));
    expect(userStates.get('123456789')).toBe('aguardando_consentimento');
  });

  test('confirma LGPD com "sim"', async () => {
    const { userStates } = require('@core/stateManager');
    userStates.set('123456789', 'aguardando_consentimento');
    await handleMessage(mockMessage('sim'));
    expect(sendMessage).toHaveBeenCalledWith(expect.stringContaining('Qual é o seu nome'));
    expect(userStates.get('123456789')).toBe('perguntando_nome');
  });

  test('define nome e avança para cidade', async () => {
    const { userStates, userData } = require('@core/stateManager');
    userStates.set('123456789', 'perguntando_nome');
    await handleMessage(mockMessage('Artur Chaves'));
    expect(userData.get('123456789')?.nome).toBe('artur chaves');
    expect(userStates.get('123456789')).toBe('perguntando_cidade');
  });

  test('pula CPF e vai para optin_jogos', async () => {
    const { userStates, userData } = require('@core/stateManager');
    userStates.set('123456789', 'perguntando_cpf');
    userData.set('123456789', {});
    await handleMessage(mockMessage('pular'));
    expect(userData.get('123456789')?.cpf).toBeNull();
    expect(userStates.get('123456789')).toBe('optin_jogos');
  });

  test('responde optin_jogos com "sim"', async () => {
    const { userStates, userData } = require('@core/stateManager');
    userStates.set('123456789', 'optin_jogos');
    userData.set('123456789', {});
    await handleMessage(mockMessage('sim'));
    expect(userData.get('123456789')?.optinJogos).toBe(true);
    expect(userStates.get('123456789')).toBe('optin_promocoes');
  });

  test('responde optin_promocoes com "sim"', async () => {
    const { userStates, userData } = require('@core/stateManager');
    userStates.set('123456789', 'optin_promocoes');
    userData.set('123456789', {
      nome: 'Artur',
      cidade: 'São Paulo',
      cpf: '12345678900',
      optinJogos: true,
    });
    await handleMessage(mockMessage('sim'));
    expect(sendMessage).toHaveBeenCalledWith(expect.stringContaining('Confere aí'));
    expect(userStates.get('123456789')).toBe('confirmacao_final');
  });

  test('finaliza cadastro com sucesso', async () => {
    const { userStates, userData } = require('@core/stateManager');
    userStates.set('123456789', 'confirmacao_final');
    userData.set('123456789', {
      nome: 'Artur',
      cidade: 'São Paulo',
      cpf: '12345678900',
      optinJogos: true,
      optinPromocoes: true,
    });
    await handleMessage(mockMessage('sim'));
    expect(prisma.fan.upsert).toHaveBeenCalled();
    expect(userStates.get('123456789')).toBeUndefined();
    expect(userData.get('123456789')).toBeUndefined();
  });
});