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
print("ok")
