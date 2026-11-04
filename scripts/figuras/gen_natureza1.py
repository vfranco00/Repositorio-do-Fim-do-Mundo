import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
import math
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "11-natureza-e-desastres", "img") + "/"
os.makedirs(D, exist_ok=True)
WOOD = "#8b5a2b"; AGUA = "#4a90d9"; AGUA_C = "#cfe6fb"; SOLO = "#e8d3b0"; VERDE = "#2b8a3e"; PERIGO = "#d62828"; PERIGO2 = "#b3001b"


def pessoa_cima(cx, cy, cor=SOC, mochila=True):
    """Pessoa vista de cima, de frente para a ESQUERDA (rio acima)."""
    s = ""
    if mochila:
        s += f'<rect x="{cx+5}" y="{cy-11}" width="12" height="22" rx="3" fill="#7a6a3a" stroke="{OUT}" stroke-width="2"/>'
    s += f'<ellipse cx="{cx}" cy="{cy}" rx="8" ry="18" fill="{cor}" stroke="{OUT}" stroke-width="2.5"/>'
    s += f'<circle cx="{cx-2}" cy="{cy}" r="8.5" fill="{SKIN}" stroke="{OUT}" stroke-width="2"/>'
    s += f'<circle cx="{cx-10}" cy="{cy}" r="2.6" fill="{SKIN}" stroke="{OUT}" stroke-width="1.5"/>'  # nariz: rosto p/ esquerda
    return s


def setas_corrente(x0, x1, ys, cor="#7fb2e5"):
    s = ""
    for y in ys:
        x = x0
        while x + 50 < x1:
            s += arrow(x, y, x + 40, y, cor, 2.5)
            x += 90
    return s


# =====================================================================
# TRAVESSIA DE RIO
# =====================================================================
b = []
b.append(text(340, 56, "Rio visto de cima. A água corre da esquerda para a direita →", 13, "#333", False, "middle"))
# margens e rio (cena CERTO)
b.append(f'<rect x="10" y="68" width="660" height="42" fill="{SOLO}"/>')
b.append(f'<rect x="10" y="110" width="660" height="190" fill="{AGUA_C}"/>')
b.append(f'<rect x="10" y="300" width="660" height="40" fill="{SOLO}"/>')
b.append(f'<line x1="10" y1="110" x2="670" y2="110" stroke="#6b4f2a" stroke-width="2.5"/>')
b.append(f'<line x1="10" y1="300" x2="670" y2="300" stroke="#6b4f2a" stroke-width="2.5"/>')
b.append(setas_corrente(20, 660, (126, 286)))
b.append(f'<line x1="340" y1="112" x2="340" y2="298" stroke="#9bbbd8" stroke-width="2" stroke-dasharray="5 5"/>')
b.append(f'<rect x="14" y="72" width="76" height="24" rx="6" fill="{VERDE}"/>' + text(52, 89, "CERTO", 14, "#fff", True, "middle"))
# --- sozinho
b.append(text(100, 90, "Sozinho", 13.5, "#222", True))
b.append(f'<path d="M110 104 L 290 312" fill="none" stroke="{VERDE}" stroke-width="3.5" stroke-dasharray="9 6"/>')
b.append(arrow(276, 296, 294, 318, VERDE, 3.5))
b.append(f'<line x1="178" y1="196" x2="152" y2="198" stroke="{WOOD}" stroke-width="5" stroke-linecap="round"/>')
b.append(f'<circle cx="149" cy="198" r="5" fill="{WOOD}" stroke="{OUT}" stroke-width="1.5"/>')
b.append(pessoa_cima(190, 196))
b += [text(30, 152, "rosto virado", 11.5, "#222", True), text(30, 166, "para rio acima", 11.5, "#222", True),
      text(30, 226, "bastão do lado", 11.5), text(30, 240, "de cima = 3º apoio", 11.5)]
b += [text(226, 168, "anda de lado,", 11.5, "#222", True), text(226, 182, "em DIAGONAL,", 11.5, VERDE, True),
      text(226, 196, "A FAVOR da", 11.5, VERDE, True), text(226, 210, "correnteza", 11.5, VERDE, True)]
