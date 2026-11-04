import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
# Figuras de 09-quimica-e-oficios: sabao, lixivia de cinza, tear, ceramica.
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "09-quimica-e-oficios", "img") + "/"
os.makedirs(D, exist_ok=True)
import math, random
WOOD = "#8b5a2b"; SOLO = "#e8d3b0"; AGUA = "#4a90d9"; AGUA2 = "#cfe6fb"; RED = "#d62828"; DRED = "#b3001b"; GREEN = "#2b8a3e"

def lbl(x, y, s, size=12, color="#222", bold=False, anchor="start"):
    b = ' font-weight="bold"' if bold else ''
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}"{b} text-anchor="{anchor}" '
            f'stroke="#fff" stroke-width="4" stroke-linejoin="round" paint-order="stroke">{s}</text>')

def lines(x, y, arr, size=12, color="#222", bold=False, dy=15, anchor="start"):
    return "".join(text(x, y + i * dy, t, size, color, bold, anchor) for i, t in enumerate(arr))

def num(x, y, n, cor="#1e1e1e"):
    return f'<circle cx="{x}" cy="{y}" r="12" fill="{cor}"/>' + text(x, y + 5, str(n), 14, "#fff", True, "middle")

def chama(x, y, s=1.0):
    return (f'<path d="M{x} {y} C {x-14*s} {y-14*s}, {x-6*s} {y-26*s}, {x} {y-40*s} C {x+4*s} {y-26*s}, {x+16*s} {y-18*s}, {x} {y} Z" fill="#f4a020" stroke="#c0400a" stroke-width="1.5"/>'
            f'<path d="M{x} {y-3*s} C {x-6*s} {y-10*s}, {x-2*s} {y-18*s}, {x} {y-24*s} C {x+3*s} {y-16*s}, {x+7*s} {y-10*s}, {x} {y-3*s} Z" fill="#ffe066"/>')

# =====================================================================
# SABAO: fluxograma
# =====================================================================
b = []
b.append(box(8, 44, 664, 44, "#fff4e5", "#ef8a2b"))
b.append(text(340, 62, "Receita base (óleo de soja, girassol, milho ou de fritura bem coado):", 13, "#222", True, "middle"))
b.append(text(340, 80, "1 kg de óleo  +  130 g de soda cáustica (escamas 97–99%)  +  350 mL de água", 13.5, DRED, True, "middle"))
CX = [8, 234, 460]; CW = 212
def card(i, row, titulo, linhas_txt, icone):
    x = CX[i]; y = 98 if row == 0 else 290
    s = f'<rect x="{x}" y="{y}" width="{CW}" height="182" rx="8" fill="#f7f7f7" stroke="#bbb" stroke-width="1.5"/>'
    s += num(x + 18, y + 20, i + 1 + 3 * row) + text(x + 36, y + 25, titulo, 13.5, "#222", True)
    s += icone(x, y)
    s += lines(x + 10, y + 128, linhas_txt, 11.5)
    return s
def ic_balanca(x, y):
    return (f'<rect x="{x+56}" y="{y+96}" width="100" height="18" rx="4" fill="#bfc6cc" stroke="{OUT}" stroke-width="2"/>'
            f'<rect x="{x+92}" y="{y+100}" width="28" height="10" rx="2" fill="#dff3d9" stroke="{OUT}" stroke-width="1.2"/>'
            + text(x + 106, y + 109, "130 g", 8, "#222", True, "middle") +
            f'<path d="M{x+66} {y+92} L {x+146} {y+92} L {x+136} {y+64} L {x+76} {y+64} Z" fill="#fff" stroke="{OUT}" stroke-width="2"/>'
            + "".join(f'<rect x="{x+86+(k%5)*10}" y="{y+78-(k//5)*7}" width="7" height="5" rx="1.5" fill="#f0f0f0" stroke="#777" stroke-width="1"/>' for k in range(9)))
def ic_soda_agua(x, y):
    s = (f'<path d="M{x+60} {y+56} L {x+70} {y+116} L {x+142} {y+116} L {x+152} {y+56} Z" fill="#fff" stroke="{OUT}" stroke-width="2.5"/>'
         f'<path d="M{x+63} {y+74} L {x+70} {y+116} L {x+142} {y+116} L {x+149} {y+74} Z" fill="{AGUA2}" stroke="none"/>'
         f'<path d="M{x+168} {y+38} l 20 -6 l 4 16 l -20 6 Z" fill="#eee" stroke="{OUT}" stroke-width="2"/>')
    for k in range(6):
        s += f'<rect x="{x+150-k*7}" y="{y+52+k*5}" width="5" height="4" rx="1" fill="#fafafa" stroke="#777" stroke-width="1"/>'
    s += f'<path d="M{x+90} {y+66} q -6 -8 0 -16 q 6 -8 0 -16" fill="none" stroke="#999" stroke-width="2"/>'
    s += f'<path d="M{x+112} {y+66} q -6 -8 0 -16 q 6 -8 0 -16" fill="none" stroke="#999" stroke-width="2"/>'
    s += lbl(x + 106, y + 104, "água fria", 10.5, "#1d4f80", True, "middle")
    s += lbl(x + 168, y + 66, "soda", 10.5, "#222", True)
    return s
