# Quintal das Pretas — Arquitetura de Informação & Diretrizes Visuais

> Documento-guia do site institucional **Quintal das Pretas**
> URL: [www.quintaldaspretas.com.br](https://www.quintaldaspretas.com.br)
> Conceito: cultura, ancestralidade e arte com a identidade do interior de Minas Gerais
> (regiões de **Pedro Leopoldo** e **Matozinhos**).
>
> **Status do conteúdo:** textos provisórios em *Lorem Ipsum* (placeholders).
> As imagens são representadas por *placeholders* até a chegada do material definitivo.

---

## 1. Mapa do Site (Sitemap)

```
www.quintaldaspretas.com.br
│
├── / (Home)                         index.html
│     └── Portal de entrada: hero ancestral, destaques, atalhos para as 7 seções
│
├── 1. Quem Somos                    quem-somos.html
│     ├── História
│     ├── Missão & Valores
│     └── Idealizadoras (galeria)
│
├── 2. Cia Pé de Pano                cia-pe-de-pano.html
│     ├── Destaque "30 anos de teatro no interior de Minas Gerais"
│     ├── Histórico do grupo
│     └── Portfólio cênico (galerias de espetáculos)
│
├── 3. Agenda                        agenda.html
│     └── Linha do tempo / lista de eventos
│           (data · evento · local · CTA "Mais Informações/Ingressos")
│
├── 4. Notícias                      noticias.html
│     └── Feed em mosaico de cards
│           (imagem · título · data · resumo)
│
├── 5. Projetos                      projetos.html
│     ├── Ativos / Em andamento
│     ├── No início
│     ├── Em conclusão
│     └── Ainda não iniciados
│
├── 6. Apoie                         apoie.html
│     ├── Leis de Incentivo à Cultura
│     ├── Doação direta (PIX)
│     ├── Parcerias corporativas
│     └── Voluntariado
│
└── 7. Contato                       contato.html
      ├── Formulário (Nome · E-mail · Assunto · Mensagem)
      ├── E-mail institucional
      ├── Redes sociais (Instagram, YouTube)
      └── Mapa de localização
```

O menu superior contém **7 abas principais**. O logotipo retorna sempre à Home.

---

## 2. Arquitetura de Informação por Seção

### 1. Quem Somos
Espaço institucional para contar a **história, missão e valores**. Layout
equilibrado entre blocos de texto e *placeholders* para fotos do espaço e das
idealizadoras. Tom acolhedor, em primeira pessoa coletiva.

### 2. Cia Pé de Pano
Página da companhia de teatro, com **destaque visual forte** para a celebração
dos **30 anos de teatro no interior de Minas Gerais**. Layout estilo portfólio
cênico: galerias de espetáculos + histórico do grupo em linha do tempo.

### 3. Agenda
Seção dinâmica em **formato de linha do tempo / lista de eventos**. Cada item
exibe **data, nome do evento/espetáculo, local** e um botão
**"Mais Informações/Ingressos"**. Filtro por mês/categoria.

### 4. Notícias
**Feed/blog em cards (mosaico)** com imagem de destaque, título, data e breve
resumo. Pensado para crescimento (paginação ou "carregar mais").

### 5. Projetos — *área central e mais robusta*
Projetos categorizados visualmente pelo **status atual**, com **tags coloridas**
e divisões por subtítulos:

| Projeto | Financiamento | Status |
|---|---|---|
| Territórios do Axé — a Ancestralidade Viva em Pedro Leopoldo | MINC | Ainda não iniciou |
| Arte da Terra: Formação Artística no Quintal das Pretas | FUNARTE | Ainda não iniciou |
| Manutenção de Programação Artística | Prefeitura de Matozinhos | Ainda não iniciou |
| Cia Pé de Pano — 30 anos de teatro no interior de Minas Gerais | FEC/2025 | No início |
| Videocast Papo de Quintal | — | Ativo / Em andamento |
| Quintal Aprendiz | — | Finalizando / Fase de conclusão |

**Convenção de cores das tags de status:**
- 🟢 **Ativo / Em andamento** — verde-folha
- 🟡 **No início** — amarelo-ouro/mostarda
- 🟠 **Finalizando / Fase de conclusão** — terracota
- ⚪ **Ainda não iniciou** — neutro/argila clara

### 6. Apoie
Seção de captação e engajamento com blocos explicativos para **Leis de Incentivo
à Cultura, doação via PIX, parcerias corporativas e voluntariado**, cada um com
**CTA em destaque**.

### 7. Contato
**Formulário** (Nome, E-mail, Assunto, Mensagem), **e-mail institucional**,
**links de redes sociais** (Instagram, YouTube) e **mapa de localização** da
região integrado.

---

## 3. Diretrizes Estéticas e Visuais

### Conceito
O design deve **respirar cultura, ancestralidade e arte**, evocando **calor,
acolhimento e ancestralidade**. Evita-se o que é puramente corporativo, frio ou
minimalista-tecnológico. O "quintal" é a metáfora: chão de terra, luz dourada,
ervas, roda, oralidade.

### Paleta de Cores
| Token | Hex | Uso |
|---|---|---|
| `--terracota` | `#B5532A` | Terra/argila — chão do quintal, destaques quentes |
| `--terracota-escuro` | `#8A3D1E` | Hover, sombras quentes |
| `--mostarda` | `#E0A526` | Luz, axé — chamadas e acentos |
| `--ouro` | `#C9881A` | Detalhes dourados |
| `--verde-folha` | `#4A6B3A` | Natureza/ervas — apoio e status ativo |
| `--verde-escuro` | `#2F4626` | Texto sobre claro, rodapé |
| `--preto-quente` | `#1E1813` | Contraste e legibilidade (preto amarronzado) |
| `--linho` | `#F4E9D6` | Fundo base (tecido linho/areia) |
| `--areia` | `#EAD9BE` | Blocos alternados |

### Tipografia
- **Títulos:** serifada com personalidade (display) — `Playfair Display`, fallback `Georgia, serif`.
- **Corpo:** sans humanista e legível — `Mulish` / `Nunito Sans`, fallback `system-ui, sans-serif`.
- Hierarquia generosa, entrelinhas largas, sensação de respiro.

### Elementos Gráficos & Texturas
- Texturas sutis de **barro, palha, madeira, chita e linho** (padrões SVG/CSS leves).
- **Grafismos afro-brasileiros** (geometrias tipo adinkra/kente) nas
  **divisórias de seção** e ornamentos.
- Cantos levemente orgânicos, sombras quentes e suaves (nunca duras/neutras).
- Imagens com leve textura/borda artesanal.

### Acessibilidade
- Contraste mínimo AA entre texto e fundo (preto-quente sobre linho/areia).
- Navegação por teclado, `:focus-visible` evidente, `alt` em todas as imagens.
- Áreas de toque ≥ 44px no mobile.

---

## 4. Estrutura Técnica de Arquivos

```
quintal-das-pretas/
├── index.html                 Home
├── quem-somos.html
├── cia-pe-de-pano.html
├── agenda.html
├── noticias.html
├── projetos.html
├── apoie.html
├── contato.html
├── build.py                   Gerador estático (cabeçalho/rodapé DRY)
├── ARQUITETURA.md             Este documento
└── assets/
    ├── css/style.css          Design system + estilos
    ├── js/main.js             Menu mobile, filtros, formulário
    └── img/                    Imagens definitivas (futuro)
```

As páginas são geradas por `build.py` a partir de um layout único, garantindo
cabeçalho, menu e rodapé idênticos em todas as abas. Para regenerar:

```bash
python3 build.py
```

> Site **estático** (HTML/CSS/JS), sem dependências de build externas — abre
> direto no navegador e é fácil de hospedar.
