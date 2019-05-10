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
      const client = JSON.parse(JSON.stringify(this.clients[index]));
      console.log(client);
    },
  },
};
</script>
