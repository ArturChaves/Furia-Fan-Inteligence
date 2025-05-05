import { isYes, isNo } from '@utils/respostaBooleana';

describe('respostaBooleana', () => {
  describe('isYes', () => {
    it('deve reconhecer variações de sim', () => {
      expect(isYes('sim')).toBe(true);
      expect(isYes('Sim')).toBe(true);
      expect(isYes('S')).toBe(true);
      expect(isYes('s')).toBe(true);
      expect(isYes('claro')).toBe(true);
    });

    it('deve retornar false para respostas negativas ou indefinidas', () => {
      expect(isYes('não')).toBe(false);
      expect(isYes('n')).toBe(false);
      expect(isYes('talvez')).toBe(false);
      expect(isYes('')).toBe(false);
    });
  });

  describe('isNo', () => {
    it('deve reconhecer variações de não', () => {
      expect(isNo('não')).toBe(true);
      expect(isNo('Nao')).toBe(true);
      expect(isNo('n')).toBe(true);
      expect(isNo('N')).toBe(true);
    });

    it('deve retornar false para respostas positivas ou indefinidas', () => {
      expect(isNo('sim')).toBe(false);
      expect(isNo('s')).toBe(false);
      expect(isNo('talvez')).toBe(false);
      expect(isNo('')).toBe(false);
    });
  });
});
