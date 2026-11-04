import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
import math
# Figuras da seção 06-energia: fogo e fogões
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "06-energia", "img") + "/"
os.makedirs(D, exist_ok=True)
WOOD = "#8b5a2b"; WOOD2 = "#a8743f"; SOLO = "#e8d3b0"; DANGER = "#d62828"; DARK = "#b3001b"
VERDE = "#2b8a3e"; AGUA = "#4a90d9"; AGUA2 = "#cfe6fb"; CINZA = "#9a9a9a"; TIJ = "#c8553d"

def rect(x, y, w, h, fill, stroke=OUT, sw=2, rx=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'
def line(x1, y1, x2, y2, color=OUT, w=2, dash=None, cap="round"):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}" stroke-linecap="{cap}"{d}/>'
def poly(pts, fill, stroke=OUT, sw=2):
    p = " ".join(f"{x},{y}" for x, y in pts)
    return f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'
def path(d, fill="none", stroke=OUT, sw=2, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round" {extra}/>'
def flame(cx, cy, s=1.0):
    """chama com base em (cx, cy), altura ~ 70*s"""
    def P(dx, dy): return f"{cx+dx*s:.1f},{cy+dy*s:.1f}"
    o = (f'<path d="M{P(-26,0)} C{P(-34,-26)} {P(-14,-38)} {P(-12,-58)} C{P(-2,-44)} {P(4,-48)} {P(2,-72)} '
         f'C{P(18,-52)} {P(30,-40)} {P(26,0)} Z" fill="#f08c00" stroke="{OUT}" stroke-width="2"/>')
    i = (f'<path d="M{P(-13,0)} C{P(-18,-16)} {P(-6,-24)} {P(-4,-36)} C{P(2,-28)} {P(8,-30)} {P(8,-44)} '
         f'C{P(16,-28)} {P(18,-18)} {P(13,0)} Z" fill="#ffd43b"/>')
    return o + i
def stick(x1, y1, x2, y2, w, color=WOOD):
    return limb([(x1, y1), (x2, y2)], w, color)
def tlines(x, y, lines, size=12.5, color="#222", bold_first=False, lh=None, anchor="start"):
    lh = lh or size * 1.3
    out = []
    for k, s in enumerate(lines):
        out.append(text(x, y + k * lh, s, size, color, bold_first and k == 0, anchor))
    return "".join(out)
def rtext(x, y, s, ang, size=14, color="#222", bold=True):
    b = ' font-weight="bold"' if bold else ''
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}"{b} text-anchor="middle" transform="rotate({ang:.1f} {x} {y})">{s}</text>'

# =====================================================================
# 1. TRIANGULO DO FOGO + TAMANHOS DE MATERIAL
# =====================================================================
b = []
T, L, R = (170, 72), (48, 282), (292, 282)
for (a, c, col) in ((T, L, DANGER), (T, R, AGUA), (L, R, WOOD)):
    b.append(line(a[0], a[1], c[0], c[1], OUT, 18))
for (a, c, col) in ((T, L, DANGER), (T, R, AGUA), (L, R, WOOD)):
    b.append(line(a[0], a[1], c[0], c[1], col, 12))
b.append(flame(170, 250, 1.25))
def side_label(P1, P2, txt, dist, size, color, bold=True):
    ang = math.atan2(P2[1] - P1[1], P2[0] - P1[0])
    mx, my = (P1[0] + P2[0]) / 2, (P1[1] + P2[1]) / 2
    nx, ny = math.sin(ang), -math.cos(ang)
    return rtext(round(mx + nx * dist, 1), round(my + ny * dist, 1), txt, math.degrees(ang), size, color, bold)
b.append(side_label(L, T, "CALOR", 16, 15, DARK))
b.append(side_label(L, T, "chama, faísca, sol", 34, 11.5, "#444", False))
b.append(side_label(T, R, "OXIGÊNIO (ar)", 16, 15, "#1f5f9e"))
b.append(side_label(T, R, "vento, ar por baixo", 34, 11.5, "#444", False))
b.append(text(170, 310, "COMBUSTÍVEL", 15, "#6b3f17", True, "middle"))
b.append(text(170, 326, "isca, gravetos, lenha", 11.5, "#444", False, "middle"))
# texto da direita
b.append(text(330, 80, "Tire um lado e o fogo APAGA:", 15, "#222", True))
b.append('<circle cx="338" cy="104" r="7" fill="%s"/>' % DANGER)
b.append(tlines(352, 109, ["ÁGUA esfria → tira o CALOR"], 13))
b.append('<circle cx="338" cy="132" r="7" fill="%s"/>' % AGUA)
b.append(tlines(352, 137, ["TERRA, AREIA, TAMPA ou pano molhado", "abafam → tiram o AR"], 13))
b.append('<circle cx="338" cy="177" r="7" fill="%s"/>' % WOOD)
b.append(tlines(352, 182, ["ACEIRO (faixa sem mato) ou afastar", "a lenha → tira o COMBUSTÍVEL"], 13))
b.append(box(330, 222, 330, 96, "#eef7ee", VERDE))
b.append(tlines(342, 244, ["Para ACENDER, junte os três:",
                           "material fino e SECO, ar passando por",
                           "baixo e entre os gravetos, e calor",
                           "concentrado num ponto só."], 13, "#1d5a2a", True, 18))
