<script setup>
import Introduction from './components/Introduction.vue';
import BeginnerIntermedidateAdvancedText from './components/BeginnerIntermediateAdvancedText.vue';
import ChatBotField from './components/ChatBotField.vue';

</script>

<template>
  <div class="app-container">
    <header>
      <h1>Surf Buddy</h1>
        <Introduction />
    </header>

    <main>
      <section class="chatbot-section">
         <ChatBotField />
      </section>

      <section class="skill-level-section">
         <BeginnerIntermedidateAdvancedText />
      </section>

    </main>
  </div>
</template>

<style scoped>
/* Apply general header styles */
.header {
  line-height: 1.5;
  display: flex; /* align items */
  align-items: center;
  justify-content: space-between; /* Distribute space evenly */
  padding: 1rem; /* Add some padding for spacing */
  background-color: #f0f0f0; /* Light background color */
}

h1 {
  font-size: 2rem; /* Increase font size */
  color: #333; /* Darken text color */
  margin: 0; /* Reset default margin */
}

/* For larger screens */
@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

}
</style>
