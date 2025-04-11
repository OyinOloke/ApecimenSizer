<template>
  <div class="home">
    <h1>Calculate Specimen Real Size</h1>
    <form @submit.prevent="calculateSpecimen">
      <div>
        <label for="username">Username:</label>
        <input type="text" v-model="username" required />
      </div>
      <div>
        <label for="specimenSize">Specimen Size:</label>
        <input type="number" v-model="specimenSize" required />
      </div>
      <div>
        <label for="magnification">Magnification:</label>
        <input type="number" v-model="magnification" required />
      </div>
      <button type="submit">Calculate</button>
    </form>
    <div v-if="calculatedSize">
      <p><strong>Calculated Real Size: </strong>{{ calculatedSize }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      specimenSize: null,
      magnification: null,
      calculatedSize: null
    };
  },
  methods: {
    async calculateSpecimen() {
      const response = await fetch('http://localhost:8000/calculate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: this.username,
          specimen_size: this.specimenSize,
          magnification: this.magnification
        }),
      });
      const data = await response.json();
      this.calculatedSize = data.actual_size;
    }
  }
};
</script>

<style scoped>
.home {
  text-align: center;
  padding: 20px;
}

input {
  margin: 5px;
}
</style>