def ic_juntar(x, y):
    return (f'<path d="M{x+40} {y+66} L {x+46} {y+116} L {x+150} {y+116} L {x+156} {y+66} Z" fill="#fff" stroke="{OUT}" stroke-width="2.5"/>'
            f'<path d="M{x+42} {y+80} L {x+46} {y+116} L {x+150} {y+116} L {x+154} {y+80} Z" fill="#f6dd84"/>'
            f'<g transform="rotate(35 {x+170} {y+56})"><rect x="{x+152}" y="{y+40}" width="34" height="40" rx="4" fill="#fff" stroke="{OUT}" stroke-width="2"/>'
            f'<rect x="{x+154}" y="{y+56}" width="30" height="22" fill="{AGUA2}"/></g>'
            f'<path d="M{x+150} {y+62} Q {x+140} {y+66} {x+136} {y+80}" fill="none" stroke="{AGUA}" stroke-width="3"/>'
            + lbl(x + 96, y + 104, "óleo 40–50 °C", 10.5, "#6b4a00", True, "middle")
            + lbl(x + 168, y + 36, "lixívia", 10.5, "#1d4f80", True, "middle"))
def ic_traco(x, y):
    return (f'<path d="M{x+40} {y+66} L {x+46} {y+116} L {x+150} {y+116} L {x+156} {y+66} Z" fill="#fff" stroke="{OUT}" stroke-width="2.5"/>'
            f'<path d="M{x+42} {y+78} L {x+46} {y+116} L {x+150} {y+116} L {x+154} {y+78} Z" fill="#f3e6b8"/>'
            f'<path d="M{x+62} {y+80} q 14 -5 28 0 q 14 5 28 0" fill="none" stroke="#c9b26a" stroke-width="3"/>'
            f'<rect x="{x+128}" y="{y+34}" width="10" height="44" rx="4" fill="{WOOD}" stroke="{OUT}" stroke-width="2" transform="rotate(20 {x+133} {y+56})"/>'
            f'<ellipse cx="{x+120}" cy="{y+80}" rx="12" ry="5" fill="{WOOD}" stroke="{OUT}" stroke-width="2"/>'
            f'<path d="M{x+120} {y+86} L {x+120} {y+96}" stroke="#c9b26a" stroke-width="3"/>'
            + lbl(x + 70, y + 50, "o \"fio\" que cai", 10.5, "#222", True, "middle") + lbl(x + 70, y + 62, "fica marcado", 10.5, "#222", True, "middle"))
def ic_forma(x, y):
    s = (f'<path d="M{x+56} {y+70} L {x+56} {y+116} L {x+156} {y+116} L {x+156} {y+70}" fill="#fff" stroke="{OUT}" stroke-width="2.5"/>'
         f'<rect x="{x+58}" y="{y+82}" width="96" height="32" fill="#f6eecb"/>'
         f'<path d="M{x+46} {y+64} Q {x+106} {y+44} {x+166} {y+64}" fill="none" stroke="#7a8fa6" stroke-width="5"/>')
    s += lbl(x + 106, y + 104, "caixa de leite", 10.5, "#222", True, "middle")
    s += lbl(x + 106, y + 46, "pano por cima", 10.5, "#3f6d9e", True, "middle")
    return s
def ic_cura(x, y):
    s = f'<rect x="{x+30}" y="{y+108}" width="150" height="8" fill="{WOOD}" stroke="{OUT}" stroke-width="2"/>'
    for k in range(5):
        s += f'<rect x="{x+36+k*29}" y="{y+86}" width="20" height="22" rx="3" fill="#f6eecb" stroke="{OUT}" stroke-width="2"/>'
    s += f'<rect x="{x+70}" y="{y+40}" width="70" height="38" rx="4" fill="#fff" stroke="{OUT}" stroke-width="2"/><rect x="{x+70}" y="{y+40}" width="70" height="10" fill="{RED}"/>'
    s += text(x + 105, y + 72, "4–6 sem.", 11, "#222", True, "middle")
    return s
b.append(card(0, 0, "Pese tudo", ["Balança de cozinha. Óleo de", "fritura: coe em pano e deixe", "assentar; use só o de cima."], ic_balanca))
b.append(card(1, 0, "SODA NA ÁGUA", ["Ao ar livre, de óculos e luvas.", "Esquenta a ~90 °C e solta", "vapor: não respire. Esfrie."], ic_soda_agua))
b.append(card(2, 0, "Junte devagar", ["Lixívia e óleo ambos a", "40–50 °C. Despeje a lixívia", "em fio no óleo, mexendo."], ic_juntar))
b.append(card(0, 1, "Mexa até o traço", ["15 min a 2 h (à mão, mexa", "5 min, descanse 10). Ponto de", "mingau ralo, que marca."], ic_traco))
b.append(card(1, 1, "Forma 24–48 h", ["Forma de plástico, madeira", "forrada ou caixa de leite.", "Desenforme e corte em barras."], ic_forma))
b.append(card(2, 1, "Cure 4–6 semanas", ["Sombra, seco, ventilado,", "barras separadas. Só use", "depois do teste de pH."], ic_cura))
for (x1, y1, x2, y2) in ((222, 190, 232, 190), (448, 190, 458, 190), (556, 282, 120, 288)):
    pass
