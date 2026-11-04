import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
import math
# Figuras da seção 06-energia: biogás, iluminação, micro-hidrelétrica, aquecedor solar
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "06-energia", "img") + "/"
os.makedirs(D, exist_ok=True)
SOLO = "#e8d3b0"; DANGER = "#d62828"; DARK = "#b3001b"; VERDE = "#2b8a3e"; AGUA = "#4a90d9"; AGUA2 = "#cfe6fb"
WOOD = "#8b5a2b"; AZUL = "#1f5f9e"

def rect(x, y, w, h, fill, stroke=OUT, sw=2, rx=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'
def line(x1, y1, x2, y2, color=OUT, w=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}" stroke-linecap="round"{d}/>'
def pline(pts, color, w=4, fill="none"):
    p = " ".join(f"{x},{y}" for x, y in pts)
    return f'<polyline points="{p}" fill="{fill}" stroke="{color}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>'
def pipe(pts, w=10, color="#adb5bd"):
    return pline(pts, OUT, w + 4) + pline(pts, color, w)
def path(d, fill="none", stroke=OUT, sw=2, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round" {extra}/>'
def tlines(x, y, lines, size=12, color="#222", bold_first=False, lh=None, anchor="start"):
    lh = lh or size * 1.3
    return "".join(text(x, y + k * lh, s, size, color, bold_first and k == 0, anchor) for k, s in enumerate(lines))
def small_flame(cx, cy, s=1.0, c1="#4dabf7", c2="#d0ebff"):
    def P(dx, dy): return f"{cx+dx*s:.1f},{cy+dy*s:.1f}"
    return (f'<path d="M{P(-10,0)} C{P(-12,-12)} {P(-4,-16)} {P(0,-28)} C{P(4,-16)} {P(12,-12)} {P(10,0)} Z" fill="{c1}" stroke="{OUT}" stroke-width="1.2"/>'
            f'<path d="M{P(-5,0)} C{P(-6,-7)} {P(-2,-9)} {P(0,-16)} C{P(2,-9)} {P(6,-7)} {P(5,0)} Z" fill="{c2}"/>')
def sun(cx, cy, r=22):
    o = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffd43b" stroke="#e67700" stroke-width="2"/>'
    for k in range(12):
        a = k * math.pi / 6
        o += line(cx + (r + 6) * math.cos(a), cy + (r + 6) * math.sin(a), cx + (r + 16) * math.cos(a), cy + (r + 16) * math.sin(a), "#e67700", 2.5)
    return o
def leader(px, py, tx, ty):
    return line(px, py, tx, ty, "#777", 1.3) + f'<circle cx="{px}" cy="{py}" r="3" fill="#777"/>'

# =====================================================================
# 1. BIODIGESTOR DE LONA (corte)
# =====================================================================
b = []
GY = 240
b.append(rect(0, GY, 680, 190, SOLO, "none", 0))
b.append(line(0, GY, 680, GY, "#6b4f2a", 3))
# vala trapezoidal
TL, TR, BL, BR, BOT = 150, 520, 186, 484, 372
b.append(path(f"M{TL},{GY} L{BL},{BOT} L{BR},{BOT} L{TR},{GY} Z", "#fff", "none", 0))
# liquido e lodo
LV = 268
b.append(path(f"M{TL + (BL-TL)*(LV-GY)/(BOT-GY):.0f},{LV} L{BL},{BOT} L{BR},{BOT} L{TR - (TR-BR)*(LV-GY)/(BOT-GY):.0f},{LV} Z", "#9c7a45", "none", 0))
b.append(path(f"M{BL-6},{BOT-30} L{BL},{BOT} L{BR},{BOT} L{BR+6},{BOT-30} Z", "#5c4422", "none", 0))
for k in range(9):
    x = 226 + k * 28
    b.append(f'<circle cx="{x}" cy="{280 if k % 2 else 336}" r="{3 + k % 2}" fill="#d9c49a" stroke="#6b4f2a" stroke-width="1"/>')
# gas (domo da lona)
b.append(path(f"M{TL-6},{GY} Q335,{GY-150} {TR+6},{GY} L{TR - 7},{LV} L{TL + 8},{LV} Z", "#eef7d9", "none", 0))
b.append(path(f"M{TL},{GY} L{BL},{BOT} L{BR},{BOT} L{TR},{GY}", "none", "#343a40", 4))
b.append(path(f"M{TL-6},{GY} Q335,{GY-150} {TR+6},{GY}", "none", "#343a40", 5))
b.append(text(335, 200, "BIOGÁS", 15, "#3b6b20", True, "middle"))
b.append(text(335, 216, "(metano + gás carbônico)", 11.5, "#3b6b20", False, "middle"))
b.append(text(335, 300, "esterco + água fermentando", 12, "#fff", True, "middle"))
b.append(text(335, 316, "sem ar, 30 a 40 dias", 12, "#fff", True, "middle"))
b.append(text(335, BOT - 10, "lodo", 11.5, "#fff", True, "middle"))
# entrada
b.append(rect(52, GY - 40, 70, 46, "#c9c9c9", OUT, 2.5, 3))
b.append(rect(56, GY - 30, 62, 32, "#9c7a45", "none", 0))
b.append(pipe([(100, GY + 2), (232, 340)], 12))
b.append(arrow(150, 296, 210, 330, "#6b3f17", 3))
b.append(tlines(10, 128, ["1. CAIXA DE CARGA", "esterco + água 1:1,", "todo dia"], 12, "#222", True, 15))
b.append(leader(86, GY - 40, 70, 172))
# saida
b.append(pipe([(438, 344), (560, LV - 2)], 12))
b.append(rect(548, LV - 20, 74, 40, "#c9c9c9", OUT, 2.5, 3))
b.append(rect(552, LV - 4, 66, 20, "#6b5a2a", "none", 0))
b.append(arrow(622, LV + 2, 662, LV + 2, "#6b3f17", 3))
b.append(tlines(548, LV + 44, ["2. SAÍDA: sai o", "biofertilizante;", "fica MAIS BAIXA", "que a entrada"], 11.5, "#222", True, 14))
# saida de gas e linha
b.append(pipe([(335, GY - 76), (335, 92), (392, 92)], 6, "#ffd8a8"))
b.append(pipe([(392, 92), (630, 92), (630, 168)], 6, "#ffd8a8"))
# selo d'agua (garrafa)
b.append(pipe([(335, 92), (300, 92), (300, 140)], 4, "#ffd8a8"))
b.append(rect(284, 112, 32, 52, AGUA2, OUT, 2, 5))
b.append(rect(286, 130, 28, 32, AGUA, "none", 0, 3))
b.append(tlines(276, 124, ["3. SELO D'ÁGUA", "(segurança)"], 11, "#222", True, 13, "end"))
# filtro H2S
b.append(rect(424, 80, 84, 24, "#e9ecef", OUT, 2, 6))
for k in range(14):
    x = 428 + k * 5.6
    b.append(path(f"M{x:.1f},84 q4,8 0,16", "none", "#868e96", 1.3))
b.append(tlines(424, 66, ["4. FILTRO H₂S", ], 11, "#222", True))
b.append(text(466, 120, "palha de aço", 11, "#444", False, "middle"))
# gasometro
b.append(f'<ellipse cx="572" cy="70" rx="44" ry="20" fill="#dee2e6" stroke="{OUT}" stroke-width="2.5"/>')
b.append(rect(556, 42, 32, 10, "#868e96", OUT, 1.5, 2))
b.append(tlines(520, 120, ["5. GASÔMETRO", "bolsa ou câmara", "de pneu + peso"], 11, "#222", True, 13))
b.append(pipe([(572, 90), (572, 92)], 6, "#ffd8a8"))
# fogao
b.append(rect(604, 186, 56, 12, "#495057", OUT, 2, 2))
b.append(line(610, 198, 610, GY, OUT, 3)); b.append(line(654, 198, 654, GY, OUT, 3))
b.append(small_flame(632, 186, 0.8))
b.append(text(598, 200, "6. FOGÃO", 11, "#222", True, "end"))
b.append(tlines(400, 148, ["lona grossa", "(infla com o gás)"], 11.5, "#343a40", True, 14))
b.append(box(20, 438, 640, 82, "#fdecea", DANGER))
b.append(tlines(34, 460, ["NUNCA entre no biodigestor, nem vazio, nem em caixa de esterco: o gás mata em",
                          "segundos e quem desce para socorrer morre junto. Nada de fogo, cigarro ou faísca",
                          "perto. Procure vazamentos com espuma de sabão. Cerque contra crianças e animais."], 12.5, "#7a1010", False, 18))
open(D + "biodigestor.svg", "w").write(svg(680, 530, "Biodigestor de lona (corte)", "\n".join(b)))

# =====================================================================
# 2. LAMPADA DE GARRAFA (luz de Moser)
# =====================================================================
b = []
RY = 190
# telha ondulada (corte)
d = f"M30,{RY}"
for k in range(16):
    x = 30 + k * 26
    d += f" q6.5,-9 13,0 q6.5,9 13,0"
b.append(path(d + f" L446,{RY+8} " + "".join(f" q-6.5,9 -13,0 q-6.5,-9 -13,0" for k in range(16)) + " Z", "#9aa3ab", OUT, 2))
# interior da casa
b.append(rect(30, RY + 8, 416, 232, "#fbf3dc", "none", 0))
b.append(line(30, RY + 240, 446, RY + 240, "#6b4f2a", 3))
b.append(line(40, RY + 8, 40, RY + 240, "#999", 6)); b.append(line(436, RY + 8, 436, RY + 240, "#999", 6))
# raios de luz no comodo
for k in range(13):
    a = math.radians(-8 + k * 16)
    cx0, cy0 = 238, 296
    L = 400
    if math.sin(a) > 0.01: L = min(L, (RY + 232 - cy0) / math.sin(a))
    if math.sin(a) < -0.01: L = min(L, (RY + 14 - cy0) / math.sin(a))
    if math.cos(a) > 0.01: L = min(L, (430 - cx0) / math.cos(a))
    if math.cos(a) < -0.01: L = min(L, (46 - cx0) / math.cos(a))
    b.append(line(cx0 + 34 * math.cos(a), cy0 + 34 * math.sin(a), cx0 + L * math.cos(a), cy0 + L * math.sin(a), "#fcc419", 2.5, "6 6"))
# garrafa
BX, BT, BB, BW = 214, 106, 340, 48
b.append(path(f"M{BX},{BT+30} Q{BX},{BT+14} {BX+14},{BT+6} L{BX+14},{BT} L{BX+BW-14},{BT} L{BX+BW-14},{BT+6} Q{BX+BW},{BT+14} {BX+BW},{BT+30} L{BX+BW},{BB} Q{BX+BW/2},{BB+10} {BX},{BB} Z", "#e7f5ff", OUT, 2.5))
b.append(path(f"M{BX+3},{BT+40} L{BX+BW-3},{BT+40} L{BX+BW-3},{BB-2} Q{BX+BW/2},{BB+6} {BX+3},{BB-2} Z", "#a5d8ff", "none", 0, 'fill-opacity="0.8"'))
b.append(rect(BX + 12, BT - 14, BW - 24, 16, "#212529", OUT, 2, 3))
# colar de chapa
b.append(rect(160, RY - 12, 156, 8, "#ced4da", OUT, 2, 2))
b.append(f'<ellipse cx="{BX-2}" cy="{RY-12}" rx="7" ry="5" fill="#495057"/><ellipse cx="{BX+BW+2}" cy="{RY-12}" rx="7" ry="5" fill="#495057"/>')
# sol
b.append(sun(90, 86))
for (x0, y0) in ((122, 90), (126, 112), (118, 66)):
    b.append(arrow(x0, y0, BX + 8, y0 + 50 if y0 < 100 else BT + 70, "#f59f00", 3))
# cotas
b.append(line(BX + BW + 22, BT, BX + BW + 22, RY - 12, "#333", 1.5)); b.append(text(BX + BW + 28, 156, "1/3", 12.5, "#222", True))
b.append(line(BX + BW + 22, RY + 8, BX + BW + 22, BB, "#333", 1.5)); b.append(text(BX + BW + 28, 274, "2/3", 12.5, "#222", True))
b.append(text(330, 400, "dentro de casa", 12, "#8a6d10", True, "middle"))
# rotulos
labs = [(BX + 24, BT - 6, 70, ["Tampa COBERTA (tubo de", "filme, tampa preta ou fita):", "o sol estraga a tampa"]),
        (BX + BW - 6, 150, 128, ["Garrafa PET 2 L incolor,", "lisa, sem rótulo"]),
        (300, RY - 8, 176, ["Chapa de metal ~25 × 25 cm", "com furo justo; vede tudo", "com silicone ou cola epóxi"]),
        (BX + BW - 6, 300, 250, ["Água FILTRADA + 2", "tampinhas (~10 mL) de", "água sanitária (sem limo)"])]
for (px, py, ty, ls) in labs:
    b.append(leader(px, py, 466, ty - 4)); b.append(tlines(470, ty, ls, 11.5, "#222", True, 14))
b.append(box(462, 312, 200, 112, "#fff9db", "#f59f00"))
b.append(tlines(474, 334, ["Clareia como uma lâmpada", "de 40 a 60 W. Só funciona", "de DIA. Dura anos; troque", "a água se ficar turva ou", "verde. Água não vaza se", "a vedação for bem feita."], 11.5, "#5c3d00", False, 15))
open(D + "lampada-garrafa.svg", "w").write(svg(680, 440, "Lâmpada de garrafa no telhado (luz do dia)", "\n".join(b)))

# =====================================================================
# 3. MICRO-HIDRELETRICA: MEDIR VAZAO E QUEDA
# =====================================================================
b = []
b.append(line(340, 48, 340, 420, "#ccc", 2))
b.append(text(170, 66, "1. VAZÃO: método do balde", 14, "#222", True, "middle"))
# corrego e barragem
b.append(rect(10, 230, 320, 120, SOLO, "none", 0))
b.append(path("M20,170 L170,210 L170,236 L20,236 Z", AGUA2, "none", 0))
b.append(path("M20,186 Q90,192 150,206", "none", AGUA, 2))
b.append(rect(150, 196, 22, 44, "#8a8a8a", OUT, 2, 3))
b.append(text(122, 262, "pedras/tábua", 11, "#444", False, "middle"))
b.append(text(122, 276, "represando", 11, "#444", False, "middle"))
b.append(pipe([(166, 212), (220, 214)], 10, "#adb5bd"))
b.append(path("M222,214 Q234,222 236,250", "none", AGUA, 5))
# balde
b.append(path("M206,250 L214,320 L262,320 L270,250 Z", "#ffe066", OUT, 2.5))
b.append(path("M210,282 L215,318 L261,318 L266,282 Z", AGUA, "none", 0))
b.append(text(238, 304, "20 L", 12, "#fff", True, "middle"))
b.append(f'<circle cx="300" cy="150" r="20" fill="#fff" stroke="{OUT}" stroke-width="2.5"/>')
b.append(line(300, 150, 300, 136, OUT, 2.5)); b.append(line(300, 150, 310, 156, OUT, 2.5)); b.append(rect(295, 124, 10, 6, OUT, OUT, 1))
b.append(text(300, 186, "cronômetro", 11, "#444", False, "middle"))
b.append(box(20, 360, 300, 52, "#eef5ff", "#3f6d9e"))
b.append(tlines(30, 380, ["Encheu 20 L em 10 s → 20 ÷ 10 = 2 L/s.", "Meça na SECA (vazão mínima)."], 12, "#1b3d6b", False, 17))
# direita: queda com mangueira de nivel
b.append(text(510, 66, "2. QUEDA: mangueira de nível", 14, "#222", True, "middle"))
def gy(x): return 170 + (x - 350) * 0.42
b.append(path(f"M350,{gy(350)} L670,{gy(670)} L670,350 L350,350 Z", SOLO, "#6b4f2a", 2))
def vara(x, h):
    yb = gy(x); o = rect(x - 4, yb - h, 8, h, "#f8f9fa", OUT, 1.5)
    for k in range(1, int(h // 10)):
        o += line(x - 4, yb - k * 10, x + (1 if k % 5 else 4), yb - k * 10, OUT, 1)
    return o
xa, xb, LV = 420, 590, 150
b.append(vara(xa, gy(xa) - 118)); b.append(vara(xb, gy(xb) - 118))
hose = f"M{xa+8},124 L{xa+8},{gy(xa)-6} Q{xa+20},{gy(xa)+4} {(xa+xb)/2},{gy((xa+xb)/2)-4} Q{xb-20},{gy(xb)-2} {xb-8},{gy(xb)-8} L{xb-8},124"
b.append(path(hose, "none", "#555", 7)); b.append(path(hose, "none", "#e7f5ff", 4))
water = f"M{xa+8},{LV} L{xa+8},{gy(xa)-6} Q{xa+20},{gy(xa)+4} {(xa+xb)/2},{gy((xa+xb)/2)-4} Q{xb-20},{gy(xb)-2} {xb-8},{gy(xb)-8} L{xb-8},{LV}"
b.append(path(water, "none", AGUA, 4))
b.append(line(380, LV, 640, LV, DANGER, 1.5, "6 4"))
b.append(text(505, 112, "a água fica no MESMO nível", 11.5, DARK, True, "middle"))
b.append(text(505, 126, "nas duas pontas", 11.5, DARK, True, "middle"))
b.append(line(xa - 14, LV, xa - 14, gy(xa), "#222", 2)); b.append(text(xa - 20, (LV + gy(xa)) / 2 + 5, "a", 14, "#222", True, "end"))
b.append(line(xb + 14, LV, xb + 14, gy(xb), "#222", 2)); b.append(text(xb + 20, (LV + gy(xb)) / 2 + 5, "b", 14, "#222", True))
b.append(text(xa, gy(xa) + 22, "vara A", 11, "#444", True, "middle")); b.append(text(xb + 4, gy(xb) + 22, "vara B", 11, "#444", True, "middle"))
b.append(text(500, 326, "mangueira transparente cheia", 11, "#1f5f9e", True, "middle"))
b.append(text(500, 340, "de água, sem bolhas", 11, "#1f5f9e", True, "middle"))
b.append(box(350, 290 + 70, 310, 52, "#eef5ff", "#3f6d9e"))
b.append(tlines(360, 380, ["Desnível = b − a. Desça repetindo e SOME", "tudo, da captação até a turbina."], 12, "#1b3d6b", False, 17))
b.append(box(20, 424, 640, 48, "#fff4e5", "#ef8a2b"))
b.append(text(340, 446, "Potência (W) ≈ 5 × vazão (L/s) × queda (m)", 15, "#222", True, "middle"))
b.append(text(340, 464, "Ex.: 2 L/s com 15 m de queda → ≈ 150 W, dia e noite = 3,6 kWh por dia", 12, "#444", False, "middle"))
open(D + "micro-hidro-medicao.svg", "w").write(svg(680, 482, "Micro-hidrelétrica: medir vazão e queda", "\n".join(b)))

# =====================================================================
# 4. AQUECEDOR SOLAR DE AGUA (termossifao) — vista de lado
# =====================================================================
b = []
GY = 410
b.append(rect(0, GY, 680, 30, SOLO, "none", 0)); b.append(line(0, GY, 680, GY, "#6b4f2a", 3))
b.append(sun(60, 90, 20))
# coletor de lado (inclinado)
b.append('<polygon points="96,362 112,374 312,258 296,246" fill="#212529" stroke="#1e1e1e" stroke-width="2.5" stroke-linejoin="round"/>')
b.append(line(108, 372, 108, GY, "#666", 5)); b.append(line(290, 262, 290, GY, "#666", 5))
b.append(tlines(70, 436 - 0, [""], 11))
# caixa
TX, TY, TW, TH = 400, 106, 160, 96
b.append(rect(TX - 8, TY - 8, TW + 16, TH + 16, "#f1dfa6", OUT, 2, 8))
b.append(rect(TX, TY, TW, TH / 2, "#ffc9c9", "none", 0)); b.append(rect(TX, TY + TH / 2, TW, TH / 2, AGUA2, "none", 0))
b.append(rect(TX, TY, TW, TH, "none", OUT, 2.5, 4))
b.append(text(TX + TW / 2, TY + 30, "quente (em cima)", 11.5, DARK, True, "middle"))
b.append(text(TX + TW / 2, TY + 80, "fria (embaixo)", 11.5, AZUL, True, "middle"))
b.append(line(TX + 10, TY + TH + 8, TX + 10, GY, "#999", 6)); b.append(line(TX + TW - 10, TY + TH + 8, TX + TW - 10, GY, "#999", 6))
b.append(text(TX + 50, TY - 32, "CAIXA ISOLADA", 12.5, "#222", True, "middle"))
b.append(text(TX + 50, TY - 17, "(isopor, serragem, lã)", 11, "#444", False, "middle"))
# cano quente: topo do coletor -> parte de cima da caixa
b.append(pipe([(306, 250), (350, 206), (350, 126), (TX, 126)], 8, "#ff8787"))
# cano frio: fundo da caixa -> parte de baixo do coletor
b.append(pipe([(TX, 188), (378, 188), (378, 392), (84, 392), (84, 362), (100, 364)], 8, "#74c0fc"))
b.append(arrow(336, 196, 336, 150, DARK, 3)); b.append(tlines(240, 160, ["quente sobe", "sozinha"], 11.5, DARK, True, 14))
b.append(arrow(364, 270, 364, 330, AZUL, 3)); b.append(tlines(306, 300, ["fria", "desce"], 11.5, AZUL, True, 14))
# saida chuveiro e entrada
b.append(pipe([(TX + TW, 122), (622, 122), (622, 330)], 6, "#ff8787"))
b.append(tlines(600, 352, ["para o", "chuveiro"], 11, "#222", False, 13))
b.append(pipe([(TX + 130, 60), (TX + 130, TY)], 6, "#74c0fc"))
b.append(text(TX + 140, 64, "entrada de", 11, "#222")); b.append(text(TX + 140, 78, "água (boia)", 11, "#222"))
# altura
b.append(line(312, 252, 470, 252, "#222", 1.2, "3 3"))
b.append(line(470, 252, 470, TY + TH + 8, "#222", 1.5))
b.append(tlines(420, 278, ["≥ 30 cm entre o", "fundo da caixa e", "o topo do coletor"], 11.5, "#222", True, 14))
b.append(tlines(40, 270, ["COLETOR PRETO", "virado para o NORTE"], 12, "#222", True, 15))
b.append(box(20, 450, 640, 60, "#fff4e5", "#ef8a2b"))
b.append(tlines(34, 472, ["Sem bomba: a água aquecida fica mais leve e sobe. ~1 m² de coletor para cada 50 L/dia.",
                          "Inclinação = latitude + 10°. PVC comum deforma acima de ~60 °C: prefira CPVC, PPR ou cobre."], 12.5, "#222", False, 18))
open(D + "aquecedor-solar.svg", "w").write(svg(680, 520, "Aquecedor solar de água sem bomba (termossifão)", "\n".join(b)))
print("ok outros")
