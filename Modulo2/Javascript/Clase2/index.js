// Funciones en JS

// Bloque de funcion en python

/* 
  def nombre_funcion(param1, param2):
      # Cuerpo de la función
      pass

*/

function nombreFuncion(param1, param2) {
  // Cuerpo de la función
  console.log("Parámetro 1:", param1);
  console.log("Parámetro 2:", param2);
}

// Llamada a la función
nombreFuncion("valor1", "valor2");

// Convenciones de nombrado en lenguajes de programación

// snake_case - nombre_funcion - Se usa en python y ruby para nombrar funciones y variables
// camelCase - nombreFuncion - Se usa en javascript y java para nombrar funciones y variables
// PascalCase - NombreFuncion - Se usa en C# y otros lenguajes para nombrar clases
// kebab-case - nombre-funcion - Se usa en HTML y CSS para nombrar clases y IDs

// Funciones de retorno en JS

function sumar(a, b) {
  return a + b;
}

function restar(a, b) {
  return a - b;
}

var a = 10;
var b = 5;
var c = 8;

var resultadoSuma = sumar(a, b);
var resultadoResta = restar(resultadoSuma, c);

console.log("Resultado Suma:", resultadoSuma);
console.log("Resultado Resta:", resultadoResta);

function calcularNotas(notas) {
  let suma = 0;
  for (let i = 0; i < notas.length; i++) {
    suma += notas[i];
  }
  return suma / notas.length;
}

// array.length == len(array) - python

var resultadoNotas = calcularNotas([12, 15, 17, 20, 18]);

console.log("Resultado Notas:", resultadoNotas);

// Estructuras de datos

// Arreglos (Arrays) - Listas Python

var numeros = [1, 2, 3, 4, 5];
console.log("Arreglo de Números:", numeros);

// Objetos - Diccionarios en Python

var persona = {
  nombre: "Juan",
  edad: 30,
  ciudad: "Madrid",
};
console.log("Objeto Persona:", persona);

// Manejo de Arreglos

var frutas = ["manzana", "banana", "naranja"];
console.log("Arreglo de Frutas:", frutas);

// Acceder a elementos
console.log("Primera fruta:", frutas[0]);
console.log("Segunda fruta:", frutas[1]);
console.log("Tercera fruta:", frutas[2]);

frutas[2] = "Mango";

console.log("Arreglo de Frutas Modificado:", frutas);

// Metodos en Arreglos

numeros = [1, 2, 3, 4, 5, 3];

// Agregar un elemento al final
numeros.push(6);
console.log("Arreglo después de push:", numeros);

// Agregar un elemento al inicio
numeros.unshift(0);
console.log("Arreglo después de unshift:", numeros);

// Eliminar el último elemento
numeros.pop();
console.log("Arreglo después de pop:", numeros);

// Eliminar el primer elemento
numeros.shift();
console.log("Arreglo después de shift:", numeros);

// Tamaño del arreglo
console.log("Tamaño del Arreglo:", numeros.length);

// Índice de un elemento
console.log("Índice del elemento 3:", numeros.indexOf(3)); // -1 si no existe
console.log("Índice del elemento 10:", numeros.lastIndexOf(3)); // -1 si no existe

// Revertir el arreglo
numeros.reverse();
console.log("Arreglo después de reverse:", numeros);

// Ordenar el arreglo
numeros.sort();
console.log("Arreglo después de sort:", numeros);

// Objetos en Javascript
var estudiante = {
  nombre: "Juan",
  edad: 30,
  ciudad: "Madrid",
  notas: [12, 15, 17, 20, 18],
};

console.log("Objeto Estudiante:", estudiante);

// estudiante["nombre"] - python

// Acceder a propiedades
console.log("Nombre:", estudiante.nombre);
console.log("Edad:", estudiante.edad);
console.log("Ciudad:", estudiante.ciudad);
console.log("Notas:", estudiante.notas);

// Agregar una nueva propiedad
estudiante.direccion = "Calle Falsa 123";
console.log("Dirección:", estudiante.direccion);

// Editar

estudiante.nombre = "Juan Pérez";
estudiante.edad = 31;

// Eliminar

delete estudiante.direccion;

console.log("Objeto Estudiante:", estudiante);

var trabajadores = [
  {
    nombre: "Ana",
    puesto: "Desarrollador",
    salario: 50000,
  },
  {
    nombre: "Carlos",
    puesto: "Desarrollador",
    salario: 40000,
  },
  {
    nombre: "Laura",
    puesto: "Desarrollador",
    salario: 45000,
  },
  {
    nombre: "Luis",
    puesto: "Diseñador",
    salario: 45000,
  },
  {
    nombre: "Pedro",
    puesto: "Gerente",
    salario: 60000,
  },
  {
    nombre: "María",
    puesto: "Analista",
    salario: 55000,
  },
];

function filtrarSalario(trabajadores, salarioMinimo) {
  let nuevoArray = [];
  for (let i = 0; i < trabajadores.length; i++) {
    if (trabajadores[i].salario >= salarioMinimo) {
      nuevoArray.push(trabajadores[i]);
    }
  }

  return nuevoArray;
}

function filtrarPorPuesto(trabajadores, puesto) {
  let nuevoArray = [];
  for (let i = 0; i < trabajadores.length; i++) {
    if (trabajadores[i].puesto === puesto) {
      nuevoArray.push(trabajadores[i]);
    }
  }
  return nuevoArray;
}

var trabajadoresFiltrados = filtrarSalario(trabajadores, 55000);

console.log("Trabajadores con salario >= 50000:", trabajadoresFiltrados);

var desarrolladores = filtrarPorPuesto(trabajadores, "Desarrollador");
console.log("Desarrolladores:", desarrolladores);

// Dado un arreglo de trabajadores, donde cada trabajador tiene nombre, horas trabajadas y salario por hora
// Crear una funcion que calcule el pago de un trabajador
// Condiciones: Si el trabajador hizo mas de 40 horas, las horas extra se pagan al doble de su
// Pago por hora.

var trabajadores = [
  {
    nombre: "Juan",
    horas: 45,
    salario: 20,
  },
  {
    nombre: "Ana",
    horas: 38,
    salario: 22,
  },
  {
    nombre: "Pedro",
    horas: 50,
    salario: 18,
  },
];

const limiteHoras = 40;

function calcularSueldo(trabajador) {
  if (trabajador.horas > limiteHoras) {
    let pagoHorasLegales = limiteHoras * trabajador.salario;
    let horasExtra = trabajador.horas - limiteHoras;
    let pagoHorasExtra = horasExtra * (trabajador.salario * 2);

    return pagoHorasLegales + pagoHorasExtra;
  } else {
    return trabajador.horas * trabajador.salario;
  }
}

var pagoTrabajadores = [];

for (let i = 0; i < trabajadores.length; i++) {
  console.log(trabajadores[i].nombre);

  let pago = calcularSueldo(trabajadores[i]);

  pagoTrabajadores.push({
    nombre: trabajadores[i].nombre,
    pagoSemanal: pago,
  });
}

console.log("Pagos Semanales:", pagoTrabajadores);
