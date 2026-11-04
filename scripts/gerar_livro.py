#!/usr/bin/env python3
"""Junta todos os arquivos .md do repositório em um único Markdown (livro/_livro.md),
pronto para o pandoc gerar o HTML/PDF.

- Ordem: README da raiz (introdução) -> cada seção numerada (README da seção + arquivos).
- Cada seção vira um capítulo (#), cada arquivo vira um subcapítulo (##).
- Links entre arquivos viram links internos do livro.
- Caminhos de imagens são corrigidos para a raiz do repositório.
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join(RAIZ, "livro", "_livro.md")
SECOES = sorted(d for d in os.listdir(RAIZ)
                if os.path.isdir(os.path.join(RAIZ, d)) and re.match(r"^\d\d-", d)) + ["anexos"]

LINK_MD = re.compile(r"\]\(((?:\.\./)?(?:[\w.-]+/)*[\w.-]+\.md)(#[^)]+)?\)")
METADADOS = """---
title: "Repositório do Fim do Mundo"
subtitle: "Manual prático de sobrevivência, autossuficiência e reconstrução — Brasil"
lang: pt-BR
---

"""
IMG = re.compile(r"(!\[[^\]]*\]\()(img/)")


def ident(caminho_rel):
    """ID estável de um arquivo: '02-saude/04-medicamentos-e-doses.md' -> 'arq-02-saude-04-medicamentos-e-doses'."""
    caminho_rel = caminho_rel.replace(os.sep, "/")
    if caminho_rel.endswith("README.md"):
        base = caminho_rel[: -len("README.md")].strip("/") or "inicio"
        return "sec-" + base
    return "arq-" + caminho_rel[:-3].replace("/", "-")


def resolve(dir_atual, alvo):
    caminho = os.path.normpath(os.path.join(dir_atual, alvo))
    return os.path.relpath(caminho, RAIZ)


def processa(caminho_rel, nivel_extra):
    dir_atual = os.path.dirname(os.path.join(RAIZ, caminho_rel))
    with open(os.path.join(RAIZ, caminho_rel), encoding="utf-8") as f:
        linhas = f.read().splitlines()
    saida, em_codigo, primeiro_titulo = [], False, True
    for linha in linhas:
        if linha.strip().startswith("```"):
            em_codigo = not em_codigo
            saida.append(linha)
            continue
        if not em_codigo:
            m = re.match(r"^(#{1,6})\s+(.*)$", linha)
            if m:
                nivel = min(6, len(m.group(1)) + nivel_extra)
                texto = m.group(2)
                if primeiro_titulo:
                    texto += " {#" + ident(caminho_rel) + "}"
                    primeiro_titulo = False
                linha = "#" * nivel + " " + texto
            # imagens: img/x.svg -> secao/img/x.svg
            pasta = os.path.relpath(dir_atual, RAIZ)
            linha = IMG.sub(lambda mm: mm.group(1) + (pasta + "/img/" if pasta != "." else "img/"), linha)

            # links para outros .md -> âncora interna
            def troca(mm):
                alvo, ancora = mm.group(1), mm.group(2)
                if alvo.startswith("http"):
                    return mm.group(0)
                rel = resolve(dir_atual, alvo)
                if not os.path.exists(os.path.join(RAIZ, rel)):
                    return mm.group(0)
                return "](" + (ancora if ancora else "#" + ident(rel)) + ")"
            linha = LINK_MD.sub(troca, linha)
            # links para pastas (ex.: (00-emergencia/)) -> âncora da seção
            linha = re.sub(r"\]\((?:\.\./)?(\d\d-[\w-]+|anexos|livro)/\)",
                           lambda mm: "](#sec-" + mm.group(1) + ")" if mm.group(1) != "livro" else mm.group(0), linha)
        saida.append(linha)
    return "\n".join(saida)


def main():
    partes = []
    # Introdução: README da raiz, sem o índice geral (o livro tem sumário próprio)
    intro = processa("README.md", 0)
    intro = re.split(r"\n## Índice geral", intro)[0]
    intro = re.sub(r"^# .*\n", "", intro, count=1)  # o título já vem dos metadados
    partes.append(METADADOS + intro)
    for secao in SECOES:
        pasta = os.path.join(RAIZ, secao)
        if not os.path.isdir(pasta):
            continue
        if os.path.exists(os.path.join(pasta, "README.md")):
            partes.append("\n\n" + processa(f"{secao}/README.md", 0))
        for arq in sorted(os.listdir(pasta)):
            if arq.endswith(".md") and arq != "README.md":
                partes.append("\n\n" + processa(f"{secao}/{arq}", 1))
    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    with open(SAIDA, "w", encoding="utf-8") as f:
        f.write("\n".join(partes) + "\n")
    print(SAIDA)


if __name__ == "__main__":
    sys.exit(main())
