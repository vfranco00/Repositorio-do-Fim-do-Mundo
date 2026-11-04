import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
# Figuras de 10-comunicacao-e-navegacao/01-radio.md
import math
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "10-comunicacao-e-navegacao", "img") + "/"
os.makedirs(D, exist_ok=True)
GREEN = "#2b8a3e"; RED = "#d62828"; DARK = "#1e1e1e"; BLUE = "#3f6d9e"; WOOD = "#8b5a2b"; COPPER = "#c06a1a"

def dim(x1, x2, y, label, color=DARK, size=12.5, bold=True):
    s = f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="1.5"/>'
    for x in (x1, x2):
        s += f'<line x1="{x}" y1="{y-7}" x2="{x}" y2="{y+7}" stroke="{color}" stroke-width="1.5"/>'
    s += f'<polygon points="{x1},{y} {x1+9},{y-4} {x1+9},{y+4}" fill="{color}"/><polygon points="{x2},{y} {x2-9},{y-4} {x2-9},{y+4}" fill="{color}"/>'
    s += f'<rect x="{(x1+x2)/2 - len(label)*4.1}" y="{y-10}" width="{len(label)*8.2}" height="20" fill="#fff"/>'
    s += text((x1 + x2) / 2, y + 5, label, size, color, bold, "middle")
    return s

def insulator(cx, cy, w=22, h=12):
    return f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="4" fill="#f0f0f0" stroke="{DARK}" stroke-width="2"/>'

# ---------- ANTENA DIPOLO ----------
b = []
WY = 140
# postes / arvores
for x in (34, 646):
    b.append(f'<rect x="{x-6}" y="96" width="12" height="270" fill="{WOOD}" stroke="{DARK}" stroke-width="2"/>')
b.append('<line x1="0" y1="366" x2="680" y2="366" stroke="#6b4f2a" stroke-width="3"/>')
b.append(f'<line x1="40" y1="108" x2="92" y2="{WY}" stroke="#a08050" stroke-width="2.5"/>')
b.append(f'<line x1="640" y1="108" x2="588" y2="{WY}" stroke="#a08050" stroke-width="2.5"/>')
b.append(text(52, 92, "corda", 11, "#6b4f2a", True))
# fios
b.append(f'<line x1="104" y1="{WY}" x2="329" y2="{WY}" stroke="{COPPER}" stroke-width="4"/>')
b.append(f'<line x1="351" y1="{WY}" x2="576" y2="{WY}" stroke="{COPPER}" stroke-width="4"/>')
b.append(insulator(98, WY)); b.append(insulator(582, WY)); b.append(insulator(340, WY, 24, 18))
b.append(text(98, WY + 24, "isolador", 11, "#444", False, "middle")); b.append(text(582, WY + 24, "isolador", 11, "#444", False, "middle"))
# cotas
b.append(dim(104, 576, 74, "COMPRIMENTO TOTAL (m) = 143 ÷ frequência (MHz)", DARK, 12.5))
b.append(dim(104, 329, 112, "cada braço = 71,5 ÷ f", COPPER, 12))
b.append(dim(351, 576, 112, "cada braço = 71,5 ÷ f", COPPER, 12))
# cabo coaxial com choque
b.append(f'<path d="M340 {WY+9} L340 210" stroke="{DARK}" stroke-width="6" fill="none"/>')
for i in range(4):
    yy = 214 + i * 9
    b.append(f'<ellipse cx="340" cy="{yy}" rx="22" ry="6" fill="none" stroke="{DARK}" stroke-width="4"/>')
