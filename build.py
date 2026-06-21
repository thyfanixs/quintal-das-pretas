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
import re

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


def imagem_ou_ph(base, rotulo, classe="", icone="📷", alt=None):
    """Usa a foto real em assets/img/quem-somos/{base}.{ext} se existir;
    caso contrário, mostra o placeholder. Rode build.py após subir a foto."""
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        rel = f"assets/img/quem-somos/{base}{ext}"
        if os.path.exists(os.path.join(BASE, rel)):
            return (f'<img class="foto-real {classe}" src="{rel}" '
                    f'alt="{alt or rotulo}" loading="lazy" />')
    return foto_ph(rotulo, classe, icone)


def imagem_arquivo(rel_base, rotulo, classe="", icone="📷", alt=None):
    """Usa a foto real em assets/img/{rel_base}.{ext} se existir; senão, placeholder.
    Caminho fora de assets/img/cia/ para não entrar na galeria da Cia."""
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        rel = f"assets/img/{rel_base}{ext}"
        if os.path.exists(os.path.join(BASE, rel)):
            return (f'<img class="foto-real {classe}" src="{rel}" '
                    f'alt="{alt or rotulo}" loading="lazy" />')
    return foto_ph(rotulo, classe, icone)


def nav_html(ativo):
    itens = []
    for arquivo, rotulo in NAV:
        cls = ' class="ativo" aria-current="page"' if arquivo == ativo else ""
        itens.append(f'<li><a href="{arquivo}"{cls}>{rotulo}</a></li>')
    return "\n".join(itens)


