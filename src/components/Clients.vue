<template>
  <div>
    <new-client @save="clients.push($event)" />
    <client-table :clients="clients" />
  </div>
</template>

<script>
import NewClient from './NewClient';
import ClientTable from './ClientTable';

export default {
  name: 'Clients',
  components: {NewClient, ClientTable},
  data() {
    return {
      clients: [],
    };
  },
};
</script>
