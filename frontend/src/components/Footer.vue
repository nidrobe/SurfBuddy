<template>
  <footer>
    <div class="footer-content">
      <p>&copy; {{ currentYear }} Surf Buddy AI. All rights reserved.</p>
    </div>
  </footer>
</template>

<script>
  export default {
    name: 'Footer',
    data() {
    return {
      currentYear: new Date().getFullYear()
    };
  }
  }
</script>
  
<style scoped>

  
  footer {
  background-color: #1c3a57; 
  padding: 20px;
  text-align: center;
  font-size: 0.8em;
  color: #555;
}

.footer-content {
  max-width: 960px; /* Keep content within a reasonable width */
  margin: 0 auto;   /* Center the content */
  color: white;
}
</style>