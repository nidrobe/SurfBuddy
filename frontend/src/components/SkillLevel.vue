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
  </div>

</template>

<script>
  export default {
    name: 'SkillLevel'
  }
</script>
  
<style scoped>

  .skilllevel-text {
    border: 1px solid rgb(0, 0, 0,0.2);
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
    color: #32cdab;
    position: relative;
    top: -.83333rem;
  }

  .arrowdown {
    border: solid #32cdab;
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
  color: #32cdab;
  text-shadow: none;
  background: none;
}
  
</style>