b.append(f'<path d="M340 246 L340 300 Q340 330 370 330 L452 330" stroke="{DARK}" stroke-width="6" fill="none"/>')
b.append(text(368, 222, "5 a 8 voltas do próprio cabo", 11, "#222", True))
b.append(text(368, 236, "(10–15 cm de diâmetro):", 11, "#444"))
b.append(text(368, 250, "evita interferência no cabo", 11, "#444"))
b.append(text(352, 276, "cabo coaxial de 50 ohms", 11.5, "#222", True)); b.append(text(352, 290, "(RG-58; RG-213 se for", 11, "#444")); b.append(text(352, 303, "longo)", 11, "#444"))
# radio
b.append(f'<rect x="452" y="304" width="110" height="56" rx="6" fill="#4b4f55" stroke="{DARK}" stroke-width="2.5"/>')
b.append(f'<rect x="464" y="314" width="50" height="18" fill="#a9d18e" stroke="{DARK}"/>')
b.append(f'<circle cx="538" cy="334" r="11" fill="#888" stroke="{DARK}" stroke-width="2"/>')
b.append(text(507, 354, "rádio", 11, "#fff", True, "middle"))
b.append(f'<rect x="580" y="320" width="40" height="40" rx="3" fill="#2e2e2e" stroke="{DARK}" stroke-width="2"/>')
b.append(text(600, 344, "12 V", 11, "#fff", True, "middle"))
b.append(f'<path d="M562 330 L580 330" stroke="{RED}" stroke-width="3"/>')
# detalhe do centro
b.append(f'<rect x="20" y="170" width="200" height="118" rx="8" fill="#f7f7f7" stroke="#999"/>')
b.append(text(120, 188, "detalhe do centro", 12, "#222", True, "middle"))
b.append(f'<line x1="30" y1="214" x2="104" y2="214" stroke="{COPPER}" stroke-width="4"/>')
b.append(f'<line x1="136" y1="214" x2="210" y2="214" stroke="{COPPER}" stroke-width="4"/>')
b.append(insulator(120, 214, 34, 16))
b.append(f'<path d="M112 222 L112 262" stroke="#9a9a9a" stroke-width="7"/>')
b.append(f'<path d="M104 214 Q 104 236 112 240" stroke="{COPPER}" stroke-width="2.5" fill="none"/>')
b.append(f'<path d="M136 214 Q 136 230 116 236" stroke="#555" stroke-width="2.5" fill="none" stroke-dasharray="3 2"/>')
b.append(text(30, 240, "vivo (fio do", 11, "#222", True)); b.append(text(30, 253, "meio) → braço 1", 11, "#222", True))
b.append(text(144, 246, "malha →", 11, "#222", True)); b.append(text(144, 259, "braço 2", 11, "#222", True))
b.append(text(120, 280, "vede com fita e silicone", 11, "#444", False, "middle"))
# tabela
ty = 388
b.append(box(20, ty, 640, 132, "#eef5ff", BLUE))
b.append(text(34, ty + 22, "Exemplos (corte 3–5% mais comprido e vá aparando as pontas)", 13, "#222", True))
rows = [("PX / Faixa do Cidadão, 27,1 MHz", "5,28 m", "2,64 m"), ("Radioamador 40 m, 7,1 MHz", "20,1 m", "10,07 m"),
        ("Radioamador 2 m, 145 MHz", "99 cm", "49 cm"), ("VHF marítimo, 156,8 MHz", "91 cm", "46 cm")]
b.append(text(380, ty + 44, "total", 12, "#444", True, "middle")); b.append(text(500, ty + 44, "cada braço", 12, "#444", True, "middle"))
for i, (n, t, c) in enumerate(rows):
    y = ty + 64 + i * 18
    b.append(text(34, y, n, 12.5)); b.append(text(380, y, t, 12.5, "#222", True, "middle")); b.append(text(500, y, c, 12.5, COPPER, True, "middle"))
b.append(text(340, ty + 150, "Quanto mais ALTA e livre (longe de fios de energia, telhados de metal e árvores), melhor.", 12.5, "#222", True, "middle"))
open(D + "antena-dipolo.svg", "w").write(svg(680, ty + 162, "Antena dipolo de meia-onda", "\n".join(b)))

# ---------- ALCANCE x ALTURA (VHF/UHF) ----------
b = []
def person(cx, base, col=SOC):
    s = limb([(cx - 5, base - 30), (cx - 6, base)], 7, col) + limb([(cx + 5, base - 30), (cx + 6, base)], 7, col)
    s += limb([(cx, base - 58), (cx, base - 30)], 16, col) + head(cx, base - 70, 9, col)
    s += f'<line x1="{cx+10}" y1="{base-52}" x2="{cx+10}" y2="{base-82}" stroke="{DARK}" stroke-width="3"/>'
    return s
