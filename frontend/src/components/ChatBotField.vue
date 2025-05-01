<template>
  <div class="chatbot-field">
    <p>Chatfield</p>
    <button @click="sendTestRequest">Send Test Request</button>
    <p v-if="responseMessage">{{ responseMessage }}</p>  <!-- Display response -->
  </div>
</template>

<script>
import axios from 'axios';

  export default {
    name: 'ChatBotField',
    data() {
    return {
      responseMessage: null // Data property to store the response
    };
  },
  methods: {
    async sendTestRequest() {
      try {
        const accessToken = null // Intentionally set to null to test anonymous access
        let headers = {};

        if (accessToken) { // Only construct the headers if there's a valid token
          headers = {
            'Authorization': `Bearer ${accessToken}`
          };
        }
        const response = await axios.get('http://127.0.0.1:8000/api/test/', {
          headers: headers // Pass the headers object to axios
        });
        this.responseMessage = response.data.message; 
      } catch (error) {
        console.error('Error sending request:', error);
        this.responseMessage = 'Error connecting to the backend.'; // Display error
      }
    }
  }
  }
</script>
  
<style scoped>
  
  .chatbot-field {
    height: 240px;
    border: 1px solid rgb(0, 0, 0,0.2);
    padding: 8px;
    margin: 8px;
    color: rgba(0,0,0,0.8);
  }
</style>