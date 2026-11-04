#!/usr/bin/env python3
"""Verifica links relativos e imagens quebrados em todos os .md do repositório.
Uso: python3 scripts/checar_links.py   (sai com código 1 se encontrar problemas)
"""
import os
import re
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)\)")


def ancora(titulo):
    """Aproxima a regra do GitHub para gerar âncoras de títulos."""
    t = titulo.strip().lower()
    t = re.sub(r"[^\w\- ]", "", t, flags=re.UNICODE)
    return t.replace(" ", "-")


def ancoras_do_arquivo(caminho):
    res, em_codigo = set(), False
    with open(caminho, encoding="utf-8") as f:
        for linha in f:
            if linha.strip().startswith("```"):
                em_codigo = not em_codigo
            elif not em_codigo:
                m = re.match(r"^#{1,6}\s+(.*)$", linha)
                if m:
                    res.add(ancora(unicodedata.normalize("NFC", m.group(1))))
    return res


def main():
    problemas = 0
    for pasta, _, arquivos in os.walk(RAIZ):
        if "/." in pasta or "/livro" in pasta or "/node_modules" in pasta:
            continue
        for arq in arquivos:
            if not arq.endswith(".md"):
                continue
            caminho = os.path.join(pasta, arq)
            texto = open(caminho, encoding="utf-8").read()
            texto = re.sub(r"```.*?```", "", texto, flags=re.S)
            for alvo in LINK.findall(texto):
                if alvo.startswith(("http://", "https://", "mailto:")):
                    continue
                arquivo, _, anc = alvo.partition("#")
                destino = os.path.normpath(os.path.join(pasta, arquivo)) if arquivo else caminho
                rel = os.path.relpath(caminho, RAIZ)
                if not os.path.exists(destino):
                    print(f"QUEBRADO  {rel}: {alvo}")
                    problemas += 1
                elif anc and destino.endswith(".md"):
                    if unicodedata.normalize("NFC", anc) not in ancoras_do_arquivo(destino):
                        print(f"ÂNCORA?   {rel}: {alvo}")
                        problemas += 1
    print(f"\n{problemas} problema(s) encontrado(s).")
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main())
