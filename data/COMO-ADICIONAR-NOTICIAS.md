# Como publicar notícias

As notícias ficam no arquivo **`data/noticias.json`**. A página `noticias.html` lê
esse arquivo e monta o mosaico sozinha — **sem mexer no código nem regerar o site**.
As mais recentes aparecem primeiro (ordenadas pela data).

## Passo a passo (pela web do GitHub)
1. (Opcional) Suba a imagem de destaque em **`assets/img/noticias/`**.
2. Abra **`data/noticias.json`** e clique no lápis (Edit).
3. Adicione um bloco `{ ... }` dentro dos colchetes `[ ]`, separando por vírgula.
4. Commit (na branch `main`). Pronto.

## Modelo
```json
[
  {
    "id": "nova-parceria-cultural",
    "data": "2026-06-14",
    "titulo": "Quintal firma nova parceria cultural",
    "resumo": "Breve resumo da notícia que aparece no card.",
    "imagem": "assets/img/noticias/parceria.jpg",
    "conteudo": [
      "Primeiro parágrafo do texto completo.",
      "Segundo parágrafo."
    ],
    "galeria": [
      { "imagem": "assets/img/noticias/parceria-01.jpg", "alt": "Descrição da foto" }
    ],
    "botoes": [
      { "rotulo": "Baixar o documento (PDF)", "link": "assets/docs/documento.pdf" },
      { "rotulo": "Fazer inscrição", "link": "https://forms.gle/..." }
    ]
  }
]
```

## Regras
- **`data`** (AAAA-MM-DD) e **`titulo`** são obrigatórios.
- **`id`**: nome curto, sem espaços nem acentos (ex.: `nova-parceria-cultural`). Com ele, o
  card abre a notícia completa no próprio site. Sem `id`, o card leva para o **`link`** externo.
- **`resumo`**, **`imagem`**, **`conteudo`** (lista de parágrafos), **`galeria`** (fotos),
  **`botoes`** (links em destaque no fim da notícia) e **`link`** são opcionais.
- **`destaque`: true** fixa a notícia no topo da lista (use em uma notícia por vez).
- PDFs e outros documentos ficam em **`assets/docs/`**.
- Vírgula entre os blocos; nenhuma depois do último.
- Em caso de erro, confira o JSON em https://jsonlint.com
