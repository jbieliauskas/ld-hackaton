<template>
  <div id="app">
    <new-client @save="clients.push($event)" />
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
