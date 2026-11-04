import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
import math
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "04-agricultura", "img") + "/"
os.makedirs(D, exist_ok=True)
# Figuras de 04-agricultura (parte 1): canteiro e dupla escavação, compostagem,
# consórcio milho-feijão-abóbora, maniva de mandioca.

SOIL = "#e8d3b0"; SOIL2 = "#c9a878"; SOIL3 = "#a8865a"; DARKSOIL = "#6b4f2a"
GREEN = "#2b8a3e"; LG = "#8fd19e"; WOOD = "#8b5a2b"; RED = "#d62828"; RED2 = "#b3001b"
ORANGE = "#ef8a2b"; WATER = "#4a90d9"; WATERL = "#cfe6fb"

def lines(x, y, txts, size=12, color="#222", bold_first=False, anchor="start", lh=None):
    lh = lh or size + 3
    out = []
    for i, t in enumerate(txts):
        out.append(text(x, y + i * lh, t, size, color, bold_first and i == 0, anchor))
    return "".join(out)

def dim_h(x1, x2, y, label, size=12, color="#333", above=True):
    ty = y - 6 if above else y + size + 4
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="1.5"/>'
            f'<line x1="{x1}" y1="{y-6}" x2="{x1}" y2="{y+6}" stroke="{color}" stroke-width="1.5"/>'
            f'<line x1="{x2}" y1="{y-6}" x2="{x2}" y2="{y+6}" stroke="{color}" stroke-width="1.5"/>'
            + text((x1 + x2) / 2, ty, label, size, color, True, "middle"))

def dim_v(x, y1, y2, label, size=12, color="#333", side="right"):
    tx = x + 8 if side == "right" else x - 8
    an = "start" if side == "right" else "end"
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{color}" stroke-width="1.5"/>'
            f'<line x1="{x-6}" y1="{y1}" x2="{x+6}" y2="{y1}" stroke="{color}" stroke-width="1.5"/>'
            f'<line x1="{x-6}" y1="{y2}" x2="{x+6}" y2="{y2}" stroke="{color}" stroke-width="1.5"/>'
            + text(tx, (y1 + y2) / 2 + 4, label, size, color, True, an))

def leader(x1, y1, x2, y2, color="#555"):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.2"/>'
            f'<circle cx="{x2}" cy="{y2}" r="2.5" fill="{color}"/>')

def num(x, y, n, color=ORANGE):
    return (f'<circle cx="{x}" cy="{y}" r="11" fill="{color}" stroke="#1e1e1e" stroke-width="1.5"/>'
            + text(x, y + 4.5, str(n), 13, "#fff", True, "middle"))

def curved_arrow(x1, y1, cx, cy, x2, y2, color="#d62828", w=3):
    a = math.atan2(y2 - cy, x2 - cx); L = 12
    p1 = (x2 - L * math.cos(a - 0.45), y2 - L * math.sin(a - 0.45))
    p2 = (x2 - L * math.cos(a + 0.45), y2 - L * math.sin(a + 0.45))
    return (f'<path d="M{x1} {y1} Q {cx} {cy} {x2 - 6*math.cos(a):.1f} {y2 - 6*math.sin(a):.1f}" fill="none" stroke="{color}" stroke-width="{w}"/>'
            f'<polygon points="{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{color}"/>')

def plant(x, y, s=1.0):
    """muda pequena vista de lado, com a base em (x, y)"""
    return (f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y-14*s}" stroke="{GREEN}" stroke-width="2.5"/>'
            f'<ellipse cx="{x-8*s}" cy="{y-16*s}" rx="{9*s}" ry="{5*s}" fill="{LG}" stroke="{GREEN}" stroke-width="1.5" transform="rotate(-25 {x-8*s} {y-16*s})"/>'
            f'<ellipse cx="{x+8*s}" cy="{y-16*s}" rx="{9*s}" ry="{5*s}" fill="{LG}" stroke="{GREEN}" stroke-width="1.5" transform="rotate(25 {x+8*s} {y-16*s})"/>'
            f'<ellipse cx="{x}" cy="{y-24*s}" rx="{5*s}" ry="{8*s}" fill="{LG}" stroke="{GREEN}" stroke-width="1.5"/>')

def check(x, y, ok=True):
    if ok:
        return f'<path d="M{x-8} {y} l6 7 l12 -14" fill="none" stroke="{GREEN}" stroke-width="4" stroke-linecap="round"/>'
    return (f'<path d="M{x-8} {y-8} l16 16 M{x+8} {y-8} l-16 16" stroke="{RED}" stroke-width="4" stroke-linecap="round"/>')