b.append(arrow(220, 188, 236, 188, "#555", 3)); b.append(arrow(446, 188, 462, 188, "#555", 3)); b.append(arrow(446, 380, 462, 380, "#555", 3)); b.append(arrow(220, 380, 236, 380, "#555", 3))
b.append('<path d="M566 280 L 566 285 L 114 285 L 114 287" fill="none" stroke="#555" stroke-width="3"/>')
# seguranca
b.append(box(8, 482, 664, 112, "#fdecec", RED))
b.append(text(20, 502, "SEGURANÇA (soda cáustica cega e queima)", 14, DRED, True))
b += [text(20, 522, "• Óculos (ou máscara de solda/vidro), luvas de borracha, manga comprida, sapato fechado.", 12),
      text(20, 539, "• SEMPRE a soda na água fria, aos poucos. NUNCA água sobre a soda (ferve e espirra).", 12, DRED, True),
      text(20, 556, "• Use plástico PP (nº 5), inox, vidro grosso ou barro. NUNCA alumínio (reage e solta gás que pega fogo).", 12),
      text(20, 573, "• Respingo no olho: água corrente 15–20 min, pálpebras abertas. NÃO use vinagre.", 12, DRED, True),
      text(20, 590, "• Na pele: muita água por 15 min. Crianças e animais longe. Guarde a soda fechada e rotulada.", 12)]
open(D + "sabao-processo.svg", "w").write(svg(680, 604, "Sabão em barra com soda: passo a passo", "\n".join(b)))

# =====================================================================
# BARRIL DE LIXIVIA (DECOADA) DE CINZA - corte
# =====================================================================
b = []
# suporte de tijolos
for bx in (50, 196):
    for k in range(4):
        b.append(f'<rect x="{bx}" y="{300+k*22}" width="44" height="22" fill="#b5523b" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<line x1="20" y1="388" x2="420" y2="388" stroke="#6b4f2a" stroke-width="3"/>')
b.append(f'<rect x="20" y="388" width="400" height="20" fill="{SOLO}"/>')
# barril (corte)
bx0, bx1, top, bot = 60, 230, 80, 296
b.append(f'<rect x="{bx0-10}" y="{top}" width="10" height="{bot-top+4}" fill="{WOOD}" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<rect x="{bx1}" y="{top}" width="10" height="{bot-top+4}" fill="{WOOD}" stroke="{OUT}" stroke-width="2"/>')
for k in range(6):
    xa = bx0 + k * (bx1 - bx0) / 6
    b.append(f'<rect x="{xa+3:.0f}" y="{bot}" width="{(bx1-bx0)/6-6:.0f}" height="8" fill="{WOOD}" stroke="{OUT}" stroke-width="2"/>')
# camadas
b.append(f'<rect x="{bx0}" y="{top+30}" width="{bx1-bx0}" height="{bot-top-30}" fill="#9a9a9a"/>')   # cinza
random.seed(3)
for k in range(260):
    xx = random.uniform(bx0 + 3, bx1 - 3); yy = random.uniform(top + 34, 246)
    b.append(f'<circle cx="{xx:.1f}" cy="{yy:.1f}" r="1.3" fill="#d0d0d0"/>')
b.append(f'<rect x="{bx0}" y="{top+12}" width="{bx1-bx0}" height="18" fill="{AGUA2}"/>')
b.append(f'<line x1="{bx0}" y1="{top+12}" x2="{bx1}" y2="{top+12}" stroke="{AGUA}" stroke-width="2"/>')
b.append(f'<rect x="{bx0}" y="250" width="{bx1-bx0}" height="18" fill="#e9cf6a"/>')   # palha
for k in range(36):
    xx = bx0 + 4 + k * 4.5
    b.append(f'<line x1="{xx:.1f}" y1="{252+(k%3)*4}" x2="{xx+9:.1f}" y2="{262-(k%2)*5}" stroke="#a88a2a" stroke-width="1.5"/>')
for k in range(13):  # pedras
    for j in range(2):
        xx = bx0 + 8 + k * 12.6 + (j * 5); yy = 276 + j * 11
        b.append(f'<ellipse cx="{xx:.1f}" cy="{yy}" rx="7" ry="5.5" fill="#7d7d7d" stroke="#444" stroke-width="1.2"/>')
