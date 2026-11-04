import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "11-natureza-e-desastres", "img") + "/"
os.makedirs(D, exist_ok=True)
WOOD = "#8b5a2b"; AGUA = "#4a90d9"; AGUA_C = "#cfe6fb"; SOLO = "#e8d3b0"; VERDE = "#2b8a3e"; PERIGO = "#d62828"; PERIGO2 = "#b3001b"
BARRO = "#a07850"   # agua de enchente (barrenta)


def carro(x, yg, L, H, r, cor, tipo="pequeno", ang=0):
    """Carro de perfil, frente para a esquerda. x = frente, yg = chao."""
    yb = yg - r * 0.55          # fundo da carroceria
    yt = yg - H                 # teto
    h = yb - yt
    if tipo == "pequeno":
        pts = [(0.02, 0), (0, 0.18), (0.01, 0.45), (0.30, 0.55), (0.44, 1), (0.84, 1), (0.97, 0.58), (1, 0.2), (0.98, 0)]
        jan = [(0.33, 0.58), (0.45, 0.93), (0.62, 0.93), (0.62, 0.58)]
        jan2 = [(0.65, 0.58), (0.65, 0.93), (0.83, 0.93), (0.93, 0.58)]
        rodas = (0.18, 0.80)
    else:
        pts = [(0.01, 0), (0, 0.2), (0.01, 0.55), (0.26, 0.6), (0.36, 1), (0.97, 1), (1, 0.6), (1, 0.2), (0.99, 0)]
        jan = [(0.38, 0.64), (0.45, 0.93), (0.62, 0.93), (0.62, 0.64)]
        jan2 = [(0.65, 0.64), (0.65, 0.93), (0.95, 0.93), (0.95, 0.64)]
        rodas = (0.17, 0.80)
    P = lambda q: f"{x + q[0]*L:.1f},{yb - q[1]*h:.1f}"
    s = f'<g transform="rotate({ang} {x+L/2} {yg})">'
    s += f'<polygon points="{" ".join(P(q) for q in pts)}" fill="{cor}" stroke="{OUT}" stroke-width="2.5" stroke-linejoin="round"/>'
    for j in (jan, jan2):
        s += f'<polygon points="{" ".join(P(q) for q in j)}" fill="#dfeefa" stroke="{OUT}" stroke-width="2"/>'
    for rx in rodas:
        cx = x + rx * L
        s += f'<circle cx="{cx:.1f}" cy="{yg - r:.1f}" r="{r}" fill="#333" stroke="{OUT}" stroke-width="2"/>'
        s += f'<circle cx="{cx:.1f}" cy="{yg - r:.1f}" r="{r*0.45:.1f}" fill="#bbb"/>'
    s += '</g>'
    return s


def regua(x, ytop, ybot, rotulo, cor=PERIGO2):
    s = f'<line x1="{x}" y1="{ytop}" x2="{x}" y2="{ybot}" stroke="{cor}" stroke-width="2.5"/>'
    s += f'<line x1="{x-6}" y1="{ytop}" x2="{x+6}" y2="{ytop}" stroke="{cor}" stroke-width="2.5"/>'
    s += f'<line x1="{x-6}" y1="{ybot}" x2="{x+6}" y2="{ybot}" stroke="{cor}" stroke-width="2.5"/>'
    s += text(x - 10, (ytop + ybot) / 2 + 5, rotulo, 13, cor, True, "end")
    return s


def agua_corrente(x0, x1, ytop, yg):
    s = f'<rect x="{x0}" y="{ytop}" width="{x1-x0}" height="{yg-ytop}" fill="{BARRO}" fill-opacity="0.55"/>'
    s += f'<line x1="{x0}" y1="{ytop}" x2="{x1}" y2="{ytop}" stroke="#6b4a2a" stroke-width="2"/>'
    return s


# =====================================================================
# ENCHENTE: FORCA DA AGUA
# =====================================================================
b = []
SC = 0.8  # px por cm
# --- Painel A: pessoa, 15 cm
yg = 236
b.append(f'<rect x="14" y="{yg}" width="200" height="8" fill="#6b5a40"/>')
yw = yg - 15 * SC
# pessoa desequilibrada (pes levados para a direita)
b.append(limb([(126, yg-4), (112, yg-60), (106, 170)], 15, VIT))
b.append(limb([(142, yg-8), (122, yg-62), (112, 170)], 15, VIT))
b.append(limb([(108, 176), (92, 116)], 30, VIT))
b.append(limb([(94, 122), (60, 132), (44, 120)], 10, VIT)); b.append(hand(42, 118, 6))
b.append(limb([(96, 120), (130, 104), (150, 90)], 10, VIT)); b.append(hand(152, 88, 6))
b.append(head(84, 96, 15, VIT, -0.3, -0.2))
b.append(agua_corrente(14, 214, yw, yg))
for xx in (30, 100, 160):
    b.append(arrow(xx, yg - 5, xx + 30, yg - 5, "#fff", 2.5))
