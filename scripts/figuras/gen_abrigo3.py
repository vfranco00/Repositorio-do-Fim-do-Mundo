import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
# Figuras de 07-abrigo-e-construcao/03-madeira-e-carpintaria.md e 04-alvenaria-cal-argamassas.md
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "07-abrigo-e-construcao", "img") + "/"
os.makedirs(D, exist_ok=True)
WOOD = "#8b5a2b"; WOOD2 = "#c08a52"; SOLO = "#e8d3b0"; AGUA = "#4a90d9"; AGUA2 = "#cfe6fb"; VERDE = "#2b8a3e"; PERIGO = "#d62828"
BAMBU = "#d8c26a"; BAMBU2 = "#b49b3c"; CONC = "#b5b5b5"

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
def marca_x(x, y):
    return ci(x, y, 10, PERIGO, OUT, 1.5) + ln(x - 4.5, y - 4.5, x + 4.5, y + 4.5, "#fff", 3) + ln(x - 4.5, y + 4.5, x + 4.5, y - 4.5, "#fff", 3)
def marca_ok(x, y):
    return ci(x, y, 10, VERDE, OUT, 1.5) + pl([(x - 5, y), (x - 1, y + 5), (x + 6, y - 5)], "#fff", 3)
def cota(x1, y1, x2, y2, label, dx=0, dy=-6, cor="#b3001b", size=11.5, anchor="middle"):
    import math
    a = math.atan2(y2 - y1, x2 - x1); nx, ny = -math.sin(a) * 5, math.cos(a) * 5
    s = ln(x1, y1, x2, y2, cor, 1.5) + ln(x1 - nx, y1 - ny, x1 + nx, y1 + ny, cor, 1.5) + ln(x2 - nx, y2 - ny, x2 + nx, y2 + ny, cor, 1.5)
    return s + text((x1 + x2) / 2 + dx, (y1 + y2) / 2 + dy, label, size, cor, True, anchor)

# =====================================================================
# 1) PILHA DE SECAGEM DE MADEIRA (tabiques)
# =====================================================================
b = []
GY = 330
b.append(rc(0, GY, 680, 30, SOLO, "none", 0)); b.append(ln(0, GY, 680, GY, "#6b4f2a", 3))
x0, x1 = 60, 470
# base: tocos/blocos
for x in (70, 190, 310, 430):
    b.append(rc(x, GY - 44, 30, 44, CONC, OUT, 2))
b.append(rc(x0, GY - 56, x1 - x0, 12, WOOD, OUT, 2))  # travessa de apoio
y = GY - 56
for camada in range(6):
    # tabiques alinhados
    y -= 9
    for x in (72, 192, 312, 432):
        b.append(rc(x, y, 12, 9, "#6a4320", OUT, 1.2))
    y -= 12
    b.append(rc(x0, y, x1 - x0, 12, WOOD2, OUT, 1.5))
    b.append(rc(x0, y, 7, 12, "#d62828", "none", 0)); b.append(rc(x1 - 7, y, 7, 12, "#d62828", "none", 0))
# telhado e peso
b.append(pg([(40, y - 14), (490, y - 14), (482, y - 26), (48, y - 26)], "#7a7a7a", OUT, 2))
b.append(rc(240, y - 46, 40, 20, "#9a9a9a", OUT, 2, 4)); b.append(text(260, y - 52, "peso", 11, "#222", True, "middle"))
# vento
for yy in (GY - 110, GY - 150):
    b.append(arrow(6, yy, 52, yy, "#4a90d9", 3))
b.append(text(4, GY - 168, "vento", 11, "#1d5fa8", True))
# rótulos
b.append(text(494, 86, "telhado ou chapa com", 11.5, "#222", True)); b.append(text(494, 100, "beiral + peso em cima", 11.5, "#222", True))
b.append(ln(492, 94, 470, y - 20, "#555", 1.2))
b += [tl(494, 150, ["tabiques: sarrafos SECOS", "de 2–2,5 cm, a cada", "40–60 cm, sempre um", "EM CIMA do outro"], 11.5, "#6a4320", True)]
b.append(ln(492, 160, 445, 200, "#555", 1.2))
b += [tl(494, 238, ["pontas pintadas", "(tinta, cera ou parafina):", "não racham"], 11.5, "#b3001b", True)]
b.append(ln(492, 244, 466, 250, "#555", 1.2))
b += [tl(494, 290, ["base nivelada,", "30–50 cm do chão"], 11.5, "#222", True)]
b.append(ln(492, 292, 462, 300, "#555", 1.2))
b.append(box(14, 368, 652, 52, "#eef5ff", "#3f6d9e"))
b += [text(26, 388, "Tempo de secagem ao ar: cerca de 1 ano para cada 2,5 cm de espessura (menos no calor seco).", 11.5, "#1e3a5f", True),
      text(26, 406, "Tabique fora de prumo = tábua empenada. Lugar ventilado e à sombra, longe do chão úmido e de cupins.", 11.5)]
