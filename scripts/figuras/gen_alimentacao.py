import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
import math
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "03-alimentacao", "img") + "/"
os.makedirs(D, exist_ok=True)
WOOD = "#8b5a2b"; SOIL = "#e8d3b0"; WATER = "#4a90d9"; WATERL = "#cfe6fb"
RED = "#d62828"; DRED = "#b3001b"; GREEN = "#2b8a3e"; CLAY = "#c8703a"; ORANGE = "#ef8a2b"


def lines(x, y, arr, size=12, color="#222", bold=False, lh=15, anchor="start"):
    out = []
    for i, s in enumerate(arr):
        bb = bold if isinstance(bold, bool) else (i in bold)
        out.append(text(x, y + i * lh, s, size, color, bb, anchor))
    return "".join(out)


def lead(x1, y1, x2, y2, color="#555"):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.3"/>'
            f'<circle cx="{x2}" cy="{y2}" r="2.6" fill="{color}"/>')


def save(name, w, h, title, b):
    with open(D + name, "w", encoding="utf-8") as f:
        f.write(svg(w, h, title, "\n".join(b)))


def panel(x, y, w, h, n, title):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#fafafa" stroke="#c8c8c8"/>'
            f'<circle cx="{x+20}" cy="{y+22}" r="14" fill="{ORANGE}" stroke="{OUT}" stroke-width="1.5"/>'
            + text(x + 20, y + 27, str(n), 15, "#fff", True, "middle")
            + text(x + 42, y + 27, title, 14, "#222", True))


# =====================================================================
# 1. SECADOR SOLAR INDIRETO
# =====================================================================
b = []
b.append(f'<rect x="0" y="400" width="680" height="14" fill="{SOIL}"/>'
         '<line x1="0" y1="400" x2="680" y2="400" stroke="#6b4f2a" stroke-width="2"/>')
# sol
b.append('<circle cx="110" cy="100" r="30" fill="#f7c948" stroke="#e0a800" stroke-width="2"/>')
for k in range(8):
    a = k * math.pi / 4
    b.append(f'<line x1="{110+38*math.cos(a):.1f}" y1="{100+38*math.sin(a):.1f}" x2="{110+50*math.cos(a):.1f}" '
             f'y2="{100+50*math.sin(a):.1f}" stroke="#e0a800" stroke-width="3" stroke-linecap="round"/>')
b.append(text(110, 105, "SOL", 13, "#7a5200", True, "middle"))
for (x1, y1, x2, y2) in [(98, 152, 110, 325), (118, 152, 150, 314), (136, 146, 190, 303)]:
    b.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#f2a900" stroke-width="2.5" stroke-dasharray="7 5"/>')
# caixa de secagem (camara)
b.append(f'<rect x="350" y="128" width="150" height="178" fill="#fbf3e6" stroke="{WOOD}" stroke-width="6"/>')
b.append('<rect x="345" y="266" width="12" height="30" fill="#fff1dc"/>')
# coletor
b.append('<polygon points="70,340 352,261 352,298 70,376" fill="#fff1dc"/>')
b.append('<line x1="70" y1="376" x2="352" y2="298" stroke="#1e1e1e" stroke-width="7"/>')
b.append('<line x1="70" y1="340" x2="352" y2="261" stroke="#7fbfea" stroke-width="4"/>')
b.append('<line x1="70" y1="340" x2="70" y2="376" stroke="#555" stroke-width="2.5" stroke-dasharray="3 2"/>')
# pes
b.append(f'<rect x="66" y="378" width="8" height="22" fill="{WOOD}" stroke="{OUT}" stroke-width="1"/>')
b.append(f'<rect x="206" y="338" width="8" height="62" fill="{WOOD}" stroke="{OUT}" stroke-width="1"/>')
b.append(f'<rect x="356" y="306" width="10" height="84" fill="{WOOD}" stroke="{OUT}" stroke-width="1"/>')
b.append(f'<rect x="484" y="306" width="10" height="84" fill="{WOOD}" stroke="{OUT}" stroke-width="1"/>')
for x in (350, 478):
    b.append(f'<rect x="{x}" y="384" width="22" height="16" rx="2" fill="{WATERL}" stroke="{OUT}" stroke-width="1.5"/>')
# bandejas com fatias
for ty in (160, 190, 220, 250):
    b.append(f'<line x1="356" y1="{ty}" x2="494" y2="{ty}" stroke="#444" stroke-width="2.5" stroke-dasharray="4 2"/>')
    for (xa, xb) in [(359, 377), (392, 417), (433, 457), (473, 493)]:
        b.append(f'<rect x="{xa}" y="{ty-7}" width="{xb-xa}" height="6" rx="3" fill="#f4a259" stroke="#a0522d" stroke-width="1"/>')
# chamine
b.append(f'<rect x="405" y="88" width="40" height="40" fill="{WOOD}" stroke="{OUT}" stroke-width="2"/>')
b.append('<rect x="409" y="88" width="32" height="40" fill="#fbf3e6"/>')
b.append('<line x1="405" y1="90" x2="445" y2="90" stroke="#444" stroke-width="2.5" stroke-dasharray="3 2"/>')
b.append('<rect x="393" y="66" width="64" height="7" fill="#555" stroke="#1e1e1e" stroke-width="1"/>')
b.append('<line x1="410" y1="73" x2="410" y2="88" stroke="#555" stroke-width="2.5"/><line x1="440" y1="73" x2="440" y2="88" stroke="#555" stroke-width="2.5"/>')
# setas do ar
b.append(arrow(16, 358, 64, 358, WATER, 3.5))
b.append(arrow(95, 360, 185, 335, "#f08c00", 3.5))
b.append(arrow(205, 330, 330, 295, "#e8590c", 3.5))
b.append('<g opacity="0.8">')
for x in (385, 425, 466):
    b.append(arrow(x, 292, x, 140, "#d9480f", 2.5))