# linha de tamanhos
b.append(line(20, 346, 660, 346, "#ccc", 2))
b.append(text(340, 372, "Junte TUDO antes de acender, do mais fino ao mais grosso (o dobro do que acha que precisa)", 12.5, "#222", True, "middle"))
cols = [84, 212, 340, 468, 596]
# 1 isca: tufo de fibras
cx = cols[0]
for k in range(16):
    x0 = cx - 34 + k * 4.5
    b.append(path(f"M{x0},{462} Q{x0+12},{440} {x0-2},{418} T{x0+6},{396}", "none", "#c9a227", 1.6))
b.append(path(f"M{cx-40},{462} Q{cx},{452} {cx+40},{462}", "none", "#8a6d10", 2))
# 2 gravetos finos
cx = cols[1]
for k in range(9):
    b.append(line(cx - 40 + k * 3, 462 - k * 2, cx + 30 + k * 2, 400 + k * 3, "#6b3f17", 1.8))
# 3 gravetos (lapis)
cx = cols[2]
for k in range(5):
    b.append(stick(cx - 42 + k * 6, 462 - k * 4, cx + 36 + k * 3, 404 + k * 6, 4, WOOD2))
# 4 galhos (polegar)
cx = cols[3]
for k in range(3):
    b.append(stick(cx - 44 + k * 8, 460 - k * 8, cx + 40 + k * 4, 410 + k * 10, 10, WOOD))
# 5 lenha (toras vistas de frente)
cx = cols[4]
for (dx, dy, r) in ((-30, 446, 20), (12, 446, 20), (-9, 410, 19), (40, 416, 13)):
    b.append(f'<circle cx="{cx+dx}" cy="{dy}" r="{r}" fill="#d9a066" stroke="{OUT}" stroke-width="2.5"/>')
    b.append(f'<circle cx="{cx+dx}" cy="{dy}" r="{r*0.55:.1f}" fill="none" stroke="{WOOD}" stroke-width="1.5"/>')
for k in range(4):
    b.append(arrow(cols[k] + 50, 432, cols[k + 1] - 50, 432, "#888", 3))
labs = [("1. ISCA", "fibras finas e secas", "2 punhados"),
        ("2. GRAVETO FINO", "grossura de palito", "de fósforo · 1 braçada"),
        ("3. GRAVETO", "grossura de lápis", "1 braçada"),
        ("4. GALHO", "grossura do polegar", "2 braçadas"),
        ("5. LENHA", "do punho ao braço", "uma pilha")]
for cx, (a, c, d) in zip(cols, labs):
    b.append(text(cx, 488, a, 12.5, "#222", True, "middle"))
    b.append(text(cx, 504, c, 11.5, "#333", False, "middle"))
    b.append(text(cx, 519, d, 11.5, "#333", False, "middle"))
b.append(text(340, 546, "Madeira seca QUEBRA com estalo. Se só dobra, está verde ou úmida.", 12, DARK, True, "middle"))
open(D + "triangulo-do-fogo.svg", "w").write(svg(680, 560, "Triângulo do fogo e o material para acender", "\n".join(b)))

# =====================================================================
# 2. ESTRUTURAS DE FOGUEIRA
# =====================================================================
b = []
# grade 2x2
b.append(line(340, 50, 340, 590, "#ccc", 2)); b.append(line(10, 300, 670, 300, "#ccc", 2))
# ---- TIPI (vista de lado) ----
gx, gy = 170, 210   # base central
b.append(line(40, gy + 2, 300, gy + 2, "#6b4f2a", 3))
b.append(path(f"M{gx-22},{gy} Q{gx},{gy-26} {gx+22},{gy} Z", "#e6c35c", "#8a6d10", 1.5))  # isca
for k, dx in enumerate((-70, -52, -34, -16, 16, 34, 52, 70)):
    b.append(stick(gx + dx, gy - 2, gx + dx * 0.08, gy - 118, 6 if abs(dx) > 40 else 4, WOOD if k % 2 else WOOD2))
b.append(flame(gx, gy - 4, 0.75))
b.append(text(170, 72, "TIPI (cone)", 15, "#222", True, "middle"))
b.append(tlines(20, 240, ["Isca no centro, gravetos em pé em cone,",
                          "com uma ABERTURA do lado do vento para",
                          "pôr o fogo. Acende rápido, chama alta:",
                          "bom para começar e ferver água."], 12))
