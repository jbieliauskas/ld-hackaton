<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md6>
            <v-card class="elevation-12 mb-5">
              <v-card-title primary-title>
                <h1 class="headline">Šablonas</h1>
              </v-card-title>
              <v-card-text>
                <v-form>
                  <!-- <h1></h1> -->
                  <new-client @save="clients.push($event)" />
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary">Login</v-btn>
              </v-card-actions>
            </v-card>

            <v-card class="elevation-12">
              <v-card-title>
                <h1 class="headline">Klientai</h1>
              </v-card-title>
              <v-card-text>
                <clients 
                  :clients="clients" 
                  @trackLink="setClientTrackLink"
                  @call="callClient"
                />
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
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
          personId: client.personId,
        })
        .catch(console.error);
    },
  },
};
</script>
