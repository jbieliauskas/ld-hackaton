<template>
  <div>
    <h1>Šablonas</h1>

    <input type="text" placeholder="Vardas" v-model="name" />
    <br />

    <label>
      <input type="radio" value="transport" v-model="damageType" /> 
      Transporto žala
    </label>
    <label>
      <input type="radio" value="property" v-model="damageType" /> 
        Turtinė žala
    </label>
    <br />

    <input type="text" placeholder="Skambučio laikas" v-model="callETA" />
    <br />

    <textarea v-model="template">Šablonas</textarea>
    <br />

    <button @click="save">OK</button>
  </div>
</template>

<script>
export default {
  name: 'NewClient',
  data() {
    return {
      name: null,
      damageType: null,
      callETA: null,
      template: null,
    };
  },
  methods: {
    save() {
      this.$emit('save', {
        name: this.name,
        damageType: this.damageType,
        callETA: this.callETA,
        template: this.template,
      });
    },
  },
};
</script>