def tree(x, base, h=50):
    return (f'<rect x="{x-3}" y="{base-h*0.4}" width="6" height="{h*0.4}" fill="{WOOD}"/>'
            f'<circle cx="{x}" cy="{base-h*0.65}" r="{h*0.32}" fill="#5e9c4a" stroke="#3d6b2f" stroke-width="1.5"/>')
def house(x, base, w=40, h=28):
    return (f'<rect x="{x}" y="{base-h}" width="{w}" height="{h}" fill="#e4d2b5" stroke="{DARK}" stroke-width="1.5"/>'
            f'<polygon points="{x-4},{base-h} {x+w/2},{base-h-16} {x+w+4},{base-h}" fill="#b5523b" stroke="{DARK}" stroke-width="1.5"/>')
rows = [(66, "No plano, rádio de mão com rádio de mão (1,5 m de altura)", "1 a 5 km na prática (até ~10 km sem nada no meio)", RED),
        (246, "Antena num mastro de 10 m + rádio de mão", "até ~18 km sem morros no caminho", "#c26a00"),
        (426, "Antena no alto de um morro de 100 m + rádio de mão", "até ~45 km (repetidoras ficam em morros)", GREEN)]
for k, (y0, t1, t2, col) in enumerate(rows):
    base = y0 + 136
    b.append(text(20, y0 + 6, t1, 13, "#222", True))
    b.append(f'<line x1="20" y1="{base}" x2="660" y2="{base}" stroke="#6b4f2a" stroke-width="3"/>')
    if k == 0:
        b.append(person(60, base)); b.append(person(600, base))
        for x in (190, 230, 420): b.append(tree(x, base, 54))
        b.append(house(300, base, 46, 34)); b.append(house(470, base))
        b.append(f'<line x1="70" y1="{base-82}" x2="190" y2="{base-60}" stroke="{col}" stroke-width="2.5" stroke-dasharray="6 4"/>')
        b.append(text(210, base - 70, "árvores, casas e morros bloqueiam", 11.5, col, True))
        top = (70, base - 82)
    elif k == 1:
        b.append(house(40, base, 50, 30))
        b.append(f'<line x1="70" y1="{base}" x2="70" y2="{base-96}" stroke="{DARK}" stroke-width="4"/>')
        b.append(f'<line x1="60" y1="{base-96}" x2="80" y2="{base-96}" stroke="{DARK}" stroke-width="3"/>')
        b.append(text(80, base - 70, "10 m", 11.5, "#222", True))
        b.append(person(600, base)); b.append(tree(300, base, 46)); b.append(house(420, base))
        b.append(f'<line x1="70" y1="{base-96}" x2="610" y2="{base-82}" stroke="{col}" stroke-width="2.5" stroke-dasharray="6 4"/>')
    else:
        b.append(f'<path d="M20 {base} Q 90 {base-96} 170 {base-96} Q 250 {base-96} 330 {base} Z" fill="#c9b48a" stroke="{DARK}" stroke-width="2"/>')
        b.append(f'<line x1="170" y1="{base-96}" x2="170" y2="{base-122}" stroke="{DARK}" stroke-width="4"/>')
        b.append(text(170, base - 36, "morro de 100 m", 12, "#222", True, "middle"))
        b.append(person(600, base)); b.append(tree(460, base, 46))
        b.append(f'<line x1="170" y1="{base-122}" x2="610" y2="{base-82}" stroke="{col}" stroke-width="2.5" stroke-dasharray="6 4"/>')
    b.append(text(340, base + 22, t2, 12.5, col, True, "middle"))