open(D + "pilha-madeira.svg", "w").write(svg(680, 430, "Pilha para secar madeira (tábuas separadas por tabiques)", "\n".join(b)))

# =====================================================================
# 2) TESOURA DE TELHADO SIMPLES
# =====================================================================
b = []
import math
S = 80  # px por metro
xl, xr, yb = 110, 110 + 6 * S, 300
inc = 0.35
ap = ((xl + xr) / 2, yb - 3 * S * inc)
def barra(p1, p2, w, fill=WOOD2):
    a = math.atan2(p2[1] - p1[1], p2[0] - p1[0]); nx, ny = -math.sin(a) * w / 2, math.cos(a) * w / 2
    return pg([(p1[0] + nx, p1[1] + ny), (p2[0] + nx, p2[1] + ny), (p2[0] - nx, p2[1] - ny), (p1[0] - nx, p1[1] - ny)], fill, OUT, 2)
def marc(x, y, n):
    return ci(x, y, 10, "#fff", OUT, 1.8) + text(x, y + 4.5, str(n), 12.5, "#222", True, "middle")
# paredes
b.append(rc(xl - 16, yb + 8, 32, 64, "#d9cbb0", OUT, 2)); b.append(rc(xr - 16, yb + 8, 32, 64, "#d9cbb0", OUT, 2))
b.append(text(xl, yb + 88, "parede", 11, "#444", False, "middle")); b.append(text(xr, yb + 88, "parede", 11, "#444", False, "middle"))
# linha, pernas, pendural, escoras
b.append(rc(xl - 30, yb - 4, (xr - xl) + 60, 16, WOOD2, OUT, 2))
b.append(barra((xl - 26, yb + 2), ap, 14)); b.append(barra((xr + 26, yb + 2), ap, 14))
b.append(rc(ap[0] - 7, ap[1], 14, yb - ap[1] + 12, WOOD2, OUT, 2))
mL = ((xl + ap[0]) / 2, (yb + ap[1]) / 2); mR = ((xr + ap[0]) / 2, (yb + ap[1]) / 2)
b.append(barra((ap[0] - 6, yb - 6), (mL[0] + 6, mL[1] + 6), 11)); b.append(barra((ap[0] + 6, yb - 6), (mR[0] - 6, mR[1] + 6), 11))
# chapas metálicas nas emendas
for (x, y) in ((ap[0], ap[1] + 6), (ap[0], yb + 4), (xl, yb + 2), (xr, yb + 2)):
    b.append(rc(x - 11, y - 9, 22, 18, "#6c757d", OUT, 1.5, 2))
# terças
terL = []
for f in (0.08, 0.5, 0.92):
    for side in (-1, 1):
        x = ap[0] + side * (1 - f) * (ap[0] - xl)
        yy = ap[1] + (1 - f) * (yb - ap[1])
        b.append(rc(x - 9, yy - 26, 18, 18, "#6a4320", OUT, 1.5))
        if side < 0: terL.append((x, yy))
b.append(rc(ap[0] - 10, ap[1] - 30, 20, 20, "#6a4320", OUT, 1.5))
# marcadores numerados (em cima de cada peça)
def ypern(x):  # altura da perna esquerda num x
    return yb + 2 - (x - (xl - 26)) / (ap[0] - (xl - 26)) * (yb + 2 - ap[1])
b.append(marc(xl + 110, yb + 4, 1))
b.append(marc(xl + 30, ypern(xl + 30), 2))
b.append(marc(ap[0], (ap[1] + yb) / 2 + 16, 3))
b.append(marc((ap[0] + mL[0]) / 2, (yb - 6 + mL[1] + 6) / 2, 4))
tx_, ty_ = terL[1]; b.append(marc(tx_, ty_ - 44, 5)); b.append(ln(tx_, ty_ - 34, tx_, ty_ - 26, OUT, 1.5))
b.append(marc(ap[0], ap[1] - 48, 6)); b.append(ln(ap[0], ap[1] - 38, ap[0], ap[1] - 30, OUT, 1.5))
b.append(marc(xl - 34, yb + 30, 7)); b.append(ln(xl - 26, yb + 24, xl - 12, yb + 10, OUT, 1.5))
# cotas
b.append(cota(xr + 40, ap[1], xr + 40, yb, "", 0, 0))
b += [tl(xr + 46, (ap[1] + yb) / 2, ["~1 m", "(35%)"], 11, "#b3001b", True)]
b.append(cota(xl, yb + 104, xr, yb + 104, "vão de 6 m (de parede a parede)", 0, -6))
# legenda
leg = [("1", "LINHA 6 × 16 cm (trabalha esticada)"), ("2", "PERNA 6 × 12 cm"),
       ("3", "PENDURAL 6 × 12 cm (pendura a linha no meio)"), ("4", "ESCORA 6 × 12 cm (apoia o meio da perna)"),
       ("5", "TERÇA 6 × 12 cm, a cada 1,5–2 m"), ("6", "CUMEEIRA (a terça do topo)"), ("7", "chapa de ferro + parafusos em cada emenda")]