b += [text(30, 326, "pés arrastando, um passo de cada vez", 11.5, "#222")]
# --- grupo
b.append(text(352, 90, "Em grupo: fila no sentido da água", 13.5, "#222", True))
gx = [420, 476, 532]
for i, x in enumerate(gx):
    b.append(pessoa_cima(x, 205, ["#ef8a2b", "#6f8aa3", "#6f8aa3"][i]))
for x in gx[1:]:  # bracos segurando a mochila de quem esta na frente
    for (ya, yb_) in ((196, 198), (214, 212)):
        b.append(f'<line x1="{x-8}" y1="{ya}" x2="{x-38}" y2="{yb_}" stroke="{OUT}" stroke-width="5" stroke-linecap="round"/>')
        b.append(f'<line x1="{x-8}" y1="{ya}" x2="{x-38}" y2="{yb_}" stroke="{SKIN}" stroke-width="3" stroke-linecap="round"/>')
b.append(f'<line x1="408" y1="206" x2="384" y2="208" stroke="{WOOD}" stroke-width="5" stroke-linecap="round"/>')
b.append(f'<circle cx="381" cy="208" r="5" fill="{WOOD}" stroke="{OUT}" stroke-width="1.5"/>')
b += [text(352, 148, "o MAIS FORTE na frente", 11.5, "#222", True), text(352, 162, "(rio acima): quebra a água", 11.5),
      text(556, 166, "os outros seguram", 11.5), text(556, 180, "a cintura ou a", 11.5), text(556, 194, "mochila do", 11.5), text(556, 208, "da frente", 11.5)]
b.append(f'<path d="M476 232 L 520 296" fill="none" stroke="{VERDE}" stroke-width="3.5" stroke-dasharray="9 6"/>')
b.append(arrow(512, 284, 526, 306, VERDE, 3.5))
b += [text(546, 250, "todos andam", 11.5, "#222", True), text(546, 264, "juntos, de lado,", 11.5, "#222", True), text(546, 278, "no mesmo ritmo", 11.5, "#222", True)]
b += [text(352, 326, "nunca amarre ninguém ao outro", 11.5, "#222")]

# ---------- ERRADO ----------
y0 = 356
b.append(f'<rect x="14" y="{y0}" width="84" height="24" rx="6" fill="{PERIGO}"/>' + text(56, y0+17, "ERRADO", 14, "#fff", True, "middle"))
pw = 212


def mini_rio(x, y, w=200, h=96):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="14" fill="{SOLO}"/>'
    s += f'<rect x="{x}" y="{y+14}" width="{w}" height="{h-28}" fill="{AGUA_C}"/>'
    s += f'<rect x="{x}" y="{y+h-14}" width="{w}" height="14" fill="{SOLO}"/>'
    s += arrow(x+10, y+24, x+46, y+24, "#7fb2e5", 2.5) + arrow(x+10, y+h-22, x+46, y+h-22, "#7fb2e5", 2.5)
    return s


def xis(cx, cy, r=13):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r+3}" fill="#fff" stroke="{PERIGO}" stroke-width="3"/>'
            f'<line x1="{cx-r*0.55}" y1="{cy-r*0.55}" x2="{cx+r*0.55}" y2="{cy+r*0.55}" stroke="{PERIGO}" stroke-width="4"/>'
            f'<line x1="{cx+r*0.55}" y1="{cy-r*0.55}" x2="{cx-r*0.55}" y2="{cy+r*0.55}" stroke="{PERIGO}" stroke-width="4"/>')


ym = y0 + 32
# 1) contra a correnteza
x = 14
b.append(mini_rio(x, ym))
b.append(f'<path d="M{x+170} {ym+8} L {x+90} {ym+92}" fill="none" stroke="{PERIGO}" stroke-width="3" stroke-dasharray="7 5"/>')
b.append(arrow(x+100, ym+82, x+88, ym+95, PERIGO, 3))
b.append(pessoa_cima(x+132, ym+50, "#6f8aa3", False))
b.append(xis(x+182, ym+64))
b += [text(x, ym+116, "Subir em diagonal contra", 11.5, "#222", True), text(x, ym+130, "a água ou dar as costas", 11.5, "#222", True),
      text(x, ym+144, "para ela: cansa e derruba.", 11.5)]
