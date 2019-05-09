<template>
  <div id="app">
    <PhoneCall mp3="https://liepa.rastija.lt/DesktopModules/LiepasAdmin/TextToSpeech.ashx/85136c79cbf9fe36bb9d05d0639c70c265c18d37-Vladas-50.mp3"/>
  </div>
</template>

<script>
import PhoneCall from './components/PhoneCall.vue'

export default {
  name: 'app',
  components: {
    PhoneCall
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