def layout(titulo, descricao, ativo, conteudo):
    return f"""<!DOCTYPE html>
<!-- Página gerada por build.py — não editar à mão (rode: python3 build.py) -->
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; script-src 'self'; connect-src 'self' https://formsubmit.co; frame-src https://www.google.com https://maps.google.com; base-uri 'self'; form-action 'self' https://formsubmit.co" />
  <title>{titulo} · {SITE_NOME}</title>
  <meta name="description" content="{descricao}" />
  <link rel="icon" type="image/svg+xml" href="assets/img/emblema.svg" />
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
        <img class="marca-selo" src="assets/img/emblema.svg" alt="" width="52" height="60" />
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
            <img src="assets/img/emblema.svg" alt="" width="46" height="53" />
            <div>
              <strong>Quintal das Pretas</strong>
              <span>Ponto de Cultura</span>
            </div>
          </div>
          <p>Associação cultural e Ponto de Cultura em Matozinhos, Minas Gerais.
          Cultura, memória e identidade afro-brasileira por meio da arte, da
          educação e da valorização dos saberes populares.</p>
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
            <li><a href="https://instagram.com/quintaldaspretas" target="_blank" rel="noopener">Instagram @quintaldaspretas</a></li>
            <li><a href="https://instagram.com/ciapedepano_oficial" target="_blank" rel="noopener">Instagram @ciapedepano_oficial</a></li>
            <li><a href="https://www.youtube.com/@ciapedepano_matozinhos1996" target="_blank" rel="noopener">YouTube</a></li>
            <li><a href="mailto:quintaldaspretas2015@gmail.com">quintaldaspretas2015@gmail.com</a></li>
          </ul>
        </div>
      </div>
      <div class="rodape-bottom">
        <span>© <span class="js-ano">2026</span> {SITE_NOME}. Todos os direitos reservados.</span>
        <span>Feito com carinho no interior de Minas Gerais.</span>
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
        ("quem-somos.html", "Quem Somos", "Nossa história, missão e valores.", "quem-somos.jpg"),
        ("cia-pe-de-pano.html", "Cia Pé de Pano", "30 anos de teatro no interior de Minas.", "cia.jpg"),
        ("agenda.html", "Agenda", "Próximos espetáculos e encontros.", "agenda.jpg"),
        ("noticias.html", "Notícias", "Novidades do quintal.", "noticias.jpg"),
        ("projetos.html", "Projetos", "O que cultivamos hoje.", "projetos.jpg"),
        ("apoie.html", "Apoie", "Faça parte dessa roda.", "apoie.jpg"),
    ]
    cards = "\n".join(
        f"""<a class="card" href="{href}">
          <img src="assets/img/home/{img}" alt="" loading="lazy" />
          <div class="card-corpo">
            <h3>{rotulo}</h3>
            <p class="card-resumo">{desc}</p>
          </div>
        </a>"""
        for href, rotulo, desc, img in atalhos
    )
    conteudo = f"""
    <section class="home-hero">
      <div class="container">
        <p class="kicker">Matozinhos · Minas Gerais</p>
        <h1>Onde a ancestralidade vira chão, roda e arte</h1>
        <p>Somos chão de terra batida, axé e palco. Em Matozinhos, o Quintal das Pretas
        mantém viva a memória afro-brasileira pela arte, pela educação e pela ancestralidade,
        fazendo de cada cena, cada tambor e cada encontro um ato de pertencimento, acolhimento
        e transformação.</p>
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
        <p class="secao-intro">Mais que um espaço, o Quintal das Pretas é ponto de encontro:
        lugar de roda, de escuta e de criação onde artistas, mestres da cultura popular e a
        comunidade se reúnem. Aqui a arte e a educação caminham juntas, fortalecendo a memória,
        a identidade afro-brasileira e os laços que sustentam o nosso território.</p>
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
          <p>O trabalho da companhia nasce da vivência cultural do interior mineiro e do
          compromisso com um fazer teatral autoral genuíno, acessível e voltado para a
          formação de público. Suas produções transitam entre o teatro, a música e a
          oralidade, promovendo experiências poéticas que conectam arte, patrimônio cultural
          e identidade.</p>
          <p><a class="btn btn-primario" href="cia-pe-de-pano.html">Cia Pé de Pano</a></p>
        </div>
      </div>
    </section>

    <section class="faixa-cta">
      <div class="container">
        <h2>Esse quintal é nosso</h2>
        <p>Cultura se faz junto. Apoie, participe e ajude a manter viva a arte, a memória e a
        ancestralidade no coração de Minas.</p>
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
    p1 = ("O Quintal das Pretas é uma associação cultural sediada em Matozinhos, "
          "Minas Gerais, que atua na promoção da cultura, da memória, da identidade "
          "afro-brasileira e do desenvolvimento comunitário por meio da arte, da "
          "educação e da valorização dos saberes populares. Com trajetória construída "
          "ao longo de mais de duas décadas, a instituição se consolidou como um espaço "
          "de encontro, criação, formação e fortalecimento de vínculos entre artistas, "
          "mestres da cultura popular e a comunidade.")
    p2 = ("Reconhecido como Ponto de Cultura pelo Programa Viva Cultura do Ministério "
          "da Cultura em 2024, o Quintal das Pretas mantém uma programação contínua e "
          "acessível, oferecendo apresentações artísticas, oficinas, rodas de conversa, "
          "ações formativas e atividades voltadas à preservação da memória e das "
          "tradições mineiras. O espaço abriga iniciativas que promovem a diversidade "
          "cultural e o acesso democrático aos bens culturais.")
    p3 = ("Entre suas principais realizações está a atuação da Cia Pé de Pano, coletivo "
          "de teatro com 30 anos de existência, responsável pela criação e circulação de "
          "espetáculos que dialogam com a história, a oralidade e a cultura popular de "
          "Minas Gerais, como <em>Chico Rei</em> e <em>Caminho da Boiada</em>. Por meio "
          "de suas ações, o Quintal das Pretas reafirma seu compromisso com a "
          "transformação social, a valorização das identidades culturais e a construção "
          "de um território mais criativo, inclusivo e participativo.")

    valores = [
        ("Memória & Ancestralidade",
         "Preservação da memória, das tradições mineiras e da identidade afro-brasileira."),
        ("Arte & Formação",
         "Apresentações, oficinas, rodas de conversa e ações formativas com acesso "
         "democrático aos bens culturais."),
        ("Comunidade & Transformação",
         "Fortalecimento de vínculos e construção de um território mais criativo, "
         "inclusivo e participativo."),
    ]
    valores_html = "\n".join(
        f'<div class="valor-card"><h3>{t}</h3><p>{d}</p></div>'
        for t, d in valores
    )
    equipe = [
        ("Ita Ferreira", "Atriz e Diretora Artística da Cia Pé de Pano"),
        ("Adriana Ferreira", "Produtora Cultural"),
        ("Valéria Ferreira", "Artesã e Quitandeira"),
        ("Renilde Ferreira", "Cozinheira e Quitandeira"),
    ]
    def iniciais(nome):
        partes = nome.split()
        return (partes[0][0] + partes[-1][0]).upper()
    idealizadoras = "\n".join(
        f"""<div class="pessoa-card">
          <span class="pessoa-avatar" aria-hidden="true">{iniciais(nome)}</span>
          <div><h3>{nome}</h3><p>{funcao}</p></div>
        </div>"""
        for nome, funcao in equipe
    )
    conteudo = page_hero(
        "Quem Somos",
        "Cultura, memória e identidade afro-brasileira",
        "Associação cultural sediada em Matozinhos (MG) — Ponto de Cultura reconhecido "
        "pelo Programa Viva Cultura do Ministério da Cultura (2024).",
    ) + f"""
    <section class="secao linho">
      <div class="container">
        <div class="split">
          <div>
            <span class="olho">Nossa história</span>
            <h2 class="secao-titulo">Mais de duas décadas no interior de Minas</h2>
            <p>{p1}</p>
            <p>{p2}</p>
          </div>
          {imagem_ou_ph("espaco", "Foto do espaço / quintal", "", "🏡")}
        </div>
        <p style="margin-top:1.6rem">{p3}</p>
      </div>
    </section>

    <section class="secao areia">
      <div class="container">
        <span class="olho">Missão &amp; Valores</span>
        <h2 class="secao-titulo">O que nos move</h2>
        <p class="secao-intro">Promover a cultura, a memória, a identidade afro-brasileira
        e o desenvolvimento comunitário por meio da arte, da educação e da valorização
        dos saberes populares.</p>
        <div class="grid grid-3">
{valores_html}
        </div>
      </div>
    </section>

    <section class="secao linho">
      <div class="container">
        <span class="olho">Idealizadoras</span>
        <h2 class="secao-titulo">As mãos que cultivam o quintal</h2>
        <p class="secao-intro">Conheça as pessoas que constroem o Quintal das Pretas, dia
        após dia, com arte, afeto e saberes populares.</p>
        <div class="idealizadoras-foto">
          {imagem_ou_ph("idealizadoras", "Foto das idealizadoras", "natural", "👩🏾‍🎨")}
        </div>
        <div class="grid grid-2">
{idealizadoras}
        </div>
      </div>
    </section>
"""
    return layout(
        "Quem Somos",
        "O Quintal das Pretas é uma associação cultural de Matozinhos (MG), Ponto de "
        "Cultura (MINC, 2024), que promove cultura, memória e identidade afro-brasileira.",
        "quem-somos.html",
        conteudo,
    )


