# Como adicionar eventos na Agenda

Os eventos da Agenda ficam no arquivo **`data/eventos.json`**. A página
`agenda.html` lê esse arquivo e se monta sozinha — **não precisa mexer no código
nem regerar o site**. Eventos com data passada somem da lista automaticamente.

## Passo a passo (pela web do GitHub)

1. (Opcional) Suba a imagem do evento em **`assets/img/agenda/`**
   (Add file → Upload files). Ex.: `chico-rei.jpg`.
2. Abra **`data/eventos.json`** no GitHub e clique no lápis (Edit).
3. Adicione um bloco `{ ... }` dentro dos colchetes `[ ]`, **separando os eventos
   por vírgula**. Veja o modelo abaixo.
4. Commit changes (na branch `main`). Pronto — a agenda atualiza.

## Modelo de um evento

```json
[
  {
    "data": "2026-07-12",
    "titulo": "Espetáculo Chico Rei",
    "local": "Praça de Matozinhos (MG)",
    "imagem": "assets/img/agenda/chico-rei.jpg",
    "link": "https://link-dos-ingressos-ou-inscricao",
    "descricao": "Breve descrição do evento (opcional)."
  },
  {
    "data": "2026-08-03",
    "titulo": "Oficina de Teatro Comunitário",
    "local": "Sede do Quintal das Pretas — Matozinhos (MG)"
  }
]
```

## Regras importantes
- **`data`** é obrigatória e no formato **AAAA-MM-DD** (ano-mês-dia). É o que ordena e
  esconde eventos passados.
- **`titulo`** é obrigatório.
- **`local`**, **`imagem`**, **`link`** e **`descricao`** são **opcionais** — se não
  tiver, é só não incluir a linha.
- Cuidado com a vírgula: **entre** eventos tem vírgula; **depois do último não**.
- Todo texto entre aspas. Se o título tiver aspas, escreva `\"` no lugar.

> Dica: se a agenda sumir depois de uma edição, geralmente é uma vírgula a mais/menos
> no JSON. É só corrigir que ela volta. Cole o conteúdo em https://jsonlint.com para
> conferir se está válido.
