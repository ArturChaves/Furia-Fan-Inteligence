

import { FanData } from '../domain/fanData';

export const userStates = new Map<string, string>();
export const userData = new Map<string, FanData>();
export const userLastSeen = new Map<string, number>();

export const TIMEOUT_MINUTES = 5;

export function resetSession(userId: string) {
  userStates.set(userId, 'inicio');
  userData.delete(userId);
  userLastSeen.delete(userId);
}

export function isSessionExpired(userId: string): boolean {
  const lastSeen = userLastSeen.get(userId);
  if (!lastSeen) return false;
  const now = Date.now();
  return now - lastSeen > TIMEOUT_MINUTES * 60 * 1000;
}

export function updateLastSeen(userId: string) {
  userLastSeen.set(userId, Date.now());
}