# ---------------------------------------------------------------------------
# CIA PÉ DE PANO
# ---------------------------------------------------------------------------
def galeria_cia():
    """Monta a galeria da Cia a partir das fotos em assets/img/cia/.
    Basta colocar as fotos (.jpg/.jpeg/.png/.webp) na pasta e rodar build.py.
    Sem fotos -> placeholders. Grade limpa de imagens (sem legenda)."""
    pasta = os.path.join(BASE, "assets", "img", "cia")
    exts = (".jpg", ".jpeg", ".png", ".webp", ".avif")
    fotos = []
    if os.path.isdir(pasta):
        fotos = sorted(
            f for f in os.listdir(pasta)
            if f.lower().endswith(exts) and not f.startswith(".")
        )
    if not fotos:
        return "\n".join(foto_ph(f"Espetáculo {i}", "", "🎭") for i in range(1, 7))

    itens = []
    for i, nome in enumerate(fotos, start=1):
        itens.append(
            f'<figure class="card foto-cena">'
            f'<img src="assets/img/cia/{nome}" alt="Cia Pé de Pano em cena — foto {i}" loading="lazy" />'
            f'</figure>'
        )
    return "\n".join(itens)


def page_cia():
    galeria = galeria_cia()
    espetaculos = [
        ("Infantil", "Povo de um Lugar",
         "Voltado ao público infantil, aborda temas ligados ao patrimônio cultural e à "
         "memória. A montagem circulou por diversos municípios mineiros, com apresentações "
         "em escolas, espaços culturais e projetos de formação de plateia."),
        ("Conto cênico-musical", "Caminho da Boiada",
         "Inspirado na histórica viagem realizada por João Guimarães Rosa em 1952, ao lado "
         "de uma comitiva de vaqueiros pelo sertão mineiro. Percorreu festivais, festas "
         "literárias, escolas, ruas, praças e celebrações rurais, com destaque para a "
         "apresentação no Grande Teatro do Palácio das Artes, em Belo Horizonte."),
        ("Conto cênico-musical", "Ciclos",
         "Inspirado na obra de Agripa Vasconcelos, revisita diferentes períodos da história "
         "de Minas Gerais por meio de personagens e acontecimentos marcantes da formação "
         "cultural e social do estado. Reafirma o compromisso da Cia com a pesquisa "
         "histórica, a preservação da memória e a valorização das narrativas populares."),
        ("Em montagem · 2025", "Chico Rei",
         "Inspirado na obra do escritor matozinhense Agripa Vasconcelos, celebra a trajetória "
         "do Rei Galanga e as tradições do Congado mineiro, num mergulho na ancestralidade "
         "afro-brasileira. Em sua primeira experiência em festival competitivo, recebeu sete "
         "premiações, incluindo melhor espetáculo, direção e dramaturgia, além de outras seis "
         "indicações no 9º Festival Internacional de Teatro de Guaranésia (MG), em abril de 2026."),
    ]
    espetaculos_html = "\n".join(
        f"""<article class="card">
          <div class="card-corpo">
            <span class="card-data">{tema}</span>
            <h3>{nome}</h3>
            <p class="card-resumo">{desc}</p>
          </div>
        </article>"""
        for tema, nome, desc in espetaculos
    )
    conteudo = page_hero(
        "Cia Pé de Pano",
        "Teatro autoral, música e oralidade",
        "Há três décadas, a Cia Pé de Pano leva ao palco a cultura, a memória e as "
        "narrativas populares do interior de Minas Gerais.",
    ) + f"""
    <section class="secao linho">
      <div class="container">
        <div class="destaque-30">
          <div class="numero">30</div>
          <h2>anos de teatro no interior de Minas Gerais</h2>
          <p>O trabalho da companhia nasce da vivência cultural do interior mineiro e do
          compromisso com um fazer teatral autoral genuíno, acessível e voltado para a
          formação de público. Suas produções transitam entre o teatro, a música e a
          oralidade, promovendo experiências poéticas que conectam arte, patrimônio cultural
          e identidade.</p>
        </div>
      </div>
    </section>

    <section class="secao areia">
      <div class="container">
        <span class="olho">Trajetória</span>
        <h2 class="secao-titulo">Histórico e repertório</h2>
        <p class="secao-intro">Desde 2015, a Cia Pé de Pano é residente do Ponto de Cultura
        Quintal das Pretas, espaço dedicado à criação artística, realização de oficinas,
        ensaios, ações formativas e fortalecimento da produção cultural comunitária.</p>

        <h3 class="sub-titulo">Principais espetáculos</h3>
        <div class="grid grid-2">
{espetaculos_html}
        </div>

        <div class="bloco-texto">
          <p>A relevância artística e cultural da Cia Pé de Pano foi reconhecida por meio de
          homenagens, certificados e moções de congratulação concedidas por instituições
          culturais e órgãos públicos, reafirmando sua contribuição para o fortalecimento das
          artes cênicas, da cultura popular e da memória mineira.</p>
          <p>A Cia Pé de Pano segue desenvolvendo projetos que fortalecem as tradições
          populares, promovem o encontro entre gerações e ampliam o alcance da cultura mineira
          dentro e fora do estado.</p>
        </div>
        <div class="cia-destaque-img">
          {imagem_arquivo("cia-destaque", "Foto da Cia Pé de Pano", "natural", "🎭",
                          "Cia Pé de Pano")}
        </div>
      </div>
    </section>

    <section class="secao linho">
      <div class="container">
        <span class="olho">Portfólio cênico</span>
        <h2 class="secao-titulo">Galeria de espetáculos</h2>
        <p class="secao-intro">Registros dos espetáculos da Cia Pé de Pano nos palcos
        e nas ruas do interior de Minas Gerais.</p>
        <div class="grid grid-3">
{galeria}
        </div>
        <p class="credito-fotos">Fotos: Lucas Rocha</p>
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
    intro = ("Acompanhe aqui a agenda do Ponto de Cultura Quintal das Pretas, da Cia Pé "
             "de Pano e os compromissos institucionais de seus representantes. Este espaço "
             "reúne nossa programação artística, ações formativas, encontros, apresentações, "
             "participações em eventos e atividades que fortalecem a cultura, a memória, a "
             "identidade de nossa comunidade e as nossas parcerias institucionais. Fique por "
             "dentro e caminhe conosco nessa trajetória de arte, educação e transformação social.")
    conteudo = page_hero(
        "Agenda",
        "Caminhe conosco",
        "Programação artística, ações formativas, encontros e compromissos institucionais "
        "do Quintal das Pretas e da Cia Pé de Pano.",
    ) + f"""
    <section class="secao linho">
      <div class="container">
        <span class="olho">Nossa programação</span>
        <h2 class="secao-titulo">Próximos eventos</h2>
        <p class="secao-intro">{intro}</p>

        <!-- A lista é montada automaticamente a partir de data/eventos.json.
             Para adicionar um evento, edite esse arquivo (veja data/COMO-ADICIONAR-EVENTOS.md). -->
        <ul class="timeline" id="agenda-lista" data-fonte="data/eventos.json" hidden></ul>
        <p class="secao-intro" id="agenda-status">Carregando agenda…</p>
        <div class="agenda-vazia" id="agenda-vazia" hidden>
          <div class="agenda-cena" aria-hidden="true">
            <span class="agenda-sol"></span>
            <span class="agenda-cordao"></span>
            <span class="agenda-luz luz-1"></span>
            <span class="agenda-luz luz-2"></span>
            <span class="agenda-luz luz-3"></span>
            <span class="agenda-luz luz-4"></span>
            <span class="agenda-folha folha-1"></span>
            <span class="agenda-folha folha-2"></span>
            <span class="agenda-folha folha-3"></span>
            <span class="agenda-banco"></span>
            <span class="agenda-ritmo ritmo-1"></span>
            <span class="agenda-ritmo ritmo-2"></span>
            <span class="agenda-ritmo ritmo-3"></span>
            <span class="agenda-tambor"><i></i></span>
          </div>
          <div class="agenda-vazia-texto">
            <span class="olho">Enquanto a próxima roda não começa</span>
            <h3>O quintal está preparando novos encontros</h3>
            <p>Em breve chegam novas datas de espetáculos, oficinas e rodas de conversa.
            Até lá, acompanhe os bastidores e as novidades pelas nossas redes.</p>
            <a class="btn btn-terra" href="https://instagram.com/quintaldaspretas"
               target="_blank" rel="noopener">Acompanhar no Instagram</a>
          </div>
        </div>
        <noscript><p class="secao-intro">Ative o JavaScript para ver a programação,
        ou acompanhe nossos eventos pelas redes sociais.</p></noscript>
      </div>
    </section>
