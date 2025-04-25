<template>
  <div class="skilllevel-text">
    <div>
      <span class="firstline">Which Surf</span>
      <br>
      <span class="secondline">level do I have?</span>
      <br>
      <span><i class="arrowdown"></i></span>
    </div>

    <div class="navigation">
      <ul>
        <li><a href="#beginner">Beginner</a></li>
        <li><a href="#intermediate">Intermediate</a></li>
        <li><a href="#advanced">Advanced</a></li>
      </ul>
    </div>

    <div class="skillevel-description">
      <div class="beginner-description">
        <h3 class="beginner-description-header">White water and your first waves</h3>
        <br>
        <div class="beginner-description-content">
          <p>
            As a beginner, you might have only surfed a little or not at all. 
            Higher volume surfboards are just right for you. They make it easier for you to get up (takeoff), 
            paddle and give you enough stability to progress quickly. Fun in the water is guaranteed. 
          </p>
        </div>
      </div>
      <div class="beginner-image">
        <img src="../assets/beginner.jpeg" alt="beginner surfers at the beach" width="200" height="200">
      </div>
    </div>
  </div>

</template>

<script>
  export default {
    name: 'SkillLevel'
  }
</script>
  
<style scoped>

  .skilllevel-text {
    /* border: 1px solid rgb(0, 0, 0,0.2); */
    height: 100%;
    padding: 8px;
    margin: 8px;
    color: rgba(0,0,0,0.8);
    text-align: center;
  }

  .firstline {
    font-family: "Open Sans", sans-serif;
    display: inline-block;  
    transform: rotate(-9deg) skewX(-6deg);
    font-size: 1.66667rem;
    text-transform: uppercase;
    letter-spacing: .1rem;
    overflow:auto;
    color: #999;
  }

  .secondline {
    font-family: "Open Sans",sans-serif;
    display: inline-block;
    transform: rotate(-9deg) skewX(-6deg);
    font-size: 1.66667rem;
    text-transform: uppercase;
    letter-spacing: .1rem;
    overflow: auto;
    color: #1c3a57;
    position: relative;
    top: -.83333rem;
  }

  .arrowdown {
    border: solid #1c3a57;
    border-width: 0 3px 3px 0;
    display: inline-block;
    padding: 9px;
    transform: rotate(45deg);
    -webkit-transform: rotate(45deg);
  }

  .navigation {
    font-family: "Open Sans",sans-serif;
    padding: 10px;
    color: #999;
  }


ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  display: flex;
  justify-content: space-around;
}

li {
  flex-grow: 1;
}

li a {
  display: block;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  color: inherit; 
}

li a:hover {
  color: #1c3a57;
  text-shadow: none;
  background: none;
}

.skillevel-description {
    display: flex;            /* Make this a flex container */
    align-items: center;      /* Vertically align items */
    justify-content: center; /* Distribute items horizontal*/
  }

  .beginner-description {
    flex: 1;                 /* Allow it to grow and take available space */
    padding-right: 1px;     /* Add some space between text and image */
    text-align: left;       /* left-justify contents */
    font-size: 0.9em;
    line-height: 1.4;
  }

  .beginner-image {
    flex: 1;                 /* Allow it to grow and take available space */
  }
  
</style>