# =====================================================================
# 1. CANTEIRO E DUPLA ESCAVAÇÃO
# =====================================================================
b = []
b.append(text(20, 64, "1. Canteiro em corte (medidas)", 15, "#222", True))
# solo original
b.append(f'<rect x="0" y="200" width="680" height="45" fill="{SOIL}"/>')
b.append(f'<line x1="0" y1="200" x2="680" y2="200" stroke="{DARKSOIL}" stroke-width="2"/>')
# canteiro principal 150-450 (1,2 m = 300 px)
b.append(f'<polygon points="150,200 158,142 442,142 450,200" fill="{SOIL2}" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<rect x="158" y="136" width="284" height="7" fill="#e9cf6b" stroke="#a88a2a" stroke-width="1"/>')
for px in (195, 265, 335, 405):
    b.append(plant(px, 137, 1.0))
# canteiro vizinho (parcial)
b.append(f'<polygon points="575,200 583,142 668,142 668,200" fill="{SOIL2}" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<rect x="583" y="136" width="85" height="7" fill="#e9cf6b" stroke="#a88a2a" stroke-width="1"/>')
b.append(plant(620, 137, 1.0))
# cotas
b.append(dim_h(150, 450, 98, "1,0 a 1,2 m de largura", 13))
b.append(lines(470, 86, ["alcança o meio dos", "dois lados sem pisar"], 12, "#2b6a1e", True))
b.append(dim_v(462, 142, 200, "20–30 cm", 12))
b.append(dim_h(25, 150, 222, "", 12))
b.append(text(87, 216, "caminho", 12, "#222", True, "middle"))
b.append(text(87, 240, "40–50 cm", 12, "#222", True, "middle"))
b.append(dim_h(450, 575, 222, "", 12))
b.append(text(512, 216, "caminho", 12, "#222", True, "middle"))
b.append(text(512, 240, "40–50 cm", 12, "#222", True, "middle"))
b.append(text(300, 175, "terra fofa + composto", 12, "#fff", True, "middle"))
b.append(text(300, 268, "Comprimento: até 10 m.  Cobertura de palha por cima.  NUNCA pise no canteiro.", 12.5, "#b3001b", True, "middle"))

# ---------- dupla escavação ----------
b.append('<line x1="20" y1="288" x2="660" y2="288" stroke="#bbb" stroke-width="1"/>')
b.append(text(20, 312, "2. Dupla escavação (faz-se uma vez; depois é só afofar com garfo)", 15, "#222", True))
Y0, Y1, Y2, Y3 = 384, 464, 544, 564   # superfície, fim camada de cima, fim camada de baixo, subsolo
X0 = 70
SL = [70, 150, 230, 310, 390]  # inícios das faixas de 30 cm (80 px)
# subsolo
b.append(f'<rect x="{X0}" y="{Y2}" width="510" height="{Y3-Y2}" fill="#d9c49c"/>')
# camada de baixo (30-60 cm)
b.append(f'<rect x="{X0}" y="{Y1}" width="510" height="{Y2-Y1}" fill="{SOIL}"/>')
# camada de cima (0-30 cm), só nas faixas ainda não mexidas (310 em diante)
b.append(f'<rect x="310" y="{Y0}" width="270" height="{Y1-Y0}" fill="{SOIL2}"/>')
# faixas prontas (70-230): fundo afofado (pontilhado) + terra de cima recolocada (fofa, abaulada)
for x in (70, 150):
    b.append(f'<rect x="{x}" y="{Y1}" width="80" height="{Y2-Y1}" fill="#f1e2c6"/>')
    for i in range(6):
        for j in range(4):
            b.append(f'<circle cx="{x+8+i*13}" cy="{Y1+10+j*18}" r="2" fill="{SOIL3}"/>')
    b.append(f'<path d="M{x} {Y1} L{x} {Y0-4} Q {x+40} {Y0-16} {x+80} {Y0-4} L{x+80} {Y1} Z" fill="#b8925e"/>')
    for i in range(6):
        for j in range(4):
            b.append(f'<circle cx="{x+8+i*13}" cy="{Y0+8+j*18}" r="2" fill="{DARKSOIL}"/>')