# ---- CABANA (log cabin) ----
cx, by = 474, 212
b.append(line(380, by + 2, 568, by + 2, "#6b4f2a", 3))
# camadas: alterna toras de lado (retangulo) e toras de frente (circulos)
y = by
for layer in range(5):
    w = 150 - layer * 14
    if layer % 2 == 0:  # toras de frente: dois circulos nas pontas
        r = 11 - layer
        for sx in (-1, 1):
            b.append(f'<circle cx="{cx + sx*(w/2 - r)}" cy="{y - r}" r="{r}" fill="#d9a066" stroke="{OUT}" stroke-width="2"/>')
        y -= 2 * r
    else:  # tora de lado (comprida, na frente)
        h = 16 - layer
        b.append(rect(cx - w / 2, y - h, w, h, WOOD, OUT, 2, 5))
        y -= h
b.append(flame(cx, by - 6, 0.55))
# vista de cima (#)
tx, ty = 610, 150
for k in (-1, 1):
    b.append(stick(tx - 40, ty + k * 22, tx + 40, ty + k * 22, 9, WOOD))
    b.append(stick(tx + k * 22, ty - 40, tx + k * 22, ty + 40, 9, WOOD2))
b.append(f'<circle cx="{tx}" cy="{ty}" r="10" fill="#f08c00" stroke="{OUT}" stroke-width="1.5"/>')
b.append(text(tx, ty + 66, "vista de cima", 11, "#444", False, "middle"))
b.append(text(510, 72, "CABANA (camadas cruzadas)", 15, "#222", True, "middle"))
b.append(tlines(352, 240, ["Pares de toras cruzados em camadas, com um",
                           "pequeno tipi aceso dentro. Queima por igual e",
                           "faz MUITA BRASA: o melhor para cozinhar,",
                           "assar e para chapa ou grelha por cima."], 12))
# ---- ESTRELA (vista de cima) ----
cx, cy = 170, 430
b.append(f'<circle cx="{cx}" cy="{cy}" r="96" fill="#f4efe6" stroke="#c9bba0"/>')
for k in range(5):
    a = -math.pi / 2 + k * 2 * math.pi / 5
    x1, y1 = cx + 20 * math.cos(a), cy + 20 * math.sin(a)
    x2, y2 = cx + 92 * math.cos(a), cy + 92 * math.sin(a)
    b.append(stick(x2, y2, x1, y1, 16, WOOD))
    b.append(f'<circle cx="{x1:.1f}" cy="{y1:.1f}" r="7" fill="#f08c00" stroke="{OUT}" stroke-width="1.5"/>')
    ax, ay = cx + 118 * math.cos(a + 0.28), cy + 118 * math.sin(a + 0.28)
b.append(f'<circle cx="{cx}" cy="{cy}" r="18" fill="#f08c00" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="#ffd43b"/>')
b.append(arrow(cx + 128, cy - 40, cx + 92, cy - 26, DANGER, 3))
b.append(text(cx + 108, cy - 50, "empurre", 11.5, DARK, True))
b.append(text(170, 322, "ESTRELA (vista de cima)", 15, "#222", True, "middle"))
b.append(tlines(20, 548, ["4–6 toras grossas com as pontas no centro.",
                          "Empurre para dentro conforme queimam.",
                          "Economiza lenha e dura a noite toda.",
                          "Para diminuir o fogo, afaste as toras."], 11.5, lh=14))
# ---- VALA (corte lateral) ----
gy = 400
b.append(rect(350, gy, 310, 90, SOLO, "none", 0))
b.append(line(350, gy, 660, gy, "#6b4f2a", 3))
b.append(path(f"M420,{gy} L432,{gy+52} L578,{gy+52} L590,{gy}", "#fff", "#6b4f2a", 3))
b.append(rect(420, gy - 1, 170, 4, "#fff", "none", 0))
for k in range(4):
    b.append(stick(450 + k * 30, gy + 44, 466 + k * 30, gy + 24, 8, WOOD))
b.append(flame(505, gy + 36, 0.5))
# panela apoiada em 2 varas verdes
b.append(stick(400, gy - 8, 610, gy - 8, 8, "#5f8f3a"))
b.append(path(f"M470,{gy-12} L474,{gy-58} L536,{gy-58} L540,{gy-12} Z", "#7d7d7d", OUT, 2.5))
b.append(rect(464, gy - 64, 82, 8, "#5f5f5f", OUT, 2, 3))
b.append(arrow(372, gy + 30, 428, gy + 30, AGUA, 3))
b.append(text(358, gy + 20, "vento", 11.5, "#1f5f9e", True))
b.append(text(505, 322, "VALA (corte de lado)", 15, "#222", True, "middle"))
b.append(tlines(560, gy - 34, ["2 varas verdes"], 11.5, "#3b6b20", True))
b.append(line(432, gy + 66, 578, gy + 66, "#555", 1.5)); b.append(text(505, gy + 82, "60–90 cm de comprimento", 11.5, "#333", False, "middle"))
b.append(line(612, gy, 612, gy + 52, "#555", 1.5)); b.append(text(618, gy + 30, "20–30 cm", 11.5, "#333"))
b.append(tlines(352, 524, ["Vala de 30 cm de largura, com a ponta",
                           "aberta para o vento. Panela apoiada nas",
                           "bordas. Protege do vento, esconde o fogo",
                           "e quase não espalha brasa."], 11.5, lh=14))
