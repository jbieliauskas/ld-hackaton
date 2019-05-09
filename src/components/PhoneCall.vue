<template>
  <div>
    <div class="center">
      <div class="keyboard">
        <li class="callButton">
          <img
            width="50"
            height="50"
            src="data:image/png;base64,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"
            @click="playSound"
          >
        </li>
        <li class="letter clearl" @click="$emit('response', 1)">1</li>
        <li class="letter" @click="$emit('response', 2)">2</li>
        <li class="letter" @click="$emit('response', 3)">3</li>
        <li class="letter clearl">4</li>
        <li class="letter">5</li>
        <li class="letter">6</li>
        <li class="letter clearl">7</li>
        <li class="letter">8</li>
        <li class="letter">9</li>
        <li class="letter clearl">*</li>
        <li class="letter">0</li>
        <li class="letter">#</li>
        <li class="callButton clearl">
          <img
            width="80"
            height="80"
            src="https://cdn3.iconfinder.com/data/icons/cosmo-color-multimedia-2/40/hang-512.png"
            @click="stopCall"
          >
        </li>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PhoneCall",
  callSound: null,
  textSound: null,
  props: {
    mp3: String
  },
  methods: {
    playSound() {
      this.callSound.pause();
      if (this.mp3) {
        this.textSound = new Audio(this.mp3);
        this.textSound.play();
      }
    },
    stopCall() {
      if (this.textSound) {
        this.textSound.pause();
      } else {
        this.callSound.pause();
      }
      this.$emit("response", "stopped");
    }
  },
  mounted() {
    this.callSound = new Audio(
      "https://www.redringtones.com/wp-content/uploads/2016/08/Skype-ringtone.mp3"
    );
    this.callSound.play();
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
.keyboard {
  margin: 0;
  padding: 0;
  list-style: none;
}
.keyboard li {
  float: left;
  margin: 0 5px 5px 0;
  width: 60px;
  height: 60px;
  font-size: 24px;
  line-height: 60px;
  text-align: center;
  background: #fff;
  border: 1px solid #e5e5e5;
  border-radius: 5px;
}
.clearl {
  clear: left;
}
.keyboard li:hover {
  position: relative;
  top: 1px;
  left: 1px;
  border-color: #f9f9f9;
  cursor: pointer;
}
.keyboard .callButton {
  width: 90px;
  margin-left: 45px;
}
.center {
  display: flex;
  justify-content: center;
}
</style>