b.append(regua(30, yw, yg, ""))
b.append(text(40, 214, "15 cm", 13, PERIGO2, True))
b += [text(14, 270, "15 cm de água correndo", 12.5, "#222", True), text(14, 286, "DERRUBA um adulto", 12.5, PERIGO2, True),
      text(14, 302, "(só um pouco acima do", 11.5, "#444"), text(14, 316, "tornozelo)", 11.5, "#444")]
b.append(f'<line x1="226" y1="54" x2="226" y2="324" stroke="#ccc" stroke-width="2"/>')
# --- Painel B: carro pequeno, 30 cm
L, H, r = 380 * SC, 145 * SC, 30 * SC
x0 = 300
b.append(f'<rect x="238" y="{yg}" width="428" height="8" fill="#6b5a40"/>')
yw = yg - 30 * SC
b.append(carro(x0, yg - 6, L, H, r, "#e9c46a", "pequeno", -3))
b.append(agua_corrente(238, 666, yw, yg))
for xx in (250, 400, 560):
    b.append(arrow(xx, yg - 9, xx + 34, yg - 9, "#fff", 2.5))
b.append(regua(278, yw, yg, ""))
b.append(text(250, yw - 8, "30 cm", 13, PERIGO2, True))
b.append(arrow(520, 92, 640, 92, PERIGO, 4))
b += [text(520, 78, "flutua e é levado", 12, PERIGO2, True)]
b += [text(238, 270, "30 cm de água correndo ARRASTA um carro pequeno", 12.5, "#222", True),
      text(238, 286, "(o carro boia: os pneus perdem o contato com o chão)", 11.5, "#444")]
b.append(f'<line x1="14" y1="330" x2="666" y2="330" stroke="#ccc" stroke-width="2"/>')
# --- Painel C: carro grande, 60 cm
yg2 = 520
L, H, r = 480 * SC, 185 * SC, 38 * SC
x0 = 76
b.append(f'<rect x="14" y="{yg2}" width="652" height="8" fill="#6b5a40"/>')
yw2 = yg2 - 60 * SC
b.append(carro(x0, yg2 - 4, L, H, r, "#7a9cc6", "grande", -2))
b.append(agua_corrente(14, 666, yw2, yg2))
for xx in (60, 200, 340, 500):
    b.append(arrow(xx, yg2 - 14, xx + 34, yg2 - 14, "#fff", 2.5))
b.append(regua(40, yw2, yg2, ""))
b.append(text(14, yw2 - 8, "60 cm", 13, PERIGO2, True))
b += [text(470, 360, "60 cm de água correndo", 12.5, "#222", True), text(470, 376, "ARRASTA carro grande,", 12.5, PERIGO2, True),
      text(470, 392, "caminhonete e SUV", 12.5, PERIGO2, True)]
# regras
yb = 538
b.append(box(14, yb, 652, 122, "#fdecec", PERIGO))
b += [text(28, yb+21, "Água correndo acima do tornozelo: NÃO entre. Rua ou ponte alagada: dê meia-volta.", 12.5, PERIGO2, True),
      text(28, yb+40, "A água barrenta esconde bueiros sem tampa, buracos, fios com energia e esgoto.", 12.5),
      text(28, yb+60, "Preso no carro com a água subindo: 1. solte o cinto  2. abra a janela (ou quebre)", 12.5, "#222", True),
      text(28, yb+77, "3. tire as crianças primeiro  4. saia pela janela e suba no teto. Não espere afundar.", 12.5, "#222", True),
      text(28, yb+97, "Contato com água de enchente = risco de leptospirose (febre e dor na panturrilha", 12.5),
      text(28, yb+114, "1 a 30 dias depois): procure atendimento e diga que teve contato.", 12.5)]
open(D + "enchente-forca-agua.svg", "w").write(svg(680, yb + 132, "Enchente: pouca água correndo já mata", "\n".join(b)))