open(D + "estruturas-fogueira.svg", "w").write(svg(680, 600, "Quatro formas de montar a fogueira", "\n".join(b)))


# =====================================================================
# 3. ARCO E BROCA
# =====================================================================
b = []
GY = 400
b.append(line(20, GY, 425, GY, "#6b4f2a", 3))
# folha embaixo do entalhe
b.append(path(f"M214,{GY+2} Q254,{GY-8} 300,{GY+2} Q254,{GY+16} 214,{GY+2} Z", "#6bab4a", OUT, 1.5))
b.append(f'<ellipse cx="256" cy="{GY+3}" rx="10" ry="4" fill="#4a2e14"/>')
# prancha
b.append(rect(60, 380, 320, 18, "#e0b47a", OUT, 2.5, 3))
b.append(poly([(247, 380), (261, 380), (258, 398), (250, 398)], "#4a2e14", OUT, 1))
# pe / bota segurando a prancha
b.append(limb([(150, 330), (138, 236)], 30, "#6f8aa3"))
b.append(path("M118,378 L118,334 Q120,318 146,318 L166,318 Q172,350 214,356 Q232,362 230,378 Z", "#5a4630", OUT, 2.5))
# broca
b.append(rect(246, 182, 16, 200, "#d9a066", OUT, 2.5, 3))
# soquete + mao
b.append(rect(220, 160, 68, 24, "#8a8a8a", OUT, 2.5, 10))
b.append(limb([(254, 150), (214, 108), (170, 84)], 16, SKIN))
b.append(f'<ellipse cx="254" cy="152" rx="24" ry="11" fill="{SKIN}" stroke="{OUT}" stroke-width="2"/>')
# arco e corda (1 volta na broca)
b.append(path("M190,300 Q300,262 412,296", "none", OUT, 11))
b.append(path("M190,300 Q300,262 412,296", "none", WOOD, 7))
b.append(line(192, 300, 247, 284, "#333", 2.5)); b.append(line(261, 296, 410, 297, "#333", 2.5))
b.append(path("M247,284 Q266,286 261,292 Q244,298 247,284", "none", "#333", 2.5))
b.append(hand(412, 298, 12))
b.append(arrow(330, 330, 410, 330, DANGER, 3)); b.append(arrow(330, 330, 250, 330, DANGER, 3))
b.append(text(330, 350, "movimentos longos", 11.5, DARK, True, "middle"))
b.append(text(30, 226, "o pé firma", 11.5, "#222", True)); b.append(text(30, 241, "a prancha", 11.5, "#222", True))
# rotulos a direita
lab = [(286, 172, 70, ["SOQUETE (apoio da mão)", "pedra ou madeira dura com", "cavidade lisa; unte com gordura"]),
       (262, 222, 140, ["BROCA", "reta e seca, 20–25 cm, grossura", "do polegar; ponta de baixo", "arredondada"]),
       (395, 286, 228, ["ARCO", "galho firme, do comprimento do", "braço; a corda dá 1 volta na", "broca, bem esticada"]),
       (372, 389, 316, ["PRANCHA (base)", "~2 cm de espessura, madeira", "macia e seca (ver texto)"]),
       (270, 400, 384, ["Folha embaixo do entalhe", "recolhe o pó que vira brasa"])]
for (px, py, ty, ls) in lab:
    b.append(line(px, py, 434, ty - 4, "#777", 1.3))
    b.append(f'<circle cx="{px}" cy="{py}" r="3" fill="#777"/>')
    b.append(tlines(440, ty, ls, 11.5, "#222", True, 14))
