import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
import math
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "08-ferramentas-e-mecanica", "img") + "/"
os.makedirs(D, exist_ok=True)
RED = "#d62828"; DRED = "#b3001b"; GREEN = "#2b8a3e"; DGREEN = "#1d6b2c"; WOOD = "#8b5a2b"
TUBE = "#3a3a3a"


def lines(x, y, ls, size=12, color="#222", bold=False, anchor="start", lh=None):
    lh = lh or size * 1.3
    return "\n".join(text(x, y + i * lh, s, size, color, bold, anchor) for i, s in enumerate(ls))


def badge(x, y, n, fill="#3f6d9e", r=13):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>'
            f'<text x="{x}" y="{y+5}" font-size="15" font-weight="bold" fill="#fff" text-anchor="middle">{n}</text>')


def arcpath(cx, cy, r, a1, a2):
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    x2, y2 = cx + r * math.cos(math.radians(a2)), cy + r * math.sin(math.radians(a2))
    return f"M{x1:.1f} {y1:.1f} A {r} {r} 0 0 1 {x2:.1f} {y2:.1f}"


# =====================================================================
# 1) REMENDO DE CAMARA
# =====================================================================
b = []
PW, PH = 210, 228
pos = [(15, 46), (235, 46), (455, 46), (15, 284), (235, 284), (455, 284)]
tit = [["Tire o pneu de um lado", "com 2 ou 3 espátulas"],
       ["Encha um pouco e ache", "o furo: bolhas na água"],
       ["Lixe em volta do furo", "(maior que o remendo)"],
       ["Cola em camada fina;", "espere ficar FOSCA"],
       ["Aperte o remendo do", "centro para as bordas"],
       ["Ache o espinho no pneu", "antes de montar"]]
cap = [["Não use chave de fenda:", "ela fura a câmara."],
       ["Marque o furo com giz ou", "caneta. Sem bacia: ouça o ar."],
       ["Lixa fina, até a borracha", "ficar opaca e áspera."],
       ["3–5 min (até 10 no frio).", "Não sopre, não toque."],
       ["Aperte forte 1–2 min.", "Tire o plástico de cima depois."],
       ["Passe a mão DEVAGAR por", "dentro do pneu e do aro."]]


def tubo(x, y, w, h=30):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{TUBE}" stroke="#111" stroke-width="2"/>'
            f'<rect x="{x+8}" y="{y+5}" width="{w-16}" height="5" rx="2.5" fill="#6a6a6a"/>')


for i, ((x, y), t, c) in enumerate(zip(pos, tit, cap)):
    b.append(box(x, y, PW, PH, "#f7f7f7", "#999"))
    b.append(badge(x + 20, y + 22, i + 1))
    b.append(lines(x + 40, y + 20, t, 12.5, "#1e1e1e", True, "start", 16))
    b.append(lines(x + PW / 2, y + PH - 28, c, 11.5, "#333", False, "middle", 15))

# 1 - espatulas
x, y = pos[0]; cx, cy = x + 105, y + 244
b.append(f'<clipPath id="cp1"><rect x="{x+3}" y="{y+40}" width="{PW-6}" height="146"/></clipPath><g clip-path="url(#cp1)">')
b.append(f'<path d="{arcpath(cx, cy, 118, 195, 345)}" fill="none" stroke="#1e1e1e" stroke-width="26"/>')
b.append(f'<path d="{arcpath(cx, cy, 98, 195, 345)}" fill="none" stroke="#b0b0b0" stroke-width="10"/>')
for k in range(9):
    a = math.radians(200 + k * 17.5)
    b.append(f'<line x1="{cx+30*math.cos(a):.1f}" y1="{cy+30*math.sin(a):.1f}" x2="{cx+94*math.cos(a):.1f}" y2="{cy+94*math.sin(a):.1f}" stroke="#999" stroke-width="2"/>')