b.append('</g>')
b.append(arrow(418, 84, 386, 76, "#d9480f", 2.5))
b.append(arrow(432, 84, 464, 76, "#d9480f", 2.5))
# rotulos
b.append(lines(8, 318, ["ar frio", "entra"], 12, "#1d5d9b", True))
b.append(lines(180, 216, ["cobertura transparente", "(vidro ou plástico)"], 12, "#222", [0]))
b.append(lead(250, 246, 262, 284))
b.append(lines(222, 360, ["fundo PRETO", "(chapa ou lona preta)"], 11.5, "#222", [0]))
b.append(lead(240, 349, 240, 333))
b.append(lines(515, 76, ["saída do ar quente", "e úmido (com tela e", "chapéu contra chuva)"], 12, "#222", [0]))
b.append(lead(512, 100, 448, 104))
b.append(lines(515, 152, ["bandejas de TELA", "(nylon, mosquiteiro", "ou inox; nunca tela", "galvanizada)"], 12, "#222", [0]))
b.append(lead(512, 176, 496, 190))
b.append(lines(515, 236, ["caixa fechada e", "ESCURA: o sol não", "bate na comida"], 12, "#222", [1]))
b.append(lead(512, 246, 503, 262))
b.append(lines(515, 334, ["pés altos com latinha", "de água (barra formiga)"], 11.5))
b.append(lead(512, 352, 500, 390))
b.append(box(20, 420, 640, 66, "#eef5ff", "#3f6d9e"))
b.append(lines(34, 440, ["Caminho do ar: entra frio embaixo, esquenta no coletor preto, sobe pelas bandejas",
                         "e sai úmido pela chaminé. Temperatura ideal: 45–60 °C. Coletor virado para o NORTE",
                         "(no Brasil), inclinado 15–30°. Recolha a comida ou feche à noite (o sereno molha)."], 12.5, "#222", False, 17))
save("secador-solar.svg", 680, 498, "Secador solar indireto — corte lateral", b)


# =====================================================================
# 2. GELADEIRA DE BARRO (POTE-EM-POTE)
# =====================================================================
b = []
b.append(f'<rect x="0" y="406" width="680" height="10" fill="{SOIL}"/>'
         '<line x1="0" y1="406" x2="680" y2="406" stroke="#6b4f2a" stroke-width="2"/>')
b.append(text(210, 78, "Deixe na SOMBRA, onde bate vento", 13, GREEN, True, "middle"))
# tijolos
for x in (90, 180, 270):
    b.append(f'<rect x="{x}" y="388" width="60" height="18" fill="#b5523b" stroke="{OUT}" stroke-width="1.5"/>')
# pote de fora
b.append(f'<path d="M60,130 L88,380 Q210,405 332,380 L360,130 Z" fill="{CLAY}" stroke="{OUT}" stroke-width="2.5"/>')
b.append('<path d="M74,130 L100,367 Q210,391 320,367 L346,130 Z" fill="#c9ad80" stroke="#7a4a22" stroke-width="1.5"/>')
# textura de areia molhada
import random
random.seed(3)
pts = []
for _ in range(260):
    x = random.uniform(78, 342); y = random.uniform(140, 382)
    # dentro do pote externo?
    def inside_outer(x, y):
        if y > 367:
            return 100 < x < 320 and y < 367 + 22 * (1 - ((x - 210) / 110) ** 2)
        xl = 74 + (y - 130) * 26 / 237; xr = 346 - (y - 130) * 26 / 237
        return xl + 2 < x < xr - 2
    def inside_inner(x, y):
        if y > 322:
            return 138 < x < 282 and y < 322 + 14 * (1 - ((x - 210) / 72) ** 2) + 4
        xl = 118 + (y - 140) * 20 / 182; xr = 302 - (y - 140) * 20 / 182
        return xl - 3 < x < xr + 3 and y > 136
    if inside_outer(x, y) and not inside_inner(x, y):
        pts.append((x, y))
for i, (x, y) in enumerate(pts):
    if i % 4 == 0:
        b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.2" fill="{WATER}" opacity="0.75"/>')
    else:
        b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.2" fill="#8a6d45"/>')
# pote de dentro
b.append(f'<path d="M118,140 L138,322 Q210,338 282,322 L302,140 Z" fill="{CLAY}" stroke="{OUT}" stroke-width="2.5"/>')
b.append('<path d="M129,140 L148,312 Q210,327 272,312 L291,140 Z" fill="#fff7ec" stroke="#7a4a22" stroke-width="1.2"/>')
# comida
b.append('<path d="M150,300 L262,300" stroke="#ccc" stroke-width="1"/>')
for (cx, cy, r) in [(170, 296, 15), (204, 300, 15), (238, 296, 15), (186, 270, 14), (222, 270, 14)]:
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#e03131" stroke="#8a1c1c" stroke-width="1.5"/>'
             f'<path d="M{cx-4},{cy-r+1} l4,-5 l4,5" fill="#2b8a3e" stroke="#2b8a3e" stroke-width="2"/>')
b.append('<polygon points="160,248 250,232 252,244 162,256" fill="#f08c00" stroke="#a65c00" stroke-width="1.5"/>')
for (cx, cy) in [(185, 215), (215, 208), (245, 214)]:
    b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="20" ry="11" fill="#69b34c" stroke="#2b6a1e" stroke-width="1.5"/>')
# pano molhado
b.append('<path d="M46,132 Q60,112 92,116 Q210,100 328,116 Q360,112 374,132 L374,142 Q210,130 46,142 Z" fill="#9cb8cf" stroke="#3f6d9e" stroke-width="2"/>')
for x in (52, 368):
    b.append(f'<line x1="{x}" y1="142" x2="{x}" y2="168" stroke="{WATER}" stroke-width="2" stroke-dasharray="4 4"/>')
# evaporacao
def wavy_arrow(x1, y1, dx, dy):
    mx, my = x1 + dx / 2, y1 + dy / 2
    nx, ny = -dy * 0.25, dx * 0.25
    x2, y2 = x1 + dx, y1 + dy
    s = f'<path d="M{x1},{y1} Q{mx+nx:.1f},{my+ny:.1f} {x2},{y2}" fill="none" stroke="{WATER}" stroke-width="2.5"/>'
    a = math.atan2(dy, dx); L = 9
    p1 = (x2 + L * math.cos(a + 2.6), y2 + L * math.sin(a + 2.6)); p2 = (x2 + L * math.cos(a - 2.6), y2 + L * math.sin(a - 2.6))
    s += f'<polygon points="{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{WATER}"/>'
    return s
for y in (200, 260, 320):
    xl = 60 + (y - 130) * 28 / 250
    b.append(wavy_arrow(xl - 4, y, -38, -16))