# gotas e balde
for k in range(5):
    xx = bx0 + 18 + k * 33
    b.append(f'<path d="M{xx} {bot+10} q -3 6 0 9 q 3 -3 0 -9 Z" fill="#7a4a1a"/>')
b.append(f'<path d="M98 336 L 104 386 L 186 386 L 192 336 Z" fill="#fff" stroke="{OUT}" stroke-width="2.5"/>')
b.append(f'<path d="M100 350 L 104 386 L 186 386 L 190 350 Z" fill="#8a5a24"/>')
b.append(lbl(145, 376, "decoada", 11.5, "#fff", True, "middle").replace('stroke="#fff"', 'stroke="#8a5a24"'))
# jarra de agua
b.append(f'<g transform="rotate(-35 262 56)"><rect x="246" y="36" width="40" height="46" rx="6" fill="#fff" stroke="{OUT}" stroke-width="2"/><rect x="248" y="56" width="36" height="24" fill="{AGUA2}"/></g>')
b.append(f'<path d="M244 66 Q 224 72 212 92" fill="none" stroke="{AGUA}" stroke-width="3"/>')
# rotulos
L = [(252, 104, ["água da chuva,", "aos poucos"], AGUA),
     (252, 170, ["CINZA de lenha", "peneirada (até 10 cm", "da borda)"], "#222"),
     (252, 258, ["palha ou capim 5–8 cm"], "#222"),
     (252, 284, ["pedras/cascalho 5–8 cm"], "#222"),
     (252, 304, ["furos no fundo"], "#222")]
for (x, y, arr, cor) in L:
    for i, t in enumerate(arr):
        b.append(lbl(x, y + i * 14, t, 11.5, cor, i == 0))
b.append(lbl(252, 352, "balde de plástico", 11, "#222", True))
b.append(lbl(252, 366, "ou barro (nunca", 11, "#222", True))
b.append(lbl(252, 380, "alumínio)", 11, "#222", True))
b.append(lbl(20, 70, "barril ou balde de 20–200 L", 12, "#222", True))
# testes a direita
b.append('<line x1="452" y1="50" x2="452" y2="410" stroke="#ccc" stroke-width="2"/>')
b.append(text(564, 66, "Teste de força", 14, "#222", True, "middle"))
# copo com ovo
b.append(f'<path d="M486 104 L 492 190 L 560 190 L 566 104" fill="#fff" stroke="{OUT}" stroke-width="2.5"/>')
b.append(f'<path d="M487 128 L 492 190 L 560 190 L 565 128 Z" fill="#a8743a"/>')
b.append(f'<ellipse cx="526" cy="130" rx="15" ry="20" fill="#f6ead2" stroke="{OUT}" stroke-width="2" transform="rotate(-10 526 130)"/>')
b.append(f'<path d="M487 128 L 565 128 L 562 150 L 490 150 Z" fill="#a8743a" opacity="0.9"/>')
b.append(f'<line x1="487" y1="128" x2="565" y2="128" stroke="#5a3a10" stroke-width="2"/>')
b.append(lbl(526, 210, "ovo boia mostrando", 11.5, GREEN, True, "middle"))
b.append(lbl(526, 224, "um pedaço do tamanho", 11.5, GREEN, True, "middle"))
b.append(lbl(526, 238, "de uma moeda = boa", 11.5, GREEN, True, "middle"))
b.append(lines(584, 108, ["afunda:", "fraca"], 11.5, DRED, True))
b.append(lines(584, 150, ["boia muito", "alto: forte", "demais (dilua)"], 11.5, "#555"))
# pena
b.append(f'<path d="M500 290 Q 540 262 600 252" fill="none" stroke="#555" stroke-width="2"/>')
for k in range(9):
    xx = 512 + k * 9; yy = 284 - k * 3.6
    b.append(f'<line x1="{xx}" y1="{yy}" x2="{xx+8}" y2="{yy-14}" stroke="#999" stroke-width="2"/>')
    b.append(f'<line x1="{xx}" y1="{yy}" x2="{xx+12}" y2="{yy+6}" stroke="#999" stroke-width="2"/>')
b.append(lines(470, 318, ["Pena de galinha mergulhada", "se desmancha em minutos:", "decoada forte."], 11.5, "#222"))
b.append(lines(470, 368, ["Fraca? Passe de novo por", "cinza nova ou ferva em", "tacho de ferro para concentrar."], 11.5, "#222"))
b.append(box(8, 420, 664, 66, "#fdecec", RED))
b.append(text(20, 440, "A decoada é cáustica como a soda: óculos e luvas. Olho: água corrente 15–20 min.", 12.5, DRED, True))
b.append(text(20, 458, "Use só cinza de madeira sem tinta, verniz ou cola. Cinza de madeira dura (lenha) é a mais forte.", 12.5))
b.append(text(20, 476, "Rende: ~10 L de cinza dão 3–5 L de decoada forte. As primeiras porções são as mais fortes.", 12.5))
open(D + "barril-lixivia.svg", "w").write(svg(680, 496, "Barril de decoada (lixívia de cinza) — corte", "\n".join(b)))