for i, (n, t) in enumerate(leg):
    col, row = (0, i) if i < 4 else (1, i - 4)
    x = 26 + col * 330; y = 436 + row * 20
    b.append(marc(x, y - 4, n)); b.append(text(x + 16, y, t, 11, "#222"))
b.append(box(14, 520, 652, 70, "#eef5ff", "#3f6d9e"))
b += [text(26, 540, "Tesouras a cada ~3 m. Sobre as terças: caibros 5 × 6 cm a cada 50 cm; sobre os caibros: ripas 1,5 × 5 cm", 11.5),
      text(26, 557, "na distância que a telha pede (meça encaixando 2 telhas). Medidas para madeira de lei e vão até ~6 m.", 11.5),
      text(26, 575, "Vão maior, sobrado ou madeira fraca: peça cálculo. Amarre a tesoura na parede.", 11.5, "#b3001b", True)]
open(D + "tesoura-telhado.svg", "w").write(svg(680, 540, "Tesoura de telhado simples (de pendural)", '<g transform="translate(0,-60)">' + "\n".join(b) + "</g>"))

# =====================================================================
# 3) BAMBU: CORTES, ENCAIXES E AMARRAÇÃO
# =====================================================================
b = []
def colmo_v(x, y1, y2, w, nos=()):
    s = rc(x - w / 2, y1, w, y2 - y1, BAMBU, OUT, 2)
    for yy in nos:
        s += rc(x - w / 2 - 2, yy - 3, w + 4, 6, BAMBU2, OUT, 1.5, 2)
    return s
def colmo_h(x1, x2, y, w, nos=()):
    s = rc(x1, y - w / 2, x2 - x1, w, BAMBU, OUT, 2)
    for xx in nos:
        s += rc(xx - 3, y - w / 2 - 2, 6, w + 4, BAMBU2, OUT, 1.5, 2)
    return s
for x in (226, 454):
    b.append(ln(x, 50, x, 546, "#ddd", 1.5))
