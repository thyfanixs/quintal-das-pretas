#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador estático do site Quintal das Pretas.

Mantém cabeçalho, menu e rodapé em um único lugar (DRY) e escreve as 8 páginas
HTML. Para regenerar o site após editar conteúdo ou layout:

    python3 build.py

Conteúdo textual usa Lorem Ipsum (placeholder) e as imagens são marcadas como
placeholders, conforme o briefing.
"""

import os

BASE = os.path.dirname(os.path.abspath(__file__))

SITE_NOME = "Quintal das Pretas"
SITE_URL = "https://www.quintaldaspretas.com.br"

# (arquivo, rótulo no menu)
NAV = [
    ("quem-somos.html", "Quem Somos"),
    ("cia-pe-de-pano.html", "Cia Pé de Pano"),
    ("agenda.html", "Agenda"),
    ("noticias.html", "Notícias"),
    ("projetos.html", "Projetos"),
    ("apoie.html", "Apoie"),
    ("contato.html", "Contato"),
]

LOREM_CURTO = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus quis "
    "nisl eget urna luctus tincidunt non a sapien."
)
LOREM_MEDIO = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod "
    "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim "
    "veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea "
    "commodo consequat. Duis aute irure dolor in reprehenderit in voluptate."
)
LOREM_LONGO = LOREM_MEDIO + (
    " Excepteur sint occaecat cupidatat non proident, sunt in culpa qui "
    "officia deserunt mollit anim id est laborum. Curabitur pretium tincidunt "
    "lacus, eget pulvinar mauris malesuada eu."
)


def foto_ph(rotulo, classe="", icone="📷"):
    return (
        f'<div class="foto-ph {classe}" role="img" aria-label="Placeholder de imagem: {rotulo}">'
        f'<span><span class="icone">{icone}</span>{rotulo}</span></div>'
    )


def nav_html(ativo):
    itens = []
    for arquivo, rotulo in NAV:
        cls = ' class="ativo" aria-current="page"' if arquivo == ativo else ""
        itens.append(f'<li><a href="{arquivo}"{cls}>{rotulo}</a></li>')
    return "\n".join(itens)


def layout(titulo, descricao, ativo, conteudo):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{titulo} · {SITE_NOME}</title>
  <meta name="description" content="{descricao}" />
  <link rel="icon" type="image/svg+xml" href="assets/img/logo-selo.svg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700;9..144,900&family=Mulish:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/css/style.css" />
</head>
<body>
  <a href="#conteudo" class="sr-only">Pular para o conteúdo</a>
  <div class="grafismo" aria-hidden="true"></div>

  <header class="cabecalho">
    <div class="container cabecalho-inner">
      <a class="marca" href="index.html" aria-label="{SITE_NOME} — página inicial">
        <img class="marca-selo" src="assets/img/logo-selo.svg" alt="" width="56" height="56" />
        <span class="marca-texto">
          <span class="marca-titulo">Quintal das Pretas</span>
          <span class="marca-sub">Ponto de Cultura</span>
        </span>
      </a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="nav-principal" aria-label="Abrir menu">☰</button>
      <nav class="nav-principal" id="nav-principal" aria-label="Navegação principal">
        <ul>
{nav_html(ativo)}
        </ul>
      </nav>
    </div>
  </header>

  <main id="conteudo">
{conteudo}
  </main>

  <div class="grafismo" aria-hidden="true"></div>
  <footer class="rodape">
    <div class="container">
      <div class="rodape-grid">
        <div>
          <div class="rodape-marca">
            <img src="assets/img/logo-selo.svg" alt="" width="48" height="48" />
            <div>
              <strong>Quintal das Pretas</strong>
              <span>Ponto de Cultura</span>
            </div>
          </div>
          <p>Espaço de cultura, ancestralidade e arte no interior de Minas Gerais
          — entre Pedro Leopoldo e Matozinhos. {LOREM_CURTO}</p>
        </div>
        <div>
          <h4>Navegue</h4>
          <ul>
            <li><a href="quem-somos.html">Quem Somos</a></li>
            <li><a href="cia-pe-de-pano.html">Cia Pé de Pano</a></li>
            <li><a href="agenda.html">Agenda</a></li>
            <li><a href="projetos.html">Projetos</a></li>
            <li><a href="apoie.html">Apoie</a></li>
          </ul>
        </div>
        <div>
          <h4>Conecte-se</h4>
          <ul>
            <li><a href="contato.html">Fale conosco</a></li>
            <li><a href="https://instagram.com" target="_blank" rel="noopener">Instagram</a></li>
            <li><a href="https://youtube.com" target="_blank" rel="noopener">YouTube</a></li>
            <li><a href="mailto:contato@quintaldaspretas.com.br">contato@quintaldaspretas.com.br</a></li>
          </ul>
        </div>
      </div>
      <div class="rodape-bottom">
        <span>© <span class="js-ano">2026</span> {SITE_NOME}. Todos os direitos reservados.</span>
        <span>Feito com axé no interior de Minas Gerais.</span>
      </div>
    </div>
  </footer>

  <script src="assets/js/main.js"></script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------
def page_home():
    atalhos = [
        ("quem-somos.html", "Quem Somos", "Nossa história, missão e valores.", "🏡"),
        ("cia-pe-de-pano.html", "Cia Pé de Pano", "30 anos de teatro no interior de Minas.", "🎭"),
        ("agenda.html", "Agenda", "Próximos espetáculos e encontros.", "🗓️"),
        ("noticias.html", "Notícias", "Novidades do quintal.", "📰"),
        ("projetos.html", "Projetos", "O que cultivamos hoje.", "🌱"),
        ("apoie.html", "Apoie", "Faça parte dessa roda.", "🤝"),
    ]
    cards = "\n".join(
        f"""<a class="card" href="{href}">
          {foto_ph(rotulo, 'largo', icone)}
          <div class="card-corpo">
            <h3>{rotulo}</h3>
            <p class="card-resumo">{desc}</p>
          </div>
        </a>"""
        for href, rotulo, desc, icone in atalhos
    )
    conteudo = f"""
    <section class="home-hero">
      <div class="container">
        <p class="kicker">Pedro Leopoldo · Matozinhos · Minas Gerais</p>
        <h1>Onde a ancestralidade vira chão, roda e arte</h1>
        <p>{LOREM_MEDIO}</p>
        <div class="hero-ctas">
          <a class="btn btn-primario" href="projetos.html">Conheça os projetos</a>
          <a class="btn btn-secundario" href="apoie.html">Apoie o Quintal</a>
        </div>
      </div>
    </section>

    <section class="secao linho">
      <div class="container">
        <span class="olho">Bem-vinde ao quintal</span>
        <h2 class="secao-titulo">Um terreiro de cultura e acolhimento</h2>
        <p class="secao-intro">{LOREM_LONGO}</p>
        <div class="grid grid-3">
{cards}
        </div>
      </div>
    </section>

    <section class="secao areia">
      <div class="container">
        <div class="destaque-30">
          <div class="numero">30</div>
          <h2>anos de teatro no interior de Minas Gerais</h2>
          <p>{LOREM_MEDIO}</p>
          <p><a class="btn btn-primario" href="cia-pe-de-pano.html">Cia Pé de Pano</a></p>
        </div>
      </div>
    </section>

    <section class="faixa-cta">
      <div class="container">
        <h2>Esse quintal é nosso</h2>
        <p>{LOREM_CURTO}</p>
        <a class="btn btn-terra btn-cta" href="apoie.html">Quero apoiar</a>
      </div>
    </section>