b.append(lines(6, 352, ["a água", "evapora"], 12, "#1d5d9b", True))
# rotulos
b.append(lines(415, 112, ["pano MOLHADO por cima", "(funciona como tampa)"], 12, "#222", [0]))
b.append(lead(412, 118, 372, 124))
b.append(lines(415, 192, ["pote de DENTRO:", "aqui vai a comida"], 12, "#222", [0]))
b.append(lead(412, 198, 297, 206))
b.append(lines(415, 250, ["AREIA MOLHADA", "4 a 8 cm em volta e no fundo", "(molhe 1 a 2 vezes por dia)"], 12, "#1d5d9b", [0]))
b.append(lead(412, 256, 312, 258))
b.append(lines(415, 322, ["pote de FORA: barro SEM", "verniz ou esmalte (tem", "que \"suar\")"], 12, "#222", [0]))
b.append(lead(412, 328, 336, 300))
b.append(box(20, 422, 640, 98, "#eef5ff", "#3f6d9e"))
b.append(lines(34, 442, ["Como funciona: a água atravessa o barro e evapora, levando o calor (como o suor e a moringa).",
                         "Clima SECO e com vento (sertão, cerrado na seca): fica de 6 a 12 °C mais frio que o ar.",
                         "Clima úmido (litoral, Amazônia, dias de chuva): esfria pouco, só 1 a 3 °C.",
                         "Bom para verduras, frutas e tomate (duram 2 a 4 vezes mais). NÃO fica frio o bastante",
                         "para guardar carne, peixe ou leite por vários dias."], 12.5, "#222", False, 17))
save("geladeira-de-barro.svg", 680, 530, "Geladeira de barro pote-em-pote — corte", b)


# =====================================================================
# 3. DEFUMADOR SIMPLES
# =====================================================================
b = []
b.append(f'<polygon points="0,330 180,330 420,250 680,250 680,422 0,422" fill="{SOIL}"/>')
b.append('<polyline points="0,330 180,330 420,250 680,250" fill="none" stroke="#6b4f2a" stroke-width="2.5"/>')
# fornalha
b.append('<rect x="50" y="330" width="120" height="62" fill="#3b2f2a" stroke="#8a8a8a" stroke-width="7"/>')
b.append(f'<rect x="72" y="374" width="80" height="9" rx="4" fill="{WOOD}" stroke="{OUT}" stroke-width="1"/>')
b.append(f'<rect x="80" y="366" width="70" height="9" rx="4" fill="{WOOD}" stroke="{OUT}" stroke-width="1" transform="rotate(-8 115 370)"/>')
for (x, h) in [(86, 22), (104, 30), (122, 24), (138, 18)]:
    b.append(f'<path d="M{x-9},372 Q{x-6},{372-h*0.6} {x},{372-h} Q{x+6},{372-h*0.6} {x+9},372 Z" fill="#f08c00" stroke="#d9480f" stroke-width="1"/>')
    b.append(f'<path d="M{x-4},372 Q{x-2},{372-h*0.4} {x},{372-h*0.6} Q{x+2},{372-h*0.4} {x+4},372 Z" fill="#ffd43b"/>')
