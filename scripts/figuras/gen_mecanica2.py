import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
import math
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "08-ferramentas-e-mecanica", "img") + "/"
os.makedirs(D, exist_ok=True)
RED = "#d62828"; DRED = "#b3001b"; GREEN = "#2b8a3e"; DGREEN = "#1d6b2c"; WOOD = "#8b5a2b"


def lines(x, y, ls, size=12, color="#222", bold=False, anchor="start", lh=None):
    lh = lh or size * 1.3
    return "\n".join(text(x, y + i * lh, s, size, color, bold, anchor) for i, s in enumerate(ls))


def arc(cx, cy, r, a1, a2, color="#d62828", w=2.5):
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    x2, y2 = cx + r * math.cos(math.radians(a2)), cy + r * math.sin(math.radians(a2))
    sweep = 1 if a2 > a1 else 0
    return f'<path d="M{x1:.1f} {y1:.1f} A {r} {r} 0 0 {sweep} {x2:.1f} {y2:.1f}" fill="none" stroke="{color}" stroke-width="{w}"/>'


def xmark(x, y, r=16):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{RED}" stroke="#fff" stroke-width="2"/>'
            f'<path d="M{x-r*0.45} {y-r*0.45} L{x+r*0.45} {y+r*0.45} M{x+r*0.45} {y-r*0.45} L{x-r*0.45} {y+r*0.45}" stroke="#fff" stroke-width="4" stroke-linecap="round"/>')


def okmark(x, y, r=16):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{GREEN}" stroke="#fff" stroke-width="2"/>'
            f'<path d="M{x-r*0.5} {y} L{x-r*0.12} {y+r*0.4} L{x+r*0.5} {y-r*0.38}" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')


def fmt(v):
    s = f"{v:g}".replace(".", ",")
    return s


# =====================================================================
# 1) MISTURA 2 TEMPOS
# =====================================================================
b = []
L = [0.5, 1, 2, 5, 10, 20]
rows = [(25, "#fde2e2", "#b3001b", "motores antigos, alguns", "rabetas e motos 2T"),
        (40, "#fff1d6", "#a35a00", "várias roçadeiras e", "motosserras de entrada"),
        (50, "#e3f1e6", "#1d6b2c", "maioria das motosserras e", "roçadeiras atuais")]
x0, cw, c0 = 20, 78, 190
y0 = 56
b.append(f'<rect x="{x0}" y="{y0}" width="{c0-x0+cw*len(L)}" height="52" fill="#3f6d9e" rx="6"/>')
b.append(text(x0 + 12, y0 + 22, "Gasolina →", 13, "#fff", True))
b.append(text(x0 + 12, y0 + 41, "Proporção ↓", 13, "#fff", True))
for i, l in enumerate(L):
    cx = c0 + cw * i + cw / 2
    lab = (fmt(l) + " L")
    b.append(text(cx, y0 + 33, lab, 15, "#fff", True, "middle"))
for r, (p, bg, fg, d1, d2) in enumerate(rows):
    y = y0 + 58 + r * 66
    b.append(f'<rect x="{x0}" y="{y}" width="{c0-x0+cw*len(L)}" height="60" fill="{bg}" stroke="{fg}" stroke-width="1.5" rx="6"/>')
    b.append(text(x0 + 12, y + 28, f"1:{p}", 22, fg, True))
    b.append(lines(x0 + 12, y + 44, [d1, d2], 9.5, "#444", False, "start", 11))
    for i, l in enumerate(L):
        cx = c0 + cw * i + cw / 2
        ml = l * 1000 / p
        b.append(text(cx, y + 30, fmt(ml), 19, "#1e1e1e", True, "middle"))
        b.append(text(cx, y + 48, "mL de óleo", 10.5, "#444", False, "middle"))
    b.append(f'<line x1="{c0-4}" y1="{y+6}" x2="{c0-4}" y2="{y+54}" stroke="{fg}" stroke-width="1"/>')