"""
    return layout(
        "Início",
        "Quintal das Pretas — espaço de cultura, ancestralidade e arte no interior de Minas Gerais.",
        "index.html",
        conteudo,
    )


def page_hero(kicker, titulo, texto):
    return f"""
    <section class="page-hero">
      <div class="container">
        <p class="kicker">{kicker}</p>
        <h1>{titulo}</h1>
        <p>{texto}</p>
      </div>
    </section>
"""


# ---------------------------------------------------------------------------
# QUEM SOMOS
# ---------------------------------------------------------------------------
def page_quem_somos():
    valores = [
        ("Ancestralidade", LOREM_CURTO),
        ("Acolhimento", LOREM_CURTO),
        ("Arte & Território", LOREM_CURTO),
    ]
    valores_html = "\n".join(
        f'<div class="valor-card"><h3>{t}</h3><p>{d}</p></div>'
        for t, d in valores
    )
    idealizadoras = "\n".join(
        foto_ph(f"Idealizadora {i}", "alto", "👩🏾‍🎨") for i in range(1, 5)
    )
    conteudo = page_hero(
        "Quem Somos",
        "Nossa história começa na terra",
        LOREM_MEDIO,
    ) + f"""
    <section class="secao linho">
      <div class="container">
        <div class="split">
          <div>
            <span class="olho">Nossa história</span>
            <h2 class="secao-titulo">Raízes no interior de Minas</h2>
            <p>{LOREM_LONGO}</p>
            <p>{LOREM_MEDIO}</p>
          </div>
          {foto_ph("Foto do espaço / quintal", "", "🏡")}
        </div>
      </div>
    </section>

    <section class="secao areia">
      <div class="container">
        <span class="olho">Missão & Valores</span>
        <h2 class="secao-titulo">O que nos move</h2>
        <p class="secao-intro">{LOREM_MEDIO}</p>
        <div class="grid grid-3">
{valores_html}
        </div>
      </div>
    </section>

    <section class="secao linho">
      <div class="container">
        <span class="olho">Idealizadoras</span>
        <h2 class="secao-titulo">As mãos que cultivam o quintal</h2>
        <p class="secao-intro">{LOREM_MEDIO}</p>
        <div class="grid grid-3">
{idealizadoras}
        </div>
      </div>
    </section>