# =====================================================================
# TEAR DE PENTE-LICO
# =====================================================================
b = []
b.append(text(170, 64, "O pente-liço visto de frente", 13.5, "#222", True, "middle"))
fx0, fx1, fy0, fy1 = 30, 310, 84, 236
b.append(f'<rect x="{fx0}" y="{fy0}" width="{fx1-fx0}" height="{fy1-fy0}" rx="6" fill="{WOOD}" stroke="{OUT}" stroke-width="2.5"/>')
b.append(f'<rect x="{fx0+14}" y="{fy0+14}" width="{fx1-fx0-28}" height="{fy1-fy0-28}" fill="#f6f3ee" stroke="{OUT}" stroke-width="1.5"/>')
slats = [fx0 + 26 + k * 22 for k in range(12)]
for xs in slats:
    b.append(f'<rect x="{xs-3.5}" y="{fy0+14}" width="7" height="{fy1-fy0-28}" fill="#d7b98c" stroke="{OUT}" stroke-width="1.2"/>')
    b.append(f'<circle cx="{xs}" cy="{(fy0+fy1)/2}" r="3.2" fill="#fff" stroke="{OUT}" stroke-width="1"/>')
for xs in slats:   # fio do furo (vermelho)
    b.append(f'<line x1="{xs}" y1="{fy0-14}" x2="{xs}" y2="{(fy0+fy1)/2-3}" stroke="#c0392b" stroke-width="2"/>')
    b.append(f'<line x1="{xs}" y1="{(fy0+fy1)/2+3}" x2="{xs}" y2="{fy1+14}" stroke="#c0392b" stroke-width="2"/>')
for xs in slats[:-1]:   # fio da fenda (azul)
    b.append(f'<line x1="{xs+11}" y1="{fy0-14}" x2="{xs+11}" y2="{fy1+14}" stroke="#2f6ea8" stroke-width="2"/>')
b.append(lbl(36, 258, "azul: fio passa na FENDA (livre)", 11.5, "#2f6ea8", True))
b.append(lbl(36, 274, "vermelho: fio passa no FURO da ripa (preso)", 11.5, "#c0392b", True))
b.append(lbl(36, 290, "1 ripa a cada 5–8 mm = 25–40 fios em 10 cm", 11.5, "#222"))
b.append(lbl(36, 306, "ripas: taquara, palito de picolé, madeira fina", 11.5, "#222"))
# vistas laterais
b.append('<line x1="340" y1="50" x2="340" y2="312" stroke="#ccc" stroke-width="2"/>')
def cala(y0, sobe, titulo, nomes):
    s = text(354, y0 - 50, titulo, 12.5, "#222", True)
    s += f'<rect x="356" y="{y0-8}" width="10" height="16" rx="3" fill="{WOOD}" stroke="{OUT}" stroke-width="1.5"/>'
    s += f'<rect x="652" y="{y0-8}" width="10" height="16" rx="3" fill="{WOOD}" stroke="{OUT}" stroke-width="1.5"/>'
    dh = 32
    hy = y0 - dh if sobe else y0 + dh
    s += f'<rect x="556" y="{min(hy, y0)-14}" width="9" height="{dh+28}" rx="3" fill="#d7b98c" stroke="{OUT}" stroke-width="1.5"/>'
    s += f'<polyline points="366,{y0} 560,{hy} 652,{y0}" fill="none" stroke="#c0392b" stroke-width="2.5"/>'
    s += f'<line x1="366" y1="{y0}" x2="652" y2="{y0}" stroke="#2f6ea8" stroke-width="2.5"/>'
    xs = 490
    my = y0 + (hy - y0) * (xs - 366) / (560 - 366) / 2
    s += f'<ellipse cx="{xs}" cy="{my:.1f}" rx="15" ry="4.5" fill="#a0522d" stroke="{OUT}" stroke-width="1.5"/>'
    ly = y0 + 18 if sobe else y0 - 10
    s += lbl(xs, ly, "lançadeira passa na cala", 10.5, "#6b3a10", True, "middle")
    s += lbl(572, y0 + (14 if sobe else -20), "pente", 10.5, "#222", True)
    if nomes:
        s += lbl(380, y0 + 36, "lado do tecido", 10.5, "#555", False) + lbl(648, y0 + 36, "urdume", 10.5, "#555", False, "end")
    return s
b.append(cala(124, True, "Pente PARA CIMA: abre a 1ª cala", True))
b.append(cala(258, False, "Pente PARA BAIXO: abre a 2ª cala", False))

