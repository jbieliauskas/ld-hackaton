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
        <tr v-for="({name, callETA}, index) in clients" :key="index">
          <td>{{ name }}</td>
          <td>{{ callETA }}</td>
          <td>Rezultatas</td>
          <td><a href="#">Takelis</a></td>
          <td><button>Skambinti</button></td>
        </tr>
      </tbody>
    </table>
</template>

<script>
export default {
  name: 'ClientTable',
  props: {
    clients: {
      type: Array,
      required: true,
    },
  },
};
</script>
