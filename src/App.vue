<template>
  <div id="app">
    <h1>Šablonas</h1>
    <new-client @save="clients.push($event)" />
    <h1>Klientai</h1>
    <clients :clients="clients" />
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
};
</script>