# faixa aberta (230-310): vazia em cima, fundo sendo afofado
b.append(f'<rect x="230" y="{Y0}" width="80" height="{Y1-Y0}" fill="#ffffff"/>')
b.append(f'<rect x="230" y="{Y1}" width="80" height="{Y2-Y1}" fill="#f1e2c6"/>')
# contornos
b.append(f'<path d="M{X0} {Y0} L{X0} {Y3} L580 {Y3} L580 {Y0}" fill="none" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<path d="M230 {Y0} L230 {Y1} L310 {Y1} L310 {Y0}" fill="none" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<line x1="310" y1="{Y0}" x2="580" y2="{Y0}" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<line x1="{X0}" y1="{Y1}" x2="580" y2="{Y1}" stroke="#555" stroke-width="1" stroke-dasharray="5 4"/>')
b.append(f'<line x1="{X0}" y1="{Y2}" x2="580" y2="{Y2}" stroke="#555" stroke-width="1" stroke-dasharray="5 4"/>')
# divisões das faixas
for x in (150, 390, 470):
    b.append(f'<line x1="{x}" y1="{Y0}" x2="{x}" y2="{Y2}" stroke="#777" stroke-width="1" stroke-dasharray="3 4"/>')
# garfo enfiado no fundo da vala aberta
for tx in (250, 262, 274, 286):
    b.append(f'<line x1="{tx}" y1="{Y1-2}" x2="{tx}" y2="{Y1+46}" stroke="#666" stroke-width="3" stroke-linecap="round"/>')
b.append(f'<line x1="248" y1="{Y1-4}" x2="288" y2="{Y1-4}" stroke="#666" stroke-width="5"/>')
b.append(f'<line x1="268" y1="{Y1-6}" x2="300" y2="{Y0-52}" stroke="{WOOD}" stroke-width="6" stroke-linecap="round"/>')
b.append(f'<line x1="291" y1="{Y0-56}" x2="313" y2="{Y0-46}" stroke="{WOOD}" stroke-width="6" stroke-linecap="round"/>')
# seta: terra de cima da faixa seguinte para a vala aberta
b.append(curved_arrow(350, Y0 + 30, 330, Y0 - 50, 262, Y0 + 30, RED, 3.5))
# monte de terra da 1a vala no fim do canteiro
b.append(f'<path d="M592 {Y0} Q 628 {Y0-48} 664 {Y0} Z" fill="{SOIL2}" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<line x1="585" y1="{Y0}" x2="670" y2="{Y0}" stroke="{DARKSOIL}" stroke-width="2"/>')
# cotas de profundidade
b.append(dim_v(56, Y0, Y1, "30", 11, "#333", "left"))
b.append(dim_v(56, Y1, Y2, "30", 11, "#333", "left"))
b.append(text(30, Y2 + 14, "cm", 11, "#333", True, "middle"))
# rótulos nas camadas
b.append(text(445, Y0 + 44, "camada de cima", 12, "#fff", True, "middle"))
b.append(text(445, Y1 + 44, "camada de baixo", 12, "#6b4f2a", True, "middle"))
b.append(text(110, Y0 - 24, "pronto", 12, GREEN, True, "middle"))
b.append(text(190, Y0 - 24, "pronto", 12, GREEN, True, "middle"))
# números
b.append(num(270, Y0 + 20, 1))
b.append(num(232, Y1 + 62, 2))
b.append(num(350, Y0 - 40, 3))
b.append(num(628, Y0 - 50, 4))
# legenda numerada
ly = 596
b.append(num(30, ly - 4, 1)); b.append(lines(48, ly, ["Abra uma vala de 30 x 30 cm no começo", "do canteiro; a terra vai para o fim dele."], 12))
b.append(num(30, ly + 40, 2)); b.append(lines(48, ly + 44, ["Solte o fundo da vala com o garfo, mais", "30 cm, sem tirar a terra (só afofa)."], 12))
b.append(num(360, ly - 4, 3)); b.append(lines(378, ly, ["Jogue a terra de cima da faixa seguinte", "dentro da vala aberta. Repita até o fim."], 12))
b.append(num(360, ly + 40, 4)); b.append(lines(378, ly + 44, ["A terra da 1ª vala fecha a última.", "Espalhe composto e nivele com rastelo."], 12))
b.append(box(20, 664, 640, 34, "#eaf6ec", GREEN))
b.append(text(340, 686, "Resultado: terra fofa até 60 cm — raízes fundas, menos rega, plantas mais juntas.", 12.5, "#1e5e2a", True, "middle"))
open(D + "canteiro-dupla-escavacao.svg", "w").write(svg(680, 710, "Canteiro e dupla escavação", "\n".join(b)))

