<template>
  <tr>
    <td>{{ name }}</td>
    <td>{{ callTime }}</td>
    <td>Rezultatas</td>
    <td><a v-if="trackLink !== null" :href="trackLink">Takelis</a></td>
    <td><button>Skambinti</button></td>
  </tr>
</template>

<script>
import { setTimeout } from 'timers';

export default {
  props: {
    name: {
      type: String,
      required: true,
    },
    callTime: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      trackLink: null,
    };
  },
  created() {
    setTimeout(() => {
      this.trackLink = 'https://9gag.com';
    }, 1000);
  },
};
</script>
