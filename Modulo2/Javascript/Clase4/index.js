const estudiantes = [
  { nombre: "Jose", edad: 20, notaFinal: 18, curso: "Full Stack" },
  { nombre: "Maria", edad: 22, notaFinal: 16, curso: "Data Science" },
  { nombre: "Pedro", edad: 21, notaFinal: 17, curso: "UX/UI" },
  { nombre: "Eva", edad: 20, notaFinal: 15, curso: "Full Stack" },
];

var result = estudiantes.map((estudiante) => {
  if (estudiante.curso === "Full Stack") {
    return {
      nombre: estudiante.nombre,
      edad: estudiante.edad,
      notaFinal: estudiante.notaFinal,
      curso: estudiante.curso,
    };
  }
});

var filtered = estudiantes.filter(
  (estudiante) => estudiante.curso === "Full Stack"
);

console.log(result);
console.log(filtered);

// Promesas
// Async / Await
// Fetch
