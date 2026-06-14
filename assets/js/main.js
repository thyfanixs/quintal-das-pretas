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

  /* ----- Agenda dinâmica (lê data/eventos.json; sem rebuild) ----- */
  var listaAgenda = document.getElementById("agenda-lista");
  if (listaAgenda) {
    var statusAg = document.getElementById("agenda-status");
    var MESES = ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN",
                 "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"];
    var fonte = listaAgenda.getAttribute("data-fonte") || "data/eventos.json";

    var escAg = function (s) {
      return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
        return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
      });
    };
    var parseDataAg = function (iso) {
      var m = /^(\d{4})-(\d{2})-(\d{2})/.exec(iso || "");
      return m ? new Date(+m[1], +m[2] - 1, +m[3]) : null;
    };
    var linkSeguro = function (u) {
      // só permite http(s) ou caminho relativo/absoluto do próprio site
      return /^(https?:\/\/|\/|[\w./-]+$)/i.test(u || "") && !/^javascript:/i.test(u || "");
    };

    fetch(fonte, { cache: "no-store" })
      .then(function (r) { if (!r.ok) throw new Error("http"); return r.json(); })
      .then(function (eventos) {
        if (!Array.isArray(eventos)) eventos = [];
        var hoje = new Date(); hoje.setHours(0, 0, 0, 0);
        var proximos = eventos
          .map(function (e) { e._d = parseDataAg(e.data); return e; })
          .filter(function (e) { return e._d && e._d >= hoje; })
          .sort(function (a, b) { return a._d - b._d; });

        if (!proximos.length) {
          if (statusAg) statusAg.textContent =
            "Em breve, novos eventos. Acompanhe nossas redes sociais!";
          return;
        }
        listaAgenda.innerHTML = proximos.map(function (e) {
          var dia = ("0" + e._d.getDate()).slice(-2);
          var mes = MESES[e._d.getMonth()];
          var img = e.imagem
            ? '<img class="evento-img" src="' + escAg(e.imagem) + '" alt="' +
              escAg(e.titulo || "Evento") + '" loading="lazy" />' : "";
          var local = e.local ? '<p class="evento-local">' + escAg(e.local) + "</p>" : "";
          var desc = e.descricao ? '<p class="card-resumo">' + escAg(e.descricao) + "</p>" : "";
          var btn = (e.link && linkSeguro(e.link))
            ? '<a class="btn btn-terra" href="' + escAg(e.link) +
              '" target="_blank" rel="noopener">Mais informações / Ingressos</a>' : "";
          return '<li class="evento">' +
            '<div class="evento-data"><span class="evento-dia">' + dia +
            '</span><span class="evento-mes">' + mes + "</span></div>" +
            img +
            '<div class="evento-corpo"><h3>' + escAg(e.titulo || "Evento") + "</h3>" +
            local + desc + btn + "</div>" +
            "</li>";
        }).join("");
        listaAgenda.hidden = false;
        if (statusAg) statusAg.hidden = true;
      })
      .catch(function () {
        if (statusAg) statusAg.textContent =
          "Não foi possível carregar a agenda agora. Tente novamente mais tarde.";
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
