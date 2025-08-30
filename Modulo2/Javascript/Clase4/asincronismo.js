// function sincrona() {
//   setTimeout(() => {
//     console.log("Fin sincronismo");
//   }, 2000);

//   console.log("Fin sincronismo de nuevo");
// }

// console.log("Inicio sincronismo");

// sincrona();

// console.log("Fin sincronismo de nuevo 2");

// Promesas

const promesa = new Promise((resolve, reject) => {
  let exito = Math.random() > 0.5;
  console.log("Exito:", exito);
  setTimeout(() => {
    if (exito) {
      resolve("Fin promesa");
    } else {
      reject("Error en la promesa");
    }
  }, 2000);
});

console.log("Inicio promesa");

promesa
  .then((resultado) => {
    console.log("Resultado exitoso:", resultado);
  })
  .catch((error) => {
    console.error("Error en la promesa:", error);
  })
  .finally(() => {
    console.log("Fin promesa");
  });

api_url = "https://randomuser.me/api?results=7";

// const usuarios = fetch(api_url)
//   .then((response) => {
//     if (!response.ok) {
//       throw new Error("Error en la respuesta de la API");
//     }
//     return response.json();
//   })
//   .then((data) => {
//     return data.results;
//   })
//   .catch((error) => {
//     console.error("Error en la solicitud:", error);
//   });

async function getUsers() {
  try {
    const response = await fetch(api_url);
    if (!response.ok) {
      throw new Error("Error en la respuesta de la API");
    }
    const data = await response.json();

    data.results.forEach((user) => {
      console.log("Nombre Usuario:", user.name.first, user.name.last);
    });
  } catch (error) {
    console.error("Error en la solicitud:", error);
  }
}

getUsers();

console.log("Se ejecuta antes de imprimir los usuarios");
