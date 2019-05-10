<template>
  <td>
    <a 
      v-if="value !== null" 
      :href="value"
    >
      Takelis.mp3
    </a>
  </td>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TrackLink',
  props: {
    value: {
      type: String,
      default: null,
    },
    name: {
      type: String,
      required: true,
    },
    damageType: {
      type: String,
      required: true,
    },
    amount: {
      type: String,
      required: true,
    },
    carBrand: {
      type: String,
      default: null,
    },
    carNumber: {
      type: String,
      default: null,
    },
    template: {
      type: String,
      required: true,
    },
  },
  methods: {
    callSynthesizer() {
      if(this.damageType === 'property') {
        return this.callSynthesizerForProperty();
      }
      return this.callSynthesizerForTransport();
    },
    callSynthesizerForProperty() {
      return axios.post('http://localhost:5000/synthesizer/property', {
        Vardas: this.name,
        Suma: this.amount,
        Sablonas: this.template,
      });
    },
    callSynthesizerForTransport() {
      return axios.post('http://localhost:5000/synthesizer/transport', {
        Vardas: this.name,
        Suma: this.amount,
        Marke: this.carBrand,
        Numeris: this.carNumber,
        Sablonas: this.template,
      });
    },
  },
  created() {
    this
      .callSynthesizer()
      .then(
        ({data}) => this.$emit('load', data)
      )
      .catch(console.error);
  },
};
</script>