# 2) acima de cachoeira / galhada
x = 14 + pw + 8
b.append(mini_rio(x, ym))
b.append(f'<line x1="{x+70}" y1="{ym+8}" x2="{x+70}" y2="{ym+92}" stroke="{PERIGO}" stroke-width="3" stroke-dasharray="7 5"/>')
b.append(pessoa_cima(x+70, ym+50, "#6f8aa3", False))
# galhada (tronco caido) e cachoeira rio abaixo
b.append(f'<line x1="{x+118}" y1="{ym+20}" x2="{x+150}" y2="{ym+70}" stroke="{WOOD}" stroke-width="7" stroke-linecap="round"/>')
for (a, c) in ((ym+30, 8), (ym+44, -10), (ym+58, 9)):
    b.append(f'<line x1="{x+118+(a-ym-20)*0.64:.0f}" y1="{a}" x2="{x+118+(a-ym-20)*0.64+c:.0f}" y2="{a-9}" stroke="{WOOD}" stroke-width="3"/>')
for i in range(5):
    yy = ym + 20 + i * 13
    b.append(f'<path d="M{x+168} {yy} l8 4 l-8 4 l8 4" fill="none" stroke="#fff" stroke-width="2.5"/>')
b.append(f'<rect x="{x+180}" y="{ym+14}" width="20" height="68" fill="#9a9a9a"/>')
b.append(xis(x+36, ym+64))
b += [text(x+104, ym+11, "galhada", 10.5, "#5a3a10", True), text(x+168, ym+11, "queda", 10.5, "#444", True)]
b += [text(x, ym+116, "Atravessar logo acima de", 11.5, "#222", True), text(x, ym+130, "galhada, corredeira ou", 11.5, "#222", True),
      text(x, ym+144, "cachoeira: se cair, a água", 11.5), text(x, ym+158, "leva você para lá.", 11.5)]
# 3) amarrado na corda
x = 14 + 2 * (pw + 8)
b.append(mini_rio(x, ym))
b.append(f'<rect x="{x+20}" y="{ym+2}" width="8" height="10" fill="{WOOD}" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<path d="M{x+24} {ym+8} Q {x+40} {ym+40} {x+92} {ym+52}" fill="none" stroke="#c8a000" stroke-width="3"/>')
b.append(pessoa_cima(x+100, ym+52, "#6f8aa3", False))
b.append(f'<path d="M{x+104} {ym+60} q 16 10 30 4" fill="none" stroke="{AGUA}" stroke-width="2.5"/>')
b.append(xis(x+168, ym+50))
b += [text(x, ym+116, "Corda AMARRADA no corpo:", 11.5, "#222", True), text(x, ym+130, "a correnteza puxa você", 11.5),
      text(x, ym+144, "para baixo da água.", 11.5), text(x, ym+158, "Corda só como corrimão.", 11.5, VERDE, True)]
# regras
yb = ym + 172
b.append(box(14, yb, 652, 82, "#fdecec", PERIGO))
b += [text(28, yb+21, "Água acima do joelho e correndo forte = perigo. Acima da cintura = NÃO atravesse.", 12.5, PERIGO2, True),
      text(28, yb+40, "Rio cheio, barrento, com galhos descendo: ESPERE baixar (riacho baixa em horas).", 12.5),
      text(28, yb+59, "Abra as fivelas da mochila (barrigueira e peito) para soltá-la se cair. Vá calçado.", 12.5),
      text(28, yb+76, "Teste: jogue um galho. Se ele anda mais rápido do que você caminha, é forte demais.", 12.5)]
H = yb + 92
open(D + "travessia-rio.svg", "w").write(svg(680, H, "Como atravessar um rio a pé (visto de cima)", "\n".join(b)))


