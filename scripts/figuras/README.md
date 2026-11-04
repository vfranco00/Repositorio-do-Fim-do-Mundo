# Figuras (diagramas SVG)

Os diagramas do repositório são desenhados por código, para ficarem nítidos na tela e na
impressão, leves e editáveis.

- `fig.py` — funções de desenho compartilhadas (figuras humanas com contorno, setas, textos, caixas).
- `gen_*.py` — um gerador por grupo de figuras; cada um grava os `.svg` na pasta `img/` da seção.
- `render.js` — gera uma folha PNG com vários SVGs para conferir visualmente.

Regerar tudo (a partir da raiz do repositório):

```bash
for g in scripts/figuras/gen_*.py; do python3 "$g"; done
```

Conferir visualmente (precisa de Node + Playwright):

```bash
NODE_PATH=$(npm root -g) node scripts/figuras/render.js /tmp/folha.png 02-saude/img/*.svg
```

Os SVGs de `01-agua/img/` foram escritos à mão (não têm gerador).
