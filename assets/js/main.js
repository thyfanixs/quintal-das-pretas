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

  /* ----- Copiar chave PIX ----- */
  var btnPix = document.getElementById("copiar-pix");
  if (btnPix) {
    btnPix.addEventListener("click", function () {
      var chave = btnPix.getAttribute("data-pix") || "";
      var feito = function () {
        var original = btnPix.textContent;
        btnPix.textContent = "Chave copiada! ✓";
        setTimeout(function () { btnPix.textContent = original; }, 2200);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(chave).then(feito, feito);
      } else {
        feito();
      }
    });
  }

  /* ----- Revelação suave ao rolar ----- */
  var prefereReduzir = window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var alvos = document.querySelectorAll(
    ".secao .secao-titulo, .secao .secao-intro, .card, .valor-card, " +
    ".apoio-card, .evento, .destaque-30, .pix-box, .foto-ph, .form-grid, .contato-info"
  );

  function revelarTudo() {
    var pend = document.querySelectorAll(".reveal:not(.visivel)");
    for (var i = 0; i < pend.length; i++) pend[i].classList.add("visivel");
  }

  try {
    if (!prefereReduzir && "IntersectionObserver" in window && alvos.length) {
      // ativa o modo animado só agora (o CSS só oculta sob html.anima)
      document.documentElement.classList.add("anima");

      var io = new IntersectionObserver(function (entradas, obs) {
        entradas.forEach(function (e) {
          if (e.isIntersecting) {
            e.target.classList.add("visivel");
            obs.unobserve(e.target);
          }
        });
      }, { threshold: 0.1, rootMargin: "0px 0px -40px 0px" });

      alvos.forEach(function (el) {
        el.classList.add("reveal");
        io.observe(el);
      });

      // Failsafe: se por algum motivo o observer não disparar
      // (preview embutido, aba em segundo plano, etc.), revela tudo.
      setTimeout(revelarTudo, 2600);
      window.addEventListener("load", function () { setTimeout(revelarTudo, 400); });
    }
  } catch (err) {
    // qualquer falha: garante conteúdo 100% visível
    document.documentElement.classList.remove("anima");
    revelarTudo();
  }
})();
