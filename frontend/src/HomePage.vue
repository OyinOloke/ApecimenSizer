<template>
  <div class="app">
    <div class="container">
      <div class="header">
        <h1>Specimen Size Calculator</h1>
      </div>

      <div class="input-section">
        <input v-model="specimenSize" type="number" placeholder="Enter Specimen Size" class="input-box" />
        <input v-model="magnification" type="number" placeholder="Enter Magnification" class="input-box" />
        <button @click="calculate" class="button">Calculate</button>
      </div>

      <div v-if="actualSize !== null" class="results">
        <p>Actual size: {{ actualSize }}</p>
      </div>
    </div>
    <div class="watermark">Oyins Magnification Calculation</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      specimenSize: null,
      magnification: null,
      actualSize: null,
    };
  },
  methods: {
    calculate() {
      this.actualSize = this.specimenSize / this.magnification;
    },
  },
};
</script>

<style>
.app {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(to bottom, #ffffff, #ffe6f7);
  position: relative;
}

.container {
  padding: 20px;
  background-color: #ffe6f7;
  border-radius: 12px;
  width: 100%;
  max-width: 600px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.header {
  text-align: center;
  margin-bottom: 20px;
}

h1 {
  font-family: 'Roboto', sans-serif;
  color: #ff3366;
  font-size: 2.5rem;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin: 0;
}

.input-section {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.input-box {
  padding: 12px;
  margin: 8px 0;
  border-radius: 8px;
  border: 1px solid #ff66b2;
  font-size: 1rem;
  font-family: 'Arial', sans-serif;
  color: #333;
  background-color: #fff;
  transition: all 0.3s ease;
}

.input-box:focus {
  border-color: #ff3366;
  outline: none;
}

.button {
  background-color: #ff3366;
  color: white;
  padding: 12px 20px;
  margin: 10px 0;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  font-size: 1.1rem;
  font-weight: bold;
  transition: all 0.3s ease;
  width: 100%;
}

.button:hover {
  background-color: #e60057;
  transform: scale(1.05);
}

.results {
  margin-top: 20px;
  background-color: #ffb3d9;
  padding: 15px;
  border-radius: 8px;
  font-size: 1.2rem;
  font-family: 'Verdana', sans-serif;
  color: #4d004d;
}

.results p {
  margin: 0;
  font-weight: bold;
}

.watermark {
  position: absolute;
  bottom: 10px;
  right: 10px;
  font-size: 1.5rem;
  color: rgba(0, 0, 0, 0.1);
  font-family: 'Arial', sans-serif;
  font-weight: bold;
  transform: rotate(45deg);
  pointer-events: none;
}
</style>
