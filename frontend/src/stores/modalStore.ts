import { writable } from 'svelte/store';

export const isModalOpen = writable(false);
export const modalContent = writable('');

export const dummyFn: () => void = () => {};
