// 1. Arrow functions

// Son una forma mas corta de escribir funciones en JavaScript. Se introdujeron en ECMAScript 6.

// 2. Programcion funcional y imperativa

// Programacion funcional

// Es un paradigma de programacion que trata de evitar el cambio de estado y los datos mutables. En su lugar, se basa en la evaluacion de funciones matematicas y en la aplicacion de funciones puras.

// Caracteristicas

// - Funciones puras
// - Funciones de primera clase
// - Funciones Callback
// - Funciones de orden superior
// - Funciones recursivas
// - Inmutabilidad

// Programacion imperativa

// Es un paradigma de programacion que se basa en la ejecucion de instrucciones que cambian el estado del programa. Se enfoca en como se deben hacer las cosas.

// Caracteristicas

// - Variables mutables
// - Ciclos
// - Condiciones
// - Estructuras de control
// - Procedimientos
// - Metodos

// Arrow Functions

function saludar(nombre) {
  console.log("Hola, " + nombre);

  return nombre;
}

const saludar2 = (nombre) => {
  console.log("Hola, " + nombre);
};

console.log(saludar("David"));
console.log(saludar2("David"));

const saludo = () => "Hola a todos";

console.log(saludo());

// const suma = (a, b) => a + b;

function restar(a, b) {
  return a - b;
}

// console.log(suma(5, 3));
// console.log(restar(5, 3));

// Funciones de primera clase

// var operacion = suma;

// console.log(operacion(5, 3));

function saludo_general(parametro, funcion) {
  console.log(funcion(parametro));
}

console.log(saludo_general("David", saludar));
console.log(saludo_general("David", saludar2));

const suma = (a, b) => a + b;
const resta = (a, b) => a - b;
const multiplicacion = (a, b) => a * b;
const division = (a, b) => a / b;

const operacion = (a, b, funcion) => funcion(a, b);

console.log(operacion(10, 5, suma));
console.log(operacion(10, 5, resta));
console.log(operacion(10, 5, multiplicacion));
console.log(operacion(10, 5, division));

function validadorNota(nota) {
  if (nota >= 10) {
    return "Aprobado";
  } else if (nota > 14) {
    return "Regular";
  } else if (nota >= 8 && nota < 10) {
    return "Te falto poco";
  } else {
    return "Reprobado";
  }
}

function validadorNota2(nota) {
  if (nota >= 10) {
    return "Aprobado";
  } else if (nota > 17) {
    return "Sobresaliente";
  } else {
    return "Reprobado";
  }
}

estudiantes = [
  { nombre: "David", nota: 18, seccion: "A" },
  { nombre: "Ana", nota: 15, seccion: "B" },
  { nombre: "Luis", nota: 9, seccion: "A" },
  { nombre: "Marta", nota: 20, seccion: "B" },
];

function listarEstudiantes(estudiantes, funcion) {
  for (let i = 0; i < estudiantes.length; i++) {
    console.log(
      "El estudiante " +
        estudiantes[i].nombre +
        " ha sacado " +
        estudiantes[i].nota +
        " y está " +
        funcion(estudiantes[i].nota)
    );
  }
}

console.log(listarEstudiantes(estudiantes, validadorNota));
console.log(listarEstudiantes(estudiantes, validadorNota2));

const filtrarNotas = (estudiantes) => {
  newArray = [];
  for (var i = 0; i < estudiantes.length; i++) {
    if (estudiantes[i].nota >= 10) {
      newArray.push(estudiantes[i]);
    }
  }
  return newArray;
};

const filtrarSeccion = (estudiantes, seccion = "A") => {
  newArray = [];
  for (var i = 0; i < estudiantes.length; i++) {
    if (estudiantes[i].seccion === seccion) {
      newArray.push(estudiantes[i]);
    }
  }
  return newArray;
};

const filtrarEstudiantes = (estudiantes, funcion) => {
  return funcion(estudiantes, "B");
};

console.log(filtrarEstudiantes(estudiantes, filtrarNotas));
console.log(filtrarEstudiantes(estudiantes, filtrarSeccion));

estudiantes.forEach((element) => {
  if (element.nota > 10) {
    console.log("Aprobado");
  } else {
    console.log("No aprobado");
  }
});

var estudiantesAprobados = estudiantes.filter((element) => element.nota > 10);

console.log(estudiantesAprobados);

result = estudiantes.every((element) => element.nota > 10);
result2 = estudiantes.some((element) => element.nota < 10);

console.log(result);
console.log(result2);

productos = [
  { nombre: "Producto 1", precio: 100 },
  { nombre: "Producto 2", precio: 200 },
  { nombre: "Producto 3", precio: 300 },
];

var resultado = productos.reduce((acumulador, producto) => {
  return acumulador + producto.precio;
}, 100);

console.log(resultado);

nuevos_productos = productos.map((producto) => {
  precio = producto.precio * 1.21;

  return { nombre: producto.nombre, precio: precio };
});

console.log(nuevos_productos);

// Inmutabilidad

var nombre = "David";

nombre = "Juan";

const nombre2 = "Pedro";

// nombre2 = "Luis";

var array = [1, 2, 3];

var nuevoArray = [...array, 4, 5, 6]; // Spread operator

console.log(nuevoArray);

estudiante = {
  name: "David",
  age: 25,
  curso: "JavaScript",
};

Object.freeze(estudiante);

estudiante.name = "Juan";

console.log(estudiante);