# tear de cintura
b.append('<line x1="8" y1="322" x2="672" y2="322" stroke="#ccc" stroke-width="2"/>')
b.append(text(340, 344, "Tear de cintura com pente-liço (sem armação)", 13.5, "#222", True, "middle"))
b.append(f'<rect x="0" y="470" width="680" height="16" fill="{SOLO}"/><line x1="0" y1="470" x2="680" y2="470" stroke="#6b4f2a" stroke-width="2"/>')
b.append(f'<rect x="640" y="352" width="26" height="118" fill="{WOOD}" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<line x1="640" y1="404" x2="606" y2="398" stroke="#555" stroke-width="2"/><line x1="640" y1="404" x2="606" y2="426" stroke="#555" stroke-width="2"/>')
b.append(f'<rect x="600" y="394" width="8" height="36" rx="3" fill="{WOOD}" stroke="{OUT}" stroke-width="1.5"/>')
for k in range(7):
    ya = 398 + k * 5; yb = 400 + k * 4
    b.append(f'<line x1="604" y1="{ya}" x2="300" y2="{yb}" stroke="#c9a46a" stroke-width="1.6"/>')
b.append(f'<rect x="200" y="398" width="100" height="30" fill="#e9d2a2" stroke="#8a6a3a" stroke-width="1.5"/>')
for k in range(9):
    b.append(f'<line x1="{206+k*11}" y1="398" x2="{206+k*11}" y2="428" stroke="#c9a46a" stroke-width="1"/>')
b.append(f'<rect x="430" y="380" width="9" height="66" rx="3" fill="#d7b98c" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<rect x="192" y="392" width="10" height="42" rx="3" fill="{WOOD}" stroke="{OUT}" stroke-width="1.5"/>')
# tecelao sentado inclinado para tras
b.append(limb([(132, 452), (196, 460), (238, 462)], 20, "#6f8aa3"))
b.append(limb([(134, 448), (104, 380)], 34, "#6f8aa3"))
b.append(head(96, 352, 20, "#f2c9a5", 1, 0.1))
b.append(limb([(108, 392), (150, 410), (188, 410)], 11, "#6f8aa3")); b.append(hand(192, 410, 8))
b.append(f'<path d="M196 394 L 128 430 M196 432 L 130 444" stroke="#7a4a1a" stroke-width="3"/>')
b.append(f'<path d="M126 428 Q 112 438 128 448" fill="none" stroke="#7a4a1a" stroke-width="7"/>')
b += [lbl(612, 344, "árvore/poste", 11, "#222", True, "middle"), lbl(520, 392, "urdume", 11, "#222", True, "middle"),
      lbl(434, 372, "pente-liço", 11, "#222", True, "middle"), lbl(250, 392, "tecido pronto", 11, "#222", True, "middle"),
      lbl(150, 486, "cinto nas costas: você estica a urdidura inclinando o corpo", 11, "#222", True)]
b.append(box(8, 494, 664, 66, "#eef5ff", "#3f6d9e"))
b.append(text(20, 514, "Tecer: pente para cima → passe a lançadeira → bata o fio com o pente → pente para baixo →", 12.5))
b.append(text(20, 532, "passe de volta → bata. Deixe o fio da trama em arco (não esticado) antes de bater, senão o", 12.5))
b.append(text(20, 550, "tecido vai estreitando. Fios das bordas firmes, mas sem puxar.", 12.5))
open(D + "tear-pente-lico.svg", "w").write(svg(680, 570, "Tear de pente-liço", "\n".join(b)))

# =====================================================================
# CERAMICA: queima em buraco (corte)
# =====================================================================
def pote(cx, base_y, w, h, boca_baixo=True, cor="#c87f4a"):
    # pote de boca para baixo: corpo arredondado, boca no chao
    if boca_baixo:
        return (f'<path d="M{cx-w*0.32} {base_y} C {cx-w*0.62} {base_y-h*0.35}, {cx-w*0.5} {base_y-h}, {cx} {base_y-h} '
                f'C {cx+w*0.5} {base_y-h}, {cx+w*0.62} {base_y-h*0.35}, {cx+w*0.32} {base_y} Z" fill="{cor}" stroke="{OUT}" stroke-width="2.5"/>')
    return ""
b = []
b.append(f'<rect x="0" y="200" width="420" height="200" fill="{SOLO}"/><line x1="0" y1="200" x2="420" y2="200" stroke="#6b4f2a" stroke-width="3"/>')
b.append(f'<path d="M50 200 L 90 296 L 330 296 L 370 200 Z" fill="#5a4a3a" stroke="{OUT}" stroke-width="2.5"/>')
b.append(f'<path d="M86 286 L 90 296 L 330 296 L 334 286 Z" fill="#c8a878"/>')   # serragem/esterco
random.seed(5)
for k in range(60):
    xx = random.uniform(92, 328); yy = random.uniform(287, 295)
    b.append(f'<circle cx="{xx:.1f}" cy="{yy:.1f}" r="1.2" fill="#8a6a40"/>')
for (cx, w, h) in ((140, 70, 56), (210, 80, 66), (284, 66, 50)):
    b.append(pote(cx, 286, w, h))