"""
    return layout(
        "Quem Somos",
        "A história, a missão e os valores do Quintal das Pretas.",
        "quem-somos.html",
        conteudo,
    )


# ---------------------------------------------------------------------------
# CIA PÉ DE PANO
# ---------------------------------------------------------------------------
def page_cia():
    galeria = "\n".join(
        foto_ph(f"Espetáculo {i}", "", "🎭") for i in range(1, 7)
    )
    marcos = [
        ("1995", "Fundação da companhia", LOREM_CURTO),
        ("2005", "Primeira turnê pelo interior", LOREM_CURTO),
        ("2015", "Reconhecimento regional", LOREM_CURTO),
        ("2025", "Celebração de 30 anos", LOREM_CURTO),
    ]
    marcos_html = "\n".join(
        f"""<li class="evento">
          <div class="evento-data"><span class="evento-dia">{ano}</span></div>
          <div class="evento-corpo"><h3>{titulo}</h3><p class="card-resumo">{desc}</p></div>
        </li>"""
        for ano, titulo, desc in marcos
    )
    conteudo = page_hero(
        "Cia Pé de Pano",
        "Companhia de teatro",
        LOREM_MEDIO,
    ) + f"""
    <section class="secao linho">
      <div class="container">
        <div class="destaque-30">
          <div class="numero">30</div>
          <h2>anos de teatro no interior de Minas Gerais</h2>
          <p>{LOREM_LONGO}</p>
        </div>
      </div>
    </section>

    <section class="secao areia">
      <div class="container">
        <span class="olho">Histórico do grupo</span>
        <h2 class="secao-titulo">Uma trajetória em cena</h2>
        <p class="secao-intro">{LOREM_MEDIO}</p>
        <ul class="timeline">
{marcos_html}
        </ul>
      </div>
    </section>

    <section class="secao linho">
      <div class="container">
        <span class="olho">Portfólio cênico</span>
        <h2 class="secao-titulo">Galeria de espetáculos</h2>
        <p class="secao-intro">{LOREM_CURTO}</p>
        <div class="grid grid-3">
{galeria}
        </div>
      </div>
    </section>
