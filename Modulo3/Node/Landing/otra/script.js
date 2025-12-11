// Esperar a que el DOM cargue
document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.getElementById("mobile-menu");
  const navList = document.querySelector(".nav-list");

  // Toggle del menú hamburguesa
  menuToggle.addEventListener("click", () => {
    navList.classList.toggle("active");
  });

  // Cerrar menú al hacer clic en un enlace (para UX móvil)
  document.querySelectorAll(".nav-list a").forEach((link) => {
    link.addEventListener("click", () => {
      navList.classList.remove("active");
    });
  });
});
