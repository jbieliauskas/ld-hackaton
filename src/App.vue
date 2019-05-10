<template>
  <div id="app">
    <h1>Šablonas</h1>
    <new-client @save="clients.push($event)" />
    <h1>Klientai</h1>
    <clients 
      :clients="clients" 
      @trackLink="setClientTrackLink"
      @call="callClient"
    />
  </div>
</template>

<script>
import NewClient from './components/NewClient';
import Clients from './components/Clients';
import axios from 'axios';

export default {
  name: 'App',
  components: {NewClient, Clients},
  data() {
    return {
      clients: [],
    };
  },
  methods: {
    setClientTrackLink({value, index}) {
      this.clients[index].trackLink = value;
    },
    callClient(index) {
      const client = this.clients[index];
      axios
        .post('http://localhost:3000/call', {
          track: client.trackLink,
          phone: client.phoneNumber,
        })
        .catch(console.error);
    },
  },
};
</script>