# =====================================================================
# 2. PILHA DE COMPOSTAGEM EM CAMADAS
# =====================================================================
b = []
GB, GT = 360, 128          # base e topo da pilha
XL0, XR0, XL1, XR1 = 70, 430, 150, 350
def xl(y): return XL0 + (GB - y) / (GB - GT) * (XL1 - XL0)
def xr(y): return XR0 - (GB - y) / (GB - GT) * (XR0 - XR1)
def layer(y1, y2, fill):  # y1 > y2 (y1 embaixo)
    return f'<polygon points="{xl(y1):.1f},{y1} {xl(y2):.1f},{y2} {xr(y2):.1f},{y2} {xr(y1):.1f},{y1}" fill="{fill}" stroke="#1e1e1e" stroke-width="0.8"/>'
b.append(f'<rect x="0" y="{GB}" width="680" height="22" fill="{SOIL}"/>')
b.append(f'<line x1="0" y1="{GB}" x2="680" y2="{GB}" stroke="{DARKSOIL}" stroke-width="2"/>')
# base de galhos
b.append(layer(GB, GB - 28, "#d8c3a0"))
for i in range(14):
    x = xl(GB) + 14 + i * 24
    b.append(f'<line x1="{x}" y1="{GB-6}" x2="{x+20}" y2="{GB-22}" stroke="{WOOD}" stroke-width="4" stroke-linecap="round"/>')
y = GB - 28
BROWN, GREENL, EARTH = "#b08850", "#7cc47f", "#5a4630"
ys = {}
for k in range(4):
    b.append(layer(y, y - 34, BROWN)); ys.setdefault("m", y - 17); y -= 34
    b.append(layer(y, y - 11, GREENL)); ys.setdefault("v", y - 5); y -= 11
    b.append(layer(y, y - 4, EARTH)); ys.setdefault("t", y - 2); y -= 4
# textura nas camadas marrons (folhas secas)
# cobertura de palha no topo
b.append(f'<polygon points="{xl(y)-6:.1f},{y} {xl(GT)-4:.1f},{GT-12} {xr(GT)+4:.1f},{GT-12} {xr(y)+6:.1f},{y}" fill="#efd27a" stroke="#1e1e1e" stroke-width="1.5"/>')
for i in range(12):
    x = xl(GT) + 4 + i * 17
    b.append(f'<line x1="{x}" y1="{GT-8}" x2="{x+12}" y2="{GT-2}" stroke="#b8932f" stroke-width="2"/>')
# barra de ferro (termômetro)
b.append(f'<line x1="250" y1="70" x2="250" y2="300" stroke="#666" stroke-width="5"/>')
b.append(f'<line x1="238" y1="70" x2="262" y2="70" stroke="#666" stroke-width="5" stroke-linecap="round"/>')
b.append(f'<ellipse cx="250" cy="250" rx="70" ry="40" fill="#d62828" fill-opacity="0.18"/>')
b.append(text(250, 264, "55–65 °C", 13, RED2, True, "middle"))
b.append(lines(20, 60, ["Barra de ferro no meio:", "puxe e sinta. Quente de", "não aguentar segurar = OK"], 11.5, "#333", True))
b.append(leader(185, 68, 244, 86))
# cotas
b.append(dim_h(XL0, XR0, GB + 40, "1,5 a 2 m de largura na base", 12, "#333", False))
b.append(dim_v(56, GT - 12, GB, "", 12))
b.append(lines(48, GB - 124, ["1 a", "1,5 m"], 12, "#333", True, "end"))
# rótulos à direita
RX = 455
b.append(leader(RX - 4, GT - 4, xr(GT) - 6, GT - 6))
b.append(lines(RX, GT - 18, ["COBERTURA: palha ou", "folhas (protege do sol e", "da chuva)"], 12, "#7a5d00", True))
yv = ys["v"]; ym = ys["m"]; yt = ys["t"]
b.append(leader(RX - 4, 196, xr(217) - 20, 217))
b.append(lines(RX, 186, ["MARROM 15–20 cm: folhas", "secas, palha, capim seco,", "serragem, papelão"], 12, "#6b4f2a", True))
b.append(leader(RX - 4, 243, xr(243) - 14, 243))
b.append(lines(RX, 240, ["VERDE 5 cm: restos de", "cozinha, esterco, grama", "fresca, folhas verdes"], 12, "#1e6a2a", True))
b.append(leader(RX - 4, 292, xr(285) - 10, 285))
b.append(lines(RX, 296, ["punhado de terra ou", "composto velho + ÁGUA"], 12, "#333", True))
b.append(leader(RX - 4, 340, xr(GB - 14) - 20, GB - 14))
b.append(lines(RX, 336, ["base de galhos (20 cm):", "deixa o ar entrar"], 12, "#333", True))
# ---------- proporção 3:1 ----------
def bucket(x, y, fill, lab):
    return (f'<path d="M{x} {y} L{x+6} {y+44} L{x+38} {y+44} L{x+44} {y} Z" fill="{fill}" stroke="#1e1e1e" stroke-width="2"/>'
            f'<path d="M{x+2} {y} Q {x+22} {y-22} {x+42} {y}" fill="none" stroke="#1e1e1e" stroke-width="2"/>'
            + text(x + 22, y + 28, lab, 11, "#fff", True, "middle"))