b.append(ln(10, 296, 670, 296, "#ddd", 1.5))
# --- painel 1: boca de peixe ---
b.append(text(118, 64, "1. Boca de peixe", 13.5, "#222", True, "middle"))
cx, cy, r = 118, 216, 34
b.append(ci(cx, cy, r, BAMBU, OUT, 2.5)); b.append(ci(cx, cy, r - 7, "#fff8dc", OUT, 1.5))
w = 52
b.append(f'<path d="M{cx-w/2} 84 L{cx-w/2} {cy - math.sqrt(r*r - (w/2)**2):.1f} A {r} {r} 0 0 1 {cx+w/2} {cy - math.sqrt(r*r - (w/2)**2):.1f} L{cx+w/2} 84 Z" fill="{BAMBU}" stroke="{OUT}" stroke-width="2"/>')
b.append(rc(cx - w / 2 - 2, 152, w + 4, 6, BAMBU2, OUT, 1.5, 2))
b += [tl(16, 268, ["ponta em meia-lua que abraça", "a peça redonda; nó perto do corte"], 10.5, "#222")]
b += [tl(152, 100, ["serre em V", "e arredonde", "com grosa"], 10.5, "#444")]
b += [tl(160, 214, ["peça", "vista", "de topo"], 10.5, "#444")]
# --- painel 2: parafuso passante + argamassa ---
b.append(text(340, 64, "2. Parafuso + argamassa", 13.5, "#222", True, "middle"))
b.append(colmo_v(300, 84, 244, 40, (110, 214)))
b.append(rc(284, 116, 32, 92, "#9a9a9a", OUT, 1.5, 3))
b.append(ci(352, 160, 24, BAMBU, OUT, 2.5)); b.append(ci(352, 160, 17, "#fff8dc", OUT, 1.5))
b.append(ln(266, 160, 390, 160, "#333", 5))
b.append(rc(262, 150, 6, 20, "#555", OUT, 1)); b.append(rc(388, 150, 6, 20, "#555", OUT, 1))
b += [tl(236, 102, ["pilar"], 10.5, "#444", True)]
b += [tl(330, 102, ["viga vista", "de topo"], 10.5, "#444", True)]
b += [tl(236, 262, ["vão do parafuso cheio de argamassa;", "parafuso ou barra roscada com", "arruela larga dos dois lados"], 10.5, "#222")]
b.append(ln(250, 254, 286, 196, "#555", 1.2))
# --- painel 3: corte perto do nó ---
b.append(text(562, 64, "3. Corte perto do nó", 13.5, "#222", True, "middle"))
b.append(colmo_h(480, 640, 120, 36, (520, 626)))
b.append(marca_ok(468, 120)); b += [tl(486, 160, ["ponta a 2–5 cm do nó:", "não racha"], 10.5, "#1f6b2e", True)]
b.append(colmo_h(480, 640, 220, 36, (500,)))
b.append(pl([(640, 214), (612, 218), (590, 214)], OUT, 2))
b.append(marca_x(468, 220)); b += [tl(486, 260, ["ponta longe do nó: racha", "e junta água"], 10.5, "#b3001b", True)]
# --- painel 4: amarração quadrada ---
b.append(text(118, 316, "4. Amarração quadrada", 13.5, "#222", True, "middle"))
b.append(colmo_v(118, 334, 506, 30, (350, 490)))
b.append(colmo_h(30, 206, 420, 30, (46, 190)))
for dx in (-26, -21, -16, 16, 21, 26):
    b.append(ln(118 + dx, 400, 118 + dx, 440, "#7a4a12", 3.5))
for dy in (-24, -19, 19, 24):
    b.append(ln(98, 420 + dy, 138, 420 + dy, "#a8641c", 3.5))
b += [tl(16, 524, ["volta do fiel, 3–4 voltas em quadrado,", "2–3 voltas de aperto entre as peças"], 10.5, "#222")]
b += [tl(146, 356, ["arame", "galvanizado", "ou corda"], 10.5, "#444")]
# --- painel 5: pé protegido ---
b.append(text(340, 316, "5. Pé longe do chão", 13.5, "#222", True, "middle"))
GY = 486
b.append(rc(236, GY, 210, 26, SOLO, "none", 0)); b.append(ln(236, GY, 446, GY, "#6b4f2a", 2.5))
b.append(rc(306, GY - 36, 68, 66, CONC, OUT, 2))
b.append(colmo_v(340, 336, GY - 36, 40, (360, 420)))
b.append(rc(328, 420, 24, GY - 36 - 420, "#9a9a9a", OUT, 1.2, 2))
b.append(ln(340, 400, 340, GY + 20, "#555", 4))
b += [tl(382, 420, ["vergalhão", "+ argamassa", "no 1º vão"], 10.5, "#444")]
b += [tl(240, 400, ["bloco de", "concreto", "ou pedra"], 10.5, "#444")]
b.append(ln(272, 430, 306, GY - 20, "#555", 1.2))
b += [tl(236, 530, ["no mínimo 20 cm acima do chão"], 10.5, "#b3001b", True)]
# --- painel 6: colheita ---
b.append(text(562, 316, "6. Colheita", 13.5, "#222", True, "middle"))
b.append(rc(462, GY, 206, 26, SOLO, "none", 0)); b.append(ln(462, GY, 668, GY, "#6b4f2a", 2.5))
for (x, top) in ((478, 336), (502, 348), (628, 342), (652, 356)):
    b.append(colmo_v(x, top, GY, 18, (top + 40, top + 90)))
b.append(colmo_v(564, GY - 40, GY, 26, (GY - 30,)))
b.append(ln(550, GY - 40, 578, GY - 40, PERIGO, 2.5))
b += [tl(524, 380, ["corte logo", "acima do nó,", "a 20–30 cm"], 10.5, "#222", True)]
b.append(ln(560, 412, 564, GY - 44, "#555", 1.2))
b += [tl(464, 524, ["só colmos de 3–5 anos; no máx.", "1/3 da touceira por ano"], 10.5, "#222")]
open(D + "bambu.svg", "w").write(svg(680, 552, "Bambu: cortes, encaixes e amarração", "\n".join(b)))

