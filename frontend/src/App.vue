<!--
  App.vue
  Root component. Composes TranslatorForm and TranslationResult via the useTranslation composable.
  No business logic or API calls here.
-->
<script setup>
import TranslatorForm from './components/TranslatorForm.vue';
import TranslationResult from './components/TranslationResult.vue';
import { useTranslation } from './composables/useTranslation.js';

const { result, isLoading, error, translate } = useTranslation();

/**
 * Handles the form submit event and delegates to the composable.
 *
 * @param {{ text: string, mode: string }} payload
 */
function handleSubmit({ text, mode }) {
  translate(text, mode);
}
</script>

<template>
  <div class="container py-5" style="max-width: 720px">
    <h1 class="mb-1 fw-bold">AI Technical Translator</h1>
    <p class="text-muted mb-4">
      Convierte texto técnico complejo en lenguaje sencillo.
    </p>

    <div class="card shadow-sm mb-4">
      <div class="card-body">
        <TranslatorForm @submit="handleSubmit" />
      </div>
    </div>

    <TranslationResult
      :result="result"
      :is-loading="isLoading"
      :error="error"
    />
  </div>
</template>
