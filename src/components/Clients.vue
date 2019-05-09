<template>
  <table>
      <thead>
        <tr>
          <th>Vardas</th>
          <th>Skambučio laikas</th>
          <th>Skambučio rezultatas</th>
          <th>Klausyti takelį</th>
          <th>Skambinti</th>
        </tr>
      </thead>
      <tbody>
        <client 
          v-for="(client, index) in clients"
          :key="index"
          v-bind="client"
        />
      </tbody>
    </table>
</template>

<script>
import Client from './Client.vue';

export default {
  name: 'Clients',
  components: {Client},
  props: {
    clients: {
      type: Array,
      required: true,
    },
  },
};
</script>
