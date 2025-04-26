<script setup>
import Header from './components/Header.vue';
import ChatBotField from './components/ChatBotField.vue';
import ShowResults from './components/ShowResults.vue';
import Footer from './components/Footer.vue'; 
import SkillLevel from './components/SkillLevel.vue';
</script>

<template>
  <div class="container">

    <div id="one"><Header/></div>
    <div id="two"><ChatBotField/></div>
    <div id="three"><SkillLevel/></div>
    <div id="four"><ShowResults/></div>
    <div id="five"><Footer/></div>

  </div>

</template>

<style scoped>

.container { 
  display: grid; 
  grid-template-columns:  1fr 1.25fr;  
  grid-template-rows: auto auto 1fr auto;
  gap: 10px; 
  grid-template-areas: 'header header' 
                       'chatbotfield skilllevel' 
                       'showresults skilllevel' 
                       'footer footer'; 
                       height: 100vh;
  padding: 0px; 
  box-sizing: border-box; /* Include padding in height */                  
}

.container > div { 
  font-size: 20px; 
  padding: 10px;
}   
#one { 
  grid-area: header; 
} 
#two { 
 grid-area: chatbotfield; 
}
#three { 
  grid-area: skilllevel; 
}     
#four { 
  grid-area: showresults; 
} 
#five { 
  grid-area: footer; 
  padding-left: 0;
  padding-right: 0;
  padding-bottom: 0;
  padding-top: 10px;
}    

body {
  margin: 0;
}

input{
  border: 0;
  border-radius: 8px;
  width: 100%;
  height: 30px;
}

/* For larger screens */
/* @media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

} */
</style>