"""
    return layout(
        "Cia Pé de Pano",
        "Companhia de teatro Cia Pé de Pano — 30 anos de teatro no interior de Minas Gerais.",
        "cia-pe-de-pano.html",
        conteudo,
    )


# ---------------------------------------------------------------------------
# AGENDA
# ---------------------------------------------------------------------------
def page_agenda():
    eventos = [
        ("12", "JUL", "Espetáculo: Lorem Ipsum em Cena", "Praça de Pedro Leopoldo (MG)"),
        ("19", "JUL", "Roda de Conversa: Papo de Quintal", "Sede do Quintal das Pretas"),
        ("03", "AGO", "Oficina de Teatro Comunitário", "Centro Cultural de Matozinhos (MG)"),
        ("16", "AGO", "Estreia: Territórios do Axé", "Pedro Leopoldo (MG)"),
        ("07", "SET", "Sarau Ancestral", "Quintal das Pretas"),
    ]
    itens = "\n".join(
        f"""<li class="evento">
          <div class="evento-data">
            <span class="evento-dia">{dia}</span>
            <span class="evento-mes">{mes}</span>
          </div>
          <div class="evento-corpo">
            <h3>{nome}</h3>
            <p class="evento-local">{local}</p>
          </div>
          <a class="btn btn-terra" href="#">Mais Informações / Ingressos</a>
        </li>"""
        for dia, mes, nome, local in eventos
    )
    conteudo = page_hero(
        "Agenda",
        "O que acontece no quintal",
        LOREM_MEDIO,
    ) + f"""
    <section class="secao linho">
      <div class="container">
        <span class="olho">Próximos eventos</span>
        <h2 class="secao-titulo">Linha do tempo</h2>
        <p class="secao-intro">{LOREM_CURTO}</p>
        <ul class="timeline">
{itens}
        </ul>
      </div>
    </section>
"""
    return layout(
        "Agenda",
        "Agenda de espetáculos, oficinas e encontros do Quintal das Pretas.",
        "agenda.html",
        conteudo,
    )


# ---------------------------------------------------------------------------
# NOTÍCIAS
# ---------------------------------------------------------------------------
def page_noticias():
    noticias = [
        ("Quintal celebra nova temporada", "10 jun 2026"),
        ("Bastidores de um espetáculo ancestral", "28 mai 2026"),
        ("Papo de Quintal estreia novo episódio", "15 mai 2026"),
        ("Oficinas formam novos artistas", "02 mai 2026"),
        ("Encontro de mestras e mestres", "20 abr 2026"),
        ("Memórias do interior de Minas", "08 abr 2026"),
    ]
    cards = "\n".join(
        f"""<article class="card">
          {foto_ph("Imagem de destaque", "largo", "🖼️")}
          <div class="card-corpo">
            <span class="card-data">{data}</span>
            <h3>{titulo}</h3>
            <p class="card-resumo">{LOREM_CURTO}</p>
            <a href="#">Ler mais →</a>
          </div>
        </article>"""
        for titulo, data in noticias
    )
    conteudo = page_hero(
        "Notícias",
        "Novidades do quintal",
        LOREM_MEDIO,
    ) + f"""
    <section class="secao linho">
      <div class="container">
        <span class="olho">Feed</span>
        <h2 class="secao-titulo">Últimas notícias</h2>
        <p class="secao-intro">{LOREM_CURTO}</p>
        <div class="grid grid-3">
{cards}
        </div>
        <p style="text-align:center;margin-top:2rem;">
          <a class="btn btn-verde" href="#">Carregar mais</a>
        </p>
      </div>
    </section>
