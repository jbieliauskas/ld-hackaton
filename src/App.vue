<template>
  <div id="app">
    <HelloWorld msg="A"/>
    <PhoneCall mp3="https://liepa.rastija.lt/DesktopModules/LiepasAdmin/TextToSpeech.ashx/85136c79cbf9fe36bb9d05d0639c70c265c18d37-Vladas-50.mp3"/>
  </div>
</template>

<script>
import PhoneCall from './components/PhoneCall.vue'
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'app',
  components: {
    PhoneCall, HelloWorld
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
