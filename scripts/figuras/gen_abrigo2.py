import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
# Figuras de 07-abrigo-e-construcao/02-construcao-com-terra.md
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "07-abrigo-e-construcao", "img") + "/"
os.makedirs(D, exist_ok=True)
WOOD = "#8b5a2b"; SOLO = "#e8d3b0"; AGUA = "#4a90d9"; AGUA2 = "#cfe6fb"; VERDE = "#2b8a3e"; PERIGO = "#d62828"
BARRO = "#a9764a"; ADOBE = "#c9955f"; REBOCO = "#e9dcc3"; CAL = "#fbfaf5"; PEDRA = "#9a9a9a"

def ln(x1, y1, x2, y2, c=OUT, w=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"{d}/>'
def rc(x, y, w, h, fill, stroke=OUT, sw=2, rx=0):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def pg(pts, fill, stroke=OUT, sw=2, op=None):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    o = f' fill-opacity="{op}"' if op is not None else ''
    return f'<polygon points="{p}" fill="{fill}"{o} stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'
def pl(pts, c=OUT, w=2, dash=None):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<polyline points="{p}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{d}/>'
def ci(cx, cy, r, fill, stroke=OUT, sw=2):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def tl(x, y, linhas, size=12, color="#222", bold=False, anchor="start", dy=None):
    dy = dy or size * 1.3
    return "".join(text(x, y + i * dy, s, size, color, bold, anchor) for i, s in enumerate(linhas))
def num(x, y, n, cor="#3f6d9e"):
    return ci(x, y, 11, cor, OUT, 1.5) + text(x, y + 4.5, str(n), 12.5, "#fff", True, "middle")
def pontos(x, y, w, h, n, cor, seed=1, r=1.6):
    import random; R = random.Random(seed)
    return "".join(f'<circle cx="{x + R.random()*w:.1f}" cy="{y + R.random()*h:.1f}" r="{r}" fill="{cor}"/>' for _ in range(n))

# =====================================================================
# 1) TESTE DO POTE
# =====================================================================
b = []
# pote
jx, jy, jw, jb = 60, 96, 140, 388
b.append(rc(jx - 4, jy - 18, jw + 8, 20, "#777", OUT, 2, 4))            # tampa
b.append(f'<path d="M{jx} {jy} L{jx} {jb-14} Q{jx} {jb} {jx+14} {jb} L{jx+jw-14} {jb} Q{jx+jw} {jb} {jx+jw} {jb-14} L{jx+jw} {jy} Z" fill="#f4f8fb" stroke="{OUT}" stroke-width="3"/>')
ib = jb - 6
# camadas (total de sedimento = 120 px = "10 cm")
ya, ys, yc = ib - 72, ib - 96, ib - 120
b.append(f'<path d="M{jx+3} {ya} L{jx+3} {ib-10} Q{jx+3} {ib} {jx+13} {ib} L{jx+jw-13} {ib} Q{jx+jw-3} {ib} {jx+jw-3} {ib-10} L{jx+jw-3} {ya} Z" fill="#dcbc7c"/>')
b.append(pontos(jx + 6, ya + 3, jw - 12, 64, 140, "#9c7c40", 4, 1.7))
b.append(rc(jx + 3, ys, jw - 6, 24, "#b39470", "none", 0))
b.append(pontos(jx + 6, ys + 3, jw - 12, 18, 60, "#8a7050", 5, 0.9))
b.append(rc(jx + 3, yc, jw - 6, 24, "#8f5f45", "none", 0))
b.append(rc(jx + 3, jy + 30, jw - 6, yc - jy - 30, "#d6e7f3", "none", 0))
for (x, y) in ((80, 130), (104, 128), (150, 131), (172, 129), (128, 133)):
    b.append(rc(x, y, 9, 3, "#3b2a1a", "none", 0))
b.append(ln(jx + 3, jy + 30, jx + jw - 3, jy + 30, AGUA, 2))
# réguas e rótulos
for y in (ib, ya, ys, yc):
    b.append(ln(jx + jw + 4, y, jx + jw + 26, y, "#444", 1.5))
b.append(ln(jx + jw + 18, yc, jx + jw + 18, ib, "#444", 1.5))
b += [tl(232, ib - 40, ["AREIA — 6 cm = 60%", "assenta em ~1 minuto"], 12, "#6b4a10", True)]
b += [tl(232, ys + 4, ["SILTE — 2 cm = 20%", "em ~2 horas"], 12, "#5a4630", True)]
b += [tl(232, yc - 22, ["ARGILA — 2 cm = 20%", "em 1–2 dias (água clareia)"], 12, "#6e3a22", True)]
b.append(ln(228, yc - 4, jx + jw + 28, yc + 12, "#6e3a22", 1.5))
b += [tl(232, 140, ["água", "(turva até a argila assentar)"], 11.5, "#2a5d91")]
b += [tl(232, 104, ["restos de raiz e folha boiando"], 11, "#444")]
b.append(text(jx + jw / 2, jb + 20, "total de terra assentada: 10 cm", 11.5, "#222", True, "middle"))
# passos
b.append(ln(440, 56, 440, 400, "#ddd", 1.5))
b.append(text(452, 66, "Como fazer", 14, "#222", True))
passos = [["Pote de vidro liso e reto (~1 L).", "Encha 1/3 com terra peneirada,", "tirada a 30–50 cm de fundura."],
          ["Complete com água até 3/4.", "1 colher (chá) de sal ajuda", "a argila a assentar."],
          ["Tampe e agite forte por", "2 minutos. Deixe parado em", "lugar plano, sem mexer."],
          ["Marque com caneta a areia", "(1 min), o silte (2 h) e a", "argila (quando a água clarear)."]]
for i, ps in enumerate(passos):
    y = 96 + i * 76
    b.append(num(462, y - 4, i + 1)); b += [tl(480, y, ps, 11.5, "#222")]
# caixa de interpretação
b.append(box(14, 418, 652, 126, "#eef5ff", "#3f6d9e"))
b.append(text(26, 438, "Conta: % = altura da camada ÷ altura total × 100.", 12, "#1e3a5f", True))
b.append(text(26, 455, "O teste é aproximado: confirme sempre fazendo tijolos de prova.", 11.5, "#1e3a5f"))
cols = [("#b3001b", "ARGILA abaixo de 10%", ["terra fraca, esfarela.", "Junte terra argilosa ou", "use cal/cimento."]),
        ("#1f6b2e", "ARGILA de 10% a 30%", ["boa para adobe, taipa,", "cob e superadobe.", "Ajuste com o teste."]),
        ("#b3001b", "ARGILA acima de 30%", ["racha ao secar.", "Misture areia e palha", "(serve p/ pau-a-pique)."])]
for i, (cor, t, ls) in enumerate(cols):
    x = 30 + i * 214
    b.append(text(x, 480, t, 12, cor, True)); b += [tl(x, 498, ls, 11.5, "#222")]
open(D + "teste-pote.svg", "w").write(svg(680, 554, "Teste do pote: quanto de areia, silte e argila tem a terra", "\n".join(b)))

# =====================================================================
# 2) ADOBE: FORMA E SECAGEM
# =====================================================================
b = []
b.append(text(20, 62, "1. A forma (sem fundo)", 14, "#222", True))
k = 5.0                       # px por cm
x0, y0 = 70, 210              # canto de baixo, frente, esquerda (lado de fora)
L, W, H, E = 35 * k, 20 * k, 10 * k, 2.5 * k   # externo: 35 x 20 x 10; tábua 2,5
def ob(dp):  # deslocamento oblíquo para a profundidade (cm)
    return (dp * k * 0.6, -dp * k * 0.45)
dx, dy = ob(20)
A = (x0, y0 - H); B = (x0 + L, y0 - H)
# alças (atrás)
for sx in (-1, 1):
    hx = x0 - 46 if sx < 0 else x0 + L
    ex, ey = ob(17.5)
    b.append(rc(hx + ex, y0 - H + 8 + ey, 46, 16, WOOD, OUT, 2, 7))
# topo (aro)
b.append(pg([A, B, (B[0] + dx, B[1] + dy), (A[0] + dx, A[1] + dy)], "#b07a45"))
# abertura interna
i1 = (A[0] + E + ob(2.5)[0], A[1] + ob(2.5)[1])
i2 = (B[0] - E + ob(2.5)[0], B[1] + ob(2.5)[1])
ix, iy = ob(15)
b.append(pg([i1, i2, (i2[0] + ix, i2[1] + iy), (i1[0] + ix, i1[1] + iy)], "#5b3a1a"))
b.append(pg([(i1[0], i1[1] + 26), (i2[0], i2[1] + 26), (i2[0] + ix, i2[1] + iy + 26), (i1[0] + ix, i1[1] + iy + 26)], SOLO, "none", 0, 0.9))
# lateral direita e frente
b.append(pg([B, (B[0] + dx, B[1] + dy), (x0 + L + dx, y0 + dy), (x0 + L, y0)], "#7a4c22"))
b.append(rc(x0, y0 - H, L, H, WOOD, OUT, 2.5))
for yy in (y0 - H + 16, y0 - H + 34):
    b.append(ln(x0 + 6, yy, x0 + L - 6, yy, "#6a4320", 1))
# alças (frente)
b.append(rc(x0 - 46, y0 - H + 8, 46, 16, WOOD, OUT, 2, 7)); b.append(rc(x0 + L, y0 - H + 8, 46, 16, WOOD, OUT, 2, 7))
# medidas
b.append(ln(x0 + E, y0 + 14, x0 + L - E, y0 + 14, "#b3001b", 1.5)); b.append(ln(x0 + E, y0 + 8, x0 + E, y0 + 20, "#b3001b", 1.5)); b.append(ln(x0 + L - E, y0 + 8, x0 + L - E, y0 + 20, "#b3001b", 1.5))
b.append(text(x0 + L / 2, y0 + 32, "30 cm (por dentro)", 12, "#b3001b", True, "middle"))
b.append(ln(x0 - 14, y0 - H, x0 - 14, y0, "#b3001b", 1.5)); b.append(text(x0 - 18, y0 - H / 2 + 20, "10 cm", 12, "#b3001b", True, "end"))
b.append(text(x0 + L + dx + 6, y0 - H + dy / 2 + 34, "15 cm", 12, "#b3001b", True))
b.append(text(x0 + L + dx + 6, y0 - H + dy / 2 + 48, "(por dentro)", 10.5, "#b3001b"))
b += [tl(36, 268, ["tábuas de 2,5 cm; alças nas pontas.", "Tijolo pronto: ~30 × 15 × 10 cm, ~8 kg."], 11.5, "#222")]
# passos de moldar
b.append(ln(372, 50, 372, 300, "#ddd", 1.5))
b.append(text(386, 62, "2. Moldar", 14, "#222", True))
mold = [["Terreiro plano, varrido e", "polvilhado com areia."], ["Molhe a forma e passe areia", "por dentro (solta fácil)."],
        ["Jogue bolas de barro COM FORÇA", "para encher bem os cantos."], ["Rase com a mão molhada ou", "uma régua; tire o excesso."],
        ["Levante a forma reto para cima.", "Lave e repita ao lado."]]
for i, ls in enumerate(mold):
    y = 90 + i * 44
    b.append(num(396, y - 4, i + 1)); b += [tl(414, y, ls, 11.5)]
b.append(ln(14, 312, 666, 312, "#ccc", 1))
# secagem
b.append(text(20, 336, "3. Secar à sombra (2 a 4 semanas no total)", 14, "#222", True))
def tijolo(x, y, w, h):
    return rc(x, y, w, h, ADOBE, OUT, 1.8, 2)
GY = 470
for xx in (14, 236, 458):
    b.append(rc(xx, GY, 208, 10, SOLO, "none", 0)); b.append(ln(xx, GY, xx + 208, GY, "#6b4f2a", 2.5))
# (a) deitados sob sombra
b.append(pg([(20, 384), (214, 384), (206, 376), (28, 376)], "#c9b27a", OUT, 1.5))
b.append(ln(30, 384, 30, GY, WOOD, 4)); b.append(ln(204, 384, 204, GY, WOOD, 4))
for i in range(4):
    b.append(tijolo(42 + i * 40, GY - 14, 34, 14))
b += [tl(20, 362, ["a) 2–3 dias deitados"], 12, "#222", True)]
b += [tl(20, 496, ["sob cobertura de palha ou lona,", "sem sol forte nem chuva"], 11, "#444")]
# (b) de lado
for i in range(5):
    b.append(tijolo(256 + i * 36, GY - 34, 14, 34))
b += [tl(242, 362, ["b) firmou (não afunda com", "o dedo): vire de lado e", "raspe as rebarbas"], 12, "#222", True)]
b += [tl(242, 496, ["2–4 dias depois de moldar"], 11, "#444")]
# (c) pilha em grade
bx0 = 478
b.append(rc(bx0, GY - 10, 168, 10, WOOD, OUT, 1.5))
for r in range(4):
    y = GY - 10 - (r + 1) * 17
    if r % 2 == 0:
        for i in range(4):
            b.append(tijolo(bx0 + 4 + i * 41, y, 36, 14))
    else:
        for i in range(7):
            b.append(tijolo(bx0 + 6 + i * 23, y, 13, 14))
b.append(pg([(468, GY - 88), (656, GY - 88), (648, GY - 98), (476, GY - 98)], "#c9b27a", OUT, 1.5))
b += [tl(464, 362, ["c) pilha em grade, coberta"], 12, "#222", True)]
b += [tl(464, 496, ["vãos de 2 cm, sobre tábuas,", "até completar 2–4 semanas.", "Pronto: cor clara por igual", "e som seco ao bater."], 11, "#444")]
open(D + "adobe.svg", "w").write(svg(680, 548, "Adobe: forma, moldagem e secagem", "\n".join(b)))

# =====================================================================
# 3) PAU-A-PIQUE EM CORTE
# =====================================================================
b = []
b.append(text(20, 60, "Vista de frente: as 3 etapas", 14, "#222", True))
GY = 452
b.append(rc(0, GY, 680, 50, SOLO, "none", 0)); b.append(ln(0, GY, 680, GY, "#6b4f2a", 3))
# fundação de pedra (alta)
fx0, fx1, ftop = 64, 396, 404
b.append(rc(fx0, ftop, fx1 - fx0, GY + 30 - ftop, "#b5b5b5", OUT, 2))
import random; R = random.Random(9)
for row in range(4):
    y = ftop + 2 + row * 19
    x = fx0 + 2 + (row % 2) * 16
    while x < fx1 - 12:
        w = 26 + R.random() * 14
        w = min(w, fx1 - 2 - x)
        b.append(rc(x, y, w - 3, 16, "#a3a3a3", "#666", 1.2, 5)); x += w
b.append(rc(fx0, ftop - 16, fx1 - fx0, 16, WOOD, OUT, 2))   # baldrame
# esteios e frechal
top, bot = 96, ftop - 16
b.append(rc(70, 92, 20, bot - 92, WOOD, OUT, 2)); b.append(rc(370, 92, 20, bot - 92, WOOD, OUT, 2))
b.append(rc(64, 80, 332, 16, WOOD, OUT, 2))
# zona 1: trama
z1a, z1b = 90, 178
for x in range(98, 178, 22):
    b.append(ln(x, top, x, bot, "#a0784a", 5))
for y in range(top + 12, bot, 18):
    b.append(ln(z1a, y, z1b, y, "#c9a36a", 4))
# zona 2: barro com trincas
z2a, z2b = 178, 274
b.append(rc(z2a, top, z2b - z2a, bot - top, BARRO, "none", 0))
b.append(pontos(z2a + 4, top + 4, z2b - z2a - 8, bot - top - 8, 110, "#7c5230", 11, 1.4))
for (x, y) in ((196, 180), (236, 230), (204, 290), (246, 320)):
    b.append(pl([(x, y), (x + 8, y + 12), (x + 3, y + 22), (x + 10, y + 34)], "#3b2412", 2))
# zona 3: reboco e cal
z3a, z3b = 274, 370
b.append(rc(z3a, top, z3b - z3a, bot - top, REBOCO, "none", 0))
b.append(rc(z3a + 40, top, z3b - z3a - 40, bot - top, CAL, "none", 0))
b.append(ln(z3a + 40, top, z3a + 40, bot, "#d6c8ac", 1.5))
for x in (z2a, z3a):
    b.append(ln(x, top, x, bot, "#555", 1.5, "6 4"))
# números e nomes das etapas
b.append(num(134, 124, 1)); b.append(rc(110, 140, 50, 18, "#fff", "none", 0)); b.append(text(135, 153, "trama", 12, "#222", True, "middle"))
b.append(num(226, 124, 2, "#b3001b")); b.append(text(226, 153, "barro", 12, "#fff", True, "middle"))
b.append(num(322, 124, 3)); b += [tl(322, 153, ["reboco", "+ cal"], 12, "#222", True, "middle")]
b += [tl(184, 366, ["trincas da", "1ª secagem"], 10.5, "#fff", True)]
b.append(text(70, 74, "frechal (viga de cima)", 11, "#222", True))
b += [tl(4, 420, ["fundação", "de pedra"], 10.5, "#222", True)]
b.append(ln(50, 426, 70, 434, "#555", 1.2))
# cota: base da parede acima do chão
b.append(ln(404, bot, 404, GY, "#b3001b", 1.5)); b.append(ln(399, bot, 409, bot, "#b3001b", 1.5)); b.append(ln(399, GY, 409, GY, "#b3001b", 1.5))
b.append(f'<text x="424" y="{(bot+GY)/2:.0f}" font-size="11" fill="#b3001b" font-weight="bold" text-anchor="middle" transform="rotate(-90 424 {(bot+GY)/2:.0f})">30–50 cm</text>')
# corte lateral (direita)
b.append(ln(438, 50, 438, 446, "#ddd", 1.5))
b.append(text(556, 60, "Corte: bota e chapéu", 14, "#222", True, "middle"))
cx = 514
b.append(rc(cx - 30, ftop, 60, GY + 30 - ftop, "#b5b5b5", OUT, 2))
b.append(rc(cx - 22, ftop - 16, 44, 16, WOOD, OUT, 2))
wt = top + 30
b.append(rc(cx - 16, wt, 32, bot - wt, BARRO, "none", 0))
b.append(rc(cx - 4, wt, 8, bot - wt, "#a0784a", "none", 0))
for y in range(wt + 10, bot, 18):
    b.append(ci(cx - 11, y, 3.5, "#c9a36a", OUT, 1)); b.append(ci(cx + 11, y, 3.5, "#c9a36a", OUT, 1))
b.append(rc(cx - 22, wt, 6, bot - wt, CAL, OUT, 1)); b.append(rc(cx + 16, wt, 6, bot - wt, CAL, OUT, 1))
b.append(rc(cx - 22, top + 16, 44, 14, WOOD, OUT, 2))   # frechal
# telhado com beiral
b.append(pg([(cx - 60, top - 4), (cx + 140, top + 52), (cx + 140, top + 62), (cx - 60, top + 6)], "#c8553d", OUT, 2))
b.append(ln(cx + 22, top + 78, cx + 140, top + 78, "#b3001b", 1.5))
b.append(ln(cx + 22, top + 72, cx + 22, top + 84, "#b3001b", 1.5)); b.append(ln(cx + 140, top + 72, cx + 140, top + 84, "#b3001b", 1.5))
b += [tl(cx + 81, top + 98, ["beiral", "60–100 cm"], 11, "#b3001b", True, "middle")]
for i in range(6):
    y = top + 120 + i * 36
    b.append(ln(cx + 146, y, cx + 146, y + 16, AGUA, 3))
b += [tl(cx + 40, top + 190, ["a chuva", "pinga longe", "da parede"], 11, "#1d5fa8", True)]
b += [tl(446, 210, ["reboco", "dos dois", "lados"], 11, "#222", True)]
b.append(ln(480, 236, cx - 24, 250, "#555", 1.2))
b.append(pg([(cx + 30, GY - 3), (cx + 136, GY + 3), (cx + 136, GY + 11), (cx + 30, GY + 7)], "#bbb", OUT, 1.5))
b += [tl(cx + 40, 380, ["calçada com", "caimento", "para fora"], 11, "#222", True)]
b.append(ln(cx + 70, 410, cx + 82, GY - 2, "#555", 1.2))
# legenda das etapas
b += [tl(16, 524, ["1. Trama: varas verticais a cada 20–30 cm; ripas ou bambu rachado dos dois lados, a cada 10–15 cm, amarrados."], 11, "#222")]
b += [tl(16, 540, ["2. Barro (terra + areia + palha) jogado com força dos dois lados ao mesmo tempo. Secou e rachou: encha as trincas."], 11, "#222")]
b += [tl(16, 556, ["3. Reboco de terra e cal em 2 camadas, liso, sem fresta; por fim pintura de cal (caiação)."], 11, "#222")]
# alerta barbeiro
b.append(box(14, 570, 652, 64, "#fff0f0", "#d62828"))
bx, by = 60, 602
b.append(f'<ellipse cx="{bx}" cy="{by}" rx="26" ry="11" fill="#2b1d14" stroke="{OUT}" stroke-width="1.5"/>')
for i in range(5):
    b.append(rc(bx - 20 + i * 9, by - 12, 5, 3, "#e8862a", "none", 0)); b.append(rc(bx - 20 + i * 9, by + 9, 5, 3, "#e8862a", "none", 0))
b.append(f'<ellipse cx="{bx+34}" cy="{by}" rx="11" ry="3.5" fill="#2b1d14" stroke="{OUT}" stroke-width="1.2"/>')
for (x1, y1, x2, y2) in ((bx - 8, by - 10, bx - 16, by - 22), (bx + 6, by - 10, bx + 12, by - 22), (bx - 8, by + 10, bx - 16, by + 22), (bx + 6, by + 10, bx + 12, by + 22), (bx + 14, by - 8, bx + 24, by - 18), (bx + 14, by + 8, bx + 24, by + 18)):
    b.append(ln(x1, y1, x2, y2, "#2b1d14", 2))
b += [tl(116, 592, ["BARBEIRO (doença de Chagas) mora em trinca de parede sem reboco, telhado de palha,",
                    "galinheiro e pilha de lenha. Reboque liso, tape frestas, caie, e mantenha galinheiro",
                    "e lenha longe da casa. Inseto de 2–3 cm, achatado, cabeça fina, bordas listradas."], 11, "#7a0010", False, "start", 14)]
open(D + "pau-a-pique.svg", "w").write(svg(680, 644, "Pau-a-pique (taipa de mão) bem feito", "\n".join(b)))
print("ok")