b.append(line(10, 438, 670, 438, "#ccc", 2))
# inset A: prancha vista de cima
b.append(text(120, 462, "Prancha vista de cima", 13, "#222", True, "middle"))
b.append(rect(30, 478, 180, 46, "#e0b47a", OUT, 2, 3))
b.append(f'<circle cx="120" cy="498" r="11" fill="#3a2a1a"/>')
b.append(poly([(120, 498), (109, 524), (131, 524)], "#3a2a1a", "#3a2a1a", 1))
b.append(tlines(30, 544, ["Buraco a ~1 cm da borda.", "Entalhe em V: 1/8 do círculo", "(45°), até o CENTRO do buraco."], 11.5, lh=14))
# inset B: sinais
b.append(text(340, 462, "Como saber se deu certo", 13, "#222", True, "middle"))
b.append(f'<circle cx="250" cy="486" r="8" fill="#4a2e14"/>')
b.append(tlines(264, 490, ["Pó marrom-escuro que", "solta fumaça SOZINHO", "= BRASA pronta"], 11.5, VERDE, True, 14))
b.append(f'<circle cx="250" cy="546" r="8" fill="#d9b48a"/>')
b.append(tlines(264, 550, ["Pó claro ou fino = pouca", "pressão/velocidade ou", "madeira úmida"], 11.5, DARK, False, 14))
# inset C: ninho
b.append(text(565, 462, "Brasa → ninho → chama", 13, "#222", True, "middle"))
b.append(f'<ellipse cx="560" cy="506" rx="46" ry="20" fill="#e6c35c" stroke="#8a6d10" stroke-width="2"/>')
b.append(f'<ellipse cx="560" cy="501" rx="24" ry="9" fill="#c9a227" stroke="#8a6d10" stroke-width="1.5"/>')
for k in range(9):
    x0 = 522 + k * 9
    b.append(path(f"M{x0},{518} q6,-10 14,-4 t12,-6", "none", "#8a6d10", 1.2))
b.append(f'<circle cx="560" cy="500" r="7" fill="#e8590c" stroke="{OUT}" stroke-width="1.5"/>')
b.append(arrow(640, 492, 604, 500, AGUA, 3))
b.append(tlines(476, 544, ["Ponha a brasa no ninho de isca,", "dobre por cima e sopre devagar", "e sem parar até pegar chama."], 11.5, lh=14))
open(D + "arco-e-broca.svg", "w").write(svg(680, 592, "Arco e broca: as peças e como usar", "\n".join(b)))

# =====================================================================
# 4. FOGAO FOGUETE (corte) — escala 7 px por cm
# =====================================================================
b = []
X0, YB = 90, 440   # canto externo esquerdo, topo do piso
def brick(x, y, w, h): return rect(x, y, w, h, TIJ, OUT, 1.8)
b.append(rect(0, YB + 35, 480, 50, SOLO, "none", 0))
b.append(line(0, YB + 35, 480, YB + 35, "#6b4f2a", 3))
b.append(brick(X0, YB, 105, 35)); b.append(brick(X0 + 105, YB, 105, 35))  # piso
for k in range(6):
    y = YB - 35 * (k + 1)
    if k >= 2:
        b.append(brick(X0, y, 70, 35))          # parede esquerda (acima da boca)
    b.append(brick(X0 + 140, y, 70, 35))        # parede direita
# interior escuro (canal em L)
b.append(f'<path d="M{X0},{YB-70} L{X0+70},{YB-70} L{X0+70},{YB-210} L{X0+140},{YB-210} L{X0+140},{YB} L{X0},{YB} Z" fill="#3b3330"/>')
# prateleira e lenha
b.append(rect(20, YB - 26, 160, 4, "#777", OUT, 1))
b.append(stick(28, YB - 36, 176, YB - 36, 14, WOOD)); b.append(stick(40, YB - 52, 168, YB - 52, 12, WOOD2))
b.append(flame(X0 + 105, YB - 40, 0.95))
# ar e gases
b.append(arrow(14, YB - 12, 150, YB - 12, AGUA, 3.5))
for y in (YB - 100, YB - 150):
    b.append(arrow(X0 + 105, y, X0 + 105, y - 40, "#e8590c", 4))
# calcos, panela, saia
PY = YB - 210  # topo do fogao = 230
b.append(rect(X0 + 8, PY - 17, 16, 17, "#666", OUT, 1.5)); b.append(rect(X0 + 186, PY - 17, 16, 17, "#666", OUT, 1.5))
b.append(path(f"M{X0+14},{PY-17} L{X0+18},{PY-129} L{X0+192},{PY-129} L{X0+196},{PY-17} Z", "#7d7d7d", OUT, 2.5))
b.append(rect(X0 + 10, PY - 137, 190, 9, "#5f5f5f", OUT, 2, 3))
b.append(rect(X0 + 96, PY - 147, 18, 10, "#5f5f5f", OUT, 1.5, 3))
b.append(rect(X0 + 2, PY - 92, 4, 92, "#b0b0b0", OUT, 1)); b.append(rect(X0 + 204, PY - 92, 4, 92, "#b0b0b0", OUT, 1))
for x in (X0 + 1, X0 + 209):
    pass
