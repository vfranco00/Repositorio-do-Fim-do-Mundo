#!/usr/bin/env bash
# Gera o livro único (HTML e PDF) a partir de todos os arquivos .md.
# Requisitos: python3, pandoc (>= 2.19). Para o PDF: node + playwright (Chromium).
set -euo pipefail
export LC_ALL=C.UTF-8 LANG=C.UTF-8
cd "$(dirname "$0")/.."

echo "1/3 Juntando os arquivos..."
python3 scripts/gerar_livro.py >/dev/null

echo "2/3 Gerando HTML..."
pandoc livro/_livro.md \
  --from markdown+header_attributes-implicit_figures \
  --to html5 --standalone --embed-resources \
  --toc --toc-depth=2 \
  --css scripts/livro.css \
  --resource-path=. \
  -o livro/fim-do-mundo.html
echo "   livro/fim-do-mundo.html"

echo "3/3 Gerando PDF..."
if command -v node >/dev/null 2>&1; then
  NODE_PATH="${NODE_PATH:-$(npm root -g 2>/dev/null || true)}" node scripts/pdf.js livro/fim-do-mundo.html livro/fim-do-mundo.pdf \
    || echo "   (PDF não gerado: instale o playwright ou abra o HTML no navegador e use Imprimir > Salvar como PDF)"
else
  echo "   (sem node: abra livro/fim-do-mundo.html no navegador e use Imprimir > Salvar como PDF)"
fi
rm -f livro/_livro.md
echo "Pronto."