# =====================================================================
# COVO DE GARRAFA PET
# =====================================================================
def garrafa_em_pe(cx, top, sc=1.0, corte=None):
    """Garrafa PET de 2 L em pé. top = y da tampa."""
    r = 24 * sc
    t = top
    p = (f'M{cx-6*sc} {t+10*sc} L{cx-6*sc} {t+20*sc} C{cx-8*sc} {t+34*sc} {cx-r} {t+40*sc} {cx-r} {t+56*sc} '
         f'L{cx-r} {t+140*sc} Q{cx-r} {t+148*sc} {cx-r+8*sc} {t+148*sc} L{cx+r-8*sc} {t+148*sc} Q{cx+r} {t+148*sc} {cx+r} {t+140*sc} '
         f'L{cx+r} {t+56*sc} C{cx+r} {t+40*sc} {cx+8*sc} {t+34*sc} {cx+6*sc} {t+20*sc} L{cx+6*sc} {t+10*sc} Z')
    s = f'<path d="{p}" fill="#eef7ff" stroke="{OUT}" stroke-width="2.5"/>'
    s += f'<rect x="{cx-8*sc}" y="{t}" width="{16*sc}" height="{10*sc}" rx="2" fill="#3f6d9e" stroke="{OUT}" stroke-width="2"/>'
    return s


b = []
# Painel 1 - cortar
b.append(text(20, 62, "1. Corte a garrafa", 14, "#222", True))
b.append(garrafa_em_pe(90, 78))
b.append(f'<line x1="54" y1="134" x2="126" y2="134" stroke="{PERIGO}" stroke-width="3" stroke-dasharray="6 4"/>')
b.append(f'<path d="M130 134 l10 -6 l0 12 z" fill="{PERIGO}"/>')
b += [text(146, 120, "corte onde o", 12, PERIGO2, True), text(146, 135, "\"ombro\" termina", 12, PERIGO2, True),
      text(146, 150, "(~1/3 de cima,", 12), text(146, 165, "uns 10 cm da boca)", 12)]
b += [text(146, 192, "garrafa PET de 2 L", 12, "#444"), text(146, 207, "(ou galão de 5 L para", 12, "#444"), text(146, 222, "peixes maiores)", 12, "#444")]
# Painel 2 - inverter
b.append(text(352, 62, "2. Tire a tampa e vire o funil", 14, "#222", True))
# corpo
cx = 420
b.append(f'<path d="M{cx-24} 168 L{cx-24} 226 Q{cx-24} 234 {cx-16} 234 L{cx+16} 234 Q{cx+24} 234 {cx+24} 226 L{cx+24} 168" fill="#eef7ff" stroke="{OUT}" stroke-width="2.5"/>')
b.append(f'<ellipse cx="{cx}" cy="168" rx="24" ry="5" fill="#dbeefd" stroke="{OUT}" stroke-width="2"/>')
# funil invertido (boca para baixo)
b.append(f'<path d="M{cx-24} 96 L{cx+24} 96 C{cx+24} 112 {cx+8} 118 {cx+6} 132 L{cx+6} 142 L{cx-6} 142 L{cx-6} 132 C{cx-8} 118 {cx-24} 112 {cx-24} 96 Z" fill="#eef7ff" stroke="{OUT}" stroke-width="2.5"/>')
b.append(f'<ellipse cx="{cx}" cy="96" rx="24" ry="5" fill="#dbeefd" stroke="{OUT}" stroke-width="2"/>')
b.append(arrow(cx+40, 112, cx+40, 160, "#555", 3))
b += [text(476, 104, "a parte de cima entra", 12, "#222", True), text(476, 119, "de cabeça para baixo", 12, "#222", True),
      text(476, 134, "dentro do corpo, como", 12), text(476, 149, "um funil", 12),
      text(476, 180, "o peixe entra pela boca", 12), text(476, 195, "larga e não acha a saída", 12), text(476, 210, "estreita", 12)]
b.append(f'<line x1="340" y1="48" x2="340" y2="240" stroke="#ccc" stroke-width="2"/>')
b.append(f'<line x1="14" y1="248" x2="666" y2="248" stroke="#ccc" stroke-width="2"/>')


