# Quintal das Pretas

Site institucional cultural e comunitário do **Quintal das Pretas** — um espaço
de cultura, ancestralidade e arte no interior de Minas Gerais, entre **Pedro
Leopoldo** e **Matozinhos**.

🌐 [www.quintaldaspretas.com.br](https://www.quintaldaspretas.com.br)

> **Status:** estrutura (sitemap + arquitetura de informação + diretrizes
> visuais) com conteúdo provisório em *Lorem Ipsum* e imagens em *placeholder*,
> aguardando o material definitivo.

## Estrutura

Site **estático** (HTML + CSS + JS), sem dependências de build. As 8 páginas são
geradas a partir de um layout único para manter cabeçalho, menu e rodapé
consistentes.

| Página | Aba |
|---|---|
| `index.html` | Início (Home) |
| `quem-somos.html` | 1. Quem Somos |
| `cia-pe-de-pano.html` | 2. Cia Pé de Pano |
| `agenda.html` | 3. Agenda |
| `noticias.html` | 4. Notícias |
| `projetos.html` | 5. Projetos |
| `apoie.html` | 6. Apoie |
| `contato.html` | 7. Contato |

```
assets/css/style.css   Design system (paleta terrosa, texturas, grafismos)
assets/js/main.js      Menu mobile, formulário, utilidades
build.py               Gerador estático das páginas (DRY)
ARQUITETURA.md         Sitemap, arquitetura de informação e guia de estilo
```

## Como visualizar

Abra `index.html` diretamente no navegador, ou sirva localmente:

```bash
python3 -m http.server 8000
# acesse http://localhost:8000
```

## Como regenerar as páginas

Após editar conteúdo ou layout em `build.py`:

```bash
python3 build.py
```

## Identidade visual

Paleta terrosa e quente — terracota/argila, amarelo-ouro/mostarda, verde-folha e
preto para contraste — com texturas de linho/barro e grafismos afro-brasileiros
nas divisórias. Detalhes completos em [`ARQUITETURA.md`](ARQUITETURA.md).