# combustivel em volta e por cima
for k in range(16):
    x1 = 70 + k * 18; y1 = 204 + (k % 3) * 8
    b.append(f'<line x1="{x1}" y1="{y1}" x2="{x1+40}" y2="{y1+30+(k%4)*6}" stroke="{WOOD}" stroke-width="5" stroke-linecap="round"/>')
for (ex, ey) in ((100, 262), (330, 262), (180, 214), (250, 212)):
    b.append(f'<ellipse cx="{ex}" cy="{ey}" rx="16" ry="6" fill="#6b5a3a" stroke="{OUT}" stroke-width="1.5"/>')
# pilha de lenha acima
for k in range(9):
    xa = 90 + k * 30
    b.append(f'<line x1="{xa}" y1="198" x2="{210+(xa-210)*0.2:.0f}" y2="92" stroke="{WOOD}" stroke-width="9" stroke-linecap="round"/>')
    b.append(f'<line x1="{xa}" y1="198" x2="{210+(xa-210)*0.2:.0f}" y2="92" stroke="#a87443" stroke-width="4" stroke-linecap="round"/>')
for (fx, fy, sc) in ((150, 196, 1.1), (210, 186, 1.5), (270, 196, 1.1), (180, 150, 1.0), (240, 150, 1.0), (210, 120, 1.0)):
    b.append(chama(fx, fy, sc))
b.append(lbl(380, 230, "40–50 cm", 11.5, "#222", True))
b.append(f'<line x1="372" y1="204" x2="372" y2="294" stroke="#222" stroke-width="1.5"/>')
b.append(lbl(210, 318, "≈ 1 m de largura", 11.5, "#222", True, "middle"))
b.append(lbl(14, 330, "fundo: serragem, palha", 11, "#222", True)); b.append(lbl(14, 344, "ou esterco seco", 11, "#222", True))
b.append(f'<line x1="70" y1="326" x2="96" y2="292" stroke="#555" stroke-width="1.5"/>')
b.append(lbl(160, 356, "potes BEM SECOS, de boca para baixo,", 11, "#222", True)); b.append(lbl(160, 370, "cobertos de gravetos, casca e esterco seco", 11, "#222", True))
b.append(lbl(14, 100, "pilha de lenha", 11.5, "#222", True)); b.append(lbl(14, 114, "em forma de oca", 11.5, "#222", True))
# passos
b.append('<line x1="430" y1="50" x2="430" y2="396" stroke="#ccc" stroke-width="2"/>')
steps = [("Esquente devagar", ["Potes ao lado da fogueira", "1–2 h, virando, até ficarem", "quentes demais para tocar."]),
         ("Monte o buraco", ["Fundo com serragem/esterco,", "potes, gravetos e lenha por", "cima (como no desenho)."]),
         ("Queime 2–4 h", ["Mantenha fogo forte. Os", "potes devem brilhar vermelho", "escuro: 600–800 °C."]),
         ("Abafe e espere", ["Cubra com cacos, chapas e", "terra. Espere esfriar sozinho", "(12 h ou mais)."])]
for i, (t, arr) in enumerate(steps):
    y = 70 + i * 82
    b.append(num(452, y, i + 1)); b.append(text(472, y + 5, t, 13, "#222", True))
    b.append(lines(446, y + 24, arr, 11.5))
b.append(box(8, 404, 664, 50, "#fdecec", RED))
b.append(text(20, 424, "Pote úmido explode no fogo: seque 1–3 semanas à sombra. Perdas de 10–30% são normais.", 12.5, DRED, True))
b.append(text(20, 442, "Abaixo de ~600 °C o barro NÃO vira cerâmica (desmancha na água). Teste um caco fervendo.", 12.5))
open(D + "queima-em-buraco.svg", "w").write(svg(680, 464, "Queima de cerâmica em buraco (fogueira)", "\n".join(b)))

# =====================================================================
# CERAMICA: forno simples de tijolos (corte)
# =====================================================================
def tijolos(x, y, w, h, bw=30, bh=12):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#b5523b" stroke="{OUT}" stroke-width="2"/>'
    r = 0; yy = y
    while yy < y + h - 1:
        s += f'<line x1="{x}" y1="{yy}" x2="{x+w}" y2="{yy}" stroke="#7a2e1e" stroke-width="1"/>'
        off = (bw / 2) if r % 2 else 0
        xx = x + off
        while xx < x + w:
            s += f'<line x1="{xx:.0f}" y1="{yy}" x2="{xx:.0f}" y2="{min(yy+bh, y+h)}" stroke="#7a2e1e" stroke-width="1"/>'
            xx += bw
        yy += bh; r += 1
    return s
