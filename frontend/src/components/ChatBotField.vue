<template>
  <div id="chatbot-field">
    <div id="chat-messages">
      <div v-for="(message, index) in messages" :key="index" :class="'message ' + message.sender">
        {{ message.text }}
      </div>
    </div>
    <div class="input-area">
      <input type="text" v-model="userInput" @keyup.enter="sendMessage" placeholder="Type your message...">
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChatBotField',
  data() {
    return {
      messages: [],
      userInput: ''
    };
  },
  methods: {
    async sendMessage() {
      // (Your sendMessage logic here - same as before)
      if (this.userInput.trim() !== '') {
        this.messages.push({ text: this.userInput, sender: 'user' }); // Add user message

        try {
         // axios call
          this.messages.push({ text: "Reply From Backend/LLM", sender: 'ai' }); // Add AI response
        } catch (error) {
          console.error('Error sending message:', error);
          this.messages.push({ text: 'Error: Could not connect to the server.', sender: 'ai' });
        }

        this.userInput = ''; // Clear the input field
      }
    }
  }
};
</script>

<style scoped>
#chatbot-field {
  width: 400px; /* Adjust to your desired width */
  height: 350px; /* Adjust to your desired height */
  border: 1px solid #ccc;
  border-radius: 5px;
  overflow: hidden; /* Hide scrollbars if content exceeds height */
  display: flex;
  flex-direction: column;
}

#chat-messages {
  flex-grow: 1; /* Take up remaining vertical space */
  padding: 10px;
  overflow-y: auto; /* Enable vertical scrolling */
  background-color: #f9f9f9;
}

.message {
  padding: 8px 12px;
  margin-bottom: 5px;
  border-radius: 15px;
  max-width: 70%; /* Adjust to prevent long messages from overflowing */
  word-wrap: break-word; /* Break long words to prevent overflow */
}

.message.user {
  background-color: #7dabd6; /* Light green for user messages */
  align-self: flex-end; /* Align to the right */
}

.message.ai {
  background-color: #E5E5EA; /* Light gray for AI messages */
  align-self: flex-start; /* Align to the left */
}

.input-area {
  display: flex;
  padding: 10px;
  border-top: 1px solid #ccc;
}

.input-area input {
  flex-grow: 1;
  border: none;
  padding: 8px;
  border-radius: 15px;
  margin-right: 10px;
}

.input-area button {
  background-color: #1c3a57; /* Green */
  border: none;
  color: white;
  padding: 8px 16px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  border-radius: 15px;
  cursor: pointer;
}
</style>