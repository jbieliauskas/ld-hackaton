<template>
  <v-textarea
    solo
    auto-grow
    :value="value" 
    @input="onInput"
  ></v-textarea>
</template>

<script>
export default {
  name: 'Template',
  props: {
    damageType: {
      type: String,
      required: true,
    },
    value: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      edited: false,
    };
  },
  methods: {
    onInput(event) {
      this.edited = true;
      this.emit(event.target.value);
    },
    emit(value) {
      this.$emit('input', value);
    },
    defaultValue() {
      if(this.damageType === 'property') {
        return `
          Sveiki, __Vardas__, 
          
          Jums skambina automatinis balsas iš Lietuvos draudimo. 
          Norime Jus informuoti, kad paskaičiavome žalos dydį Jūsų registruotai žalai 
          pagal būsto draudimą. Žalos dydis – __Suma__ eurų.
          Ar sutinkate su paskaičiuota suma? 
          
          Jeigu sutinkate paspauskite vieną, jeigu nesutinkate paspauskite du, 
          pakartoti žinutę – spauskite tris.
        `;
      }
      return `
        Sveiki, __Vardas__,
        
        Jums skambina automatinis balsas iš Lietuvos draudimo. 
        Norime Jus informuoti, kad pagal Jūsų registruotą žalą transporto priemonei __Marke__, 
        kurios valstybinis numeris __Numeris__, Jums yra paskaičiuota 
        nuostolio suma – __Suma__ eurų. Ar sutinkate su paskaičiuota suma? 
        
        Jeigu sutinkate paspauskite vieną, jeigu nesutinkate paspauskite du, 
        pakartoti žinutę – spauskite tris.
      `;
    },
  },
  watch: {
    damageType: {
      handler() {
        if(this.value === null || !this.edited) {
          this.emit(this.defaultValue());
        }
      },
      immediate: true,
    },
  },
};
</script>
