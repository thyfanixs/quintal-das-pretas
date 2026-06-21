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
    "data": "2026-06-14",
    "titulo": "Quintal firma nova parceria cultural",
    "resumo": "Breve resumo da notícia que aparece no card.",
    "imagem": "assets/img/noticias/parceria.jpg",
    "link": "https://link-da-materia-ou-post"
  }
]
```

## Regras
- **`data`** (AAAA-MM-DD) e **`titulo`** são obrigatórios.
- **`resumo`**, **`imagem`** e **`link`** são opcionais.
- Vírgula entre os blocos; nenhuma depois do último.
- Em caso de erro, confira o JSON em https://jsonlint.com