b.append(box(20, 610, 640, 94, "#fff4e5", "#ef8a2b"))
b.append(text(34, 632, "VHF e UHF (rádio de mão, VHF marítimo, radioamador de 2 m) andam em", 12.5, "#222", True))
b.append(text(34, 650, "LINHA RETA, como a luz: manda a ALTURA da antena e não haver morro no meio.", 12.5, "#222", True))
b.append(text(34, 668, "Suba num ponto alto para falar. Ondas curtas, AM e PX (27 MHz) podem ir muito mais", 12.5))
b.append(text(34, 686, "longe refletindo no céu (ionosfera), sobretudo à noite.", 12.5))
open(D + "alcance-e-altura.svg", "w").write(svg(680, 714, "Antena alta = mais alcance", "\n".join(b)))

# ---------- RADIO DE GALENA ----------
b = []
# antena
b.append(f'<line x1="40" y1="74" x2="300" y2="74" stroke="{COPPER}" stroke-width="3"/>')
b.append(insulator(36, 74, 14, 10)); b.append(insulator(304, 74, 14, 10))
b.append(text(170, 64, "ANTENA: fio de 15 a 30 m, o mais alto possível", 12, "#222", True, "middle"))
b.append(f'<line x1="80" y1="74" x2="80" y2="140" stroke="{COPPER}" stroke-width="3"/>')
# no A
AY = 140; GY = 330
b.append(f'<line x1="80" y1="{AY}" x2="420" y2="{AY}" stroke="{DARK}" stroke-width="2.5"/>')
b.append(f'<line x1="80" y1="{GY}" x2="520" y2="{GY}" stroke="{DARK}" stroke-width="2.5"/>')
# bobina
cx = 140
b.append(f'<line x1="{cx}" y1="{AY}" x2="{cx}" y2="180" stroke="{DARK}" stroke-width="2.5"/>')
p = f"M{cx} 180 "
for i in range(6):
    p += f"a 12 10 0 0 1 0 20 "