for a in (245, 295):
    ar = math.radians(a)
    x1, y1 = cx + 90 * math.cos(ar), cy + 90 * math.sin(ar)
    x2, y2 = cx + 160 * math.cos(ar), cy + 160 * math.sin(ar)
    b.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#1e1e1e" stroke-width="12" stroke-linecap="round"/>')
    b.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#2f7de1" stroke-width="8" stroke-linecap="round"/>')
b.append('</g>')
b.append(text(x + 105, y + 130, "pneu", 11, "#fff", True, "middle"))
b.append(text(x + 105, y + 166, "aro", 11, "#333", True, "middle"))
b.append(text(x + 105, y + 62, "espátulas", 11, "#1e5bb0", True, "middle"))

# 2 - bacia com bolhas
x, y = pos[1]
b.append(f'<path d="M{x+30} {y+110} L{x+180} {y+110} L{x+165} {y+180} L{x+45} {y+180} Z" fill="#cfe6fb" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<line x1="{x+30}" y1="{y+110}" x2="{x+180}" y2="{y+110}" stroke="#4a90d9" stroke-width="3"/>')
b.append(f'<path d="M{x+55} {y+70} C {x+60} {y+165}, {x+150} {y+165}, {x+155} {y+70}" fill="none" stroke="#111" stroke-width="18"/>')
b.append(f'<path d="M{x+55} {y+70} C {x+60} {y+165}, {x+150} {y+165}, {x+155} {y+70}" fill="none" stroke="{TUBE}" stroke-width="14"/>')
for k, (dx, dy, rr) in enumerate([(0, 0, 3), (4, -9, 4), (-2, -19, 5)]):
    b.append(f'<circle cx="{x+105+dx}" cy="{y+134+dy}" r="{rr}" fill="#fff" stroke="#2a6db5" stroke-width="1.5"/>')
b.append(text(x + 105, y + 100, "bolhas!", 11.5, "#1e5bb0", True, "middle"))

# 3 - lixar
x, y = pos[2]
b.append(tubo(x + 20, y + 110, 170))
b.append(f'<circle cx="{x+105}" cy="{y+125}" r="22" fill="none" stroke="#f5f5f5" stroke-width="2" stroke-dasharray="4 3"/>')
b.append(f'<circle cx="{x+105}" cy="{y+125}" r="3" fill="{RED}"/>')
b.append(f'<rect x="{x+82}" y="{y+62}" width="46" height="36" rx="3" fill="#d8b878" stroke="#1e1e1e" stroke-width="2" transform="rotate(-8 {x+105} {y+80})"/>')
b.append(arrow(x + 64, y + 76, x + 40, y + 76, "#555", 3)); b.append(arrow(x + 146, y + 76, x + 170, y + 76, "#555", 3))
b.append(text(x + 105, y + 160, "furo", 11, DRED, True, "middle"))
b.append(text(x + 105, y + 58, "lixa", 11, "#333", False, "middle"))

# 4 - cola
x, y = pos[3]
b.append(tubo(x + 20, y + 120, 170))
b.append(f'<ellipse cx="{x+105}" cy="{y+135}" rx="34" ry="13" fill="#7a7a7a" stroke="#bbb" stroke-width="1.5"/>')
b.append(f'<circle cx="{x+105}" cy="{y+135}" r="3" fill="{RED}"/>')
# tubinho de cola
b.append(f'<g transform="rotate(30 {x+60} {y+80})"><rect x="{x+30}" y="{y+70}" width="56" height="20" rx="4" fill="#e9e9e9" stroke="#1e1e1e" stroke-width="2"/><rect x="{x+86}" y="{y+75}" width="14" height="10" fill="#c00" stroke="#1e1e1e" stroke-width="1.5"/><text x="{x+58}" y="{y+84}" font-size="9" font-weight="bold" text-anchor="middle" fill="#1e1e1e">COLA</text></g>')
# relogio
b.append(f'<circle cx="{x+160}" cy="{y+76}" r="22" fill="#fff" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<line x1="{x+160}" y1="{y+76}" x2="{x+160}" y2="{y+60}" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<line x1="{x+160}" y1="{y+76}" x2="{x+171}" y2="{y+82}" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<path d="M{x+160} {y+76} L{x+160} {y+54} A 22 22 0 0 1 {x+180.5} {y+68} Z" fill="{RED}" fill-opacity="0.35"/>')
b.append(text(x + 160, y + 114, "3–5 min", 11.5, DRED, True, "middle"))