"""
    return layout(
        "Notícias",
        "Notícias e novidades do Quintal das Pretas.",
        "noticias.html",
        conteudo,
    )


# ---------------------------------------------------------------------------
# PROJETOS
# ---------------------------------------------------------------------------
def page_projetos():
    # (titulo, financiamento, status_label, classe_tag)
    grupos = [
        ("Ativos / Em andamento", "grupo-ativo", "tag-ativo", "Ativo · Em andamento", [
            ("Videocast Papo de Quintal", None),
        ]),
        ("No início", "grupo-inicio", "tag-inicio", "No início", [
            ("Cia Pé de Pano — 30 anos de teatro no interior de Minas Gerais", "FEC/2025"),
        ]),
        ("Em conclusão", "grupo-conclusao", "tag-conclusao", "Finalizando · Fase de conclusão", [
            ("Quintal Aprendiz", None),
        ]),
        ("Ainda não iniciados", "grupo-naoiniciou", "tag-naoiniciou", "Ainda não iniciou", [
            ("Territórios do Axé — a Ancestralidade Viva em Pedro Leopoldo", "MINC"),
            ("Arte da Terra: Formação Artística no Quintal das Pretas", "FUNARTE"),
            ("Manutenção de Programação Artística", "Prefeitura de Matozinhos"),
            ("Escola Livre de Teatro", None),
        ]),
    ]

    def card_projeto(titulo, financiamento, status_label, classe_tag):
        fin = ""
        if financiamento:
            fin = (
                f'<span class="tag tag-financiamento">Financiamento: {financiamento}</span>'
            )
        return f"""<article class="card projeto-card">
          {foto_ph("Imagem do projeto", "largo", "🌱")}
          <div class="card-corpo">
            <div class="projeto-tags">
              <span class="tag {classe_tag}">{status_label}</span>
              {fin}
            </div>
            <h3>{titulo}</h3>
            <p class="card-resumo">{LOREM_CURTO}</p>
            <a href="#">Saiba mais →</a>
          </div>
        </article>"""

    secoes = []
    for nome, classe_grupo, classe_tag, status_label, projetos in grupos:
        cards = "\n".join(
            card_projeto(t, f, status_label, classe_tag) for t, f in projetos
        )
        secoes.append(f"""<div class="status-grupo {classe_grupo}">
          <h2>{nome}</h2>
          <div class="grid grid-3">
{cards}
          </div>
        </div>""")
    secoes_html = "\n".join(secoes)

    conteudo = page_hero(
        "Projetos",
        "O que cultivamos hoje",
        LOREM_MEDIO,
    ) + f"""
    <section class="secao linho">
      <div class="container">
        <span class="olho">Organizados por status</span>
        <h2 class="secao-titulo">Nossos projetos</h2>
        <p class="secao-intro">As cores das tags indicam a fase de cada projeto:
        <strong style="color:var(--verde-folha)">ativo</strong>,
        <strong style="color:var(--ouro)">no início</strong>,
        <strong style="color:var(--terracota)">em conclusão</strong> e
        <strong style="color:var(--status-naoiniciou)">ainda não iniciado</strong>.</p>
{secoes_html}
      </div>
    </section>

    <section class="faixa-cta">
      <div class="container">
        <h2>Some-se a um projeto</h2>
        <p>{LOREM_CURTO}</p>
        <a class="btn btn-terra btn-cta" href="apoie.html">Quero apoiar</a>
      </div>
    </section>
"""
    return layout(
        "Projetos",
        "Projetos do Quintal das Pretas, organizados por status: Territórios do Axé, Arte da Terra, Papo de Quintal e mais.",
        "projetos.html",
        conteudo,
    )


# ---------------------------------------------------------------------------
# APOIE
# ---------------------------------------------------------------------------
def page_apoie():
    formas = [
        ("📜", "Leis de Incentivo à Cultura", LOREM_MEDIO, "Quero incentivar"),
        ("💸", "Doação direta (PIX)", LOREM_CURTO, "Doar via PIX"),
        ("🤝", "Parcerias corporativas", LOREM_MEDIO, "Seja parceiro"),
        ("🙌", "Voluntariado", LOREM_CURTO, "Ser voluntárie"),
    ]
    cards = "\n".join(
        f"""<div class="apoio-card">
          <div class="apoio-icone" aria-hidden="true">{icone}</div>
          <h3>{titulo}</h3>
          <p>{desc}</p>
          <a class="btn btn-verde" href="contato.html">{cta}</a>
        </div>"""
        for icone, titulo, desc, cta in formas
    )
    conteudo = page_hero(
        "Apoie",
        "Faça parte dessa roda",
        LOREM_MEDIO,
    ) + f"""
    <section class="secao linho">
      <div class="container">
        <span class="olho">Como apoiar</span>
        <h2 class="secao-titulo">Cada gesto rega o quintal</h2>
        <p class="secao-intro">{LOREM_MEDIO}</p>
        <div class="grid grid-2">
{cards}
        </div>

        <div class="pix-box">
          <div>
            <strong>Doação via PIX</strong><br />
            <span class="pix-chave">contato@quintaldaspretas.com.br</span>
          </div>
          <button type="button" class="btn btn-primario" id="copiar-pix"
                  data-pix="contato@quintaldaspretas.com.br">Copiar chave PIX</button>
        </div>
      </div>
    </section>

    <section class="faixa-cta">
      <div class="container">
        <h2>Seu apoio sustenta a cultura</h2>
        <p>{LOREM_CURTO}</p>
        <a class="btn btn-terra btn-cta" href="contato.html">Falar com a equipe</a>
      </div>
    </section>