b.append(arrow(X0 + 70, PY - 6, X0 + 14, PY - 6, "#e8590c", 2.5)); b.append(arrow(X0 + 140, PY - 6, X0 + 196, PY - 6, "#e8590c", 2.5))
b.append(arrow(X0 + 11, PY - 30, X0 + 11, PY - 92, "#e8590c", 2.5)); b.append(arrow(X0 + 199, PY - 30, X0 + 199, PY - 92, "#e8590c", 2.5))
# cotas
b.append(line(X0, YB + 52, X0 + 210, YB + 52, "#333", 1.5)); b.append(line(X0, YB + 46, X0, YB + 58, "#333", 1.5)); b.append(line(X0 + 210, YB + 46, X0 + 210, YB + 58, "#333", 1.5))
b.append(text(X0 + 105, YB + 70, "30 cm (por fora)", 12, "#222", True, "middle"))
b.append(text(12, YB - 84, "BOCA 10 × 10 cm", 11.5, "#222", True))
b.append(line(X0 + 220, PY, X0 + 220, YB, "#333", 1.5)); b.append(line(X0 + 214, PY, X0 + 226, PY, "#333", 1.5)); b.append(line(X0 + 214, YB, X0 + 226, YB, "#333", 1.5))
b.append(text(X0 + 228, YB - 24, "30 cm", 12, "#222", True))
b.append(text(X0 + 105, PY + 24, "10 cm", 11.5, "#fff", True, "middle"))
# rotulos
lab = [(X0 + 200, PY - 133, 78, ["Panela sempre TAMPADA"]),
       (X0 + 208, PY - 70, 112, ["SAIA de lata em volta:", "folga de 1 a 1,5 cm"]),
       (X0 + 202, PY - 9, 160, ["3 calços de 2–3 cm:", "o calor passa por baixo"])]
for (px, py, ty, ls) in lab:
    b.append(line(px, py, 336, ty - 4, "#777", 1.3)); b.append(f'<circle cx="{px}" cy="{py}" r="3" fill="#777"/>')
    b.append(tlines(340, ty, ls, 12, "#222", True, 15))
b.append(tlines(340, 214, ["CHAMINÉ INTERNA", "10 × 10 cm; altura =", "3 × a largura"], 12, "#222", True, 15))
b.append(line(336, 210, X0 + 142, 280, "#777", 1.3))
b.append(tlines(340, 280, ["PRATELEIRA (grade):", "lenha em cima,", "AR passa por baixo"], 12, "#1f5f9e", True, 15))
b.append(line(336, 276, 170, YB - 24, "#777", 1.3))
b.append(tlines(340, 346, ["Queime só a PONTA", "da lenha; empurre", "conforme queima"], 12, "#222", True, 15))
b.append(line(336, 342, 176, YB - 50, "#777", 1.3))
# cata-vento (vista de cima das fiadas), 3 px/cm
def pinwheel(ox, oy, boca):
    s = 3; o = []
    bricks = [(0, 0, 20, 10), (20, 0, 10, 20), (10, 20, 20, 10)]
    if boca: bricks.append((0, 20, 10, 10))
    else: bricks.append((0, 10, 10, 20))
    for (x, y, w, h) in bricks:
        o.append(rect(ox + x * s, oy + y * s, w * s, h * s, TIJ, OUT, 1.8))
    o.append(rect(ox + 10 * s, oy + 10 * s, 30, 30, "#3b3330", "none", 0))
    if boca:
        o.append(rect(ox, oy + 10 * s, 30, 30, "#3b3330", "none", 0))
        o.append(arrow(ox - 26, oy + 45, ox + 16, oy + 45, AGUA, 2.5))
    return "".join(o)
b.append(tlines(600, 66, ["Vista de cima", "das fiadas"], 12.5, "#222", True, 15, "middle"))
b.append(pinwheel(565, 100, True))
b.append(tlines(538, 210, ["Fiadas 1 e 2:", "3 tijolos + meio;", "o vão é a BOCA"], 11.5, "#222", True, 14))
b.append(pinwheel(565, 270, False))
b.append(tlines(538, 380, ["Fiadas 3 a 6:", "4 tijolos em cata-", "vento; o buraco do", "meio é a chaminé"], 11.5, "#222", True, 14))
b.append(text(538, 454, "tijolo maciço", 11.5, "#555", False)); b.append(text(538, 468, "≈ 20 × 10 × 5 cm", 11.5, "#555", False))
b.append(box(20, 528, 640, 62, "#fff4e5", "#ef8a2b"))
b.append(tlines(34, 550, ["Lenha fina e seca (2–4 cm). Fumaça saindo pela boca = lenha demais, úmida ou chaminé curta.",
                          "Barro por fora isola e veda as frestas. Gasta 40–60% menos lenha que o fogo de 3 pedras."], 12.5, "#222", False, 18))
open(D + "fogao-foguete.svg", "w").write(svg(680, 600, "Fogão foguete de tijolos (corte e medidas)", "\n".join(b)))

# =====================================================================
# 5. CARVAO NO TAMBOR
# =====================================================================
b = []
b.append(line(340, 50, 340, 440, "#ccc", 2))
def tambor(x, y, w, h):
    return rect(x, y, w, h, "none", "#555", 5)