"""
    return layout(
        "Agenda",
        "Agenda de espetáculos, oficinas, encontros e compromissos do Quintal das Pretas e da Cia Pé de Pano.",
        "agenda.html",
        conteudo,
    )


# ---------------------------------------------------------------------------
# NOTÍCIAS
# ---------------------------------------------------------------------------
def page_noticias():
    intro = ("O Quintal se renova para acolher ainda mais histórias. O Quintal segue "
             "crescendo, criando e transformando. É com esse espírito que fortalecemos "
             "parcerias e construímos novos caminhos, ampliando nossa rede de afeto, cultura "
             "e transformação social. Cada nova colaboração representa uma oportunidade de "
             "desenvolver projetos que valorizam a diversidade, promovem o diálogo e dão "
             "visibilidade a vozes e narrativas que merecem ser ouvidas. Juntos, seguimos "
             "semeando ideias, compartilhando saberes e cultivando iniciativas capazes de "
             "gerar impacto positivo em nossa comunidade.")
    conteudo = page_hero(
        "Notícias",
        "Novidades do quintal",
        "Acompanhe as histórias, parcerias e conquistas que florescem no Quintal das Pretas.",
    ) + f"""
    <section class="secao linho">
      <div class="container">
        <span class="olho">Feed</span>
        <h2 class="secao-titulo">Últimas notícias</h2>
        <p class="secao-intro">{intro}</p>

        <!-- O mosaico é montado a partir de data/noticias.json.
             Para publicar uma notícia, edite esse arquivo (veja data/COMO-ADICIONAR-NOTICIAS.md). -->
        <div class="grid grid-3" id="noticias-lista" data-fonte="data/noticias.json" hidden></div>
        <p class="secao-intro" id="noticias-status">Carregando notícias…</p>
        <noscript><p class="secao-intro">Ative o JavaScript para ver as notícias,
        ou acompanhe nossas redes sociais.</p></noscript>
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
    STATUS = {
        "ativo":      ("grupo-ativo", "tag-ativo", "Ativo · Em andamento"),
        "inicio":     ("grupo-inicio", "tag-inicio", "No início"),
        "conclusao":  ("grupo-conclusao", "tag-conclusao", "Em andamento · Fase de conclusão"),
        "naoiniciou": ("grupo-naoiniciou", "tag-naoiniciou", "Ainda não iniciou"),
    }
    GRUPOS = [
        ("ativo", "Ativos / Em andamento"),
        ("inicio", "No início"),
        ("conclusao", "Em andamento / Fase de conclusão"),
        ("naoiniciou", "Ainda não iniciados"),
    ]

    projetos = [
        {
            "titulo": "Videocast Papo de Quintal",
            "status": "ativo",
            "financiamento": "PNAB — Política Nacional Aldir Blanc (Estado de Minas Gerais)",
            "paragrafos": [
                "O Papo de Quintal nasceu de uma ideia concebida em 2021 pelo Quintal das "
                "Pretas, com o propósito de criar um espaço de diálogo, escuta e valorização "
                "das histórias, saberes e trajetórias que fortalecem a identidade e a memória "
                "da comunidade. Apresentado pela personagem Repórter Edileuza, o videocast foi "
                "pensado como um ambiente acolhedor e divertido para compartilhar experiências "
                "inspiradoras e promover reflexões sobre cultura, ancestralidade, cidadania e "
                "transformação social. O nome do videocast foi uma sugestão da atriz Polly "
                "Andreys e a personagem Edileuza foi criada em 2005 pela atriz Ita Ferreira.",
                "A sua primeira temporada foi produzida institucionalmente no final de 2024, "
                "por meio de recursos da Política Nacional Aldir Blanc (PNAB), através do "
                "município de Matozinhos. Composta por cinco episódios, a temporada destacou "
                "histórias de vida, desafios e conquistas de mulheres pretas atuantes em "
                "diferentes profissões, evidenciando suas contribuições para a sociedade e "
                "inspirando novas gerações.",
                "Mais do que um programa de entrevistas, o Papo de Quintal é um espaço de "
                "encontro entre memórias, experiências e perspectivas diversas, reafirmando o "
                "compromisso do Quintal das Pretas com a valorização das vozes negras, a "
                "promoção da diversidade e o fortalecimento da cultura local e regional.",
            ],
        },
        {
            "titulo": "Manutenção de Atividades Artístico-Culturais — FEC",
            "status": "ativo",
            "financiamento": "Edital FEC 12/2025 — FAOP / SECULT-MG",
            "paragrafos": [
                "O recurso foi adquirido via edital FEC 12/2025 para manutenção e ampliação da "
                "programação artística oferecida gratuitamente à comunidade no Ponto de Cultura "
                "Quintal das Pretas. Também, para iniciar a campanha de modernização do local "
                "com a elaboração dos projetos arquitetônicos e técnicos para oferecer melhorias "
                "no espaço com mais segurança e acessibilidade para os beneficiários.",
            ],
            "extratos": [
                {"titulo": "Extrato de Termo de Compromisso", "texto": '''Termo de Compromisso FAOP/FOMENTO nº. 128632284/2025 celebrado entre a associação quintal das pretas e a Secretaria de Estado de Cultura e Turismo - SECULT, por intermédio da Fundação de Arte de Ouro Preto - FAOP
Objeto: Constitui objeto do presente Termo de Compromisso do(a) BENEFICIÁRIO(A) cuja proposta foi aprovada em 17/11/2025 e classificada no Edital FEC 12/2025 – EDITAL FAOP-FEC 12/2025 – MANUTENÇÃO DE ATIVIDADES ARTÍSTICO-CULTURAIS DE ORGANIZAÇÕES DA SOCIEDADE CIVIL, na(s) categoria(s) prevista(s) no(s) inciso(s) I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII, XIV do art. 7º da Lei Estadual 24.462/2023.
Valor: R$100.000,00
Data da assinatura: 03/12/2025.
Vigência: 12 meses.'''},
            ],
        },
        {
            "titulo": "Projeto Quintal Aprendiz",
            "status": "conclusao",
            "financiamento": "Lei Federal 13.019/2014 — Termos de Fomento 52, 53 e 54/2025 "
                             "(Sec. Mun. de Cultura, Esporte, Turismo e Lazer) · R$ 42.000,00",
            "paragrafos": [
                "O Projeto Quintal Aprendiz é uma iniciativa do Quintal das Pretas que, desde "
                "agosto de 2025, oferece gratuitamente à comunidade oficinas, palestras, rodas "
                "de conversa, eventos culturais e apresentações artísticas, promovendo o acesso "
                "à cultura, à formação cidadã e ao fortalecimento dos vínculos comunitários. As "
                "atividades atendem moradores do entorno do Ponto de Cultura, estudantes e "
                "escolas locais, ampliando oportunidades de aprendizado, convivência e "
                "valorização das identidades culturais.",
                "O projeto integra um conjunto de ações desenvolvidas em parceria com os "
                "projetos “Apoio à Estruturação da Cia Pé de Pano” e “Apoio e Estruturação do "
                "Quintal das Pretas e da Cia Pé de Pano”, estes para aquisição de materiais para "
                "as oficinas, instrumentos e material de apoio, fortalecendo a atuação cultural, "
                "educativa e artística da instituição no município de Matozinhos.",
                "As iniciativas foram viabilizadas por meio de recursos decorrentes do Processo "
                "de Exceção de Chamamento Público nº 08/EI52/25, da Secretaria Municipal de "
                "Cultura, Esporte, Turismo e Lazer, sob a regência da Lei Federal nº 13.019/2014 "
                "e suas alterações, bem como do Decreto Municipal nº 3.006/2016. O investimento "
                "total de R$ 42.000,00 foi distribuído entre os Termos de Fomento nº 52/2025, "
                "53/2025 e 54/2025, garantindo a realização das atividades e contribuindo para o "
                "fortalecimento das ações culturais permanentes desenvolvidas pelo Quintal das "
                "Pretas e pela Cia. Pé de Pano.",
            ],
        },
        {
            "titulo": "Territórios do Axé — a Ancestralidade Viva em Pedro Leopoldo",
            "status": "inicio",
            "financiamento": "Ministério da Cultura (MinC) — Lei 13.019/2014",
            "extratos": [
                {"titulo": "Extrato do Termo de Fomento — Ministério da Cultura (SEI 2885645) — Plataforma Transferegov.br nº 994283",
                 "texto": '''Em cumprimento às orientações publicadas no site do MinC e ao art. 11, da Lei 13.019/2014 (in verbis) que trata “Da Transparência e do Controle” e do § 4º, inciso II,  do Art. 42 do Decreto 8.726/2016, serão disponibilizadas no site www.quintaldaspretas.com.br e em rede social da Associação Quintal das Pretas (@quintaldaspretas as informações relativas às parcerias celebradas com a Administração Pública.
O objeto do presente Termo de Fomento é a execução do projeto “Territórios do Axé – A Ancestralidade Viva em Pedro Leopoldo”, através ações de promoção das culturas tradicionais e populares”, visando a consecução de finalidade de interesse público e recíproco, conforme especificações estabelecidas no plano de trabalho.
Parceria - Ministério da Cultura/Secretária de Cidadania e Diversidade Cultural, representada pela Secretária de Cidadania e Diversidade Cultural, Sra. Márcia Helena Gonçalves e Associação Quintal das Pretas, CNPJ 05.769.374/0001-90, representada por sua Presidente, Sra. Giovane Ferreira da Cruz.
Valor total: R$ 300.000,00 (trezentos mil reais)
Prazo de vigência: 12 meses (prazo prorrogado para 10/06/2027)
Data da assinatura: 18/05/2026
Prestação de Contas: Em até 90 dias após a vigência'''},
            ],
        },
        {
            "titulo": "Arte da Terra: Formação Artística no Quintal das Pretas",
            "status": "naoiniciou", "financiamento": "FUNARTE", "aguardando": True,
        },
        {
            "titulo": "Manutenção de Programação Artística",
            "status": "inicio",
            "financiamento": "Município de Matozinhos — Emendas Impositivas EI 13/2026 e EI 14/2026",
            "extratos": [
                {"titulo": "Extrato — Termo de Fomento de Emenda Impositiva nº EI. 13/2026",
                 "texto": '''DECORRENTE DE PROCESSO DE EXCEÇÃO DE CHAMAMENTO PÚBLICO Nº 13/2026, DA SECRETARIA MUNICIPAL DE CULTURA, ESPORTE, TURISMO E LAZER, que resultou na publicação do EXTRATO DE JUSTIFICATIVA DE EXCEÇÃO DE CHAMAMENTO PÚBLICO DE CHAMAMENTO PÚBLICO (fundamentado art. 29, da Lei Federal nº 13.019/14 e Decreto Municipal nº 3.006/16).
Fundamento legal para publicação do extrato: Art.41 §1º do Decreto 3006/2016.
Objeto: Constitui o Termo de Fomento nº 13/2026 apoio na execução do Plano de Trabalho “Manutenção da programação artística do Ponto de Cultura Quintal das Pretas - promoção de oficinas artísticas-culturais e rodas de conversa”.
Parceria - Município de Matozinhos, com interveniência Secretaria Municipal de Cultura, Esporte, Turismo e Lazer, representada pelo Secretário Municipal Walice Carvalho dos Santos e a Associação Quintal das Pretas, CNPJ 05.769.374/0001-90, representada por sua Presidente, Sra. Giovane Ferreira da Cruz.
Valor total: R$ 20.000,00 (vinte mil reais)
Prazo de vigência: 31 de dezembro de 2026
Data da assinatura: 02/06/2026
Prestação de Contas: Em até 30 dias após a vigência'''},
                {"titulo": "Extrato — Termo de Fomento de Emenda Impositiva nº EI. 14/2026",
                 "texto": '''DECORRENTE DE PROCESSO DE EXCEÇÃO DE CHAMAMENTO PÚBLICO Nº 14/2026, DA SECRETARIA MUNICIPAL DE CULTURA, ESPORTE, TURISMO E LAZER, que resultou na publicação do EXTRATO DE JUSTIFICATIVA DE EXCEÇÃO DE CHAMAMENTO PÚBLICO DE CHAMAMENTO PÚBLICO (fundamentado art. 29, da Lei Federal nº 13.019/14 e Decreto Municipal nº 3.006/16).
Fundamento legal para publicação do extrato: Art.41 §1º do Decreto 3006/2016.
Objeto: Constitui o Termo de Fomento nº 14/2026 apoio na execução do Plano de Trabalho “Manutenção da programação artística do Ponto de Cultura Quintal das Pretas - promoção de rodas de conversa com fazedores de cultura e representantes políticos do município”.
Parceria - Município de Matozinhos, com interveniência Secretaria Municipal de Cultura, Esporte, Turismo e Lazer, representada pelo Secretário Municipal Walice Carvalho dos Santos e a Associação Quintal das Pretas, CNPJ 05.769.374/0001-90, representada por sua Presidente, Sra. Giovane Ferreira da Cruz.
Valor total: R$ 6.000,00 (seis mil reais)
Prazo de vigência: 31 de dezembro de 2026
Data da assinatura: 02/06/2026
Prestação de Contas: Em até 30 dias após a vigência'''},
            ],
        },
        {
            "titulo": "Escola Livre de Teatro",
            "status": "naoiniciou", "financiamento": None, "em_breve": True,
        },
    ]

    def tags_html(p):
        _, classe_tag, status_label = STATUS[p["status"]]
        fin = (f'<span class="tag tag-financiamento">Financiamento: {p["financiamento"]}</span>'
               if p.get("financiamento") else "")
        return (f'<div class="projeto-tags"><span class="tag {classe_tag}">{status_label}</span>'
                f'{fin}</div>')

    def bloco_detalhado(p):
        paras = "\n".join(f"<p>{par}</p>" for par in p.get("paragrafos", []))
        extratos = ""
        for ex in p.get("extratos", []):
            # texto reproduzido VERBATIM (sem alteração): cada linha vira um parágrafo
            linhas = "\n".join(
                f"<p>{ln}</p>" for ln in ex["texto"].split("\n") if ln.strip()
            )
            extratos += (f'<div class="extrato"><h4>{ex["titulo"]}</h4>'
                         f'<div class="extrato-texto">{linhas}</div></div>')
        return f"""<article class="projeto-detalhe card">
          <div class="card-corpo">
            {tags_html(p)}
            <h3>{p["titulo"]}</h3>
            {paras}
            {extratos}
          </div>
        </article>"""

    def card_compacto(p):
        if p.get("aguardando"):
            nota = ("Informações detalhadas serão divulgadas após a assinatura dos termos. "
                    "Em breve, novidades.")
        elif p.get("em_breve"):
            nota = "Projeto em planejamento. Em breve, mais informações."
        else:
            nota = ""
        return f"""<article class="card projeto-card">
          <div class="card-corpo">
            {tags_html(p)}
            <h3>{p["titulo"]}</h3>
            <p class="card-resumo">{nota}</p>
          </div>
        </article>"""

    secoes = []
    for status, nome in GRUPOS:
        do_grupo = [p for p in projetos if p["status"] == status]
        if not do_grupo:
            continue
        classe_grupo = STATUS[status][0]
        detalhados = [p for p in do_grupo if p.get("paragrafos") or p.get("extratos")]
        compactos = [p for p in do_grupo if not (p.get("paragrafos") or p.get("extratos"))]
        partes = [bloco_detalhado(p) for p in detalhados]
        if compactos:
            cards = "\n".join(card_compacto(p) for p in compactos)
            partes.append(f'<div class="grid grid-3">\n{cards}\n</div>')
        corpo = "\n".join(partes)
        secoes.append(f"""<div class="status-grupo {classe_grupo}">
          <h2>{nome}</h2>
{corpo}
        </div>""")
    secoes_html = "\n".join(secoes)

    conteudo = page_hero(
        "Projetos",
        "Onde a criação ganha forma",
        "Nossos projetos são sementes de encontros, ideias e transformações que florescem no "
        "Quintal. Cada iniciativa nasce do desejo de fortalecer vínculos, valorizar narrativas "
        "e abrir caminhos para novas possibilidades de expressão artística e social. Aqui, o "
        "fazer coletivo é central, e cada projeto se constrói no diálogo entre pessoas, "
        "territórios e saberes, gerando experiências que inspiram, acolhem e deixam marcas "
        "duradouras.",
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
        <p>Apoie a continuidade e a ampliação dessas ações culturais, gratuitas e abertas
        à comunidade.</p>
        <a class="btn btn-terra btn-cta" href="apoie.html">Quero apoiar</a>
      </div>
    </section>
"""
    return layout(
        "Projetos",
        "Projetos do Quintal das Pretas: Papo de Quintal, Quintal Aprendiz, Manutenção de "
        "Atividades Artístico-Culturais (FEC), Territórios do Axé e mais.",
        "projetos.html",
        conteudo,
    )


# ---------------------------------------------------------------------------
# APOIE
# ---------------------------------------------------------------------------
def page_apoie():
    formas = [
        ("📜", "Leis de Incentivo à Cultura",
         "Empresas e pessoas podem destinar parte do imposto devido a projetos do Quintal "
         "das Pretas por meio das leis de incentivo à cultura. É uma forma de fortalecer a "
         "arte sem custo adicional, transformando tributo em formação, espetáculos e memória. "
         "Fale com a gente para conhecer os projetos aptos a captar.", "Quero incentivar"),
        ("💸", "Doação direta (PIX)",
         "Em breve você poderá apoiar diretamente, com qualquer valor, via PIX. Cada doação "
         "ajuda a manter oficinas, espetáculos e encontros gratuitos para a comunidade. A "
         "chave será divulgada aqui em breve.", "Falar conosco"),
        ("🤝", "Parcerias corporativas",
         "Sua empresa ou instituição pode se tornar parceira do Quintal, apoiando projetos, "
         "eventos e a manutenção do espaço. Construímos parcerias sob medida, com "
         "contrapartidas e visibilidade, sempre alinhadas a valores de diversidade e impacto "
         "social.", "Seja parceiro"),
        ("🙌", "Voluntariado",
         "Doar tempo e talento também transforma. Seja na produção de eventos, nas oficinas, "
         "na comunicação ou no cuidado com o espaço, há sempre lugar para mais mãos no "
         "quintal. Venha somar.", "Ser voluntárie"),
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
        "Sua contribuição mantém viva uma cultura que é de todos. Apoie o Quintal das Pretas "
        "e ajude a semear arte, memória e transformação na nossa comunidade.",
    ) + f"""
    <section class="secao linho">
      <div class="container">
        <span class="olho">Como apoiar</span>
        <h2 class="secao-titulo">Cada gesto rega o quintal</h2>
        <p class="secao-intro">Manter um Ponto de Cultura vivo é um trabalho coletivo. Toda a
        nossa programação é gratuita e aberta à comunidade, e só existe graças a quem acredita
        e caminha junto. Há muitas formas de fazer parte: escolha a sua.</p>
        <div class="grid grid-2">
{cards}
        </div>

        <div class="pix-box">
          <div>
            <strong>Doação via PIX</strong><br />
            <span class="pix-chave">Indisponível no momento</span>
          </div>
          <span class="pix-aviso">Será liberado em breve 🌱</span>
        </div>
      </div>
    </section>

    <section class="faixa-cta">
      <div class="container">
        <h2>Seu apoio sustenta a cultura</h2>
        <p>Cada gesto, grande ou pequeno, ajuda a manter o Quintal das Pretas de portas
        abertas para toda a comunidade.</p>
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
        "Fale com o Quintal das Pretas e a Cia Pé de Pano. Tire dúvidas, proponha parcerias "
        "ou venha caminhar conosco nessa trajetória de arte, educação e transformação social.",
    ) + f"""
    <section class="secao linho">
      <div class="container">
        <div class="split" style="align-items:start">
          <div>
            <span class="olho">Envie uma mensagem</span>
            <h2 class="secao-titulo">Fale com o quintal</h2>
            <form id="form-contato" class="form-grid"
                  action="https://formsubmit.co/quintaldaspretas2015@gmail.com" method="POST">
              <input type="hidden" name="_subject" value="Nova mensagem pelo site — Quintal das Pretas" />
              <input type="hidden" name="_template" value="table" />
              <input type="hidden" name="_captcha" value="false" />
              <input type="hidden" name="_next" value="https://thyfanixs.github.io/quintal-das-pretas/obrigado.html" />
              <input type="text" name="_honey" tabindex="-1" autocomplete="off"
                     aria-hidden="true" style="position:absolute;left:-9999px" />
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
                <a href="mailto:quintaldaspretas2015@gmail.com">quintaldaspretas2015@gmail.com</a></div>
            </div>
            <div class="info-item">
              <span class="icone" aria-hidden="true">📍</span>
              <div><strong>Endereço</strong><br />Rua Dona Balá, 32, Floresta, Matozinhos, MG</div>
            </div>
            <div class="info-item">
              <span class="icone" aria-hidden="true">🔗</span>
              <div><strong>Redes sociais</strong><br />
                <span class="redes">
                  <a href="https://instagram.com/quintaldaspretas" target="_blank" rel="noopener">@quintaldaspretas</a>
                  <a href="https://instagram.com/ciapedepano_oficial" target="_blank" rel="noopener">@ciapedepano_oficial</a>
                  <a href="https://www.youtube.com/@ciapedepano_matozinhos1996" target="_blank" rel="noopener">YouTube</a>
                </span>
              </div>
            </div>
            <iframe class="mapa" title="Mapa: Rua Dona Balá, 32, Floresta, Matozinhos - MG"
              src="https://maps.google.com/maps?q=Rua%20Dona%20Bal%C3%A1%2C%2032%2C%20Floresta%2C%20Matozinhos%20-%20MG&z=16&output=embed"
              loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
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


# ---------------------------------------------------------------------------
# PAINEL — gerador de evento (página NÃO listada no menu)
# ---------------------------------------------------------------------------
def page_painel():
    conteudo = page_hero(
        "Área da equipe",
        "Gerador de eventos",
        "Ferramenta interna: preencha os campos e copie o texto gerado para colar "
        "no arquivo data/eventos.json no GitHub. Nada é publicado por aqui — o evento "
        "só vai ao ar depois do commit no repositório.",
    ) + """
    <section class="secao linho">
      <div class="container" style="max-width:760px">
        <span class="olho">Passo 1 — preencher</span>
        <h2 class="secao-titulo">Dados do evento</h2>
        <form id="gerador-evento" class="form-grid" novalidate>
          <div class="campo">
            <label for="g-data">Data *</label>
            <input type="date" id="g-data" required />
          </div>
          <div class="campo">
            <label for="g-titulo">Título *</label>
            <input type="text" id="g-titulo" required placeholder="Ex.: Espetáculo Chico Rei" />
          </div>
          <div class="campo">
            <label for="g-local">Local</label>
            <input type="text" id="g-local" placeholder="Ex.: Praça de Matozinhos (MG)" />
          </div>
          <div class="campo">
            <label for="g-imagem">Imagem (caminho do arquivo enviado)</label>
            <input type="text" id="g-imagem" placeholder="assets/img/agenda/chico-rei.jpg" />
          </div>
          <div class="campo">
            <label for="g-link">Link (ingressos / inscrição)</label>
            <input type="url" id="g-link" placeholder="https://..." />
          </div>
          <div class="campo">
            <label for="g-descricao">Descrição</label>
            <textarea id="g-descricao" placeholder="Breve descrição do evento (opcional)."></textarea>
          </div>
          <button type="submit" class="btn btn-terra">Gerar texto do evento</button>
        </form>
      </div>
    </section>

    <section class="secao areia">
      <div class="container" style="max-width:760px">
        <span class="olho">Passo 2 — copiar e colar no GitHub</span>
        <h2 class="secao-titulo">Texto gerado</h2>
        <p class="secao-intro">Copie o bloco abaixo e cole dentro dos colchetes
        <code>[ ]</code> do arquivo <strong>data/eventos.json</strong>. Se já houver
        outros eventos, coloque uma <strong>vírgula</strong> entre eles.</p>
        <pre id="evento-saida" class="saida-codigo" aria-live="polite">— preencha o formulário acima e clique em “Gerar”. —</pre>
        <div style="display:flex;gap:.8rem;flex-wrap:wrap;margin-top:1rem">
          <button type="button" class="btn btn-verde" id="copiar-evento">Copiar texto</button>
          <a class="btn btn-primario" href="https://github.com/thyfanixs/quintal-das-pretas/edit/main/data/eventos.json" target="_blank" rel="noopener">Abrir eventos.json no GitHub</a>
        </div>
        <p class="secao-intro" style="margin-top:1.4rem;font-size:.9rem">
          Guia completo em <code>data/COMO-ADICIONAR-EVENTOS.md</code>.</p>
      </div>
    </section>
