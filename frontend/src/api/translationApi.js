/**
 * @module translationApi
 * @description HTTP client for the translation backend API.
 * Responsible only for making requests and returning raw responses.
 */

const BASE_URL = 'http://localhost:8000';

/**
 * Sends a translation request to the backend.
 *
 * @param {string} text - The technical text to translate.
 * @param {string} mode - The explanation mode ('simple' | 'eli5' | 'professional' | 'analogies').
 * @returns {Promise<{translated_text: string}>} The parsed JSON response from the backend.
 * @throws {Error} If the network request fails or the server returns a non-OK status.
 */
export async function translateText(text, mode) {
  const response = await fetch(`${BASE_URL}/translate`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, mode }),
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || `Server error: ${response.status}`);
  }

  return response.json();
}