def covo_deitado(x0, yc, boca_esq=True, sc=1.0):
    """Covo montado, deitado. x0 = borda da boca. Comprimento ~190."""
    r = 26 * sc; L = 190 * sc
    s = ""
    if boca_esq:
        xb = x0 + L
        s += (f'<path d="M{x0} {yc-r} L{xb-10} {yc-r} Q{xb} {yc-r} {xb} {yc-r+10} L{xb} {yc+r-10} Q{xb} {yc+r} {xb-10} {yc+r} L{x0} {yc+r}" '
              f'fill="#eef7ff" stroke="{OUT}" stroke-width="2.5"/>')
        s += f'<ellipse cx="{x0}" cy="{yc}" rx="6" ry="{r}" fill="#dbeefd" stroke="{OUT}" stroke-width="2"/>'
        s += (f'<path d="M{x0} {yc-r} C{x0+20*sc} {yc-r} {x0+30*sc} {yc-8} {x0+50*sc} {yc-6} L{x0+62*sc} {yc-6} '
              f'M{x0} {yc+r} C{x0+20*sc} {yc+r} {x0+30*sc} {yc+8} {x0+50*sc} {yc+6} L{x0+62*sc} {yc+6}" fill="none" stroke="{OUT}" stroke-width="2.5"/>')
        s += f'<line x1="{x0+62*sc}" y1="{yc-6}" x2="{x0+62*sc}" y2="{yc+6}" stroke="{OUT}" stroke-width="2"/>'
        furos = [x0 + (80 + 22*i)*sc for i in range(5)]
        pontos = [x0 + 4, x0 + 4]
    else:
        xb = x0 - L
        s += (f'<path d="M{x0} {yc-r} L{xb+10} {yc-r} Q{xb} {yc-r} {xb} {yc-r+10} L{xb} {yc+r-10} Q{xb} {yc+r} {xb+10} {yc+r} L{x0} {yc+r}" '
              f'fill="#eef7ff" stroke="{OUT}" stroke-width="2.5"/>')
        s += f'<ellipse cx="{x0}" cy="{yc}" rx="6" ry="{r}" fill="#dbeefd" stroke="{OUT}" stroke-width="2"/>'
        s += (f'<path d="M{x0} {yc-r} C{x0-20*sc} {yc-r} {x0-30*sc} {yc-8} {x0-50*sc} {yc-6} L{x0-62*sc} {yc-6} '
              f'M{x0} {yc+r} C{x0-20*sc} {yc+r} {x0-30*sc} {yc+8} {x0-50*sc} {yc+6} L{x0-62*sc} {yc+6}" fill="none" stroke="{OUT}" stroke-width="2.5"/>')
        s += f'<line x1="{x0-62*sc}" y1="{yc-6}" x2="{x0-62*sc}" y2="{yc+6}" stroke="{OUT}" stroke-width="2"/>'
        furos = [x0 - (80 + 22*i)*sc for i in range(5)]
    for fx in furos:
        s += f'<circle cx="{fx:.0f}" cy="{yc-r+8}" r="2.5" fill="{OUT}"/><circle cx="{fx+9:.0f}" cy="{yc+r-8}" r="2.5" fill="{OUT}"/>'
    return s


def peixe(cx, cy, dirx=-1, sc=1.0, cor="#9aa7b0"):
    L = 30 * sc; h = 9 * sc
    hx = cx + dirx * L / 2; tx = cx - dirx * L / 2
    s = (f'<path d="M{hx} {cy} Q{cx} {cy-h*1.4} {tx} {cy} Q{cx} {cy+h*1.4} {hx} {cy} Z" fill="{cor}" stroke="{OUT}" stroke-width="1.8"/>'
         f'<path d="M{tx} {cy} l{-dirx*9*sc} {-7*sc} l0 {14*sc} z" fill="{cor}" stroke="{OUT}" stroke-width="1.8"/>'
         f'<circle cx="{hx - dirx*6*sc}" cy="{cy-2*sc}" r="{1.8*sc}" fill="{OUT}"/>')
    return s


