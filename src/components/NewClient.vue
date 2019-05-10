<template>
  <v-form>
    <v-container>

    <v-radio-group v-model="damageType" row>
      <v-radio label="Turtinė žala" value="property"></v-radio>
      <v-radio label="Transporto žala" value="transport"></v-radio>
    </v-radio-group>

    <v-layout row wrap>
      <v-flex md4>
        <v-text-field label="Vardas" solo v-model="name"></v-text-field>
      </v-flex>

      <v-flex md4>
        <v-text-field label="Asmens kodas" solo v-model="personId"></v-text-field>
      </v-flex>

      <v-flex md4>
        <v-text-field label="Telefono numeris" solo v-model="phoneNumber"></v-text-field>
      </v-flex>

      <v-flex md4>
        <v-text-field label="Suma" solo v-model="amount"></v-text-field>
      </v-flex>

      <v-flex md4 v-if="damageType === 'transport'">
        <v-text-field label="Markė" solo v-model="carBrand"></v-text-field>
      </v-flex>

      <v-flex md4 v-if="damageType === 'transport'">
        <v-text-field label="Valstybinis numeris" solo v-model="carNumber"></v-text-field>
      </v-flex>
    </v-layout>

    <client-template 
      :damage-type="damageType"
      :value="template"
      @input="template = $event"
    >
    </client-template>

    <v-btn fab dark color="indigo" @click="save">
      <v-icon dark>add</v-icon>
    </v-btn>

    </v-container>
  </v-form>
</template>

<script>
import ClientTemplate from './Template';

export default {
  name: 'NewClient',
  components: {ClientTemplate},
  data() {
    return {
      damageType: 'property',
      name: null,
      personId: null,
      phoneNumber: null,
      amount: null,
      carBrand: null,
      carNumber: null,
      callTime: null,
      template: null,
    };
  },
  methods: {
    save() {
      this.$emit('save', {
        damageType: this.damageType,
        name: this.name,
        personId: this.personId,
        phoneNumber: this.phoneNumber,
        amount: this.amount,
        carBrand: this.carBrand,
        carNumber: this.carNumber,
        // callTime: this.callTime,
        callTime: '',
        template: this.template,
        trackLink: null,
      });
    },
  },
};
</script>
