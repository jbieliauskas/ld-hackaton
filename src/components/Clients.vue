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
          @trackLink="$emit('trackLink', {value: $event, index})"
          @call="$emit('call', index)"
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

<style scoped>
 table {
   border-collapse: collapse;
   width: 100%;
 }

 th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}
</style>
