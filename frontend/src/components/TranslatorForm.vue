<!--
  TranslatorForm.vue
  Responsible for capturing user input (text + mode) and emitting a submit event.
  Has no knowledge of the API or translation logic.
-->
<script setup>
import { ref } from 'vue';

/**
 * @emits submit - Emitted when the user clicks Translate.
 * @property {string} text - The text entered by the user.
 * @property {string} mode - The selected explanation mode.
 */
const emit = defineEmits(['submit']);

const text = ref('');
const mode = ref('simple');

const MODES = [
  { value: 'simple', label: 'Simple' },
  { value: 'eli5', label: 'ELI5 (Explícame como si tuviera 10 años)' },
  { value: 'professional', label: 'Profesional' },
  { value: 'analogies', label: 'Analogías' },
];

/** Validates input and emits the submit event. */
function handleSubmit() {
  if (!text.value.trim()) return;
  emit('submit', { text: text.value.trim(), mode: mode.value });
}
</script>

<template>
  <form @submit.prevent="handleSubmit">
    <div class="mb-3">
      <label for="input-text" class="form-label fw-semibold"
        >Texto técnico</label
      >
      <textarea
        id="input-text"
        v-model="text"
        class="form-control"
        rows="6"
        placeholder="Pega tu texto técnico aquí..."
        required
      />
    </div>

    <div class="mb-3">
      <label for="mode-select" class="form-label fw-semibold"
        >Modo de explicación</label
      >
      <select id="mode-select" v-model="mode" class="form-select">
        <option v-for="m in MODES" :key="m.value" :value="m.value">
          {{ m.label }}
        </option>
      </select>
    </div>

    <button type="submit" class="btn btn-primary w-100">Traducir</button>
  </form>
</template>
