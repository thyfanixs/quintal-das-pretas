#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificador de links do site Quintal das Pretas.

Percorre todos os .html e checa:
  - links internos (href para .html) — o arquivo existe?
  - assets (src/href para css, js, svg, img) — o arquivo existe?
  - âncoras internas (#id) — o id existe na página?
  - links externos (http/https), mailto e tel — listados para conferência manual

Uso:  python3 check_links.py
Saída: relatório no terminal + arquivo CHECKLIST-LINKS.md
"""

import os
import re
import html
from html.parser import HTMLParser

BASE = os.path.dirname(os.path.abspath(__file__))
PAGINAS = sorted(p for p in os.listdir(BASE) if p.endswith(".html"))


class Coletor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []   # (tipo, valor)
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if d.get("id"):
            self.ids.add(d["id"])
        if tag == "a" and d.get("href"):
            self.links.append(("href", d["href"]))
        if tag in ("link", "script", "img") and d.get("src"):
            self.links.append(("src", d["src"]))
        if tag == "link" and d.get("href"):
            self.links.append(("asset", d["href"]))
        if tag == "script" and d.get("src"):
            self.links.append(("asset", d["src"]))


def classifica(valor):
    if valor.startswith(("http://", "https://")):
        return "externo"
    if valor.startswith("mailto:"):
        return "email"
    if valor.startswith("tel:"):
        return "tel"
    if valor.startswith("#"):
        return "ancora"
    return "interno"


def main():
    total_ok = 0
    total_falhas = 0
    falhas = []
    externos = set()
    emails = set()
    placeholders = {}

    linhas = ["# Checklist de Links — Quintal das Pretas", ""]
    linhas.append("> Gerado por `check_links.py`. ✅ = ok · ❌ = quebrado · 🌐 = externo (conferir manualmente)")
    linhas.append("")

    for pagina in PAGINAS:
        caminho = os.path.join(BASE, pagina)
        with open(caminho, encoding="utf-8") as f:
            conteudo = f.read()
        c = Coletor()
        c.feed(conteudo)

        linhas.append(f"## {pagina}")
        vistos = set()
        for _tipo, valor in c.links:
            valor = html.unescape(valor)
            chave = valor
            if chave != "#" and chave in vistos:  # mantém todos os placeholders "#"
                continue
            vistos.add(chave)
            tipo = classifica(valor)

            if tipo == "externo":
                externos.add(valor)
                linhas.append(f"- 🌐 `{valor}` — externo (placeholder, conferir)")
            elif tipo == "email":
                emails.add(valor)
                linhas.append(f"- ✉️ `{valor}`")
            elif tipo == "tel":
                linhas.append(f"- 📞 `{valor}`")
            elif tipo == "ancora":
                aid = valor[1:]
                if aid == "":
                    placeholders[pagina] = placeholders.get(pagina, 0) + 1
                    linhas.append(f"- ⚠️ `#` — botão placeholder (destino a definir)")
                elif aid in c.ids:
                    total_ok += 1
                    linhas.append(f"- ✅ `{valor}` — âncora encontrada")
                else:
                    total_falhas += 1
                    falhas.append((pagina, valor, "âncora inexistente"))
                    linhas.append(f"- ❌ `{valor}` — âncora inexistente")
            else:  # interno (arquivo)
                alvo = valor.split("#")[0].split("?")[0]
                if alvo == "":
                    continue
                existe = os.path.exists(os.path.join(BASE, alvo))
                if existe:
                    total_ok += 1
                    linhas.append(f"- ✅ `{valor}`")
                else:
                    total_falhas += 1
                    falhas.append((pagina, valor, "arquivo não encontrado"))
                    linhas.append(f"- ❌ `{valor}` — arquivo não encontrado")
        linhas.append("")

    # Resumo de externos placeholder (#) — apontar os que ainda são "#"
    linhas.append("## Resumo")
    linhas.append("")
    total_ph = sum(placeholders.values())
    fontes = {e for e in externos if "fonts.googleapis" in e or "fonts.gstatic" in e}
    redes = sorted(externos - fontes)
    linhas.append(f"- Links internos/assets/âncoras válidos: **{total_ok}**")
    linhas.append(f"- Quebrados: **{total_falhas}**")
    linhas.append(f"- Botões placeholder `#` (destino a definir): **{total_ph}** "
                  f"({', '.join(f'{k}: {v}' for k, v in placeholders.items()) or 'nenhum'})")
    linhas.append(f"- Recursos externos OK (Google Fonts): **{len(fontes)}**")
    linhas.append(f"- Redes sociais a definir (URL real): **{len(redes)}** "
                  f"({', '.join(redes) or 'nenhum'})")
    linhas.append(f"- E-mails: {', '.join(sorted(emails)) or 'nenhum'}")
    linhas.append("")

    with open(os.path.join(BASE, "CHECKLIST-LINKS.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))

    print(f"Páginas verificadas: {len(PAGINAS)}")
    print(f"Válidos: {total_ok} | Quebrados: {total_falhas} | Placeholders #: {sum(placeholders.values())}")
    if falhas:
        print("\nQUEBRADOS:")
        for pag, val, motivo in falhas:
            print(f"  ❌ {pag}: {val} ({motivo})")
    else:
        print("Nenhum link interno/asset/âncora quebrado. ✅")
    print(f"\nExternos placeholder (#): conferir em CHECKLIST-LINKS.md")
    print("Relatório salvo em CHECKLIST-LINKS.md")


if __name__ == "__main__":
    main()
