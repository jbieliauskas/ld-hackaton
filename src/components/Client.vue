<template>
  <tr>
    <td>{{ name }}</td>
    <td>TBD</td>
    <td>Rezultatas</td>
    <track-link 
      :value="trackLink"
      :name="name"
      :damage-type="damageType"
      :amount="amount"
      :car-brand="carBrand"
      :car-number="carNumber"
      :template="template"
      @load="$emit('trackLink', $event)"
    />
    <td>
      <button 
        @click="$emit('call')"
      >
        Skambinti
      </button>
    </td>
  </tr>
</template>

<script>
import axios from 'axios';
import TrackLink from './TrackLink';

export default {
  name: 'Client',
  components: {TrackLink},
  props: {
    name: {
      type: String,
      required: true,
    },
    callTime: {
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
    trackLink: {
      type: String,
      default: null,
    },
  },
};
</script>
