

import { validarCPF } from '@utils/validarCPF';

describe('validarCPF', () => {
  it('deve retornar true para CPFs válidos (sem máscara)', () => {
    expect(validarCPF('52998224725')).toBe(true);
    expect(validarCPF('12345678909')).toBe(true);
  });

  it('deve retornar true para CPFs válidos (com máscara)', () => {
    expect(validarCPF('529.982.247-25')).toBe(true);
    expect(validarCPF('123.456.789-09')).toBe(true);
  });

  it('deve retornar false para CPFs inválidos', () => {
    expect(validarCPF('11111111111')).toBe(false);
    expect(validarCPF('00000000000')).toBe(false);
    expect(validarCPF('12345678900')).toBe(false);
    expect(validarCPF('abc.def.ghi-jk')).toBe(false);
    expect(validarCPF('123')).toBe(false);
    expect(validarCPF(null as any)).toBe(false);
    expect(validarCPF(undefined as any)).toBe(false);
  });
});