# =====================================================================
# SINAIS DE DESLIZAMENTO
# =====================================================================
def num(cx, cy, n):
    return (f'<circle cx="{cx}" cy="{cy}" r="11" fill="{PERIGO}" stroke="#fff" stroke-width="2"/>'
            + text(cx, cy + 5, str(n), 13, "#fff", True, "middle"))


def casa(x, yg, w, h, cor="#e9dcc6"):
    s = f'<rect x="{x}" y="{yg-h}" width="{w}" height="{h}" fill="{cor}" stroke="{OUT}" stroke-width="2.5"/>'
    s += f'<polygon points="{x-8},{yg-h} {x+w/2},{yg-h-h*0.55} {x+w+8},{yg-h}" fill="#a0522d" stroke="{OUT}" stroke-width="2.5"/>'
    return s


b = []
# perfil do morro: plato -> crista -> encosta -> baixada
prof = [(10, 132), (150, 132), (190, 150), (250, 200), (320, 268), (380, 330), (420, 360), (450, 364)]
pts = " ".join(f"{x},{y}" for x, y in prof) + " 450,420 10,420"
b.append(f'<polygon points="{pts}" fill="{SOLO}" stroke="#6b4f2a" stroke-width="3" stroke-linejoin="round"/>')
# superficie de ruptura (onde a terra vai escorregar)
b.append('<path d="M160 134 Q 190 250 420 362" fill="none" stroke="#8a5a2a" stroke-width="2.5" stroke-dasharray="8 6"/>')
b += [text(190, 300, "por aqui a terra", 11, "#6b4a2a"), text(190, 313, "pode escorregar", 11, "#6b4a2a")]
# casa no alto com rachaduras
b.append(casa(40, 132, 80, 52))
b.append(f'<rect x="56" y="98" width="18" height="34" fill="#6b4f2a" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<rect x="88" y="98" width="20" height="16" fill="#dfeefa" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<path d="M84 82 l6 10 l-5 8 l7 10 l-4 8 l6 10" fill="none" stroke="{PERIGO}" stroke-width="2.5"/>')
b.append(num(30, 90, 4))
# rachaduras e degrau no terreno perto da crista
b.append(f'<path d="M140 132 l4 14 l4 -14 M160 134 l3 12 l3 -12" fill="#fff" stroke="{PERIGO}" stroke-width="2.5"/>')
b.append(f'<path d="M150 132 L162 134 L162 142" fill="none" stroke="#6b4f2a" stroke-width="2"/>')
b.append(num(152, 112, 1))
# arvore e poste inclinados
def arvore_incl(x, y, ang):
    return (f'<g transform="rotate({ang} {x} {y})"><rect x="{x-4}" y="{y-56}" width="8" height="56" fill="{WOOD}" stroke="{OUT}" stroke-width="2"/>'
            f'<circle cx="{x}" cy="{y-66}" r="22" fill="#5fa35a" stroke="{OUT}" stroke-width="2.5"/></g>')
b.append(arvore_incl(232, 186, 22))
b.append(f'<g transform="rotate(18 292 242)"><rect x="289" y="172" width="6" height="70" fill="#9a9a9a" stroke="{OUT}" stroke-width="1.8"/><rect x="279" y="176" width="26" height="5" fill="#9a9a9a" stroke="{OUT}" stroke-width="1.5"/></g>')
b.append(num(214, 110, 2))
# estalos
b.append(f'<path d="M262 120 q 8 -8 0 -16 M270 126 q 14 -14 0 -28 M278 132 q 20 -20 0 -40" fill="none" stroke="#555" stroke-width="2"/>')
b.append(text(284, 112, "crec!", 12, "#555", True))
b.append(num(336, 106, 6))
# agua barrenta minando
b.append(f'<path d="M338 282 q 10 6 14 18 q 4 10 16 14 q 12 4 18 16" fill="none" stroke="{BARRO}" stroke-width="5" stroke-linecap="round"/>')
for (dx, dy) in ((346, 296), (360, 312), (378, 326)):
    b.append(f'<ellipse cx="{dx}" cy="{dy}" rx="3" ry="4.5" fill="{BARRO}"/>')
