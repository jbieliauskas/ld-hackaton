<template>
  <div>Phone Call</div>
</template>

<script>
export default {
  name: "PhoneCall",
  props: {
    msg: String
  },
  methods: {
    playSound(sound) {
      if (sound) {
        var audio = new Audio(sound);
        audio.play();
      }
    }
  },
  mounted() {
    this.playSound("https://liepa.rastija.lt/DesktopModules/LiepasAdmin/TextToSpeech.ashx/85136c79cbf9fe36bb9d05d0639c70c265c18d37-Vladas-50.mp3");
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
