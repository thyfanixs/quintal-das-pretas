/* Quintal das Pretas — interações leves */
(function () {
  "use strict";

  /* ----- Menu mobile ----- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("nav-principal");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var aberto = nav.classList.toggle("aberto");
      toggle.setAttribute("aria-expanded", aberto ? "true" : "false");
    });
    // fecha ao clicar num link (mobile)
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        nav.classList.remove("aberto");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ----- Formulário de contato (placeholder, sem back-end) ----- */
  var form = document.getElementById("form-contato");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var aviso = document.getElementById("form-aviso");
      if (aviso) {
        aviso.hidden = false;
        aviso.textContent =
          "Axé! Recebemos sua mensagem (demonstração). Em breve conectaremos o envio real.";
      }
      form.reset();
    });
  }

  /* ----- Ano dinâmico no rodapé ----- */
  var ano = document.querySelectorAll(".js-ano");
  ano.forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
