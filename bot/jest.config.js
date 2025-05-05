/** @type {import('ts-jest').JestConfigWithTsJest} */
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/src'],
  moduleFileExtensions: ['ts', 'js', 'json'],
  transform: {
    '^.+\\.tsx?$': 'ts-jest',
  },
  moduleNameMapper: {
    '^@app/(.*)$': '<rootDir>/src/app/$1',
    '^@core/(.*)$': '<rootDir>/src/core/$1',
    '^@utils/(.*)$': '<rootDir>/src/utils/$1',
    '^@domain/(.*)$': '<rootDir>/src/domain/$1',
    '^@queue/(.*)$': '<rootDir>/src/queue/$1',
  },
  setupFilesAfterEnv: [],
};