# =====================================================================
# 4) ESQUADRO 3-4-5 E NÍVEL DE MANGUEIRA
# =====================================================================
b = []
b.append(text(170, 62, "Esquadro 3-4-5 (vista de cima)", 14, "#222", True, "middle"))
s = 62
cx0, cy0 = 70, 330
pA = (cx0, cy0); pB = (cx0 + 4 * s, cy0); pC = (cx0, cy0 - 3 * s)
b.append(ln(cx0, cy0, cx0 + 4.6 * s, cy0, "#444", 2))
b.append(ln(cx0, cy0, cx0, cy0 - 3.6 * s, "#444", 2))
b.append(ln(pC[0], pC[1], pB[0], pB[1], PERIGO, 3, "8 5"))
b.append(rc(cx0, cy0 - 18, 18, 18, "none", "#1f6b2e", 2))
for p in (pA, pB, pC):
    b.append(ci(p[0], p[1], 6, WOOD, OUT, 1.5))
b.append(text((pA[0] + pB[0]) / 2, cy0 + 22, "4 m", 14, "#222", True, "middle"))
b.append(text(cx0 - 10, (pA[1] + pC[1]) / 2 + 5, "3 m", 14, "#222", True, "end"))
b.append(text((pC[0] + pB[0]) / 2 + 14, (pC[1] + pB[1]) / 2 - 8, "5 m", 15, PERIGO, True))
b.append(text(cx0 + 22, cy0 - 24, "90°", 12, "#1f6b2e", True))
b += [tl(20, 372, ["Estaque o canto. Meça 3 m numa linha e 4 m na", "outra. A distância entre as duas marcas tem que", "dar EXATAMENTE 5 m. Deu mais? Feche o ângulo.", "Deu menos? Abra. Mesma regra: 60-80-100 cm,", "1,5-2-2,5 m ou 6-8-10 m (maior = mais preciso)."], 11.5)]
b.append(text(20, 448, "Retângulo certo: as 2 diagonais dão iguais.", 11.5, "#1f6b2e", True))
b.append(ln(340, 50, 340, 456, "#ddd", 1.5))
# nível de mangueira
b.append(text(508, 62, "Nível de mangueira", 14, "#222", True, "middle"))
GY = 330
b.append(rc(346, GY, 334, 20, SOLO, "none", 0)); b.append(ln(346, GY, 680, GY, "#6b4f2a", 2.5))
b.append(rc(366, 90, 22, GY - 90, "#d9cbb0", OUT, 2)); b.append(text(377, 84, "parede", 10.5, "#444", False, "middle"))
b.append(rc(624, 120, 14, GY - 120, WOOD, OUT, 2)); b.append(text(631, 114, "estaca", 10.5, "#444", False, "middle"))
lv = 170
hose = f"M398 128 L398 {GY-14} Q398 {GY-4} 410 {GY-4} L604 {GY-4} Q614 {GY-4} 614 {GY-14} L614 140"
b.append(f'<path d="{hose}" fill="none" stroke="#7a8a96" stroke-width="13" stroke-linecap="round"/>')
b.append(f'<path d="{hose}" fill="none" stroke="#eef6fb" stroke-width="8" stroke-linecap="round"/>')
water = f"M398 {lv} L398 {GY-14} Q398 {GY-4} 410 {GY-4} L604 {GY-4} Q614 {GY-4} 614 {GY-14} L614 {lv}"
b.append(f'<path d="{water}" fill="none" stroke="{AGUA}" stroke-width="7"/>')
b.append(ln(388, lv, 640, lv, PERIGO, 2, "7 5"))
b.append(ln(364, lv, 392, lv, OUT, 3)); b.append(ln(620, lv, 642, lv, OUT, 3))
b += [tl(406, 148, ["1. marca de referência"], 11, "#222", True)]
b.append(ln(404, 152, 384, lv - 4, "#555", 1.2))
b += [tl(504, 104, ["3. marque onde", "a água parou"], 11, "#222", True)]
b.append(ln(560, 112, 610, 160, "#555", 1.2))
b.append(text(506, lv + 20, "mesmo nível", 12, PERIGO, True, "middle"))
b += [tl(412, 236, ["2. suba ou desça a ponta da", "estaca até a água ficar na", "marca da parede"], 10.5, "#444")]
b += [tl(354, 368, ["• Mangueira transparente de 5/16\" ou 3/8\",", "  cheia de água SEM bolhas (dê batidinhas).", "• Pontas abertas na hora de ler; espere a água", "  parar de mexer. Erro: ~1 mm.", "• Água com corante ou café enxerga melhor."], 11)]
open(D + "esquadro-nivel.svg", "w").write(svg(680, 466, "Esquadro 3-4-5 e nível de mangueira", "\n".join(b)))
print("ok")
