<template>
  <div>
    <new-client @save="clients.push($event)" />
    <clients :clients="clients" />
  </div>
</template>

<script>
import NewClient from './NewClient';
import Clients from './Clients';

import axios from 'axios';

export default {
  name: 'ClientsApp',
  components: {NewClient, Clients},
  data() {
    return {
      clients: [],
    };
  },
  created() {
    // axios
    //   .post('localhost:8081/foo', {text: 'Sveiki visi!'})
    //   .then(alert)
    //   .catch(console.error);
  },
};
</script>