# --- painel 1 ---
GY = 390
b.append(rect(10, GY, 320, 50, SOLO, "none", 0)); b.append(line(10, GY, 330, GY, "#6b4f2a", 3))
TX, TY, TW, TH = 90, 130, 150, 260
b.append(rect(TX, TY, TW, TH, "#f6efe6", "none", 0))
for k in range(9):
    x = TX + 6 + k * 15.6
    b.append(rect(x, TY + 18, 13, TH - 22, WOOD2 if k % 2 else WOOD, OUT, 1.2, 3))
b.append(rect(TX + 3, TY + 14, TW - 6, 48, "#e8590c", "none", 0, extra='fill-opacity="0.85"'))
b.append(tambor(TX, TY, TW, TH))
b.append(rect(TX - 4, TH + TY - 22, 9, 10, "#fff", "none", 0)); b.append(rect(TX + TW - 5, TH + TY - 22, 9, 10, "#fff", "none", 0))
b.append(arrow(TX - 44, TY + TH - 17, TX + 10, TY + TH - 17, AGUA, 3)); b.append(arrow(TX + TW + 44, TY + TH - 17, TX + TW - 10, TY + TH - 17, AGUA, 3))
for dx in (-40, 0, 40):
    b.append(flame(TX + TW / 2 + dx, TY + 18, 0.5))
for (cx, cy, r) in ((140, 100, 12), (162, 90, 15), (188, 100, 11), (122, 90, 9)):
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#e9e9e9" stroke="#aaa" stroke-width="1.5"/>')
b.append(arrow(TX + TW / 2, TY + 90, TX + TW / 2, TY + 150, DANGER, 4))
b.append(rect(TX + TW / 2 - 50, TY + 158, 100, 20, "#fff", "none", 0, 4, 'fill-opacity="0.85"'))
b.append(text(TX + TW / 2, TY + 173, "a brasa desce", 12, DARK, True, "middle"))
b.append(text(170, 62 - 12, "", 12))
b.append(text(170, 64, "1. Acenda por CIMA, tambor aberto", 12.5, "#222", True, "middle"))
b.append(tlines(16, 420, ["furos de 2–3 cm junto ao fundo (ar)"], 11.5, "#1f5f9e", True))
b.append(text(170, 455, "Lenha SECA em pé, bem apertada", 12, "#222", True, "middle"))
b.append(text(170, 470, "Queima aberta: 1,5 a 3 horas", 12, "#222", False, "middle"))
# --- painel 2 ---
TX2 = 430
b.append(rect(350, GY, 320, 50, SOLO, "none", 0)); b.append(line(350, GY, 670, GY, "#6b4f2a", 3))
b.append(rect(TX2, TY + 60, TW, TH - 60, "#f6efe6", "none", 0))
import random
random.seed(3)
for k in range(9):
    x = TX2 + 6 + k * 15.6
    top = TY + 84
    for y in range(TY + TH - 28, int(top), -26):
        b.append(rect(x, y, 13, 22, "#2b2b2b", "#000", 1, 3))
b.append(tambor(TX2, TY, TW, TH))
b.append(rect(TX2 - 10, TY - 10, TW + 20, 12, "#555", OUT, 2, 2))
b.append(path(f"M{TX2-16},{TY+2} q-6,-14 10,-16 M{TX2+TW+16},{TY+2} q6,-14 -10,-16", "#a0784a", "#6b4f2a", 3))
b.append(path(f"M{TX2-50},{GY} Q{TX2-10},{GY-50} {TX2+2},{GY-60} L{TX2+2},{GY} Z", "#c9a26b", "#6b4f2a", 2))
b.append(path(f"M{TX2+TW+50},{GY} Q{TX2+TW+10},{GY-50} {TX2+TW-2},{GY-60} L{TX2+TW-2},{GY} Z", "#c9a26b", "#6b4f2a", 2))
b.append(text(510, 64, "2. Fumaça fina e azulada: TAMPE", 12.5, "#222", True, "middle"))
b.append(tlines(600, 96, ["barro", "vedando", "a tampa"], 11.5, "#6b3f17", True, 13))
b.append(line(612, 126, TX2 + TW + 8, TY - 4, "#777", 1.3))
b.append(tlines(352, 318, ["terra", "tampando", "os furos"], 11.5, "#6b3f17", True, 13))
b.append(text(604, 250, "carvão", 12.5, "#222", True)); b.append(line(602, 246, TX2 + TW - 20, 270, "#777", 1.3))
b.append(text(510, 455, "Espere 12 a 24 h fechado.", 12, "#222", True, "middle"))
b.append(text(510, 470, "Abra só quando estiver FRIO.", 12, DARK, True, "middle"))
b.append(box(20, 486, 640, 60, "#fff4e5", "#ef8a2b"))
b.append(tlines(34, 508, ["Rende ~1 kg de carvão para cada 4–5 kg de lenha (10–15 kg por tambor de 200 L).",
                          "Faça longe de casas e de mato seco. A fumaça tem monóxido de carbono."], 12.5, "#222", False, 18))