"""
    return layout(
        "Apoie",
        "Apoie o Quintal das Pretas: leis de incentivo, PIX, parcerias e voluntariado.",
        "apoie.html",
        conteudo,
    )


# ---------------------------------------------------------------------------
# CONTATO
# ---------------------------------------------------------------------------
def page_contato():
    conteudo = page_hero(
        "Contato",
        "Vamos conversar",
        LOREM_MEDIO,
    ) + f"""
    <section class="secao linho">
      <div class="container">
        <div class="split" style="align-items:start">
          <div>
            <span class="olho">Envie uma mensagem</span>
            <h2 class="secao-titulo">Fale com o quintal</h2>
            <form id="form-contato" class="form-grid" novalidate>
              <div class="campo">
                <label for="nome">Nome</label>
                <input type="text" id="nome" name="nome" required autocomplete="name" />
              </div>
              <div class="campo">
                <label for="email">E-mail</label>
                <input type="email" id="email" name="email" required autocomplete="email" />
              </div>
              <div class="campo">
                <label for="assunto">Assunto</label>
                <input type="text" id="assunto" name="assunto" required />
              </div>
              <div class="campo">
                <label for="mensagem">Mensagem</label>
                <textarea id="mensagem" name="mensagem" required></textarea>
              </div>
              <button type="submit" class="btn btn-terra">Enviar mensagem</button>
              <p id="form-aviso" role="status" hidden
                 style="background:var(--areia);padding:.8rem 1rem;border-radius:10px;font-weight:700;"></p>
            </form>
          </div>

          <div class="contato-info">
            <span class="olho">Outros canais</span>
            <h2 class="secao-titulo">Onde nos encontrar</h2>
            <div class="info-item">
              <span class="icone" aria-hidden="true">✉️</span>
              <div><strong>E-mail institucional</strong><br />
                <a href="mailto:contato@quintaldaspretas.com.br">contato@quintaldaspretas.com.br</a></div>
            </div>
            <div class="info-item">
              <span class="icone" aria-hidden="true">📍</span>
              <div><strong>Região</strong><br />Pedro Leopoldo e Matozinhos — Minas Gerais</div>
            </div>
            <div class="info-item">
              <span class="icone" aria-hidden="true">🔗</span>
              <div><strong>Redes sociais</strong><br />
                <span class="redes">
                  <a href="https://instagram.com" target="_blank" rel="noopener">Instagram</a>
                  <a href="https://youtube.com" target="_blank" rel="noopener">YouTube</a>
                </span>
              </div>
            </div>
            <div class="mapa-ph" role="img" aria-label="Placeholder de mapa de localização da região de Pedro Leopoldo e Matozinhos">
              🗺️ Mapa de localização<br />(integração futura — Google Maps)
            </div>
          </div>
        </div>
      </div>
    </section>
"""
    return layout(
        "Contato",
        "Fale com o Quintal das Pretas: formulário, e-mail, redes sociais e localização.",
        "contato.html",
        conteudo,
    )


PAGINAS = {
    "index.html": page_home,
    "quem-somos.html": page_quem_somos,
    "cia-pe-de-pano.html": page_cia,
    "agenda.html": page_agenda,
    "noticias.html": page_noticias,
    "projetos.html": page_projetos,
    "apoie.html": page_apoie,
    "contato.html": page_contato,
}


def main():
    for arquivo, fn in PAGINAS.items():
        caminho = os.path.join(BASE, arquivo)
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(fn())
        print(f"gerado: {arquivo}")
    print(f"\n{len(PAGINAS)} páginas geradas com sucesso.")


if __name__ == "__main__":
    main()