yb = 438
b.append(text(20, 428, "Mistura certa:", 13, "#222", True))
for i in range(3):
    b.append(bucket(130 + i * 56, yb, BROWN, "M"))
b.append(text(311, yb + 30, "+", 26, "#222", True, "middle"))
b.append(bucket(330, yb, GREENL, "V"))
b.append(lines(392, yb + 4, ["3 partes de MARROM (carbono)", "para 1 parte de VERDE (nitrogênio)", "— mais ou menos 30 de C para 1 de N"], 12, "#222", True))
# ---------- teste da esponja ----------
b.append(text(20, 516, "Teste da esponja: aperte um punhado com força", 13, "#222", True))
def blob(x, y, drops, fill):
    s = f'<ellipse cx="{x}" cy="{y}" rx="26" ry="18" fill="{fill}" stroke="#1e1e1e" stroke-width="2"/>'
    for i in range(drops):
        dx = x - (drops - 1) * 7 + i * 14
        s += f'<path d="M{dx} {y+22} q -5 9 0 13 q 5 -4 0 -13 Z" fill="{WATER}" stroke="#2a5d93" stroke-width="1"/>'
    return s
cols = [(110, 0, "#c9a878", "SECO: esfarela", "→ molhe e misture", RED2),
        (340, 2, "#8a6a3e", "CERTO: 1 ou 2 gotas", "(como esponja torcida)", GREEN),
        (570, 5, "#5a4630", "ENCHARCADO: escorre", "→ junte marrom e revire", RED2)]
for cx, dr, f, t1, t2, c in cols:
    b.append(blob(cx, 548, dr, f))
    b.append(text(cx, 600, t1, 12.5, c, True, "middle"))
    b.append(text(cx, 616, t2, 12, "#333", False, "middle"))
b.append(box(20, 630, 640, 54, "#fff4e5", ORANGE))
b.append(lines(34, 651, ["Revire (bordas para o meio) aos 7–15 dias e depois a cada 15 dias. Pronto em 2–4 meses:",
                         "escuro, esfarelando, cheiro de terra de mata, frio no meio. Sem revirar: 4–6 meses."], 12.5))
open(D + "compostagem-pilha.svg", "w").write(svg(680, 696, "Pilha de compostagem em camadas (corte)", "\n".join(b)))

# =====================================================================
# 3. CONSÓRCIO MILHO + FEIJÃO + ABÓBORA (VISTO DE CIMA)
# =====================================================================
b = []
PX0, PX1, PY0, PY1 = 50, 530, 92, 412   # 6 m x 4 m -> 80 px/m
b.append(f'<rect x="{PX0}" y="{PY0}" width="{PX1-PX0}" height="{PY1-PY0}" fill="#efe1c3" stroke="#1e1e1e" stroke-width="2"/>')
rows = [PY0 + 40, PY0 + 120, PY0 + 200, PY0 + 280]
mids = [PY0 + 80, PY0 + 160, PY0 + 240]
def milho(x, y):
    s = ""
    for ang in (0, 60, 120):
        s += f'<ellipse cx="{x}" cy="{y}" rx="13" ry="3.5" fill="#4caf50" stroke="#1e5e2a" stroke-width="1" transform="rotate({ang} {x} {y})"/>'
    s += f'<circle cx="{x}" cy="{y}" r="3.5" fill="#f2c94c" stroke="#1e1e1e" stroke-width="1"/>'
    return s
