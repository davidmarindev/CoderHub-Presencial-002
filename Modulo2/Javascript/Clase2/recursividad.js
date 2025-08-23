// Funciones Recursivas

function factorial(n) {
  if (n === 0) {
    return 1;
  }

  return n * factorial(n - 1);
}

console.log("Factorial de 5:", factorial(5));

// Pasos de la funcion factorial con n = 5
// 1. factorial(5) => 5 * factorial(4)= 24
// 2. factorial(4) => 4 * factorial(3)= 6
// 3. factorial(3) => 3 * factorial(2)= 2
// 4. factorial(2) => 2 * factorial(1)= 1
// 5. factorial(1) => 1

// Call Stack de factorial

// 5. factorial(1) => 1
// 4. factorial(2) => 2 * 1 = 2
// 3. factorial(3) => 3 * 2 = 6
// 2. factorial(4) => 4 * 6 = 24
// 1. factorial(5) => 5 * 24 = 120

function fibonacci(n) {
  if (n <= 1) {
    return n;
  }
  return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log("Fibonacci de 11:", fibonacci(11));