"""
    return layout(
        "Área da equipe",
        "Ferramenta interna para gerar eventos da agenda.",
        "",  # não corresponde a nenhuma aba do menu
        conteudo,
    )


def page_obrigado():
    conteudo = """
    <section class="secao linho">
      <div class="container" style="max-width:680px;text-align:center;padding-block:2rem">
        <div class="obrigado-selo" aria-hidden="true">🌱</div>
        <span class="olho" style="display:block">Recebemos sua mensagem</span>
        <h1 class="secao-titulo">Obrigado por falar com o Quintal das Pretas</h1>
        <p class="secao-intro" style="margin-inline:auto">Sua mensagem foi enviada com
        sucesso. Em breve a nossa equipe entrará em contato. Seguimos juntos, cultivando
        cultura, memória e afeto.</p>
        <p style="margin-top:1.6rem">
          <a class="btn btn-terra" href="index.html">Voltar ao início</a>
          <a class="btn btn-verde" href="agenda.html">Ver a agenda</a>
        </p>
      </div>
    </section>
"""
    return layout(
        "Mensagem enviada",
        "Obrigado por entrar em contato com o Quintal das Pretas.",
        "",  # fora do menu
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
    "adicionar-evento.html": page_painel,  # página interna, fora do menu
    "obrigado.html": page_obrigado,        # destino do formulário, fora do menu
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