def feijao(x, y):
    return f'<circle cx="{x}" cy="{y}" r="3.6" fill="#b6e3a8" stroke="#2b6a1e" stroke-width="1.2"/>'
abob = [(130, mids[0]), (370, mids[0]), (250, mids[2]), (490, mids[2])]
def abobora(x, y):
    s = ""
    for ang in (150, 270, 30):
        a = math.radians(ang)
        s += f'<path d="M{x} {y} q {24*math.cos(a)+8*math.sin(a):.0f} {24*math.sin(a)-8*math.cos(a):.0f} {40*math.cos(a):.0f} {40*math.sin(a):.0f}" fill="none" stroke="#3d7a2a" stroke-width="2.5"/>'
        s += f'<circle cx="{x+40*math.cos(a):.0f}" cy="{y+40*math.sin(a):.0f}" r="7" fill="#7cc47f" stroke="#2b6a1e" stroke-width="1"/>'
    s += f'<circle cx="{x}" cy="{y}" r="12" fill="#f08c00" stroke="#1e1e1e" stroke-width="2"/>'
    return s
for yy in mids:
    x = PX0 + 10
    while x < PX1 - 5:
        if not any(abs(x - ax) < 22 and ay == yy for ax, ay in abob):
            b.append(feijao(x, yy))
        x += 9
for yy in rows:
    for i in range(12):
        b.append(milho(PX0 + 20 + i * 40, yy))
for ax, ay in abob:
    b.append(abobora(ax, ay))
# cotas acima do canteiro
b.append(dim_h(PX0 + 20, PX0 + 60, 72, "0,5 m", 12))
for xx in (PX0 + 20, PX0 + 60):
    b.append(f'<line x1="{xx}" y1="72" x2="{xx}" y2="{rows[0]-8}" stroke="#555" stroke-width="1" stroke-dasharray="3 3"/>')
b.append(dim_h(130, 370, 72, "3 m entre covas de abóbora", 12, "#b05a00"))
for xx in (130, 370):
    b.append(f'<line x1="{xx}" y1="72" x2="{xx}" y2="{mids[0]-12}" stroke="#b05a00" stroke-width="1" stroke-dasharray="3 3"/>')
# cotas à direita
b.append(dim_v(548, rows[0], rows[1], "1,0 m", 12))
b.append(text(556, rows[0] + 58, "entre linhas", 11, "#333"))
b.append(text(556, rows[0] + 72, "de milho", 11, "#333"))
b.append(dim_v(548, rows[2], mids[2], "0,5 m", 12))
b.append(text(556, rows[2] + 34, "do milho ao", 11, "#333"))
b.append(text(556, rows[2] + 48, "feijão", 11, "#333"))
b.append(dim_h(PX0, PX1, PY1 + 18, "6 m", 12, "#333", False))
# legenda
ly = 470
b.append(milho(40, ly)); b.append(lines(62, ly - 4, ["MILHO: 1 cova a cada 0,5 m,", "2 plantas por cova; linhas a 1 m"], 12, "#222", True))
b.append(feijao(40, ly + 44)); b.append(feijao(50, ly + 44)); b.append(feijao(30, ly + 44))
b.append(lines(62, ly + 40, ["FEIJÃO: 1 linha no meio,", "10–12 sementes por metro"], 12, "#2b6a1e", True))
b.append(f'<circle cx="370" cy="{ly}" r="12" fill="#f08c00" stroke="#1e1e1e" stroke-width="2"/>')
b.append(lines(392, ly - 4, ["ABÓBORA: 1 cova a cada 3 m, em", "entrelinhas alternadas (no lugar do feijão)"], 12, "#b05a00", True))
b.append(lines(392, ly + 40, ["As ramas da abóbora cobrem o chão:", "seguram a umidade e abafam o mato."], 12))
b.append(box(20, 538, 640, 72, "#eaf6ec", GREEN))
b.append(lines(34, 560, ["Milho e abóbora no mesmo dia; feijão de moita junto ou até 10 dias depois.",
                         "Feijão trepador ou de corda: semeie NA COVA do milho 15–20 dias depois (o milho vira tutor).",
                         "O feijão põe nitrogênio no solo; o milho dá sombra e apoio; a abóbora cobre o chão."], 12.5))