open(D + "carvao-tambor.svg", "w").write(svg(680, 556, "Carvão vegetal num tambor de 200 litros", "\n".join(b)))

# =====================================================================
# 6. CAIXA TERMICA DE COZIMENTO
# =====================================================================
b = []
PALHA = "#f1dfa6"
b.append(rect(40, 110, 280, 270, WOOD, OUT, 3, 4))
b.append(rect(54, 124, 252, 242, PALHA, "none", 0))
for k in range(40):
    import random as _r
for k in range(60):
    x = 60 + (k * 37) % 240; y = 130 + (k * 53) % 230
    b.append(line(x, y, x + 12, y + 4, "#c9a95a", 1.2))
# almofada de cima
b.append(rect(54, 124, 252, 62, "#e9d18a", "#8a6d10", 2, 14))
for k in range(12):
    x = 64 + k * 20
    b.append(line(x, 140, x + 10, 170, "#c9a95a", 1.2))
# panela
b.append(rect(120, 198, 120, 9, "#5f5f5f", OUT, 2, 3))
b.append(path("M124,207 L128,300 L232,300 L236,207 Z", "#7d7d7d", OUT, 2.5))
b.append(rect(132, 222, 96, 72, "#c98a4a", "none", 0, extra='fill-opacity="0.6"'))
b.append(text(180, 262, "comida", 12, "#fff", True, "middle"))
b.append(text(180, 277, "quente", 12, "#fff", True, "middle"))
# tampa da caixa
b.append(rect(32, 96, 296, 14, "#6b4424", OUT, 2.5, 3))
# cotas isolamento
b.append(line(54, 336, 124, 336, "#222", 1.5)); b.append(text(89, 352, "8–10 cm", 11.5, "#222", True, "middle"))
b.append(line(180, 300, 180, 366, "#222", 1.5)); b.append(text(186, 340, "8–10 cm", 11.5, "#222", True))
b.append(text(180, 402, "isolamento em TODOS os lados", 12, "#6b3f17", True, "middle"))
b.append(text(180, 418, "(palha seca, isopor, serragem, jornal", 11.5, "#333", False, "middle"))
b.append(text(180, 433, "amassado, cobertores, roupas)", 11.5, "#333", False, "middle"))
b.append(text(180, 86, "almofada de palha ou cobertor por cima", 11.5, "#6b3f17", True, "middle"))
# passos
b.append(text(350, 72, "Como usar", 15, "#222", True))
steps = [["1. Ferva a panela CHEIA, com tampa,", "   pelo tempo da tabela."],
         ["2. Sem abrir, ponha RÁPIDO na caixa,", "   cubra com a almofada e feche."],
         ["3. Deixe o tempo indicado. Não abra", "   para espiar (perde calor)."],
         ["4. Abriu e está só morna (abaixo de", "   60 °C)? Ferva de novo antes de comer."]]
y = 98
for st in steps:
    b.append(tlines(350, y, st, 12.5, "#222", False, 16)); y += 40
# tabela
ty = 270
b.append(rect(350, ty - 18, 310, 24, "#efe7d6", "none", 0))
b.append(text(358, ty, "Alimento", 12, "#222", True)); b.append(text(500, ty, "Ferver", 12, "#222", True)); b.append(text(580, ty, "Na caixa", 12, "#222", True))
rows = [("Arroz", "5 min", "1–1,5 h"), ("Feijão (demolhado)", "15 min", "3–4 h"), ("Mandioca, batata", "5–10 min", "1–2 h"),
        ("Carne em pedaços", "15–20 min", "3–4 h"), ("Canjica, grão-de-bico", "15 min", "4–6 h")]
for k, (a, f, c) in enumerate(rows):
    yy = ty + 22 + k * 20
    if k % 2: b.append(rect(350, yy - 15, 310, 20, "#f7f3ea", "none", 0))
    b.append(text(358, yy, a, 12)); b.append(text(500, yy, f, 12)); b.append(text(580, yy, c, 12))
b.append(box(20, 446, 640, 60, "#eef7ee", VERDE))
b.append(tlines(34, 468, ["Economiza 50–70% do combustível. Quanto mais cheia a panela e menos ar sobrar, melhor.",
                          "Feijão: ferva FORTE pelo menos 15 min antes (o feijão cru tem substância tóxica)."], 12.5, "#1d5a2a", False, 18))
open(D + "caixa-termica.svg", "w").write(svg(680, 516, "Caixa térmica: cozinhar quase sem fogo", "\n".join(b)))
print("ok fogo")