b.append('<rect x="66" y="321" width="112" height="9" fill="#555" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(arrow(26, 304, 56, 326, WATER, 3))
b.append(text(10, 298, "entra ar", 11.5, "#1d5d9b", True))
# duto
b.append('<path d="M170,350 L462,276.5 L462,250 L480,250 L480,290 L170,368 Z" fill="#cfcfcf" stroke="#555" stroke-width="2"/>')
# camara
b.append('<rect x="420" y="110" width="110" height="140" fill="#f6f1ea" stroke="#6b6b6b" stroke-width="6"/>')
b.append('<rect x="463" y="244" width="16" height="10" fill="#cfcfcf"/>')
for (x, w) in [(404, 18), (530, 18)]:
    b.append(f'<rect x="{x}" y="240" width="{w}" height="10" rx="3" fill="#9a9a9a" stroke="#555" stroke-width="1"/>')
b.append('<rect x="410" y="100" width="58" height="10" fill="#555" stroke="#1e1e1e" stroke-width="1"/>')
b.append('<rect x="482" y="100" width="58" height="10" fill="#555" stroke="#1e1e1e" stroke-width="1"/>')
# varas e pecas
b.append(f'<line x1="426" y1="140" x2="524" y2="140" stroke="{WOOD}" stroke-width="5"/>')
b.append(f'<line x1="426" y1="192" x2="524" y2="192" stroke="{WOOD}" stroke-width="5"/>')
for x in (442, 470, 498):
    b.append(f'<line x1="{x+6}" y1="140" x2="{x+6}" y2="146" stroke="#333" stroke-width="1.5"/>')
    b.append(f'<rect x="{x}" y="146" width="12" height="32" rx="4" fill="#a33b2a" stroke="#5c1d14" stroke-width="1.5"/>')
for x in (452, 494):
    b.append(f'<line x1="{x}" y1="192" x2="{x}" y2="198" stroke="#333" stroke-width="1.5"/>')
    b.append(f'<ellipse cx="{x}" cy="216" rx="8" ry="18" fill="#c9a66b" stroke="#6b4f2a" stroke-width="1.5"/>')
    b.append(f'<polygon points="{x},232 {x-7},242 {x+7},242" fill="#c9a66b" stroke="#6b4f2a" stroke-width="1.5"/>')
# fumaca
SM = "#6d6d6d"
b.append(arrow(200, 352, 300, 327, SM, 3))
b.append(arrow(320, 322, 440, 292, SM, 3))
b.append(arrow(471, 284, 471, 236, SM, 3))
b.append(arrow(431, 236, 431, 122, SM, 2.5))
b.append(arrow(519, 236, 519, 122, SM, 2.5))
b.append(arrow(475, 112, 475, 66, SM, 3))
# rotulos
b.append(lines(14, 200, ["1. FOGO", "brasa + lascas ou", "serragem (pouca chama,", "muita fumaça); a tampa", "de chapa regula o ar"], 12, "#222", [0]))
b.append(lead(96, 268, 106, 352))
b.append(lines(196, 150, ["2. DUTO enterrado: 2 a 4 m,", "sempre SUBINDO (manilha,", "cano ou telhas cobertas", "de terra)"], 12, "#222", [0]))
b.append(lead(300, 206, 316, 322))
b.append(lines(545, 66, ["tampa com fresta:", "fumaça sai devagar"], 12, "#222", [0]))
b.append(lead(542, 80, 528, 102))
b.append(lines(545, 130, ["3. CÂMARA", "tambor de 200 L", "sem fundo, ou", "caixa de madeira", "ou de tijolo"], 12, "#222", [0]))
b.append(lead(542, 146, 532, 156))
b.append(lines(545, 214, ["varas ou grelhas;", "peças sem encostar", "uma na outra"], 12))
b.append(lead(542, 218, 526, 194))
b.append(box(20, 432, 640, 84, "#fff4e5", "#ef8a2b"))
b.append(lines(34, 452, ["FRIA (abaixo de 30 °C): duto longo, fogo fraco; dias a semanas. NÃO cozinha: só para",
                         "carne já bem salgada. QUENTE (câmara a 70–100 °C): duto curto ou fogo quase embaixo;",
                         "3 a 12 h; a carne cozinha (miolo acima de 70 °C). Lenha: goiabeira, laranjeira, ingá,",
                         "jabuticabeira, sabugo de milho. NUNCA: pinus, madeira pintada, tratada ou compensado."], 12.5, "#222", False, 17))
save("defumador.svg", 680, 526, "Defumador simples — corte lateral", b)


# =====================================================================
# 4. FARINHA DE MANDIOCA (FLUXOGRAMA)
# =====================================================================
b = []
PW, PH = 200, 228
P = [(12, 52), (240, 52), (468, 52), (12, 300), (240, 300), (468, 300)]
T = ["Descascar e lavar", "Ralar", "Prensar", "Peneirar", "Torrar", "Esfriar e guardar"]
TX = [["Processe no mesmo dia em", "que arrancar (a raiz estraga", "em 1–2 dias). Raspe toda a", "casca e lave bem."],
      ["Ralo de lata furada com", "prego ou rodete (caititu).", "Massa bem fina solta mais", "veneno na prensa."],
      ["Prensa ou tipiti de 6 a 12 h,", "até a massa ficar enxuta.", "O caldo (manipueira) é", "VENENO: jogue na fossa."],
      ["Desmanche os torrões e", "passe na peneira (3–4 mm).", "A fibra que sobra (crueira)", "só seca, para animais."],
      ["Tacho ou forno largo, fogo", "forte e depois médio,", "MEXENDO sem parar, 40 min", "a 2 h, até ficar sequinha."],
      ["Esfrie espalhada, peneire", "de novo e guarde em lata ou", "saco bem fechado e seco.", "Rende 1 kg para 3–4 kg."]]
for i, (x, y) in enumerate(P):
    b.append(panel(x, y, PW, PH, i + 1, T[i]))
    col = ["#222"] * 4
    for j, s in enumerate(TX[i]):
        c = DRED if (i == 2 and j >= 2) else "#222"
        bb = (i == 2 and j == 3)
        b.append(text(x + 10, y + 162 + j * 15, s, 12, c, bb))
# setas
b.append(arrow(214, 150, 237, 150, "#555", 4))
b.append(arrow(442, 150, 465, 150, "#555", 4))
b.append(arrow(214, 398, 237, 398, "#555", 4))
b.append(arrow(442, 398, 465, 398, "#555", 4))
b.append('<polyline points="568,281 568,290 112,290" fill="none" stroke="#555" stroke-width="4"/>')
b.append(arrow(112, 288, 112, 300, "#555", 4))


def raiz(x0, cy, L, H, fill, stroke="#4a2c14"):
    return (f'<path d="M{x0},{cy-H/2} L{x0+L*0.6},{cy-H*0.38} Q{x0+L},{cy-H*0.12} {x0+L+10},{cy} '
            f'Q{x0+L},{cy+H*0.12} {x0+L*0.6},{cy+H*0.38} L{x0},{cy+H/2} Q{x0-7},{cy} {x0},{cy-H/2} Z" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
# 1 descascar
x, y = P[0]
b.append(raiz(x + 28, y + 70, 120, 30, "#7b4a26"))
for k in range(4):
    xx = x + 48 + k * 26
    b.append(f'<path d="M{xx},{y+57} q3,13 0,26" fill="none" stroke="#4a2c14" stroke-width="1.2"/>')
b.append(raiz(x + 28, y + 118, 120, 28, "#fdf8ec"))
b.append(arrow(x + 16, y + 86, x + 16, y + 106, GREEN, 3))
b.append(f'<path d="M{x+168},{y+96} q10,-8 18,0 q-8,8 -18,0" fill="#7b4a26"/>')
b.append(f'<polygon points="{x+150},{y+130} {x+186},{y+100} {x+190},{y+104} {x+158},{y+134}" fill="#c9ced3" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<rect x="{x+138}" y="{y+130}" width="22" height="8" rx="3" fill="{WOOD}" stroke="{OUT}" stroke-width="1.2" transform="rotate(-40 {x+149} {y+134})"/>')
b.append(text(x + 60, y + 50, "com casca", 10.5, "#555"))
b.append(text(x + 60, y + 147, "sem casca", 10.5, "#555"))
# 2 ralar
x, y = P[1]; cx = x + 100
b.append(f'<rect x="{cx-62}" y="{y+42}" width="70" height="72" fill="{WOOD}" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<rect x="{cx-55}" y="{y+48}" width="56" height="60" fill="#c9ced3" stroke="#555" stroke-width="1.5"/>')
for r in range(8):
    for c in range(7):
        b.append(f'<circle cx="{cx-50+c*8}" cy="{y+53+r*7.2:.1f}" r="1.3" fill="#555"/>')
b.append(f'<ellipse cx="{cx-14}" cy="{y+74}" rx="40" ry="11" fill="#fdf8ec" stroke="#4a2c14" stroke-width="2" transform="rotate(-35 {cx-14} {y+74})"/>')
b.append(f'<line x1="{cx+30}" y1="{y+52}" x2="{cx+30}" y2="{y+98}" stroke="{GREEN}" stroke-width="3"/>')
b.append(f'<polygon points="{cx+30},{y+46} {cx+24},{y+56} {cx+36},{y+56}" fill="{GREEN}"/>')
b.append(f'<polygon points="{cx+30},{y+104} {cx+24},{y+94} {cx+36},{y+94}" fill="{GREEN}"/>')
b.append(text(cx + 42, y + 80, "esfregue", 10.5, "#555"))
for k in range(7):
    b.append(f'<circle cx="{cx-50+k*8}" cy="{y+117+(k%2)*3}" r="2" fill="#fdf8ec" stroke="#999" stroke-width="0.8"/>')
b.append(f'<polygon points="{cx-78},{y+122} {cx+22},{y+122} {cx+12},{y+140} {cx-68},{y+140}" fill="{WOOD}" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<path d="M{cx-74},{y+124} Q{cx-28},{y+112} {cx+18},{y+124} Z" fill="#fdf8ec" stroke="#999" stroke-width="1"/>')
# 3 prensar
x, y = P[2]; cx = x + 100
b.append(f'<rect x="{cx-88}" y="{y+44}" width="10" height="96" fill="{WOOD}" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<line x1="{cx-84}" y1="{y+56}" x2="{cx+82}" y2="{y+70}" stroke="{WOOD}" stroke-width="9" stroke-linecap="round"/>')
b.append(f'<line x1="{cx-84}" y1="{y+56}" x2="{cx+82}" y2="{y+70}" stroke="{OUT}" stroke-width="1" opacity="0.4"/>')
b.append(f'<line x1="{cx+74}" y1="{y+72}" x2="{cx+74}" y2="{y+92}" stroke="#555" stroke-width="2"/>')
b.append(f'<ellipse cx="{cx+74}" cy="{y+104}" rx="17" ry="13" fill="#9a9a9a" stroke="{OUT}" stroke-width="1.5"/>')
b.append(text(cx + 74, y + 108, "peso", 10, "#fff", True, "middle"))
b.append(f'<rect x="{cx-38}" y="{y+66}" width="44" height="10" fill="{WOOD}" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<rect x="{cx-42}" y="{y+76}" width="52" height="34" fill="#efe4c8" stroke="{OUT}" stroke-width="1.5"/>')
for k in range(6):
    b.append(f'<line x1="{cx-42+k*9}" y1="{y+76}" x2="{cx-33+k*9}" y2="{y+110}" stroke="#b39a62" stroke-width="1"/>')
b.append(f'<rect x="{cx-48}" y="{y+110}" width="64" height="5" fill="{WOOD}"/>')
for k, yy in enumerate((y + 119, y + 125)):
    for xx in (cx - 30, cx - 16, cx - 2):
        b.append(f'<path d="M{xx},{yy} q3,4 0,6 q-3,-2 0,-6" fill="#e0c52a"/>')
b.append(f'<polygon points="{cx-50},{y+128} {cx+22},{y+128} {cx+16},{y+140} {cx-44},{y+140}" fill="#f3e27a" stroke="{OUT}" stroke-width="1.5"/>')
b.append(text(cx + 30, y + 140, "VENENO", 11.5, DRED, True))
# 4 peneirar
x, y = P[3]; cx = x + 100
b.append('<defs><pattern id="tela" width="7" height="7" patternUnits="userSpaceOnUse">'
         '<rect width="7" height="7" fill="#efe1bd"/><path d="M0,0 L7,7 M7,0 L0,7" stroke="#a88a4e" stroke-width="0.9"/></pattern></defs>')
b.append(f'<ellipse cx="{cx}" cy="{y+70}" rx="72" ry="19" fill="url(#tela)" stroke="{WOOD}" stroke-width="5"/>')
for (dx, dy) in [(-30, -4), (-12, 3), (8, -6), (24, 4), (40, -2), (-44, 2)]:
    b.append(f'<circle cx="{cx+dx}" cy="{y+70+dy}" r="3.2" fill="#fdf8ec" stroke="#999" stroke-width="0.8"/>')
for (dx, dy) in [(-20, -8), (14, 6), (34, -8)]:
    b.append(f'<line x1="{cx+dx}" y1="{y+70+dy}" x2="{cx+dx+12}" y2="{y+70+dy+3}" stroke="#6b4f2a" stroke-width="2.5" stroke-linecap="round"/>')
for k in range(9):
    b.append(f'<circle cx="{cx-40+k*10}" cy="{y+96+(k%3)*7}" r="1.8" fill="#bfa76a"/>')
b.append(f'<path d="M{cx-60},{y+120} L{cx+60},{y+120} L{cx+48},{y+140} L{cx-48},{y+140} Z" fill="#c9a26b" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<path d="M{cx-56},{y+122} Q{cx},{y+106} {cx+56},{y+122} Z" fill="#fdf8ec" stroke="#999" stroke-width="1"/>')
b.append(text(cx + 64, y + 52, "fibra", 10.5, "#555", False, "middle"))
# 5 torrar
x, y = P[4]; cx = x + 100
b.append(f'<rect x="{cx-86}" y="{y+92}" width="172" height="48" fill="#b5523b" stroke="{OUT}" stroke-width="2"/>')
for yy in (y + 104, y + 116, y + 128):
    b.append(f'<line x1="{cx-86}" y1="{yy}" x2="{cx+86}" y2="{yy}" stroke="#7a3322" stroke-width="1"/>')
b.append(f'<path d="M{cx-26},{y+140} L{cx-26},{y+118} Q{cx},{y+100} {cx+26},{y+118} L{cx+26},{y+140} Z" fill="#2b2b2b"/>')
for (dx, h) in [(-12, 14), (0, 20), (12, 13)]:
    b.append(f'<path d="M{cx+dx-7},{y+139} Q{cx+dx},{y+139-h*1.4} {cx+dx+7},{y+139} Z" fill="#f08c00"/>')
b.append(f'<path d="M{cx-92},{y+78} L{cx+92},{y+78} L{cx+82},{y+92} L{cx-82},{y+92} Z" fill="#555" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<path d="M{cx-80},{y+79} Q{cx},{y+62} {cx+80},{y+79} Z" fill="#f1e3b5" stroke="#b89a55" stroke-width="1"/>')
b.append(f'<line x1="{cx+18}" y1="{y+72}" x2="{cx+72}" y2="{y+36}" stroke="{WOOD}" stroke-width="5" stroke-linecap="round"/>')
b.append(f'<rect x="{cx+6}" y="{y+68}" width="26" height="8" fill="{WOOD}" stroke="{OUT}" stroke-width="1" transform="rotate(-34 {cx+19} {y+72})"/>')
for dx in (-50, -26, -2):
    b.append(f'<path d="M{cx+dx},{y+60} q-5,-6 0,-12 q5,-6 0,-12" fill="none" stroke="#999" stroke-width="2"/>')
b.append(arrow(cx - 60, y + 118, cx - 36, y + 118, "#555", 2))
b.append(text(cx - 82, y + 114, "fogo", 10.5, "#fff", True))
# 6 guardar
x, y = P[5]; cx = x + 100
b.append(f'<path d="M{cx-80},{y+138} Q{cx-92},{y+84} {cx-62},{y+58} L{cx-22},{y+58} Q{cx+6},{y+84} {cx-6},{y+138} Z" fill="#e8dcc0" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<rect x="{cx-58}" y="{y+50}" width="32" height="10" rx="3" fill="#b38b4d" stroke="{OUT}" stroke-width="1.5"/>')
b.append(text(cx - 43, y + 106, "farinha", 12, "#6b4f2a", True, "middle"))
b.append(f'<rect x="{cx+16}" y="{y+70}" width="64" height="68" rx="4" fill="#c0c6cc" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<rect x="{cx+12}" y="{y+62}" width="72" height="10" rx="3" fill="#8f979e" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<rect x="{cx+22}" y="{y+88}" width="52" height="32" fill="#fff" stroke="#555" stroke-width="1"/>')
b.append(text(cx + 48, y + 101, "FARINHA", 9.5, "#222", True, "middle"))
b.append(text(cx + 48, y + 115, "06/2026", 9.5, "#222", False, "middle"))
b.append(box(12, 540, 656, 46, "#fde8e8", "#d62828"))
b.append(lines(24, 559, ["Mandioca BRAVA (amarga) só fica segura depois de ralar, prensar e torrar bem. Nunca coma a",
                         "massa crua nem beba a manipueira. Mandioca mansa (aipim, macaxeira) pode ser só cozida."], 12.5, "#222", False, 17))
save("farinha-de-mandioca.svg", 680, 596, "Farinha de mandioca — do pé ao saco", b)


# =====================================================================
# 5. GRAOS EM GARRAFA PET
# =====================================================================
b = []
b.append('<defs><pattern id="grao" width="8" height="6" patternUnits="userSpaceOnUse">'
         '<rect width="8" height="6" fill="#f3e6bf"/><ellipse cx="4" cy="3" rx="3" ry="1.7" fill="#e6d29a" stroke="#b39a55" stroke-width="0.6"/></pattern></defs>')
_clip = [0]


def pet(tx, ty, h=96, w=46, level=0.0, cap=True, rot=0, label=None):
    """garrafa PET 2 L; (tx,ty) = centro do fundo; rot em graus; level = fração da altura cheia de grãos"""
    _clip[0] += 1; cid = f"pet{_clip[0]}"
    hw = w / 2
    path = (f"M{-hw+6},0 Q{-hw},0 {-hw},-6 L{-hw},{-0.62*h:.1f} Q{-hw},{-0.80*h:.1f} {-0.18*w:.1f},{-0.84*h:.1f} "
            f"L{-0.18*w:.1f},{-0.92*h:.1f} L{0.18*w:.1f},{-0.92*h:.1f} L{0.18*w:.1f},{-0.84*h:.1f} "
            f"Q{hw},{-0.80*h:.1f} {hw},{-0.62*h:.1f} L{hw},-6 Q{hw},0 {hw-6},0 Z")
    s = f'<g transform="translate({tx},{ty}) rotate({rot})">'
    s += f'<defs><clipPath id="{cid}"><path d="{path}"/></clipPath></defs>'
    s += f'<path d="{path}" fill="#eef7ff"/>'
    if level > 0:
        s += f'<rect x="{-hw}" y="{-level*h:.1f}" width="{w}" height="{level*h:.1f}" fill="url(#grao)" clip-path="url(#{cid})"/>'
    for yy in (0.22, 0.42):
        s += f'<line x1="{-hw+3}" y1="{-yy*h:.1f}" x2="{hw-3}" y2="{-yy*h:.1f}" stroke="#a9c7e3" stroke-width="1.2"/>'
    s += f'<path d="{path}" fill="none" stroke="{OUT}" stroke-width="2"/>'
    if cap:
        s += f'<rect x="{-0.22*w:.1f}" y="{-h:.1f}" width="{0.44*w:.1f}" height="{0.09*h:.1f}" rx="2" fill="#2f6fb0" stroke="{OUT}" stroke-width="1.5"/>'
    if label:
        s += f'<rect x="{-hw+4}" y="{-0.50*h:.1f}" width="{w-8}" height="{0.30*h:.1f}" fill="#fff" stroke="#555" stroke-width="1"/>'
        s += text(0, -0.50 * h + 0.13 * h, label[0], 10, "#222", True, "middle")
        s += text(0, -0.50 * h + 0.25 * h, label[1], 9.5, "#222", False, "middle")
    return s + "</g>"


T = ["Limpar e secar", "Grão seco", "Encher batendo", "Tirar o oxigênio", "Etiquetar", "Guardar bem"]
TX = [["Só garrafa de água ou", "refrigerante (PET). Lave,", "enxágue e seque 2–3 dias", "de boca para baixo."],
      ["Grão seco estala ao morder", "(não amassa). Para matar", "ovos de caruncho: freezer", "por 3 a 7 dias (opcional)."],
      ["Use funil. Bata a garrafa", "no chão várias vezes para", "assentar e encha até 2 cm", "da boca."],
      ["1 absorvedor de O₂ (300 cc)", "por garrafa de 2 L; feche", "NA HORA, bem firme. Sem", "absorvedor: 2 folhas de", "louro (afasta, não mata)."],
      ["Escreva o que é e a data", "(mês/ano) com caneta", "permanente ou fita crepe.", "Gaste primeiro a mais velha."],
      ["Escuro, fresco, fora do", "chão (estrado) e dentro de", "tambor ou caixa fechada:", "rato rói garrafa PET."]]
for i, (x, y) in enumerate(P):
    b.append(panel(x, y, PW, PH, i + 1, T[i]))
    for j, s in enumerate(TX[i]):
        b.append(text(x + 10, y + 160 + j * 15, s, 12, "#222"))
b.append(arrow(214, 150, 237, 150, "#555", 4))
b.append(arrow(442, 150, 465, 150, "#555", 4))
b.append(arrow(214, 398, 237, 398, "#555", 4))
b.append(arrow(442, 398, 465, 398, "#555", 4))
b.append('<polyline points="568,281 568,290 112,290" fill="none" stroke="#555" stroke-width="4"/>')
b.append(arrow(112, 288, 112, 300, "#555", 4))
# 1
x, y = P[0]; cx = x + 100
b.append(f'<line x1="{cx-70}" y1="{y+50}" x2="{cx+20}" y2="{y+50}" stroke="{WOOD}" stroke-width="5"/>')
b.append(pet(cx - 28, y + 46, 82, 40, cap=False, rot=180))
for k in range(3):
    b.append(f'<path d="M{cx-28},{y+134+k*0} q-3,5 0,7 q3,-2 0,-7" fill="{WATER}" transform="translate(0,{k*0})"/>')
b.append(f'<path d="M{cx-28},{y+132} q-4,6 0,9 q4,-3 0,-9" fill="{WATER}"/>')
# frasco de limpeza riscado
b.append(f'<path d="M{cx+38},{y+138} L{cx+38},{y+82} Q{cx+40},{y+72} {cx+52},{y+70} L{cx+56},{y+58} L{cx+70},{y+58} L{cx+72},{y+70} Q{cx+86},{y+74} {cx+86},{y+86} L{cx+86},{y+138} Z" fill="#fff" stroke="{OUT}" stroke-width="2"/>')
b.append(text(cx + 62, y + 108, "limpeza", 9.5, "#555", False, "middle"))
b.append(f'<line x1="{cx+30}" y1="{y+60}" x2="{cx+94}" y2="{y+138}" stroke="{RED}" stroke-width="4"/>')
b.append(f'<line x1="{cx+94}" y1="{y+60}" x2="{cx+30}" y2="{y+138}" stroke="{RED}" stroke-width="4"/>')
# 2
x, y = P[1]; cx = x + 100
b.append(f'<rect x="{cx-88}" y="{y+48}" width="80" height="90" rx="6" fill="#f4f8fb" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<line x1="{cx-88}" y1="{y+74}" x2="{cx-8}" y2="{y+74}" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<rect x="{cx-18}" y="{y+82}" width="5" height="22" rx="2" fill="#888"/>')
for k in range(3):
    a = k * math.pi / 3
    b.append(f'<line x1="{cx-48-14*math.cos(a):.1f}" y1="{y+62-11*math.sin(a):.1f}" x2="{cx-48+14*math.cos(a):.1f}" y2="{y+62+11*math.sin(a):.1f}" stroke="{WATER}" stroke-width="2.5"/>')
b.append(text(cx - 52, y + 106, "−18 °C", 13, "#1d5d9b", True, "middle"))
b.append(text(cx - 52, y + 124, "3 a 7 dias", 11, "#222", False, "middle"))
b.append(f'<path d="M{cx+18},{y+62} q16,-12 32,0 l-4,4 l4,4 q-16,12 -32,0 Z" fill="#f3e6bf" stroke="#8a6d2e" stroke-width="1.5"/>')
b.append(f'<path d="M{cx+56},{y+62} l4,-4 q16,0 22,8 q-6,8 -22,8 Z" fill="#f3e6bf" stroke="#8a6d2e" stroke-width="1.5"/>')
b.append(text(cx + 50, y + 92, "estala: seco", 11, GREEN, True, "middle"))
b.append(f'<ellipse cx="{cx+50}" cy="{y+112}" rx="26" ry="6" fill="#f3e6bf" stroke="#8a6d2e" stroke-width="1.5"/>')
b.append(text(cx + 50, y + 134, "amassa: úmido", 11, DRED, True, "middle"))
# 3
x, y = P[2]; cx = x + 100
b.append(pet(cx - 20, y + 138, 82, 42, level=0.88, cap=False))
b.append(f'<polygon points="{cx-46},{y+42} {cx+6},{y+42} {cx-14},{y+62} {cx-14},{y+70} {cx-26},{y+70} {cx-26},{y+62}" fill="#d0d4d8" stroke="{OUT}" stroke-width="1.8"/>')
for k in range(6):
    b.append(f'<ellipse cx="{cx-34+k*6}" cy="{y+40-(k%2)*5}" rx="2.6" ry="1.6" fill="#e6d29a" stroke="#8a6d2e" stroke-width="0.6"/>')
for sgn in (-1, 1):
    b.append(f'<path d="M{cx-20+sgn*30},{y+128} q{sgn*8},4 {sgn*4},12" fill="none" stroke="#555" stroke-width="2"/>')
    b.append(f'<path d="M{cx-20+sgn*38},{y+124} q{sgn*10},6 {sgn*5},16" fill="none" stroke="#555" stroke-width="2"/>')
b.append(text(cx + 44, y + 120, "bata no", 11, "#555"))
b.append(text(cx + 44, y + 133, "chão", 11, "#555"))
# 4
x, y = P[3]; cx = x + 100
b.append(pet(cx - 30, y + 138, 82, 42, level=0.86, cap=False))
b.append(f'<rect x="{cx-44}" y="{y+40}" width="28" height="18" rx="2" fill="#fff" stroke="{OUT}" stroke-width="1.5"/>')
b.append(text(cx - 30, y + 53, "O₂", 11, "#222", True, "middle"))
b.append(arrow(cx - 30, y + 59, cx - 30, y + 72, GREEN, 3))
b.append(f'<rect x="{cx+30}" y="{y+50}" width="20" height="9" rx="2" fill="#2f6fb0" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<path d="M{cx+28},{y+66} Q{cx+12},{y+80} {cx-10},{y+66}" fill="none" stroke="{GREEN}" stroke-width="2.5"/>')
b.append(f'<polygon points="{cx-12},{y+60} {cx-14},{y+72} {cx-3},{y+68}" fill="{GREEN}"/>')
b.append(text(cx + 6, y + 100, "feche", 11.5, "#222", True))
b.append(text(cx + 6, y + 114, "em 1 minuto", 11.5, "#222", True))
# 5
x, y = P[4]; cx = x + 100
b.append(pet(cx, y + 138, 96, 58, level=0.88, cap=True, label=("ARROZ", "11/2026")))
# 6
x, y = P[5]; cx = x + 100
b.append(f'<rect x="{cx-72}" y="{y+54}" width="144" height="72" fill="#dfe3e6" stroke="{OUT}" stroke-width="2.5"/>')
b.append(f'<rect x="{cx-78}" y="{y+46}" width="156" height="9" rx="2" fill="#8f979e" stroke="{OUT}" stroke-width="1.5"/>')
for (bx, by) in [(cx - 4, y + 72), (cx + 66, y + 72), (cx - 4, y + 104), (cx + 66, y + 104)]:
    b.append(pet(bx, by, 62, 28, level=0.86, cap=True, rot=-90))
for k in range(4):
    b.append(f'<rect x="{cx-78+k*42}" y="{y+128}" width="30" height="10" fill="{WOOD}" stroke="{OUT}" stroke-width="1.2"/>')
b.append(box(12, 540, 656, 62, "#eef5ff", "#3f6d9e"))
b.append(lines(24, 559, ["Assim, arroz branco, milho e trigo em grão duram 5 a 10 anos ou mais; feijão também (endurece).",
                         "Só para alimento SECO (até ~10% de umidade). Úmido + sem oxigênio = risco de botulismo.",
                         "Açúcar e sal: sem absorvedor (o açúcar vira pedra). Não reaproveite o absorvedor usado."], 12, "#222", False, 16))
save("graos-em-garrafa-pet.svg", 680, 612, "Como guardar grãos em garrafa PET", b)


# =====================================================================
# 6. TAIOBA x PARECIDAS
# =====================================================================
b = []
GL = "#8cc36b"; GD = "#2b6a1e"


def folha(cx, cy, s=1.0, fill=GL):
    """folha sagitada pendurada (ponta para baixo). (cx,cy) = ponto do V entre os lobos"""
    def p(x, y):
        return f"{cx + x*s:.1f},{cy + y*s:.1f}"
    d = (f"M{p(0,0)} Q{p(-30,-8)} {p(-64,-30)} Q{p(-104,30)} {p(-44,96)} Q{p(-16,126)} {p(0,152)} "
         f"Q{p(16,126)} {p(44,96)} Q{p(104,30)} {p(64,-30)} Q{p(30,-8)} {p(0,0)} Z")
    s_ = f'<path d="{d}" fill="{fill}" stroke="{GD}" stroke-width="2.2"/>'
    s_ += f'<path d="M{p(0,0)} L{p(0,146)}" stroke="{GD}" stroke-width="2"/>'
    for (x1, y1, x2, y2) in [(0, 30, -50, 20), (0, 60, -56, 64), (0, 92, -34, 108), (0, 30, 50, 20), (0, 60, 56, 64), (0, 92, 34, 108),
                             (0, 6, -52, -16), (0, 6, 52, -16)]:
        s_ += f'<path d="M{p(x1,y1)} Q{p((x1+x2)/2, y1+4)} {p(x2,y2)}" fill="none" stroke="{GD}" stroke-width="1.1" opacity="0.8"/>'
    return s_


cols = [(120, "TAIOBA", "comestível SÓ COZIDA", GREEN), (340, "INHAME / TAIOBA-BRAVA", "folha queima a boca", "#c26a00"),
        (560, "COMIGO-NINGUÉM-PODE", "VENENOSA", DRED)]
for (cx, t1, t2, c) in cols:
    b.append(f'<rect x="{cx-104}" y="48" width="208" height="380" rx="10" fill="#fafafa" stroke="{c}" stroke-width="2"/>')
    b.append(text(cx, 72, t1, 13.5, c, True, "middle"))
    b.append(text(cx, 90, t2, 12.5, c, True, "middle"))
# taioba
cx = 120
b.append(f'<path d="M{cx},104 Q{cx+6},140 {cx},176" fill="none" stroke="#5d9c3b" stroke-width="9" stroke-linecap="round"/>')
b.append(folha(cx, 178, 0.82))
b.append(f'<circle cx="{cx}" cy="178" r="9" fill="none" stroke="{RED}" stroke-width="2.5"/>')
b.append(lines(cx - 96, 336, ["O cabo (talo) prende na", "BORDA da folha, bem no", "\"V\" entre as duas", "orelhas. Talo verde,", "sem mancha roxa."], 12, "#222", [1]))
# inhame (peltada)
cx = 340
b.append(folha(cx, 150, 0.82, "#79b45a"))
b.append(f'<path d="M{cx-4},150 Q{cx+2},140 {cx},150" fill="#79b45a"/>')
b.append(f'<path d="M{cx-10},150 Q{cx},160 {cx+10},150 L{cx+6},150 Q{cx},156 {cx-6},150 Z" fill="#79b45a" stroke="none"/>')
b.append(f'<path d="M{cx},104 Q{cx+8},150 {cx},196" fill="none" stroke="#7a3f7a" stroke-width="9" stroke-linecap="round"/>')
b.append(f'<circle cx="{cx}" cy="198" r="8" fill="#7a3f7a" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<circle cx="{cx}" cy="198" r="14" fill="none" stroke="{RED}" stroke-width="2.5"/>')
b.append(lines(cx - 96, 336, ["O cabo prende NO MEIO", "da folha (por dentro,", "longe da borda), muitas", "vezes com mancha roxa.", "Na dúvida, NÃO coma."], 12, "#222", [0, 4]))
# comigo-ninguem-pode
cx = 560
b.append(f'<rect x="{cx-9}" y="200" width="18" height="120" rx="6" fill="#7da35e" stroke="{GD}" stroke-width="2"/>')
for yy in (226, 252, 278, 304):
    b.append(f'<line x1="{cx-9}" y1="{yy}" x2="{cx+9}" y2="{yy}" stroke="{GD}" stroke-width="1.5"/>')
def folha_dief(cx, cy, ang):
    s_ = f'<g transform="translate({cx},{cy}) rotate({ang}) scale(0.7)">'
    s_ += f'<path d="M0,0 Q30,-26 90,-8 Q118,0 128,0 Q118,4 90,12 Q30,30 0,0 Z" fill="#3f8a2e" stroke="{GD}" stroke-width="2"/>'
    for (x, y, rx) in [(30, -4, 9), (52, 3, 8), (72, -3, 10), (96, 2, 6), (42, 6, 6)]:
        s_ += f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="4" fill="#f1f5e6"/>'
    s_ += f'<line x1="0" y1="0" x2="124" y2="1" stroke="{GD}" stroke-width="1.3"/>'
    return s_ + "</g>"
b.append(folha_dief(cx, 210, -60))
b.append(folha_dief(cx, 214, -125))
b.append(folha_dief(cx, 240, -10))
b.append(folha_dief(cx, 246, -170))
b.append(lines(cx - 96, 336, ["Folha comprida com", "manchas brancas; caule", "grosso tipo cana. Também", "venenosas: tinhorão,", "copo-de-leite, antúrio."], 12, "#222"))
b.append(box(20, 440, 640, 66, "#fde8e8", "#d62828"))
b.append(lines(34, 460, ["Toda folha desta família (aráceas) tem cristais que ferem boca e garganta. NUNCA coma taioba",
                         "crua. Tire o talo grosso, pique, ferva 5 min, escorra (jogue a água fora) e depois refogue.",
                         "Se coçar ou arder na boca, pare: não estava bem cozida ou não é taioba."], 12.5, "#222", False, 17))
save("taioba-e-parecidas.svg", 680, 516, "Taioba ou planta venenosa? Olhe onde o talo prende", b)

print("ok:", sorted(os.listdir(D)))