open(D + "consorcio-milho-feijao-abobora.svg", "w").write(svg(680, 622, "Consórcio milho + feijão + abóbora (visto de cima)", "\n".join(b)))

# =====================================================================
# 4. MANDIOCA: CORTE DA MANIVA E POSIÇÃO DE PLANTIO
# =====================================================================
def gema(gx, gy, s=1.0):
    """gema (olho) no lado de cima da rama, apontando para a ponta (direita)"""
    return f'<polygon points="{gx},{gy} {gx+8*s},{gy} {gx+8*s},{gy-7*s}" fill="#7a5d3a" stroke="#1e1e1e" stroke-width="1.2"/>'
b = []
b.append(text(20, 58, "1. Escolha a rama: planta sadia de 10 a 14 meses", 14, "#222", True))
x0, x1, yc = 40, 600, 124
def thick(x): return 13 - (x - x0) / (x1 - x0) * 9
pts_top = " ".join(f"{x},{yc-thick(x):.1f}" for x in range(x0, x1 + 1, 20))
pts_bot = " ".join(f"{x},{yc+thick(x):.1f}" for x in range(x1, x0 - 1, -20))
b.append(f'<polygon points="{pts_top} {pts_bot}" fill="#b7a089" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<polygon points="480,{yc-thick(480):.1f} 600,{yc-thick(600):.1f} 600,{yc+thick(600):.1f} 480,{yc+thick(480):.1f}" fill="#9cc97a" stroke="#1e1e1e" stroke-width="1.5"/>')
for x in range(50, 596, 20):
    b.append(gema(x, yc - thick(x), 0.8))
for ang in (-60, -20, 20):
    b.append(f'<ellipse cx="624" cy="{yc}" rx="22" ry="5" fill="#4caf50" stroke="#1e5e2a" stroke-width="1" transform="rotate({ang} 604 {yc})"/>')
def brace(xa, xb, y, color):
    return f'<path d="M{xa} {y} q 0 -10 10 -10 L{(xa+xb)/2-8} {y-10} q 8 0 8 -8 q 0 8 8 8 L{xb-10} {y-10} q 10 0 10 10" fill="none" stroke="{color}" stroke-width="2.5"/>'
b.append(brace(42, 190, 104, RED2)); b.append(brace(200, 470, 104, GREEN)); b.append(brace(480, 600, 104, RED2))
b.append(text(116, 80, "base: NÃO", 12.5, RED2, True, "middle"))
b.append(text(335, 80, "TERÇO MÉDIO: SIM", 13, GREEN, True, "middle"))
b.append(text(540, 80, "ponta: NÃO", 12.5, RED2, True, "middle"))
b.append(text(335, 156, "A base (grossa e lenhosa) e a ponta (verde e fina) brotam mal, secam ou apodrecem.", 12, "#333", False, "middle"))
b.append(text(335, 172, "Use rama de 2 a 3 cm de grossura, com miolo branco (medula) de no máximo metade dela.", 12, "#333", False, "middle"))
# ---------- 2. maniva ----------
b.append('<line x1="20" y1="186" x2="660" y2="186" stroke="#bbb" stroke-width="1"/>')
b.append(text(20, 210, "2. Corte manivas de 20 cm com facão afiado (corte reto, de um golpe)", 14, "#222", True))
mx0, mx1, my = 60, 360, 256
b.append(f'<rect x="{mx0}" y="{my-18}" width="{mx1-mx0}" height="36" rx="3" fill="#b7a089" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<ellipse cx="{mx1}" cy="{my}" rx="6" ry="18" fill="#f6efe0" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<ellipse cx="{mx1}" cy="{my}" rx="2.5" ry="7" fill="#fff" stroke="#999" stroke-width="1"/>')
for gx in range(80, 352, 46):
    b.append(gema(gx, my - 18, 1.3))