b.append(f'<path d="{p}" fill="none" stroke="{COPPER}" stroke-width="3"/>')
b.append(f'<line x1="{cx}" y1="300" x2="{cx}" y2="{GY}" stroke="{DARK}" stroke-width="2.5"/>')
b.append(text(cx - 18, 200, "BOBINA", 12, "#222", True, "end")); b.append(text(cx - 18, 215, "~80 voltas de", 11, "#444", False, "end"))
b.append(text(cx - 18, 229, "fio esmaltado", 11, "#444", False, "end")); b.append(text(cx - 18, 243, "0,3–0,5 mm em", 11, "#444", False, "end"))
b.append(text(cx - 18, 257, "tubo de PVC", 11, "#444", False, "end")); b.append(text(cx - 18, 271, "de 50 mm", 11, "#444", False, "end"))
# capacitor variavel
cx2 = 230
b.append(f'<line x1="{cx2}" y1="{AY}" x2="{cx2}" y2="226" stroke="{DARK}" stroke-width="2.5"/>')
b.append(f'<line x1="{cx2-22}" y1="226" x2="{cx2+22}" y2="226" stroke="{DARK}" stroke-width="4"/>')
b.append(f'<line x1="{cx2-22}" y1="240" x2="{cx2+22}" y2="240" stroke="{DARK}" stroke-width="4"/>')
b.append(f'<line x1="{cx2}" y1="240" x2="{cx2}" y2="{GY}" stroke="{DARK}" stroke-width="2.5"/>')
b.append(arrow(cx2 - 30, 256, cx2 + 30, 208, BLUE, 2.5))
b.append(text(cx2 + 30, 266, "CAPACITOR", 12, "#222", True)); b.append(text(cx2 + 30, 281, "VARIÁVEL", 12, "#222", True))
b.append(text(cx2 + 30, 296, "(de rádio velho)", 11, "#444")); b.append(text(cx2 + 30, 310, "= sintonia", 11, BLUE, True))
# diodo
dx = 340
b.append(f'<polygon points="{dx-14},{AY-12} {dx-14},{AY+12} {dx+8},{AY}" fill="{DARK}"/>')
b.append(f'<line x1="{dx+9}" y1="{AY-13}" x2="{dx+9}" y2="{AY+13}" stroke="{DARK}" stroke-width="3"/>')
b.append(text(dx, AY - 22, "DIODO de germânio", 12, "#222", True, "middle"))
b.append(text(dx, AY + 30, "(1N34, 1N60) ou cristal", 11, "#444", False, "middle"))
b.append(text(dx, AY + 44, "de galena com \"bigode\"", 11, "#444", False, "middle"))
# fone
fx = 470
b.append(f'<line x1="420" y1="{AY}" x2="{fx}" y2="{AY}" stroke="{DARK}" stroke-width="2.5"/>')
b.append(f'<line x1="{fx}" y1="{AY}" x2="{fx}" y2="200" stroke="{DARK}" stroke-width="2.5"/>')
b.append(f'<path d="M{fx-16} 200 h32 v34 l14 18 h-60 l14 -18 Z" fill="#f2c94c" stroke="{DARK}" stroke-width="2.5"/>')
b.append(f'<line x1="{fx}" y1="252" x2="{fx}" y2="{GY}" stroke="{DARK}" stroke-width="2.5"/>')
b.append(text(fx + 34, 214, "FONE de cristal", 12, "#222", True)); b.append(text(fx + 34, 229, "(alta impedância;", 11, "#444"))
b.append(text(fx + 34, 243, "fone comum de", 11, "#444")); b.append(text(fx + 34, 257, "celular quase não", 11, "#444")); b.append(text(fx + 34, 271, "funciona)", 11, "#444"))
# resistor em paralelo
rx = 636
b.append(f'<line x1="{fx}" y1="{AY}" x2="{rx}" y2="{AY}" stroke="{DARK}" stroke-width="2.5"/>')
b.append(f'<line x1="{rx}" y1="{AY}" x2="{rx}" y2="170" stroke="{DARK}" stroke-width="2.5"/>')
b.append(f'<path d="M{rx} 170 l8 5 l-16 10 l16 10 l-16 10 l16 10 l-8 5" fill="none" stroke="{DARK}" stroke-width="2.5"/>')
b.append(f'<line x1="{rx}" y1="220" x2="{rx}" y2="{GY}" stroke="{DARK}" stroke-width="2.5"/>')
b.append(f'<line x1="520" y1="{GY}" x2="{rx}" y2="{GY}" stroke="{DARK}" stroke-width="2.5"/>')
b.append(text(rx - 8, 300, "resistor", 11, "#444", False, "end")); b.append(text(rx - 8, 314, "47–100 kΩ", 11, "#444", False, "end"))
# terra
b.append(f'<line x1="300" y1="{GY}" x2="300" y2="{GY+22}" stroke="{DARK}" stroke-width="2.5"/>')
for i, w in enumerate((40, 26, 12)):
    b.append(f'<line x1="{300-w/2}" y1="{GY+22+i*7}" x2="{300+w/2}" y2="{GY+22+i*7}" stroke="{DARK}" stroke-width="2.5"/>')
b.append(text(330, GY + 32, "TERRA: haste de metal de 1–2 m enterrada", 12, "#222", True))
b.append(text(330, GY + 47, "em chão úmido, ou cano de água metálico", 11.5, "#444"))
for x, y in ((80, AY), (140, AY), (230, AY), (470, AY), (140, GY), (230, GY), (300, GY), (470, GY)):
    b.append(f'<circle cx="{x}" cy="{y}" r="4" fill="{DARK}"/>')
b.append(box(20, 400, 640, 94, "#fff4e5", "#ef8a2b"))
b.append(text(34, 422, "Não usa pilha: a energia vem da própria onda de rádio. Pega estações AM fortes (até", 12.5))
b.append(text(34, 440, "50–150 km de dia, mais longe à noite). Gire o capacitor devagar para trocar de estação.", 12.5))
b.append(text(34, 462, "Sem capacitor variável: faça uma bobina com várias derivações (ex.: a cada 10 voltas)", 12.5))
b.append(text(34, 480, "e encoste um fio em cada uma até ouvir a estação.", 12.5))
open(D + "radio-de-galena.svg", "w").write(svg(680, 504, "Rádio de galena (sem pilha) — esquema", "\n".join(b)))
print("ok")
