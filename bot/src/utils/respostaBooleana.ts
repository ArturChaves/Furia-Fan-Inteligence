export function isYes(text: string): boolean {
    return ['sim', 's', 'simmm', 'claro', 'quero', 'bora'].includes(text.trim().toLowerCase());
  }
  
  export function isNo(text: string): boolean {
    return ['não', 'nao', 'n', 'obrigado', 'deixa', 'nah'].includes(text.trim().toLowerCase());
  }