b = []
G = 440
b.append(f'<rect x="0" y="{G}" width="680" height="20" fill="{SOLO}"/><line x1="0" y1="{G}" x2="680" y2="{G}" stroke="#6b4f2a" stroke-width="3"/>')
# paredes
b.append(tijolos(70, 110, 30, G - 110)); b.append(tijolos(330, 110, 30, G - 110))
# fornalha (interior escuro) e boca
b.append(f'<rect x="100" y="340" width="230" height="{G-340}" fill="#3a2a22"/>')
b.append(f'<rect x="66" y="384" width="38" height="{G-384}" fill="#3a2a22"/>')
b.append(f'<rect x="66" y="376" width="38" height="10" fill="#7d7d7d" stroke="{OUT}" stroke-width="1.5"/>')
for k in range(4):
    b.append(f'<line x1="{20+k*8}" y1="{428-k*7}" x2="{170+k*10}" y2="{420-k*6}" stroke="{WOOD}" stroke-width="7" stroke-linecap="round"/>')
for (fx, fy, sc) in ((150, 430, 1.2), (200, 432, 1.5), (250, 430, 1.3), (295, 432, 1.0)):
    b.append(chama(fx, fy, sc))
# grelha
for k in range(6):
    b.append(f'<rect x="{100+k*40}" y="326" width="26" height="14" fill="#b5523b" stroke="{OUT}" stroke-width="1.5"/>')
# camara
b.append(f'<rect x="100" y="110" width="230" height="216" fill="#f1e6d6"/>')
for (cx, by, w, h) in ((140, 326, 56, 50), (215, 326, 64, 58), (290, 326, 56, 50), (170, 266, 54, 46), (255, 266, 54, 46)):
    b.append(pote(cx, by, w, h))
b.append(f'<rect x="150" y="266" width="130" height="6" fill="#b5523b" stroke="{OUT}" stroke-width="1"/>')
# topo com cacos
for k in range(6):
    xa = 74 + k * 50
    b.append(f'<path d="M{xa} 110 L {xa+30} 104 L {xa+34} 112 L {xa+4} 116 Z" fill="#c87f4a" stroke="{OUT}" stroke-width="1.5"/>')
# setas de tiragem
b.append(arrow(30, 412, 64, 412, AGUA, 4))
for (x1, y1, x2, y2) in ((113, 350, 113, 300), (193, 350, 193, 300), (273, 350, 273, 300), (150, 240, 150, 160), (215, 230, 215, 150), (285, 240, 285, 160),
                         (122, 100, 122, 66), (222, 100, 222, 60), (322, 100, 322, 66)):
    b.append(arrow(x1, y1, x2, y2, "#f08c00", 3.5))
# rotulos
R = [(380, 80, ["saída do calor: cubra com cacos,", "deixando frestas (tiragem)"]),
     (380, 190, ["câmara: potes secos, com", "folga de 2–3 dedos entre eles"]),
     (380, 318, ["grelha: tijolos com vãos", "de 5–8 cm"]),
     (380, 384, ["fornalha: lenha seca e fina;", "boca de 30 × 30 cm"])]
for (x, y, arr) in R:
    b.append(lines(x, y, arr, 11.5, "#222", False))
    b.append(f'<line x1="{x-6}" y1="{y-4}" x2="{x-24}" y2="{y-4}" stroke="#555" stroke-width="1.5"/>')
b.append(lbl(14, 400, "ar", 12, AGUA, True))
b.append(lbl(215, 104, "", 11))
b.append(lbl(215, 96, "60–80 cm por dentro", 11, "#222", True, "middle").replace("y=\"96\"", "y=\"128\""))
b.append(lbl(84, 106, "", 11))
b.append(lines(380, 240, ["paredes: 2 tijolos (20–25 cm)", "assentados com barro + areia"], 11.5, "#222"))
# escala de cor
b.append(text(590, 300, "Cor do fogo", 12, "#222", True, "middle"))
cores = [("#5a1a10", "~550 °C vermelho escuro"), ("#a01e10", "~700 °C vermelho"), ("#e0401a", "~850 °C cereja"), ("#f08c20", "~950 °C laranja"), ("#ffd040", "~1100 °C amarelo")]
for i, (c, t) in enumerate(cores):
    b.append(f'<rect x="530" y="{310+i*22}" width="22" height="18" fill="{c}" stroke="{OUT}" stroke-width="1"/>')
    b.append(text(558, 324 + i * 22, t, 10.5, "#222"))
b.append(box(8, 466, 664, 86, "#eef5ff", "#3f6d9e"))
b.append(text(20, 486, "Queima: 1) fogo pequeno na boca 2–3 h (secar; até ~100–200 °C); 2) aumente aos poucos por 2–3 h;", 12.5))
b.append(text(20, 504, "3) fogo forte 2–4 h até o brilho cereja (800–900 °C); mantenha 30–60 min; 4) feche boca e topo", 12.5))
b.append(text(20, 522, "e espere esfriar 12–24 h. Abrir quente racha tudo. Lenha: ~1 a 2 m³ por queima (forno pequeno).", 12.5))
b.append(text(20, 540, "Cimento comum não aguenta o calor: use tijolo e barro. Afaste de casas e de mato seco.", 12.5, DRED, True))
open(D + "forno-tijolo.svg", "w").write(svg(680, 562, "Forno simples de tijolos para cerâmica (corte)", "\n".join(b)))
print("ok")
