<template>
  <div>
    <h1>Šablonas</h1>

    <label>
      <input type="radio" value="property" v-model="damageType" /> 
        Turtinė žala
    </label>
    <label>
      <input type="radio" value="transport" v-model="damageType" /> 
      Transporto žala
    </label>
    <br />

    <div>
      <input type="text" placeholder="Vardas" v-model="name" />
      <br />

      <input type="text" placeholder="Suma" v-model="amount" />
    </div>

    <div v-if="damageType === 'transport'">
      <input type="text" placeholder="Markė" v-model="carBrand" />
      <br />

      <input type="text" placeholder="Valstybinis numeris" v-model="carNumber" />
    </div>

    <input type="text" placeholder="Skambučio laikas" v-model="callTime" />
    <br />

    <client-template 
      :damage-type="damageType"
      :value="template"
      @input="template = $event"
    >
    </client-template>
    <br />

    <button @click="save">OK</button>
  </div>
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
        amount: this.amount,
        carBrand: this.carBrand,
        carNumber: this.carNumber,
        callTime: this.callTime,
        template: this.template,
      });
    },
  },
};
</script>
