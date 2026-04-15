/**
 * @module useTranslation
 * @description Composable that encapsulates translation state and logic.
 * Components depend only on this composable, not on the API layer directly.
 */

import { ref } from 'vue';
import { translateText } from '../api/translationApi.js';

/**
 * Provides reactive translation state and the translate action.
 *
 * @returns {{
 *   result: import('vue').Ref<string>,
 *   isLoading: import('vue').Ref<boolean>,
 *   error: import('vue').Ref<string>,
 *   translate: (text: string, mode: string) => Promise<void>
 * }}
 */
export function useTranslation() {
  const result = ref('');
  const isLoading = ref(false);
  const error = ref('');

  /**
   * Calls the translation API and updates reactive state.
   *
   * @param {string} text - The technical text to translate.
   * @param {string} mode - The explanation mode.
   */
  async function translate(text, mode) {
    isLoading.value = true;
    error.value = '';
    result.value = '';

    try {
      const data = await translateText(text, mode);
      result.value = data.translated_text;
    } catch (err) {
      error.value = err.message || 'An unexpected error occurred.';
    } finally {
      isLoading.value = false;
    }
  }

  return { result, isLoading, error, translate };
}