yb = y0 + 58 + 3 * 66 + 6
b.append(text(340, yb + 14, "Conta: mL de óleo = litros × 1.000 ÷ número da proporção   (ex.: 5 L a 1:40 → 5.000 ÷ 40 = 125 mL)", 12, "#222", True, "middle"))
# como misturar com desenhos
yb += 30
b.append(box(15, yb, 650, 150, "#f7f7f7", "#999"))
# galao
gx, gy = 40, yb + 30
b.append(f'<path d="M{gx} {gy+10} L{gx+20} {gy} L{gx+70} {gy} L{gx+70} {gy+100} L{gx} {gy+100} Z" fill="#d62828" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<rect x="{gx+8}" y="{gy-12}" width="16" height="16" fill="#333" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<rect x="{gx+10}" y="{gy+40}" width="52" height="30" fill="#fff" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(text(gx + 36, gy + 53, "MISTURA", 9, "#1e1e1e", True, "middle"))
b.append(text(gx + 36, gy + 65, "1:50", 10, "#1e1e1e", True, "middle"))
# seringa
sx, sy = 130, yb + 52
b.append(f'<rect x="{sx}" y="{sy}" width="80" height="18" rx="3" fill="#eef5ff" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<rect x="{sx+2}" y="{sy+2}" width="48" height="14" fill="#c9a227"/>')
for k in range(1, 8):
    b.append(f'<line x1="{sx+k*10}" y1="{sy}" x2="{sx+k*10}" y2="{sy+7}" stroke="#1e1e1e" stroke-width="1"/>')
b.append(f'<rect x="{sx+80}" y="{sy+6}" width="12" height="6" fill="#ddd" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(f'<line x1="{sx-18}" y1="{sy+9}" x2="{sx}" y2="{sy+9}" stroke="#1e1e1e" stroke-width="3"/>')
b.append(f'<rect x="{sx-26}" y="{sy-4}" width="8" height="26" fill="#ddd" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(lines(sx + 40, sy + 40, ["seringa ou copo", "dosador só para", "o óleo 2T"], 10.5, "#444", False, "middle"))
b.append(lines(250, yb + 24, [
    "1. Galão limpo, só para mistura, com a proporção escrita nele.",
    "2. Ponha METADE da gasolina, depois TODO o óleo medido.",
    "3. Feche e agite. Complete a gasolina e agite de novo.",
    "4. Agite também antes de cada abastecimento.",
    "Óleo próprio para 2 tempos (JASO FC/FD ou API TC).",
    "Nunca gasolina pura num 2T: funde o motor em minutos.",
    "Mistura velha (mais de 30 dias) estraga carburador e motor."], 12, "#222", False, "start", 18))
H = yb + 162
open(D + "mistura-2t.svg", "w").write(svg(680, H, "Mistura 2 tempos: óleo por litro de gasolina", "\n".join(b)))

# =====================================================================
# 2) GERADOR SEGURO: ERRADO x CERTO
# =====================================================================
b = []


def casa(x, y, w=200, h=130):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#efe3c8" stroke="#1e1e1e" stroke-width="2.5"/>'
    s += f'<polygon points="{x-14},{y} {x+w/2},{y-56} {x+w+14},{y}" fill="#a0522d" stroke="#1e1e1e" stroke-width="2.5"/>'
    return s


def janela(x, y, w=44, h=40):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#cfe6fb" stroke="#1e1e1e" stroke-width="2"/>'
            f'<line x1="{x+w/2}" y1="{y}" x2="{x+w/2}" y2="{y+h}" stroke="#1e1e1e" stroke-width="1.5"/>')


def gerador(x, y, w=74, h=50):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#f2c200" stroke="#1e1e1e" stroke-width="2.5"/>'
    s += f'<rect x="{x+8}" y="{y+10}" width="{w-30}" height="{h-20}" rx="3" fill="#555" stroke="#1e1e1e" stroke-width="1.5"/>'
    s += f'<circle cx="{x+w-12}" cy="{y+16}" r="5" fill="#fff" stroke="#1e1e1e" stroke-width="1.5"/>'
    s += f'<rect x="{x+4}" y="{y+h}" width="10" height="6" fill="#333"/><rect x="{x+w-14}" y="{y+h}" width="10" height="6" fill="#333"/>'
    return s


def fumaca(x, y, dx=1, n=3, color="#8a8a8a"):
    s = ""
    for i in range(n):
        s += f'<circle cx="{x + dx*i*16}" cy="{y - i*10}" r="{7+i*3}" fill="{color}" fill-opacity="0.55"/>'
    return s


def poste(x, ground):
    s = f'<rect x="{x}" y="{ground-210}" width="12" height="210" fill="#9a9a9a" stroke="#1e1e1e" stroke-width="2"/>'
    s += f'<rect x="{x-30}" y="{ground-206}" width="72" height="8" fill="#9a9a9a" stroke="#1e1e1e" stroke-width="1.5"/>'
    s += f'<rect x="{x+14}" y="{ground-190}" width="30" height="40" rx="4" fill="#7d8a96" stroke="#1e1e1e" stroke-width="2"/>'
    return s


# ---- ERRADO
G1 = 270
b.append(f'<rect x="0" y="44" width="680" height="28" fill="#fdecec"/>')
b.append(text(20, 64, "ERRADO — pode matar", 16, DRED, True))
b.append(xmark(650, 58, 12))
b.append(f'<rect x="0" y="{G1}" width="680" height="16" fill="#e8d3b0"/>')
b.append(casa(30, G1 - 130))
b.append(janela(50, G1 - 108))
b.append(f'<rect x="130" y="{G1-90}" width="86" height="90" fill="#d9cbb0" stroke="#1e1e1e" stroke-width="2"/>')
b.append(text(173, G1 - 76, "garagem", 10.5, "#444", False, "middle"))
b.append(gerador(140, G1 - 56))
b.append(fumaca(140, G1 - 60, -1, 4))
# tomada e cabo macho-macho
b.append(f'<rect x="96" y="{G1-46}" width="18" height="24" rx="3" fill="#fff" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<path d="M140 {G1-30} C 128 {G1-30}, 124 {G1-34}, 114 {G1-34}" fill="none" stroke="#1e1e1e" stroke-width="4"/>')
b.append(xmark(80, G1 - 30, 11))
# linha para o poste
b.append(poste(330, G1))
b.append(f'<path d="M230 {G1-118} Q 268 {G1-176} 302 {G1-202}" fill="none" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(arrow(236, G1 - 128, 286, G1 - 186, RED, 4))
# eletricista agarrado ao poste
b.append(limb([(318, G1 - 122), (306, G1 - 100), (326, G1 - 82)], 10, "#3f6d9e"))
b.append(limb([(320, G1 - 122), (328, G1 - 104)], 10, "#3f6d9e"))
b.append(limb([(318, G1 - 166), (318, G1 - 122)], 18, "#3f6d9e"))
b.append(limb([(320, G1 - 160), (334, G1 - 192)], 8, "#3f6d9e"))
b.append(head(312, G1 - 182, 11, SKIN, -1, 0))
b.append(f'<path d="M301 {G1-188} q 11 -14 22 0 z" fill="#f2c200" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(lines(398, 100, ["Gerador ligado na tomada com", "cabo \"macho-macho\" (cabo suicida):"], 12.5, "#222", True))
b.append(lines(398, 136, ["• a energia VOLTA para a rede; o", "  transformador eleva para milhares de", "  volts e MATA o eletricista no poste;",
                          "• quando a luz volta: gerador queima,", "  fios esquentam, risco de incêndio."], 12, "#222"))
b.append(lines(398, 216, ["Gerador dentro de casa, garagem,", "varanda fechada ou sob a janela:", "MONÓXIDO DE CARBONO (sem cheiro)",
                          "mata quem está dormindo."], 12, DRED, True))
# ---- CERTO
T2 = 300
G2 = 530
b.append(f'<rect x="0" y="{T2}" width="680" height="28" fill="#eaf6ec"/>')
b.append(text(20, T2 + 20, "CERTO", 16, DGREEN, True))
b.append(okmark(650, T2 + 14, 12))
b.append(f'<rect x="0" y="{G2}" width="680" height="20" fill="#e8d3b0"/>')
b.append(casa(30, G2 - 130))
b.append(janela(50, G2 - 108))
# quadro + chave reversora
b.append(f'<rect x="150" y="{G2-110}" width="62" height="74" rx="4" fill="#ddd" stroke="#1e1e1e" stroke-width="2"/>')
b.append(text(181, G2 - 96, "chave", 10, "#1e1e1e", True, "middle"))
b.append(text(181, G2 - 84, "reversora", 10, "#1e1e1e", True, "middle"))
b.append(f'<rect x="160" y="{G2-76}" width="42" height="30" rx="3" fill="#fff" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(f'<line x1="181" y1="{G2-61}" x2="194" y2="{G2-72}" stroke="{RED}" stroke-width="4" stroke-linecap="round"/>')
b.append(text(164, G2 - 50, "R", 8, "#222", True)); b.append(text(178, G2 - 50, "0", 8, "#222", True)); b.append(text(192, G2 - 50, "G", 8, "#222", True))
# gerador fora, coberto
GX = 470
b.append(f'<polygon points="{GX-30},{G2-92} {GX+40},{G2-112} {GX+110},{G2-92}" fill="#a0522d" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<line x1="{GX-24}" y1="{G2-92}" x2="{GX-24}" y2="{G2}" stroke="{WOOD}" stroke-width="5"/>')
b.append(f'<line x1="{GX+104}" y1="{G2-92}" x2="{GX+104}" y2="{G2}" stroke="{WOOD}" stroke-width="5"/>')
b.append(gerador(GX, G2 - 56))
b.append(fumaca(GX + 82, G2 - 44, 1, 3))
b.append(arrow(GX + 76, G2 - 30, GX + 150, G2 - 30, "#666", 3))
# aterramento
b.append(f'<path d="M{GX+10} {G2-10} L{GX-6} {G2+4}" stroke="{GREEN}" stroke-width="3" fill="none"/>')
b.append(f'<rect x="{GX-10}" y="{G2-2}" width="8" height="24" fill="#b87333" stroke="#1e1e1e" stroke-width="1.5"/>')
# cabo ate chave reversora
b.append(f'<path d="M{GX} {G2-20} C 400 {G2-10}, 300 {G2-14}, 212 {G2-60}" fill="none" stroke="#1e1e1e" stroke-width="4"/>')
# distancia
b.append(f'<line x1="232" y1="{G2-150}" x2="{GX-30}" y2="{G2-150}" stroke="{DGREEN}" stroke-width="2.5"/>')
b.append(f'<polygon points="232,{G2-150} 244,{G2-156} 244,{G2-144}" fill="{DGREEN}"/>')
b.append(f'<polygon points="{GX-30},{G2-150} {GX-42},{G2-156} {GX-42},{G2-144}" fill="{DGREEN}"/>')
b.append(text((232 + GX - 30) / 2, G2 - 158, "6 metros ou mais", 14, DGREEN, True, "middle"))
b.append(lines(244, G2 - 124, ["escapamento virado para", "longe de portas e janelas"], 11.5, "#222"))
b.append(lines(586, G2 - 120, ["coberto,", "laterais", "abertas,", "nunca", "molhado"], 11, "#222"))
b.append(text(GX + 4, G2 + 16, "haste de terra", 10.5, "#1d6b2c", True))
b.append(box(15, G2 + 26, 650, 72, "#eaf6ec", "#2b8a3e"))
b.append(lines(28, G2 + 46, [
    "Chave reversora (instalada por eletricista): DESLIGA a rua antes de ligar o gerador na casa.",
    "Sem chave reversora: ligue cada aparelho DIRETO no gerador, com extensão grossa (2,5 mm² ou mais).",
    "Detector de CO dentro de casa. Abasteça só com o motor desligado e frio."], 12, "#1e1e1e", False, "start", 19))
open(D + "gerador-seguro.svg", "w").write(svg(680, G2 + 108, "Gerador: como ligar com segurança", "\n".join(b)))

# =====================================================================
# 3) VELA: DIAGNOSTICO PELA COR (ponta ampliada)
# =====================================================================
b = []


def ponta(cx, top, tip, elet, shell_in):
    s = ""
    # sextavado (parte de baixo)
    s += f'<rect x="{cx-52}" y="{top}" width="104" height="22" fill="#c0c0c0" stroke="#1e1e1e" stroke-width="2"/>'
    s += f'<line x1="{cx-18}" y1="{top}" x2="{cx-18}" y2="{top+22}" stroke="#888" stroke-width="1.5"/><line x1="{cx+18}" y1="{top}" x2="{cx+18}" y2="{top+22}" stroke="#888" stroke-width="1.5"/>'
    # rosca
    s += f'<rect x="{cx-40}" y="{top+22}" width="80" height="62" fill="#a8a8a8" stroke="#1e1e1e" stroke-width="2"/>'
    for k in range(7):
        s += f'<line x1="{cx-40}" y1="{top+32+k*8}" x2="{cx+40}" y2="{top+26+k*8}" stroke="#777" stroke-width="2"/>'
    # boca da rosca (interior com depósito)
    s += f'<ellipse cx="{cx}" cy="{top+84}" rx="40" ry="9" fill="{shell_in}" stroke="#1e1e1e" stroke-width="2"/>'
    # isolador (nariz) colorido
    s += f'<path d="M{cx-17} {top+82} L{cx+17} {top+82} L{cx+10} {top+122} L{cx-10} {top+122} Z" fill="{tip}" stroke="#1e1e1e" stroke-width="2.5"/>'
    # eletrodo central
    s += f'<rect x="{cx-5}" y="{top+122}" width="10" height="12" fill="{elet}" stroke="#1e1e1e" stroke-width="1.5"/>'
    # eletrodo massa em L
    s += f'<path d="M{cx+34} {top+88} L{cx+34} {top+148} L{cx-12} {top+148}" fill="none" stroke="#1e1e1e" stroke-width="11"/>'
    s += f'<path d="M{cx+34} {top+88} L{cx+34} {top+148} L{cx-12} {top+148}" fill="none" stroke="{elet}" stroke-width="6"/>'
    return s


b.append(text(340, 58, "Ponta da vela ampliada. Olhe o isolador (a parte do meio) logo depois de o motor trabalhar.", 12, "#444", False, "middle"))
C = [(88, "#c9a77c", "#9a9a9a", "#8f7a5c", "Marrom-claro", "ou cinza, seca", DGREEN, ["NORMAL", "motor bem regulado,", "mistura certa"]),
     (252, "#2a2a2a", "#555", "#2a2a2a", "Preta, fuligem", "seca (veludo)", "#a35a00", ["Mistura RICA", "filtro de ar sujo,", "afogador fechado,", "carburador"]),
     (416, "#1a1a1a", "#3a3a3a", "#1a1a1a", "Preta, molhada", "e oleosa", "#a35a00", ["ÓLEO demais", "muito óleo na", "mistura 2T, anéis", "gastos, afogado"]),
     (580, "#fbfbfb", "#e0e0e0", "#d8d8d8", "Branca, com", "bolinhas", DRED, ["Mistura POBRE", "superaquecendo:", "entrada de ar, gicleur", "entupido. PARE!"])]
TOP = 72
for cx, tip, el, sh, l1, l2, col, desc in C:
    b.append(ponta(cx, TOP, tip, el, sh))
    if "molhada" in l1:
        for dx, dy in ((-14, 100), (12, 110), (-4, 128)):
            b.append(f'<ellipse cx="{cx+dx}" cy="{TOP+dy}" rx="3" ry="5" fill="#6b4a12" stroke="#2a1a05" stroke-width="1"/>')
        b.append(f'<path d="M{cx-2} {TOP+134} q -3 8 0 14" stroke="#6b4a12" stroke-width="4" fill="none" stroke-linecap="round"/>')
    if "Branca" in l1:
        for dx, dy in ((-8, 92), (6, 98), (-3, 106), (5, 112), (-6, 116)):
            b.append(f'<circle cx="{cx+dx}" cy="{TOP+dy}" r="2.6" fill="#ccc" stroke="#888"/>')
        b.append(f'<circle cx="{cx}" cy="{TOP+134}" r="5" fill="#e0e0e0" stroke="#1e1e1e" stroke-width="1.5"/>')
    b.append(text(cx, TOP + 180, l1, 12.5, "#222", True, "middle"))
    b.append(text(cx, TOP + 196, l2, 12.5, "#222", True, "middle"))
    b.append(f'<rect x="{cx-78}" y="{TOP+206}" width="156" height="{18+len(desc)*16}" rx="7" fill="#fff" stroke="{col}" stroke-width="2"/>')
    b.append(text(cx, TOP + 224, desc[0], 13, col, True, "middle"))
    b.append(lines(cx, TOP + 241, desc[1:], 11.5, "#222", False, "middle", 16))
YB = TOP + 300
b.append(box(15, YB, 650, 86, "#eef5ff", "#3f6d9e"))
b.append(lines(28, YB + 21, [
    "Folga entre os eletrodos (meça com calibre de lâminas): motores pequenos 0,5–0,8 mm;",
    "carros 0,8–1,1 mm (veja o manual ou a etiqueta). Limpe com escova de latão, sem lixa grossa.",
    "Aperto da vela nova com anel: à mão até encostar + 1/2 volta. Vela já usada: + 1/8 de volta.",
    "Eletrodo gasto e arredondado, isolador trincado: troque a vela."], 12, "#1e1e1e", False, "start", 18))
open(D + "vela-diagnostico.svg", "w").write(svg(680, YB + 96, "Vela de ignição: o que a cor diz sobre o motor", "\n".join(b)))

# =====================================================================
# 4) MOTOSSERRA: CONTRAGOLPE E AFIACAO
# =====================================================================
b = []
bx0, by0, bx1, R = 60, 176, 330, 34
b.append(f'<rect x="20" y="{by0-52}" width="80" height="104" rx="12" fill="#f28c28" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(text(60, by0 + 4, "motor", 11, "#1e1e1e", True, "middle"))
b.append(f'<path d="M{bx0+40} {by0-R+6} L{bx1} {by0-R} A {R} {R} 0 0 1 {bx1} {by0+R} L{bx0+40} {by0+R-6} Z" fill="#c8cdd2" stroke="#1e1e1e" stroke-width="2.5"/>')
for k in range(12):
    x = bx0 + 50 + k * 22
    if x < bx1:
        b.append(f'<rect x="{x}" y="{by0-R-7}" width="12" height="7" fill="#555"/>')
        b.append(f'<rect x="{x}" y="{by0+R}" width="12" height="7" fill="#555"/>')
zx, zy = bx1, by0
b.append(f'<path d="M{zx} {zy} L{zx} {zy-R-8} A {R+8} {R+8} 0 0 1 {zx+R+8} {zy} Z" fill="{RED}" fill-opacity="0.75" stroke="{DRED}" stroke-width="2"/>')
b.append(f'<path d="M{zx} {zy-R} A {R} {R} 0 0 1 {zx+R} {zy}" fill="none" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(lines(392, 128, ["ZONA DE CONTRAGOLPE", "(quarto de cima da ponta)"], 12.5, DRED, True))
b.append(f'<line x1="390" y1="136" x2="{zx+22}" y2="{zy-26}" stroke="{DRED}" stroke-width="2"/>')
b.append(f'<path d="M{zx+6} {zy-52} C {zx-20} {zy-110}, {zx-140} {zy-112}, {zx-200} {zy-74}" fill="none" stroke="{DRED}" stroke-width="4" stroke-dasharray="8 5"/>')
b.append(f'<polygon points="{zx-212},{zy-66} {zx-196},{zy-86} {zx-192},{zy-66}" fill="{DRED}"/>')
b.append(text(zx - 90, zy - 104, "contragolpe", 12, DRED, True, "middle"))
b.append(lines(392, 178, ["Se essa parte toca a madeira, o", "sabre pula para CIMA e para TRÁS,", "na direção do rosto, em menos de", "1/10 de segundo."], 12, "#222"))
b.append(lines(20, 262, ["Nunca corte com a ponta. Segure com as DUAS mãos, polegar abraçando a alça.",
                         "Fique ao lado da linha do sabre, nunca atrás dele. Freio de corrente funcionando.",
                         "Nunca acima da altura do ombro. Corrente afiada puxa menos para trás."], 12, "#1e1e1e", False, "start", 18))
b.append('<line x1="20" y1="318" x2="660" y2="318" stroke="#ccc" stroke-width="2"/>')
b.append(text(340, 342, "Afiação com lima redonda", 15, "#222", True, "middle"))
# vista de cima
CY = 458
b.append(text(170, 366, "Visto de cima", 12.5, "#222", True, "middle"))
b.append(f'<rect x="40" y="{CY-6}" width="260" height="12" fill="#c8cdd2" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(text(52, CY + 26, "sabre", 11, "#555"))
b.append(f'<polygon points="140,{CY-6} 200,{CY-6} 192,{CY-30} 150,{CY-30}" fill="#888" stroke="#1e1e1e" stroke-width="2"/>')
b.append(text(138, CY - 14, "dente", 10.5, "#333", False, "end"))
ang = 30
fx, fy = 170, CY - 22
dx, dy = 58 * math.sin(math.radians(ang)), 58 * math.cos(math.radians(ang))
b.append(f'<line x1="{fx}" y1="{CY-90}" x2="{fx}" y2="{CY+34}" stroke="#555" stroke-width="1.5" stroke-dasharray="5 4"/>')
b.append(f'<line x1="{fx-dx:.1f}" y1="{fy+dy:.1f}" x2="{fx+dx:.1f}" y2="{fy-dy:.1f}" stroke="#1e1e1e" stroke-width="11" stroke-linecap="round"/>')
b.append(f'<line x1="{fx-dx:.1f}" y1="{fy+dy:.1f}" x2="{fx+dx:.1f}" y2="{fy-dy:.1f}" stroke="#9aa5b1" stroke-width="7" stroke-linecap="round"/>')
b.append(arc(fx, fy, 44, -90, -90 + ang))
b.append(text(fx - 10, fy - 50, "30°", 14, DRED, True, "end"))
b.append(f'<line x1="{fx-8}" y1="{fy-52}" x2="{fx+10}" y2="{fy-42}" stroke="{DRED}" stroke-width="1.5"/>')
b.append(text(fx + dx + 10, fy - dy + 6, "lima", 11.5, "#333", True))
b.append(lines(40, CY + 50, ["lima a 30° da linha que cruza", "o sabre; lima na horizontal"], 11.5, "#333"))
# vista de frente
b.append(text(490, 366, "Visto de frente", 12.5, "#222", True, "middle"))
TX = 420; TP = 420; r = 30
b.append(f'<path d="M{TX} {TP} L{TX+96} {TP} L{TX+96} {TP+14} L{TX+16} {TP+14} L{TX+16} {TP+86} L{TX} {TP+86} Z" fill="#888" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<circle cx="{TX+54}" cy="{TP + r - 0.4*r:.1f}" r="{r}" fill="#9aa5b1" fill-opacity="0.85" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<line x1="{TX+96}" y1="{TP}" x2="{TX+130}" y2="{TP}" stroke="#555" stroke-width="1.5" stroke-dasharray="4 3"/>')
b.append(f'<line x1="{TX+84}" y1="{TP-0.4*r:.1f}" x2="{TX+130}" y2="{TP-0.4*r:.1f}" stroke="#555" stroke-width="1.5" stroke-dasharray="4 3"/>')
b.append(lines(TX + 134, TP - 6, ["1/5 da lima", "acima do", "dente"], 11.5, DRED, True))
b.append(text(TX + 54, TP + 32, "lima", 11, "#1e1e1e", True, "middle"))
b.append(text(TX - 6, TP + 80, "dente", 10.5, "#333", False, "end"))
YB = 530
b.append(box(15, YB, 650, 104, "#f7f7f7", "#999"))
b.append(lines(28, YB + 20, [
    "Diâmetro da lima conforme o passo da corrente (está gravado no sabre ou no elo):",
    "  1/4\" e 3/8\" P (picco) → 4,0 mm   ·   0,325\" → 4,8 mm   ·   3/8\" → 5,2 mm   ·   0,404\" → 5,5 mm",
    "Lime só para a FRENTE, de dentro para fora do dente, 3–5 passadas iguais em cada dente.",
    "Todos os dentes de um lado, vire a máquina e faça o outro lado. Todos do mesmo tamanho.",
    "A cada 3–5 afiações, rebaixe o limitador de profundidade com gabarito e lima chata."], 12, "#1e1e1e", False, "start", 18))
open(D + "motosserra.svg", "w").write(svg(680, YB + 114, "Motosserra: contragolpe e afiação da corrente", "\n".join(b)))
print("ok gen_mecanica2")