# Painel 3 - montar
b.append(text(20, 274, "3. Encaixe, prenda e fure", 14, "#222", True))
b.append(covo_deitado(34, 334, sc=0.85))
for yy in (312, 356):
    b.append(f'<path d="M30 {yy-4} l8 8 M38 {yy-4} l-8 8" stroke="#c8a000" stroke-width="2.5"/>')
b.append('<ellipse cx="150" cy="342" rx="16" ry="8" fill="#e9c46a" stroke="#1e1e1e" stroke-width="1.8"/>')
b += [text(20, 382, "prenda em 3–4 pontos", 11.5, "#a06a00", True), text(20, 396, "com arame ou barbante", 11.5, "#a06a00", True), text(20, 410, "(os X amarelos)", 11.5, "#a06a00")]
b += [text(212, 298, "furos de ~5 mm", 11.5, "#222", True), text(212, 312, "(prego quente):", 11.5),
      text(212, 326, "a água passa e", 11.5), text(212, 340, "a garrafa afunda", 11.5)]
b += [text(212, 364, "isca dentro:", 11.5, "#222", True), text(212, 378, "massa, pão,", 11.5), text(212, 392, "ração, milho", 11.5), text(212, 406, "ou vísceras", 11.5)]
b.append(f'<line x1="340" y1="258" x2="340" y2="420" stroke="#ccc" stroke-width="2"/>')
# Painel 4 - na agua (agua corre p/ direita; boca virada rio abaixo = direita)
b.append(text(352, 274, "4. Na água: boca virada rio abaixo", 14, "#222", True))
b.append(f'<rect x="350" y="290" width="316" height="20" fill="{SOLO}"/>')
b.append(f'<rect x="350" y="310" width="316" height="84" fill="{AGUA_C}"/>')
b.append(f'<rect x="350" y="394" width="316" height="22" fill="#b89b6e"/>')
b.append(arrow(360, 322, 400, 322, "#7fb2e5", 2.5) + arrow(540, 322, 580, 322, "#7fb2e5", 2.5))
b.append(text(410, 326, "correnteza", 11, "#3f6d9e"))
# covo pequeno com boca p/ direita
sc = 0.62
b.append(covo_deitado(530, 377, boca_esq=False, sc=sc))
b.append('<ellipse cx="452" cy="358" rx="13" ry="7" fill="#8a8a8a" stroke="#1e1e1e" stroke-width="1.8"/>')
b.append(peixe(590, 370, -1, 0.8))
b.append(peixe(636, 382, -1, 0.7))
for i in range(3):
    b.append(f'<path d="M{540+i*4} {362+i*10} q 10 -4 20 0 t 20 0 t 20 0" fill="none" stroke="#c8a000" stroke-width="1.5" stroke-dasharray="3 3"/>')
# estaca e corda
b.append(f'<rect x="368" y="284" width="8" height="26" fill="{WOOD}" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<path d="M372 302 Q 378 360 418 372" fill="none" stroke="#555" stroke-width="2"/>')
b += [text(388, 304, "corda presa numa estaca na margem", 11, "#222")]
b += [text(560, 346, "o cheiro da isca", 10.5, "#8a6a00"), text(560, 357, "desce com a água", 10.5, "#8a6a00")]
b += [text(358, 410, "30 cm a 1 m de fundo · pedra para não rolar", 10.5, "#fff", True)]
# rodape
b.append(box(14, 428, 652, 64, "#eef7ff", "#3f6d9e"))
b += [text(28, 449, "Pega lambari, piaba, cará e camarão de água doce (comida e isca viva).", 12.5, "#222", True),
      text(28, 467, "Coloque em remanso raso, perto de capim ou pedras. Olhe 2–3 vezes por dia.", 12.5),
      text(28, 484, "Vários covos ao mesmo tempo rendem muito mais que um só.", 12.5)]
open(D + "covo-garrafa.svg", "w").write(svg(680, 500, "Covo (armadilha) de garrafa PET para peixe", "\n".join(b)))