b.append(text(210, my + 5, "ponta da rama →", 11.5, "#fff", True, "middle"))
b.append(dim_h(mx0, mx1, my + 36, "20 cm  ·  5 a 7 gemas (olhos)", 12, "#333", False))
b.append(dim_v(44, my - 18, my + 18, "", 11, "#333", "left"))
b.append(text(30, my - 26, "2–3 cm", 11, "#333", True, "middle"))
b.append(f'<path d="M{mx1+8} {my+6} q 6 8 0 14 q -6 -6 0 -14 Z" fill="#fff" stroke="#888" stroke-width="1.2"/>')
b.append(f'<rect x="420" y="{my-34}" width="70" height="30" fill="#b7a089" stroke="#1e1e1e" stroke-width="2"/>')
b.append(check(510, my - 20, True)); b.append(text(530, my - 15, "corte RETO", 12, GREEN, True))
b.append(f'<polygon points="420,{my+10} 470,{my+10} 490,{my+40} 420,{my+40}" fill="#b7a089" stroke="#1e1e1e" stroke-width="2"/>')
b.append(check(510, my + 26, False)); b.append(text(530, my + 31, "em bisel/lascado", 12, RED2, True))
b.append(text(40, my + 78, "Ao cortar, deve sair leite (látex) logo: rama viva. Plante as manivas no mesmo dia ou em até 2–3 dias.", 12, "#333"))
# ---------- 3. plantio ----------
b.append('<line x1="20" y1="350" x2="660" y2="350" stroke="#bbb" stroke-width="1"/>')
b.append(text(20, 374, "3. Plante", 14, "#222", True))
GY = 430
b.append(text(170, 396, "A) DEITADA (a mais usada)", 13, GREEN, True, "middle"))
b.append(f'<rect x="20" y="{GY}" width="300" height="110" fill="{SOIL}"/>')
b.append(f'<line x1="20" y1="{GY}" x2="320" y2="{GY}" stroke="{DARKSOIL}" stroke-width="2"/>')
b.append(f'<rect x="80" y="{GY+8}" width="160" height="18" fill="{SOIL2}" stroke="#1e1e1e" stroke-width="0.8" stroke-dasharray="4 3"/>')
b.append(f'<rect x="90" y="{GY+22}" width="140" height="16" rx="2" fill="#b7a089" stroke="#1e1e1e" stroke-width="2"/>')
for gx in range(100, 226, 24):
    b.append(gema(gx, GY + 22, 0.9))
b.append(plant(120, GY, 0.8)); b.append(plant(200, GY, 0.8))
b.append(dim_v(262, GY, GY + 30, "10 cm", 11))
b.append(lines(30, GY + 64, ["Em sulco ou cova de 10 cm de fundura,", "coberta com terra. Brota em 10–20 dias."], 12))
# B: inclinada / em pé
b.append(text(370, 396, "B) INCLINADA ou EM PÉ", 13, "#b05a00", True))
b.append(f'<rect x="360" y="{GY}" width="300" height="110" fill="{SOIL}"/>')
b.append(f'<line x1="360" y1="{GY}" x2="660" y2="{GY}" stroke="{DARKSOIL}" stroke-width="2"/>')
b.append(f'<g transform="rotate(-50 450 {GY+20})"><rect x="390" y="{GY+12}" width="110" height="16" rx="2" fill="#b7a089" stroke="#1e1e1e" stroke-width="2"/>'
         + "".join(gema(gx, GY + 12, 0.9) for gx in range(398, 496, 22)) + '</g>')
# vertical: ponta para cima
b.append(f'<g transform="rotate(-90 560 {GY})"><rect x="496" y="{GY-8}" width="90" height="16" rx="2" fill="#b7a089" stroke="#1e1e1e" stroke-width="2"/>'
         + "".join(gema(gx, GY - 8, 0.9) for gx in range(502, 580, 22)) + '</g>')
b.append(f'<line x1="584" y1="{GY+60}" x2="584" y2="{GY-26}" stroke="{RED}" stroke-width="2"/>')
b.append(f'<polygon points="584,{GY-34} 578,{GY-22} 590,{GY-22}" fill="{RED}"/>')
b.append(text(594, GY - 20, "gemas", 11, RED2, True)); b.append(text(594, GY - 7, "para cima", 11, RED2, True))
b.append(lines(370, GY + 84, ["2/3 enterrados, gemas apontando para", "CIMA. Bom em solo arenoso ou úmido."], 12))
b.append(box(20, 556, 640, 52, "#fff4e5", ORANGE))
b.append(lines(34, 577, ["Espaçamento: 1,0 m entre linhas × 0,6 a 0,8 m entre covas (1 maniva por cova).",
                         "Plante no início das chuvas, com o solo úmido. Ramas inteiras: guarde em pé, na sombra."], 12.5))
open(D + "mandioca-maniva.svg", "w").write(svg(680, 620, "Mandioca: maniva e plantio", "\n".join(b)))
print("ok agricultura1")
