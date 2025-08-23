// Comentario en JavaScript

// Tipos de datos
// Variables
// Operadores
// Condicionales
// Ciclos
// Funciones
// Modulos/Librerias
// Estructuras de datos
// Manejo de errores
// Manejo de Archivos

// 1. Tipos de datos

// Simples

// String
// Number
// Boolean
// Null
// Undefined
// NaN

// Compuestos

// Object == Diccionario
// Array == Lista

// Variables
// var == Variable
// let == Variable
// const == Constante

var nombre = "Juan";
let edad = 30;
const PI = 3.14;

console.log(nombre); // Imprime "Juan"
console.log(edad); // Imprime 30
console.log(PI); // Imprime 3.14

// Flujo de una variable

// 1. Declaracion
// 2. Inicialización
// 3. Uso

var suma;

var a = 5;
var b = 10;

suma = a + b; // Inicialización

console.log("Resultado de la suma:", suma); // Uso, Imprime 15

// Operadores

// Operadores de Asignación
// Operadores Aritméticos
// Operadores de Comparación
// Operadores Lógicos

// Asignación

// =
// +=
// -=
// *=
// ++
// --

// Aritméticos

// +
// -
// *
// /
// %
// **

// Comparación

// == Es igual, pero no valida tipos - "22" == 22 - Esto sera true con el ==
// === Es igual y valida tipos - "22" === 22 - Esto sera false con el ===
// !=
// !==
// >=
// <=
// >
// <

// Logicos

// && Es verdadero si ambos operandos son verdaderos
// || Es verdadero si al menos uno de los operandos es verdadero
// ! Es verdadero si el operando es falso

var suma = 5 + 10;
var resta = 10 - 5;
var multiplicacion = 5 * 10;
var division = 10 / 5;
var modulo = 10 % 3;
var potencia = 2 ** 3;

console.log("Condicion 1:", suma > resta);
console.log("Condicion 2:", resta < multiplicacion);
console.log("Condicion 3:", division === 2);
console.log("Condicion 4:", modulo !== 1);
console.log("Condicion 5:", potencia >= 8);

// Condicionales

// if
// else
// else if - elif de python
// switch - match de python

if (suma > resta) {
  console.log("Condicion 1: Verdadero");
} else {
  console.log("Condicion 1: Falso");
}

if (edad < 18) {
  console.log("Eres menor de edad");
} else if (edad >= 18 && edad < 65) {
  console.log("Eres mayor de edad");
} else {
  console.log("Eres adulto mayor");
}

switch (true) {
  case edad < 18:
    console.log("Eres menor de edad");
    break;
  case edad >= 18 && edad < 65:
    console.log("Eres mayor de edad");
    break;
  default:
    console.log("Eres adulto mayor");
}

// Ciclos

// while
// do while
// for
// for of
// for in

var i = 0;

while (i < 5) {
  console.log("Iteración while:", i);
  i++; // i += 1 o i = i + 1
}

do {
  console.log("Iteración do while:", i);
  i++;
} while (i < 10);

for (var j = 0; j < 5; j++) {
  console.log("Iteración for:", j);
}

var array = [1, 2, 3, 4, 5];
for (var elemento of array) {
  console.log("Iteración for of:", elemento);
}

var objeto = { a: 1, b: 2, c: 3 };
for (var clave in objeto) {
  console.log("Iteración for in:", clave, objeto[clave]);
}

// While

var j = 10;
while (j >= 1) {
  console.log("Iteración while:", j);
  j--;
}

var frutas = ["Peras", "Manzanas", "Bananas"];
for (var i = 1; i < frutas.length; i = i * 2) {
  console.log("Iteración for:", frutas[i]);
}

for (var i = 1; i <= 100; i++) {
  if (i % 2 === 0) {
    console.log("Número par:", i);
  } else {
    console.log("Número impar:", i);
  }
}