# 5 - aplicar remendo
x, y = pos[4]
b.append(tubo(x + 20, y + 120, 170))
b.append(f'<rect x="{x+82}" y="{y+116}" width="46" height="38" rx="6" fill="#2a2a2a" stroke="#ef8a2b" stroke-width="4"/>')
b.append(f'<ellipse cx="{x+105}" cy="{y+102}" rx="22" ry="15" fill="{SKIN}" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<path d="M{x+90} {y+92} q 15 -8 30 0" fill="none" stroke="#c99b78" stroke-width="2"/>')
b.append(f'<rect x="{x+90}" y="{y+56}" width="30" height="36" rx="10" fill="{SKIN}" stroke="#1e1e1e" stroke-width="2"/>')
b.append(arrow(x + 105, y + 50, x + 105, y + 72, RED, 3))
b.append(arrow(x + 76, y + 135, x + 50, y + 135, "#ef8a2b", 2.5)); b.append(arrow(x + 134, y + 135, x + 160, y + 135, "#ef8a2b", 2.5))
b.append(text(x + 105, y + 172, "remendo", 11, "#a35a00", True, "middle"))

# 6 - procurar espinho
x, y = pos[5]
b.append(f'<path d="M{x+20} {y+90} Q {x+105} {y+70} {x+190} {y+90} L{x+190} {y+150} Q {x+105} {y+130} {x+20} {y+150} Z" fill="#2a2a2a" stroke="#111" stroke-width="2"/>')
b.append(f'<path d="M{x+20} {y+104} Q {x+105} {y+84} {x+190} {y+104} L{x+190} {y+138} Q {x+105} {y+118} {x+20} {y+138} Z" fill="#555"/>')
b.append(text(x + 105, y + 172, "parte de dentro do pneu", 10.5, "#333", False, "middle"))
b.append(f'<polygon points="{x+150},{y+96} {x+160},{y+96} {x+155},{y+114}" fill="#c9a227" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(f'<circle cx="{x+155}" cy="{y+104}" r="16" fill="none" stroke="{RED}" stroke-width="3"/>')
b.append(f'<ellipse cx="{x+92}" cy="{y+118}" rx="34" ry="13" fill="{SKIN}" stroke="#1e1e1e" stroke-width="2"/>')
for k in range(3):
    b.append(f'<rect x="{x+110}" y="{y+106+k*8}" width="26" height="8" rx="4" fill="{SKIN}" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(text(x + 155, y + 78, "espinho", 11, DRED, True, "middle"))

b.append(box(15, 522, 650, 54, "#eef5ff", "#3f6d9e"))
b.append(lines(28, 543, ["Monte: ponha um pouco de ar na câmara, encaixe o bico primeiro, entre o pneu com as mãos.",
                         "Confira se a câmara não ficou presa entre o pneu e o aro. Encha até a pressão escrita no pneu."], 12, "#1e1e1e", False, "start", 18))
open(D + "remendo-camara.svg", "w").write(svg(680, 586, "Remendo de câmara de bicicleta, passo a passo", "\n".join(b)))

# =====================================================================
# 2) FORJA DE TAMBOR DE FREIO (CORTE)
# =====================================================================
b = []
G = 520  # chao
b.append(f'<rect x="0" y="{G}" width="680" height="20" fill="#e8d3b0"/>')
IRON = "#5a5a5a"
L, Rr, TOPY, BOT = 200, 470, 236, 330  # paredes do tambor
# mesa/pernas
b.append(f'<rect x="150" y="{BOT+18}" width="370" height="14" fill="#7d7d7d" stroke="#1e1e1e" stroke-width="2"/>')
for lx in (166, 490):
    b.append(f'<rect x="{lx}" y="{BOT+32}" width="14" height="{G-BOT-32}" fill="#7d7d7d" stroke="#1e1e1e" stroke-width="2"/>')
# carvao (antes das paredes)
import random
random.seed(4)
cx0 = (L + Rr) / 2
for _ in range(240):
    px = random.uniform(L + 16, Rr - 16)
    top_here = 206 - 30 * math.cos((px - cx0) / (Rr - L) * math.pi)  # monte
    py = random.uniform(top_here, BOT - 6)
    d = math.hypot((px - cx0) / 1.3, py - 268)
    col = "#f8c63a" if d < 30 else ("#f08c1e" if d < 52 else ("#b3361a" if d < 72 else "#2a2a2a"))
    r = random.uniform(6, 10)
    pts = " ".join(f"{px + r*math.cos(a + random.uniform(-0.3,0.3)):.1f},{py + r*0.8*math.sin(a):.1f}" for a in [k * math.pi / 3 for k in range(6)])
    b.append(f'<polygon points="{pts}" fill="{col}" stroke="#111" stroke-width="1"/>')
# paredes e fundo do tambor (corte)
b.append(f'<rect x="{L}" y="{TOPY}" width="18" height="{BOT-TOPY+18}" fill="{IRON}" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<rect x="{Rr-18}" y="{TOPY}" width="18" height="{BOT-TOPY+18}" fill="{IRON}" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<rect x="{L}" y="{BOT}" width="{cx0-14-L}" height="18" fill="{IRON}" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<rect x="{cx0+14}" y="{BOT}" width="{Rr-cx0-14}" height="18" fill="{IRON}" stroke="#1e1e1e" stroke-width="2"/>')
for xx in (L, Rr - 18):
    b.append(f'<rect x="{xx-6 if xx==L else xx}" y="{TOPY}" width="24" height="10" fill="{IRON}" stroke="#1e1e1e" stroke-width="2"/>')
# grelha
b.append(f'<rect x="{cx0-34}" y="{BOT-8}" width="68" height="8" fill="#9a9a9a" stroke="#1e1e1e" stroke-width="1.5"/>')
for k in range(5):
    b.append(f'<rect x="{cx0-26+k*12}" y="{BOT-8}" width="4" height="8" fill="#111"/>')
# tubo de ar
PX0, PX1 = cx0 - 14, cx0 + 14
b.append(f'<rect x="{PX0}" y="{BOT+18}" width="28" height="{440-BOT-18}" fill="#444" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<rect x="{PX1}" y="400" width="170" height="28" fill="#444" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<rect x="{PX0-6}" y="440" width="40" height="14" rx="3" fill="#888" stroke="#1e1e1e" stroke-width="2"/>')
# registro
b.append(f'<rect x="{PX1+70}" y="392" width="10" height="44" fill="#c0392b" stroke="#1e1e1e" stroke-width="1.5"/>')
# soprador
b.append(f'<rect x="{PX1+170}" y="384" width="66" height="60" rx="10" fill="#6aa0d8" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<circle cx="{PX1+203}" cy="414" r="18" fill="#cfe6fb" stroke="#1e1e1e" stroke-width="2"/>')
for a in range(0, 360, 60):
    ar = math.radians(a)
    b.append(f'<line x1="{PX1+203}" y1="414" x2="{PX1+203+15*math.cos(ar):.1f}" y2="{414+15*math.sin(ar):.1f}" stroke="#1e1e1e" stroke-width="2"/>')
# setas de ar
b.append(arrow(PX1 + 150, 414, PX1 + 100, 414, "#4a90d9", 4))
b.append(arrow(PX1 + 60, 414, PX1 + 8, 414, "#4a90d9", 4))
b.append(arrow(cx0, 396, cx0, 360, "#4a90d9", 4))
# peca (entra por cima da borda, inclinada)
def seg(x1, y1, x2, y2, col, w=12):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#1e1e1e" stroke-width="{w+4}" stroke-linecap="butt"/>'
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}" stroke-linecap="butt"/>')
ax, ay, bx_, by_ = 40, 176, cx0 + 4, 266
def pt(t):
    return ax + (bx_ - ax) * t, ay + (by_ - ay) * t
p1 = pt(0.62); p2 = pt(0.80)
b.append(seg(ax, ay, round(p1[0], 1), round(p1[1], 1), "#888"))
b.append(seg(round(p1[0], 1), round(p1[1], 1), round(p2[0], 1), round(p2[1], 1), "#f08c1e"))
b.append(seg(round(p2[0], 1), round(p2[1], 1), bx_, by_, "#ffd25a"))
# rotulos
b.append(lines(18, 78, ["Carvão vegetal em pedaços de 2–5 cm.", "Monte por cima e em volta da peça."], 12, "#222", True))
b.append(f'<line x1="200" y1="96" x2="{cx0-40}" y2="200" stroke="#555" stroke-width="1.5"/>')
b.append(lines(400, 78, ["Parte mais quente: 5–10 cm acima", "da entrada de ar (amarelo)."], 12, "#222", True))
b.append(f'<line x1="430" y1="96" x2="{cx0+10}" y2="256" stroke="#555" stroke-width="1.5"/>')
b.append(lines(18, 214, ["peça no meio", "do fogo"], 12, "#222", True))
b.append(lines(500, 196, ["TAMBOR DE FREIO", "de carro ou caminhão", "(ferro fundido);", "borda a 75–85 cm", "do chão (cintura)"], 12, "#1e1e1e", True))
b.append(f'<line x1="496" y1="208" x2="{Rr+2}" y2="244" stroke="#555" stroke-width="1.5"/>')
b.append(lines(500, 306, ["grelha: chapa com furos", "de 6–10 mm sobre o furo"], 11.5, "#222"))
b.append(f'<line x1="496" y1="300" x2="{cx0+36}" y2="{BOT-4}" stroke="#555" stroke-width="1.5"/>')
b.append(lines(20, 380, ["tubo de ferro preto", "1\" a 1 1/2\" (2,5–4 cm)"], 11.5, "#222"))
b.append(text(20, 419, "NUNCA galvanizado", 11.5, DRED, True))
b.append(lines(20, 446, ["tampa embaixo: abra", "para tirar as cinzas"], 11.5, "#222"))
b.append(f'<line x1="140" y1="452" x2="{PX0-8}" y2="447" stroke="#555" stroke-width="1.5"/>')
b.append(lines(PX1 + 36, 456, ["registro (tampa", "deslizante):", "regula o ar"], 11.5, "#222"))
b.append(lines(PX1 + 160, 462, ["AR: secador de", "cabelo (no frio),", "ventoinha 12 V", "ou fole"], 11.5, "#1e3f66", True))
b.append(box(15, G + 28, 650, 58, "#fdecec", "#d62828"))
b.append(lines(28, G + 50, ["Ao ar livre ou em galpão bem aberto (carvão solta MONÓXIDO). Balde de água ao lado.",
                          "Longe de capim, palha e sapé. Óculos, roupa de algodão ou couro, sapato fechado."], 12, DRED, True, "start", 19))
open(D + "forja-tambor.svg", "w").write(svg(680, G + 96, "Forja simples de tambor de freio (corte)", "\n".join(b)))

# =====================================================================
# 3) CORES DO ACO: INCANDESCENCIA E REVENIDO
# =====================================================================
b = []
b.append(text(20, 62, "1. Cor do aço aquecido (olhe na SOMBRA; no sol forte parece mais frio do que está)", 12.5, "#222", True))
heat = [("~550", "#3d0805", "vermelho", "quase preto"), ("~650", "#6e0e08", "vermelho", "sangue"),
        ("~750", "#a5180c", "vermelho", "escuro"), ("~820", "#d0301a", "cereja", ""),
        ("~900", "#ea5a1c", "cereja", "claro"), ("~1.000", "#f58a1f", "laranja", ""),
        ("~1.100", "#f8c63a", "amarelo", ""), ("~1.250", "#fdf3c0", "amarelo-", "branco")]
W = 80; X0 = 20; Y = 92
for i, (t, c, n1, n2) in enumerate(heat):
    x = X0 + i * W
    b.append(f'<rect x="{x}" y="{Y}" width="{W}" height="46" fill="{c}" stroke="#1e1e1e" stroke-width="1.5"/>')
    b.append(text(x + W / 2, Y - 8, t + " °C", 11.5, "#222", True, "middle"))
    b.append(text(x + W / 2, Y + 60, n1, 11.5, "#222", False, "middle"))
    if n2:
        b.append(text(x + W / 2, Y + 74, n2, 11.5, "#222", False, "middle"))


def bracket(x1, x2, y, label, color, sub=None):
    s = f'<path d="M{x1} {y-8} L{x1} {y} L{x2} {y} L{x2} {y-8}" fill="none" stroke="{color}" stroke-width="2.5"/>'
    s += text((x1 + x2) / 2, y + 16, label, 12, color, True, "middle")
    if sub:
        s += text((x1 + x2) / 2, y + 31, sub, 11, "#333", False, "middle")
    return s


b.append(bracket(X0 + 3 * W + 4, X0 + 7 * W - 4, Y + 98, "FORJAR (bater)", "#a35a00", "do amarelo até o cereja"))
b.append(bracket(X0 + 3 * W + 6, X0 + 5 * W - 30, Y + 146, "TEMPERAR", DRED, "~800 °C"))
b.append(bracket(X0 + 4, X0 + 3 * W - 4, Y + 98, "NÃO bata: racha", "#555", "reaqueça"))
b.append(bracket(X0 + 7 * W + 4, X0 + 8 * W - 4, Y + 98, "queima", DRED, "faíscas"))
b.append(lines(X0 + 5 * W - 20, Y + 150, ["Ímã: quando para de grudar (~770 °C),", "aqueça mais um tom e mergulhe."], 11.5, "#222"))
# revenido
Y2 = 316
b.append(text(20, Y2 - 26, "2. Cores do REVENIDO (lixe até brilhar e aqueça DEVAGAR; a cor aparece na superfície)", 12.5, "#222", True))
temp = [("200", "#efe2a6", "palha clara", ["navalha,", "raspador"]), ("220", "#e2c56a", "palha", ["faca,", "plaina"]),
        ("240", "#c99838", "palha escura", ["faca de lida,", "formão"]), ("255", "#9a6430", "bronze", ["tesoura,", "talhadeira"]),
        ("270", "#7a3a6c", "roxo", ["machado,", "enxó"]), ("290", "#2b3d8c", "azul escuro", ["facão, mola,", "chave de fenda"]),
        ("310", "#4f7fc4", "azul claro", ["mola,", "serrote"]), ("330+", "#8ea1b5", "cinza", ["mole demais:", "perdeu"])]
for i, (t, c, n, uso) in enumerate(temp):
    x = X0 + i * W
    b.append(f'<rect x="{x}" y="{Y2}" width="{W}" height="46" fill="{c}" stroke="#1e1e1e" stroke-width="1.5"/>')
    b.append(text(x + W / 2, Y2 + 28, t + " °C", 12, "#fff" if i in (4, 5) else "#1e1e1e", True, "middle"))
    b.append(text(x + W / 2, Y2 + 62, n, 11.5, "#222", True, "middle"))
    b.append(lines(x + W / 2, Y2 + 78, uso, 10.5, "#444", False, "middle", 13))
b.append(arrow(X0 + 10, Y2 + 120, X0 + 8 * W - 10, Y2 + 120, "#555", 3))
b.append(text(X0 + 10, Y2 + 138, "mais DURO (segura fio, quebra fácil)", 11.5, "#222", True))
b.append(text(X0 + 8 * W - 10, Y2 + 138, "mais TENAZ (dobra, não quebra)", 11.5, "#222", True, "end"))
b.append(box(15, Y2 + 152, 650, 74, "#fff4e5", "#ef8a2b"))
b.append(lines(28, Y2 + 173, [
    "Teste da LIMA depois da têmpera: lima nova escorrega sem morder = temperou. Se morde, repita.",
    "Revenir LOGO (em até 1 hora): aço temperado sem revenir é quebradiço como vidro.",
    "Forno de cozinha: 1 hora a 200–220 °C para facas; esfrie e repita mais 1 vez."], 12, "#1e1e1e", False, "start", 19))
open(D + "cores-do-aco.svg", "w").write(svg(680, Y2 + 236, "Cores do aço: temperatura e revenido", "\n".join(b)))

# =====================================================================
# 4) BICICLETA: PONTOS DE AJUSTE
# =====================================================================
b = []
R, F, B = (170, 300), (510, 300), (330, 312)
S, H, H2 = (300, 172), (468, 168), (480, 208)
WR = 96
for (wx, wy) in (R, F):
    for k in range(18):
        a = math.radians(k * 20)
        b.append(f'<line x1="{wx}" y1="{wy}" x2="{wx+WR*0.86*math.cos(a):.1f}" y2="{wy+WR*0.86*math.sin(a):.1f}" stroke="#aaa" stroke-width="1.5"/>')
    b.append(f'<circle cx="{wx}" cy="{wy}" r="{WR}" fill="none" stroke="#1e1e1e" stroke-width="13"/>')
    b.append(f'<circle cx="{wx}" cy="{wy}" r="{WR-9}" fill="none" stroke="#9a9a9a" stroke-width="4"/>')
    b.append(f'<circle cx="{wx}" cy="{wy}" r="8" fill="#ccc" stroke="#1e1e1e" stroke-width="2"/>')
FR = "#3f6d9e"
def tube(p1, p2, w=9):
    return (f'<line x1="{p1[0]}" y1="{p1[1]}" x2="{p2[0]}" y2="{p2[1]}" stroke="#1e1e1e" stroke-width="{w+4}" stroke-linecap="round"/>'
            f'<line x1="{p1[0]}" y1="{p1[1]}" x2="{p2[0]}" y2="{p2[1]}" stroke="{FR}" stroke-width="{w}" stroke-linecap="round"/>')
# corrente
b.append(f'<line x1="{R[0]}" y1="{R[1]-12}" x2="{B[0]}" y2="{B[1]-26}" stroke="#555" stroke-width="3"/>')
b.append(f'<line x1="{R[0]}" y1="{R[1]+12}" x2="{B[0]}" y2="{B[1]+26}" stroke="#555" stroke-width="3"/>')
b.append(f'<circle cx="{R[0]}" cy="{R[1]}" r="13" fill="#bbb" stroke="#1e1e1e" stroke-width="2"/>')
for p1, p2 in ((R, B), (R, S), (S, B), (S, H), (H2, B), (H, H2)):
    b.append(tube(p1, p2))
b.append(tube(H2, F, 7))
# coroa e pedivela
b.append(f'<circle cx="{B[0]}" cy="{B[1]}" r="27" fill="#ddd" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{B[0]+30}" y2="{B[1]+52}" stroke="#1e1e1e" stroke-width="8" stroke-linecap="round"/>')
b.append(f'<rect x="{B[0]+18}" y="{B[1]+52}" width="28" height="9" rx="2" fill="#555" stroke="#1e1e1e" stroke-width="1.5"/>')
# selim e guidao
b.append(f'<line x1="{S[0]}" y1="{S[1]}" x2="{S[0]-4}" y2="{S[1]-26}" stroke="#888" stroke-width="7"/>')
b.append(f'<path d="M{S[0]-36} {S[1]-30} Q {S[0]-6} {S[1]-42} {S[0]+24} {S[1]-32} L {S[0]+20} {S[1]-24} Q {S[0]-10} {S[1]-28} {S[0]-36} {S[1]-24} Z" fill="#333" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<line x1="{H[0]}" y1="{H[1]}" x2="{H[0]-6}" y2="{H[1]-28}" stroke="#888" stroke-width="7"/>')
b.append(f'<path d="M{H[0]-6} {H[1]-28} L{H[0]-40} {H[1]-34}" stroke="#555" stroke-width="6" stroke-linecap="round"/>')
b.append(f'<rect x="{H[0]-56}" y="{H[1]-40}" width="20" height="10" rx="4" fill="#222"/>')
b.append(f'<path d="M{H[0]-30} {H[1]-36} q -14 4 -24 14" fill="none" stroke="#222" stroke-width="2.5"/>')
# freios
for (bx, by) in ((R[0] + 30, R[1] - 92), (F[0] - 14, F[1] - 96)):
    b.append(f'<rect x="{bx-7}" y="{by-6}" width="14" height="14" rx="3" fill="#d62828" stroke="#1e1e1e" stroke-width="1.5"/>')
def call(n, x, y, tx, ty):
    return (f'<line x1="{x}" y1="{y}" x2="{tx}" y2="{ty}" stroke="#555" stroke-width="1.5"/>'
            + badge(tx, ty, n, "#ef8a2b", 12))
b.append(call(1, 92, 236, 60, 80))
b.append(call(2, R[0] + 30, R[1] - 96, 200, 80))
b.append(call(3, 250, 292, 250, 440))
b.append(call(4, B[0] + 34, B[1] + 58, 360, 440))
b.append(call(5, F[0] + 50, F[1] + 40, 600, 440))
b.append(call(6, F[0], F[1], 640, 300))
b.append(call(7, S[0] - 10, S[1] - 36, 380, 80))
T = [(1, "Pneu: pressão escrita na lateral", "(ex.: 40–65 psi); com carga, perto do máximo"),
     (2, "Freio: sapata a 1–2 mm do aro,", "sem tocar no pneu; manete firme antes da metade"),
     (3, "Corrente: limpe e lubrifique a cada", "100–200 km; sem marchas, folga de 1–1,5 cm"),
     (4, "Pedal ESQUERDO tem rosca INVERTIDA", "(aperta girando para trás da bicicleta)"),
     (5, "Raios: todos com o mesmo aperto", "(toque: mesmo som); aro sem empeno"),
     (6, "Cubos: balance a roda: sem folga,", "girando livre e sem ranger"),
     (7, "Selim: pedal embaixo, perna quase", "esticada (joelho levemente dobrado)")]
b.append(box(15, 470, 650, 182, "#f7f7f7", "#999"))
for i, (n, l1, l2) in enumerate(T):
    col = 0 if i < 4 else 1
    row = i if i < 4 else i - 4
    x = 30 + col * 330; y = 494 + row * 42
    b.append(badge(x + 8, y - 4, n, "#ef8a2b", 11))
    b.append(text(x + 26, y, l1, 11.5, "#1e1e1e", True))
    b.append(text(x + 26, y + 15, l2, 11, "#333"))
open(D + "bicicleta-ajustes.svg", "w").write(svg(680, 662, "Bicicleta: os 7 pontos para conferir", "\n".join(b)))
print("ok gen_mecanica3")
