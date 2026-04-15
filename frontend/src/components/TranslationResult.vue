<!--
  TranslationResult.vue
  Responsible only for displaying translation output, loading state, and error messages.
  Receives all state as props — no business logic inside.
-->
<script setup>
/**
 * @prop {string} result - The translated text returned by the API.
 * @prop {boolean} isLoading - Whether a translation request is in progress.
 * @prop {string} error - An error message to display, if any.
 */
defineProps({
  result: { type: String, default: '' },
  isLoading: { type: Boolean, default: false },
  error: { type: String, default: '' },
});
</script>

<template>
  <div>
    <div v-if="isLoading" class="text-center py-4">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Traduciendo...</span>
      </div>
      <p class="mt-2 text-muted">Traduciendo...</p>
    </div>

    <div v-else-if="error" class="alert alert-danger" role="alert">
      <strong>Error:</strong> {{ error }}
    </div>

    <div v-else-if="result">
      <h5 class="fw-semibold mb-2">Resultado</h5>
      <div class="result-box p-3 border rounded bg-light">
        {{ result }}
      </div>
    </div>
  </div>
</template>

<style scoped>
.result-box {
  white-space: pre-wrap;
  line-height: 1.6;
}
</style>
