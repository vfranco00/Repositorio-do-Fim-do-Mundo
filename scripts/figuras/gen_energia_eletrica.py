import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
# Figuras da seção 06-energia: eletricidade e energia solar
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "06-energia", "img") + "/"
os.makedirs(D, exist_ok=True)
DANGER = "#d62828"; RED = "#d62828"; BLK = "#1e1e1e"; AZUL = "#1f5f9e"; VERDE = "#2b8a3e"; DARK = "#b3001b"

def rect(x, y, w, h, fill, stroke=OUT, sw=2, rx=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'
def line(x1, y1, x2, y2, color=OUT, w=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}" stroke-linecap="round"{d}/>'
def wire(pts, color, w=4):
    p = " ".join(f"{x},{y}" for x, y in pts)
    return f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>'
def tlines(x, y, lines, size=12, color="#222", bold_first=False, lh=None, anchor="start"):
    lh = lh or size * 1.3
    return "".join(text(x, y + k * lh, s, size, color, bold_first and k == 0, anchor) for k, s in enumerate(lines))
def fuse_v(x, y, lab=None):   # fusivel em fio vertical, centro (x, y)
    o = rect(x - 8, y - 13, 16, 26, "#fff3bf", OUT, 2, 3) + line(x, y - 13, x, y + 13, OUT, 1.5)
    if lab: o += text(x + 13, y + 5, lab, 12, "#222", True)
    return o
def fuse_h(x, y, lab=None):
    o = rect(x - 13, y - 8, 26, 16, "#fff3bf", OUT, 2, 3) + line(x - 13, y, x + 13, y, OUT, 1.5)
    if lab: o += text(x, y - 13, lab, 12, "#222", True, "middle")
    return o
def terminal(x, y, pos):
    c = RED if pos else BLK
    return (f'<circle cx="{x}" cy="{y}" r="7" fill="{c}" stroke="{OUT}" stroke-width="1.5"/>'
            + text(x, y + 4, "+" if pos else "−", 11, "#fff", True, "middle"))
def battery(x, y, w=110, h=64, lab="12 V", lab2="100 Ah", flip=False):
    # terminais no topo: negativo a esquerda, positivo a direita (ou invertido)
    o = rect(x, y, w, h, "#4f5b66", OUT, 2.5, 5)
    o += rect(x + 14, y - 10, 18, 10, RED if flip else BLK, OUT, 1.5, 2) + rect(x + w - 32, y - 10, 18, 10, BLK if flip else RED, OUT, 1.5, 2)
    o += text(x + 23, y + 18, "+" if flip else "−", 15, "#fff", True, "middle") + text(x + w - 23, y + 18, "−" if flip else "+", 15, "#fff", True, "middle")
    o += text(x + w / 2, y + 40, lab, 14, "#fff", True, "middle") + text(x + w / 2, y + 56, lab2, 11.5, "#e6e6e6", False, "middle")
    return o
def panel(x, y, w=120, h=70, lab="18 V · 5 A"):
    o = rect(x, y, w, h, "#1d3557", OUT, 2.5, 3)
    for k in range(1, 4):
        o += line(x + k * w / 4, y + 2, x + k * w / 4, y + h - 2, "#7fa7d9", 1)
    for k in range(1, 3):
        o += line(x + 2, y + k * h / 3, x + w - 2, y + k * h / 3, "#7fa7d9", 1)
    o += rect(x + w / 2 - 44, y + h / 2 - 11, 88, 22, "#fff", "none", 0, 4, 'fill-opacity="0.9"')
    o += text(x + w / 2, y + h / 2 + 5, lab, 12, "#222", True, "middle")
    return o

# =====================================================================
# 1. ESQUEMA SOLAR OFF-GRID
# =====================================================================
b = []
# painel inclinado
b.append('<polygon points="40,150 84,64 244,64 200,150" fill="#1d3557" stroke="#1e1e1e" stroke-width="2.5" stroke-linejoin="round"/>')
for k in range(1, 4):
    x = 40 + k * 40
    b.append(line(x, 150, x + 44, 64, "#7fa7d9", 1.2))
for k in (1, 2):
    y = 150 - k * 28.7; dx = k * 14.7
    b.append(line(40 + dx, y, 200 + dx, y, "#7fa7d9", 1.2))
b.append(text(60, 176, "PAINEL SOLAR", 13, "#222", True, "end") if False else "")
b.append(tlines(186, 172, ["PAINEL SOLAR", "virado para o NORTE"], 12.5, "#222", True, 15))
# fios painel -> controlador
b.append(wire([(150, 150), (150, 222), (262, 222)], RED))
b.append(wire([(134, 150), (134, 246), (262, 246)], BLK))
b.append(fuse_v(150, 196)); b.append(text(164, 201, "F1", 12, "#222", True))
b.append(tlines(20, 286, ["F1: disjuntor ou", "fusível CC do painel"], 11.5, "#222", True, 14))
# controlador
b.append(rect(262, 196, 158, 88, "#e9ecef", OUT, 2.5, 8))
b.append(text(341, 216, "CONTROLADOR", 13, "#222", True, "middle"))
b.append(text(341, 231, "DE CARGA", 13, "#222", True, "middle"))
b.append(text(268, 262, "painel", 11, "#444")); b.append(text(414, 262, "carga", 11, "#444", False, "end"))
b.append(text(341, 278, "bateria", 11, "#444", False, "middle"))
# controlador -> bateria
BX, BY = 270, 400
b.append(wire([(296, 284), (296, BY - 10)], BLK))
b.append(wire([(384, 284), (384, BY - 10)], RED))
b.append(fuse_v(384, 340)); b.append(text(370, 345, "F2", 12, "#222", True, "end"))
b.append(rect(BX, BY, 140, 78, "#4f5b66", OUT, 2.5, 6))
b.append(rect(286, BY - 10, 20, 10, BLK, OUT, 1.5, 2)); b.append(rect(374, BY - 10, 20, 10, RED, OUT, 1.5, 2))
b.append(text(296, BY + 22, "−", 18, "#fff", True, "middle")); b.append(text(384, BY + 22, "+", 18, "#fff", True, "middle"))
b.append(text(340, BY + 50, "BATERIA", 14, "#fff", True, "middle")); b.append(text(340, BY + 67, "12 V", 11.5, "#e6e6e6", False, "middle"))
# cargas 12 V
b.append(wire([(420, 222), (508, 222)], RED)); b.append(wire([(420, 246), (508, 246)], BLK))
b.append(fuse_h(462, 222, "F3"))
b.append(rect(508, 190, 152, 96, "#fff9db", OUT, 2, 8))
b.append(text(584, 210, "CARGAS 12 V", 13, "#222", True, "middle"))
# lampada LED
b.append('<circle cx="540" cy="238" r="15" fill="#ffe066" stroke="#1e1e1e" stroke-width="2"/>')
b.append(rect(533, 252, 14, 12, "#adb5bd", OUT, 1.5, 2))
# USB
b.append(rect(566, 228, 30, 22, "#dee2e6", OUT, 2, 3)); b.append(rect(572, 236, 18, 6, "#495057", "none", 0))
b.append(text(581, 264, "USB", 10.5, "#222", True, "middle"))
b.append(text(630, 248, "rádio", 10.5, "#222", False, "middle")); b.append(text(630, 262, "ventil.", 10.5, "#222", False, "middle"))
b.append(text(584, 280, "LED, celular, rádio", 10.5, "#444", False, "middle"))
# bateria -> inversor
b.append(wire([(384, 392), (384, 374), (500, 374), (500, 414), (522, 414)], RED))
b.append(wire([(296, 392), (296, 378), (248, 378), (248, 500), (490, 500), (490, 446), (522, 446)], BLK))
b.append(fuse_h(446, 374, ""))
b.append(text(446, 362, "F4 (grosso)", 11.5, "#222", True, "middle"))
b.append(rect(522, 396, 138, 70, "#ced4da", OUT, 2.5, 6))
b.append(text(591, 422, "INVERSOR", 13, "#222", True, "middle"))
b.append(text(591, 438, "12 V CC → 127/220 V", 10.5, "#222", False, "middle"))
b.append(text(591, 452, "CA (senoidal pura)", 10.5, "#222", False, "middle"))
# tomada
b.append(wire([(600, 466), (600, 492)], "#555", 5))
b.append('<circle cx="600" cy="514" r="21" fill="#f8f9fa" stroke="#1e1e1e" stroke-width="2.5"/>')
for (dx, dy) in ((-8, -3), (8, -3), (0, 8)):
    b.append(f'<circle cx="{600+dx}" cy="{514+dy}" r="3" fill="#1e1e1e"/>')
b.append(tlines(520, 552, ["tomada 127/220 V:", "choque MATA"], 11.5, DARK, True, 14))
# legenda
b.append(line(452, 74, 486, 74, RED, 5)); b.append(text(494, 79, "fio positivo (+)", 12.5, "#222", True))
b.append(line(452, 98, 486, 98, BLK, 5)); b.append(text(494, 103, "fio negativo (−)", 12.5, "#222", True))
b.append(rect(448, 116, 40, 18, "#fff3bf", OUT, 2, 3)); b.append(text(494, 130, "fusível (no fio +)", 12.5, "#222", True))
b.append(tlines(20, 360, ["F2 e F4 ficam", "a no máximo", "20–30 cm do +", "da bateria"], 11.5, DARK, True, 14))
b.append(box(20, 576, 640, 64, "#eef5ff", "#3f6d9e"))
b.append(tlines(34, 598, ["LIGAR: 1º a bateria no controlador → 2º o painel → 3º as cargas.",
                          "DESLIGAR: na ordem contrária (o painel primeiro). O inversor vai DIRETO na bateria."], 12.5, "#1b3d6b", False, 18))
open(D + "solar-offgrid.svg", "w").write(svg(680, 650, "Sistema solar isolado (off-grid): como ligar", "\n".join(b)))

# =====================================================================
# 2. SERIE x PARALELO
# =====================================================================
b = []
b.append(line(340, 48, 340, 520, "#ccc", 2)); b.append(line(10, 290, 670, 290, "#ccc", 2))
b.append(text(170, 64, "EM SÉRIE", 16, "#222", True, "middle")); b.append(text(510, 64, "EM PARALELO", 16, "#222", True, "middle"))
b.append(text(170, 82, "(+ de uma no − da outra)", 12, "#444", False, "middle")); b.append(text(510, 82, "(+ com +, − com −)", 12, "#444", False, "middle"))
# --- baterias em serie ---
b.append(battery(40, 130)); b.append(battery(190, 130))
b.append(wire([(132, 120), (132, 106), (204, 106), (204, 120)], "#7a4f9a", 4))
b.append(text(168, 100, "ligação", 11, "#5a3a7a", True, "middle"))
b.append(wire([(64, 120), (64, 112), (28, 112), (28, 230), (90, 230)], BLK)); b.append(wire([(272, 120), (272, 112), (312, 112), (312, 230), (250, 230)], RED))
b.append(rect(90, 206, 160, 48, "#fff4e5", "#ef8a2b", 2, 8))
b.append(text(170, 228, "24 V · 100 Ah", 15, "#222", True, "middle")); b.append(text(170, 246, "a TENSÃO soma", 12, "#b35c00", True, "middle"))
# --- baterias em paralelo (a 2a desenhada com + a esquerda para os fios nao se cruzarem) ---
b.append(battery(380, 130)); b.append(battery(530, 130, flip=True))
b.append(wire([(404, 120), (404, 96), (612, 96), (612, 120)], BLK))
b.append(wire([(472, 120), (472, 108), (544, 108), (544, 120)], RED))
b.append(wire([(404, 120), (404, 112), (368, 112), (368, 230), (430, 230)], BLK))
b.append(wire([(508, 108), (508, 206)], RED))
b.append(rect(430, 206, 160, 48, "#fff4e5", "#ef8a2b", 2, 8))
b.append(text(510, 228, "12 V · 200 Ah", 15, "#222", True, "middle")); b.append(text(510, 246, "a CAPACIDADE soma", 12, "#b35c00", True, "middle"))
b.append(text(510, 276, "2 baterias de 12 V · 100 Ah", 11, "#444", False, "middle"))
b.append(text(170, 276, "2 baterias de 12 V · 100 Ah", 11, "#444", False, "middle"))
# --- paineis em serie ---
b.append(panel(36, 330)); b.append(panel(184, 330))
b.append(wire([(156, 352), (184, 352)], "#7a4f9a", 4))
b.append(text(170, 322, "+ → −", 11, "#5a3a7a", True, "middle"))
b.append(wire([(36, 386), (24, 386), (24, 444), (90, 444)], BLK)); b.append(wire([(304, 386), (316, 386), (316, 444), (250, 444)], RED))
b.append(rect(90, 420, 160, 48, "#fff4e5", "#ef8a2b", 2, 8))
b.append(text(170, 442, "36 V · 5 A", 15, "#222", True, "middle")); b.append(text(170, 460, "a TENSÃO soma", 12, "#b35c00", True, "middle"))
b.append(tlines(170, 488, ["fio mais fino; precisa de", "controlador MPPT"], 11.5, "#333", False, 14, "middle"))
# --- paineis em paralelo ---
b.append(panel(376, 314)); b.append(panel(524, 314))
b.append(text(420, 400, "−", 13, "#222", True, "end") if False else "")
b.append(wire([(420, 384), (420, 410), (584, 410), (584, 384)], BLK))
b.append(wire([(436, 384), (436, 396), (568, 396), (568, 384)], RED))
b.append(wire([(420, 410), (420, 444), (430, 444)], BLK))
b.append(wire([(510, 396), (510, 384), (510, 306), (656, 306), (656, 444), (590, 444)], RED))
b.append(rect(430, 420, 160, 48, "#fff4e5", "#ef8a2b", 2, 8))
b.append(text(510, 442, "18 V · 10 A", 15, "#222", True, "middle")); b.append(text(510, 460, "a CORRENTE soma", 12, "#b35c00", True, "middle"))
b.append(tlines(510, 488, ["serve para controlador PWM", "com bateria de 12 V"], 11.5, "#333", False, 14, "middle"))
b.append(text(170, 306, "2 painéis de 18 V · 5 A (≈ 90 W)", 11, "#444", False, "middle"))
b.append(text(510, 470 + 0, "", 11))
b.append(box(20, 526, 640, 44, "#fdecea", DANGER))
b.append(tlines(34, 545, ["Só junte peças IGUAIS (mesmo modelo, idade e carga). A energia total é a mesma",
                          "nos dois casos: 2 × 1,2 kWh = 2,4 kWh; 2 × 90 W = 180 W."], 12.5, "#7a1010", False, 16))
open(D + "serie-paralelo.svg", "w").write(svg(680, 580, "Ligação em série e em paralelo", "\n".join(b)))
print("ok eletrica")