b.append(num(326, 262, 3))
# muro embarrigado e casa embaixo
b.append(f'<path d="M398 314 Q 410 334 400 362 L 412 362 Q 422 334 410 314 Z" fill="#b5b5b5" stroke="{OUT}" stroke-width="2"/>')
b.append(num(396, 296, 5))
b.append(casa(418, 364, 30, 26))
# legenda
lx = 462
leg = [
    (1, ["Rachaduras e degraus", "no chão, no alto ou no", "meio do morro"]),
    (2, ["Árvores, postes, cercas", "e muros inclinando"]),
    (3, ["Água barrenta minando", "do barranco; mina nova,", "ou que seca de repente"]),
    (4, ["Rachaduras novas nas", "paredes; portas e janelas", "emperrando"]),
    (5, ["Muro \"embarrigando\"", "(estufando)"]),
    (6, ["Estalos, barulho de", "árvore quebrando, ronco", "de terra"]),
]
yy = 66
for n, linhas in leg:
    b.append(num(lx + 10, yy - 4, n))
    for i, l in enumerate(linhas):
        b.append(text(lx + 28, yy + i * 14, l, 11.5, "#222", i == 0))
    yy += 14 * len(linhas) + 12
# inset: para onde fugir (visto de cima)
yi = 436
b.append(text(14, yi, "Para onde fugir (visto de cima)", 13.5, "#222", True))
b.append(f'<rect x="14" y="{yi+10}" width="300" height="130" rx="8" fill="#f1e7d4" stroke="#c9b48a"/>')
for k in range(4):
    yk = yi + 26 + k * 28
    b.append(f'<path d="M24 {yk} Q 164 {yk-8} 304 {yk}" fill="none" stroke="#c9b48a" stroke-width="1.5"/>')
b.append(text(30, yi + 24, "alto do morro", 10.5, "#8a6a40"))
b.append(text(30, yi + 134, "baixada", 10.5, "#8a6a40"))
b.append(f'<path d="M140 {yi+18} Q 128 {yi+70} 132 {yi+132} L 196 {yi+132} Q 200 {yi+70} 186 {yi+18} Z" fill="{BARRO}" fill-opacity="0.75" stroke="#6b4a2a" stroke-width="2"/>')
b.append(text(163, yi + 120, "terra", 11, "#fff", True, "middle"))
b.append(f'<circle cx="163" cy="{yi+46}" r="6" fill="{SOC}" stroke="{OUT}" stroke-width="2"/>')
b.append(arrow(155, yi + 46, 84, yi + 40, VERDE, 4)); b.append(arrow(171, yi + 46, 244, yi + 40, VERDE, 4))
b.append(f'<line x1="163" y1="{yi+54}" x2="163" y2="{yi+92}" stroke="{PERIGO}" stroke-width="3" stroke-dasharray="5 4"/>')
b += [text(20, yi + 64, "PARA O LADO", 11.5, VERDE, True), text(20, yi + 78, "e para cima", 11.5, VERDE, True),
      text(222, yi + 64, "PARA O LADO", 11.5, VERDE, True), text(222, yi + 78, "e para cima", 11.5, VERDE, True)]
b += [text(206, yi + 108, "NUNCA morro", 11, PERIGO2, True), text(206, yi + 121, "abaixo", 11, PERIGO2, True)]
# causas evitaveis
b.append(box(326, yi + 10, 340, 130, "#fff4e5", "#ef8a2b"))
b += [text(340, yi + 30, "O que provoca deslizamento (evite):", 12.5, "#222", True),
      text(340, yi + 50, "• corte reto no barranco para construir", 11.5),
      text(340, yi + 66, "• aterro solto, lixo e entulho na encosta", 11.5),
      text(340, yi + 82, "• água de chuva, pia e esgoto jogada no", 11.5),
      text(340, yi + 96, "   morro (use calha e canaleta)", 11.5),
      text(340, yi + 112, "• tirar o mato; bananeira na encosta", 11.5),
      text(340, yi + 128, "   (encharca o solo)", 11.5)]
yb = yi + 152
b.append(box(14, yb, 652, 46, "#fdecec", PERIGO))
b += [text(28, yb + 19, "Chuva forte por horas ou vários dias + UM desses sinais = SAIA JÁ e avise", 12.5, PERIGO2, True),
      text(28, yb + 37, "os vizinhos. Volte só quando a chuva parar há dias e a Defesa Civil (199) liberar.", 12.5)]
open(D + "deslizamento-sinais.svg", "w").write(svg(680, yb + 56, "Sinais de que o morro vai deslizar", "\n".join(b)))
print("ok")