# =====================================================================
# ANZOIS IMPROVISADOS
# =====================================================================
b = []
LIN = "#2a62a8"
# --- Painel 1: alfinete
b.append(text(20, 62, "1. Alfinete de segurança", 14, "#222", True))
b.append('<path d="M40 100 L104 100 Q114 100 114 92 L114 88" fill="none" stroke="#888" stroke-width="3"/>')
b.append('<path d="M40 86 L104 86" fill="none" stroke="#888" stroke-width="3"/>')
b.append('<circle cx="34" cy="93" r="7" fill="none" stroke="#888" stroke-width="3"/>')
b.append(f'<rect x="100" y="80" width="18" height="12" rx="3" fill="#bbb" stroke="{OUT}" stroke-width="1.5"/>')
b.append(text(52, 124, "antes", 11, "#666"))
b.append(arrow(126, 94, 156, 94, "#555", 3))
b.append('<circle cx="184" cy="88" r="7" fill="none" stroke="#666" stroke-width="3.5"/>')
b.append('<path d="M184 95 L184 150 Q184 172 206 172 Q226 172 228 152 L224 140" fill="none" stroke="#666" stroke-width="3.5" stroke-linecap="round"/>')
b.append(f'<path d="M180 82 Q172 76 174 70" fill="none" stroke="{LIN}" stroke-width="2"/>')
b += [text(240, 86, "a mola vira o", 11.5), text(240, 100, "olhal: amarre", 11.5), text(240, 114, "a linha aqui", 11.5),
      text(240, 140, "dobre em J", 11.5, "#222", True), text(240, 154, "com alicate e", 11.5), text(240, 168, "afie a ponta", 11.5), text(240, 182, "numa pedra", 11.5)]
b.append(text(20, 206, "Agulha: aqueça na chama antes de dobrar.", 11.5, "#444"))
b.append(f'<line x1="340" y1="48" x2="340" y2="440" stroke="#ccc" stroke-width="2"/>')
# --- Painel 2: espinho
b.append(text(352, 62, "2. Espinho + graveto", 14, "#222", True))
b.append(f'<rect x="380" y="88" width="18" height="96" rx="6" fill="{WOOD}" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<path d="M397 176 L436 124 L397 154 Z" fill="#e0c48a" stroke="{OUT}" stroke-width="2"/>')
for yy in (158, 164, 170, 176):
    b.append(f'<line x1="377" y1="{yy}" x2="401" y2="{yy+2}" stroke="#555" stroke-width="2"/>')
for yy in (100, 106, 112):
    b.append(f'<line x1="377" y1="{yy}" x2="401" y2="{yy+2}" stroke="{LIN}" stroke-width="2.2"/>')
b.append(f'<path d="M389 98 Q 391 80 400 70" fill="none" stroke="{LIN}" stroke-width="2"/>')
b += [text(446, 96, "linha amarrada num", 11.5), text(446, 110, "entalhe no topo", 11.5),
      text(446, 136, "espinho firme, amarrado", 11.5, "#222", True), text(446, 150, "com a ponta virada", 11.5, "#222", True), text(446, 164, "PARA CIMA (para a", 11.5, "#222", True), text(446, 178, "linha), como um anzol", 11.5, "#222", True)]
b += [text(352, 202, "Espinhos bons: laranjeira, limoeiro,", 11.5, "#444"), text(352, 216, "unha-de-gato (já vem curvo), juá.", 11.5, "#444")]
b.append(f'<line x1="14" y1="226" x2="666" y2="226" stroke="#ccc" stroke-width="2"/>')
# --- Painel 3: lacre de lata
b.append(text(20, 252, "3. Lacre de latinha", 14, "#222", True))
b.append('<path d="M40 286 Q40 266 62 266 L110 266 Q132 266 132 286 Q132 306 110 306 L62 306 Q40 306 40 286 Z" fill="#c9c9c9" stroke="#1e1e1e" stroke-width="2"/>')
b.append('<path d="M56 286 Q56 278 66 278 L86 278 Q96 278 96 286 Q96 294 86 294 L66 294 Q56 294 56 286 Z" fill="#fff" stroke="#1e1e1e" stroke-width="1.8"/>')
b.append('<circle cx="116" cy="286" r="5" fill="#fff" stroke="#1e1e1e" stroke-width="1.8"/>')
b.append(f'<line x1="78" y1="292" x2="78" y2="309" stroke="{PERIGO}" stroke-width="3.5"/>')
b.append(text(30, 326, "1 corte aqui (vermelho)", 11, PERIGO2, True))
b.append(arrow(144, 286, 176, 286, "#555", 3))
# depois: vira um J (ponta = onde foi cortado)
b.append('<path d="M262 276 L214 276 Q196 276 196 290 Q196 304 214 304 L226 304 L232 296" fill="none" stroke="#9a9a9a" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>')
b.append('<path d="M262 276 L214 276 Q196 276 196 290 Q196 304 214 304 L226 304 L232 296" fill="none" stroke="#1e1e1e" stroke-width="1" stroke-linecap="round"/>')
b.append('<rect x="252" y="268" width="34" height="24" rx="10" fill="#c9c9c9" stroke="#1e1e1e" stroke-width="2"/>')
b.append('<circle cx="272" cy="280" r="5" fill="#fff" stroke="#1e1e1e" stroke-width="1.8"/>')
b.append(f'<path d="M277 280 Q 296 270 304 252" fill="none" stroke="{LIN}" stroke-width="2"/>')
b.append(f'<path d="M244 312 L234 300" stroke="{PERIGO}" stroke-width="2"/>')
b += [text(196, 330, "a ponta do corte vira", 11.5), text(196, 344, "o anzol: lixe na pedra", 11.5, "#222", True)]
b += [text(20, 372, "Linha no furo pequeno. Serve para", 11.5, "#444"), text(20, 386, "peixes pequenos e médios.", 11.5, "#444")]
# --- Painel 4: anzol de garganta (osso/madeira)
b.append(text(352, 252, "4. Anzol de garganta (osso, madeira)", 14, "#222", True))
b.append('<path d="M364 292 L404 286 L444 292 L404 298 Z" fill="#f1e6c8" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<path d="M404 286 Q 406 274 414 266" fill="none" stroke="{LIN}" stroke-width="2"/>')
b += [text(456, 280, "lasca de 2–3 cm, com", 11.5), text(456, 294, "ponta nas DUAS pontas,", 11.5), text(456, 308, "linha amarrada no meio", 11.5)]
b.append('<ellipse cx="404" cy="356" rx="40" ry="11" fill="#d98c7a" stroke="#1e1e1e" stroke-width="1.8"/>')
b.append('<path d="M372 356 L436 356" stroke="#f1e6c8" stroke-width="4"/>')
b.append(f'<path d="M436 356 Q 452 356 460 346" fill="none" stroke="{LIN}" stroke-width="2"/>')
b += [text(360, 392, "escondida na isca,", 11.5), text(360, 406, "deitada na direção", 11.5), text(360, 420, "da linha", 11.5)]
b.append(arrow(470, 356, 498, 356, "#555", 3))
b.append('<path d="M522 326 L528 362 L522 398 L516 362 Z" fill="#f1e6c8" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<path d="M528 362 Q 540 360 548 352" fill="none" stroke="{LIN}" stroke-width="2"/>')
b += [text(548, 372, "o peixe engole;", 11.5, "#222", True), text(548, 386, "ao puxar, ela", 11.5, "#222", True), text(548, 400, "atravessa e", 11.5, "#222", True), text(548, 414, "prende", 11.5, "#222", True)]
b.append(box(14, 446, 652, 64, "#eef7ff", "#3f6d9e"))
b += [text(28, 467, "Anzol PEQUENO (1–2 cm) pega mais peixe. Linha: nylon, fio dental, linha de costura", 12.5),
      text(28, 485, "dobrada, fibra de tucum. Chumbada: pedrinha ou porca 20–30 cm acima do anzol.", 12.5),
      text(28, 503, "Boia: rolha, isopor ou pau leve, regulada para a isca ficar perto do fundo.", 12.5)]
open(D + "anzois-improvisados.svg", "w").write(svg(680, 518, "Anzóis improvisados", "\n".join(b)))
print("ok")
