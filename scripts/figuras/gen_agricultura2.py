import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
import math
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "04-agricultura", "img") + "/"
os.makedirs(D, exist_ok=True)
# Figuras de 04-agricultura (parte 2): nível A, curva de nível, carneiro hidráulico,
# gotejamento por gravidade, garrafa PET e pote de barro enterrados.

SOIL = "#e8d3b0"; SOIL2 = "#c9a878"; DARKSOIL = "#6b4f2a"
GREEN = "#2b8a3e"; LG = "#8fd19e"; WOOD = "#8b5a2b"; RED = "#d62828"; RED2 = "#b3001b"
ORANGE = "#ef8a2b"; WATER = "#4a90d9"; WATERL = "#cfe6fb"; PIPE = "#9a9a9a"; PVC = "#e6e6e6"

def lines(x, y, txts, size=12, color="#222", bold_first=False, anchor="start", lh=None):
    lh = lh or size + 3
    return "".join(text(x, y + i * lh, t, size, color, bold_first and i == 0, anchor) for i, t in enumerate(txts))

def dim_h(x1, x2, y, label, size=12, color="#333", above=True):
    ty = y - 6 if above else y + size + 4
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="1.5"/>'
            f'<line x1="{x1}" y1="{y-6}" x2="{x1}" y2="{y+6}" stroke="{color}" stroke-width="1.5"/>'
            f'<line x1="{x2}" y1="{y-6}" x2="{x2}" y2="{y+6}" stroke="{color}" stroke-width="1.5"/>'
            + text((x1 + x2) / 2, ty, label, size, color, True, "middle"))

def dim_v(x, y1, y2, label, size=12, color="#333", side="right"):
    tx = x + 8 if side == "right" else x - 8
    an = "start" if side == "right" else "end"
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{color}" stroke-width="1.5"/>'
            f'<line x1="{x-6}" y1="{y1}" x2="{x+6}" y2="{y1}" stroke="{color}" stroke-width="1.5"/>'
            f'<line x1="{x-6}" y1="{y2}" x2="{x+6}" y2="{y2}" stroke="{color}" stroke-width="1.5"/>'
            + text(tx, (y1 + y2) / 2 + 4, label, size, color, True, an))

def leader(x1, y1, x2, y2, color="#555"):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.2"/>'
            f'<circle cx="{x2}" cy="{y2}" r="2.5" fill="{color}"/>')

def num(x, y, n, color=ORANGE):
    return (f'<circle cx="{x}" cy="{y}" r="11" fill="{color}" stroke="#1e1e1e" stroke-width="1.5"/>'
            + text(x, y + 4.5, str(n), 13, "#fff", True, "middle"))

def plant(x, y, s=1.0):
    return (f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y-14*s}" stroke="{GREEN}" stroke-width="2.5"/>'
            f'<ellipse cx="{x-8*s}" cy="{y-16*s}" rx="{9*s}" ry="{5*s}" fill="{LG}" stroke="{GREEN}" stroke-width="1.5" transform="rotate(-25 {x-8*s} {y-16*s})"/>'
            f'<ellipse cx="{x+8*s}" cy="{y-16*s}" rx="{9*s}" ry="{5*s}" fill="{LG}" stroke="{GREEN}" stroke-width="1.5" transform="rotate(25 {x+8*s} {y-16*s})"/>'
            f'<ellipse cx="{x}" cy="{y-24*s}" rx="{5*s}" ry="{8*s}" fill="{LG}" stroke="{GREEN}" stroke-width="1.5"/>')

def drop(x, y, s=1.0):
    return f'<path d="M{x} {y} q {-5*s} {8*s} 0 {12*s} q {5*s} {-4*s} 0 {-12*s} Z" fill="{WATER}" stroke="#2a5d93" stroke-width="1"/>'

def aframe(fx1, fy1, fx2, fy2, h, plumb_dx=0, lw=7, mark=True):
    """Nível A com pés em (fx1,fy1) e (fx2,fy2); altura h; o fio de prumo desloca plumb_dx na travessa."""
    ax, ay = (fx1 + fx2) / 2, min(fy1, fy2) - h
    s = ""
    for fx, fy in ((fx1, fy1), (fx2, fy2)):
        ex, ey = ax + (ax - fx) * 0.08, ay + (ay - fy) * 0.08
        s += f'<line x1="{fx}" y1="{fy}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{WOOD}" stroke-width="{lw}" stroke-linecap="round"/>'
    # travessa no meio da altura
    t = 0.5
    lx, ly = fx1 + (ax - fx1) * t, fy1 + (ay - fy1) * t
    rx, ry = fx2 + (ax - fx2) * t, fy2 + (ay - fy2) * t
    s += f'<line x1="{lx-6:.1f}" y1="{ly:.1f}" x2="{rx+6:.1f}" y2="{ry:.1f}" stroke="#a0703a" stroke-width="{lw-1}" stroke-linecap="round"/>'
    cx, cy = (lx + rx) / 2, (ly + ry) / 2
    if mark:
        s += f'<line x1="{cx:.1f}" y1="{cy-7:.1f}" x2="{cx:.1f}" y2="{cy+7:.1f}" stroke="{RED}" stroke-width="2.5"/>'
    # fio de prumo
    px, py = cx + plumb_dx, cy + h * 0.28
    s += f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{px:.1f}" y2="{py:.1f}" stroke="#333" stroke-width="1.3"/>'
    s += f'<circle cx="{px:.1f}" cy="{py+5:.1f}" r="{max(4, lw-1)}" fill="#777" stroke="#1e1e1e" stroke-width="1.5"/>'
    return s, (cx, cy)

def aframe_rot(fx, fy, span, h, theta, lw=5, marks=()):
    """Nível A com pé esquerdo em (fx,fy), abertura span, altura h, inclinado theta graus
    (horário). O fio de prumo fica sempre na vertical. marks: lista de (cor, deslocamento
    local na travessa a partir do centro). Retorna (svg, deslocamento local onde o fio cruza)."""
    th = math.radians(theta)
    def rot(x, y):
        dx, dy = x - fx, y - fy
        return fx + dx * math.cos(th) - dy * math.sin(th), fy + dx * math.sin(th) + dy * math.cos(th)
    ax_l, ay_l = fx + span / 2, fy - h
    s = f'<g transform="rotate({theta} {fx} {fy})">'
    for x in (fx, fx + span):
        ex, ey = ax_l + (ax_l - x) * 0.08, ay_l + (ay_l - fy) * 0.08
        s += f'<line x1="{x}" y1="{fy}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{WOOD}" stroke-width="{lw}" stroke-linecap="round"/>'
    cyl = fy - h / 2
    s += f'<line x1="{fx + span/4 - 6}" y1="{cyl}" x2="{fx + 3*span/4 + 6}" y2="{cyl}" stroke="#a0703a" stroke-width="{lw-1}" stroke-linecap="round"/>'
    for col, off in marks:
        s += f'<line x1="{ax_l+off}" y1="{cyl-8}" x2="{ax_l+off}" y2="{cyl+8}" stroke="{col}" stroke-width="3.5"/>'
    s += '</g>'
    axg, ayg = rot(ax_l, ay_l)
    # onde o fio vertical cruza a travessa (em coordenadas locais)
    # ponto do fio: (axg, ayg + t); converter para local e achar y_local = cyl
    best = None
    for t10 in range(0, int(h * 10)):
        t = t10 / 10
        gx, gy_ = axg, ayg + t
        dx, dy = gx - fx, gy_ - fy
        lx = fx + dx * math.cos(-th) - dy * math.sin(-th)
        ly = fy + dx * math.sin(-th) + dy * math.cos(-th)
        if best is None or abs(ly - cyl) < abs(best[1] - cyl):
            best = (lx, ly)
    s += f'<line x1="{axg:.1f}" y1="{ayg:.1f}" x2="{axg:.1f}" y2="{ayg + h*0.8:.1f}" stroke="#333" stroke-width="1.3"/>'
    s += f'<circle cx="{axg:.1f}" cy="{ayg + h*0.8 + 4:.1f}" r="{max(4, lw-1)}" fill="#777" stroke="#1e1e1e" stroke-width="1.5"/>'
    return s, best[0] - ax_l

# =====================================================================
# 1. NÍVEL "A" (PÉ-DE-GALINHA): CONSTRUÇÃO E CALIBRAGEM
# =====================================================================
b = []
b.append(text(20, 62, "Como fazer", 15, "#222", True))
b.append(f'<line x1="20" y1="400" x2="322" y2="400" stroke="{DARKSOIL}" stroke-width="3"/>')
s, _ = aframe_rot(110, 400, 200, 222, 0, 9, [(RED, 0)])
b.append(s)
b.append(dim_h(110, 310, 424, "2 m entre os pés", 12, "#333", False))
b.append(lines(20, 120, ["amarre ou pregue", "bem firme no topo"], 11.5, "#333", True))
b.append(leader(120, 130, 204, 172))
b.append(lines(20, 196, ["pernas de", "2 a 2,2 m (ripa,", "bambu, caibro)"], 11.5, "#333", True))
b.append(leader(112, 214, 192, 248))
b.append(lines(20, 262, ["fio de prumo:", "barbante + pedra"], 11.5, "#333", True))
b.append(leader(124, 266, 209, 270))
b.append(lines(20, 316, ["travessa a", "meia altura"], 11.5, "#333", True))
b.append(leader(96, 312, 166, 290))
b.append(lines(222, 330, ["marca", "do nível"], 11.5, RED2, True))
b.append(leader(232, 318, 212, 296, RED2))
b.append(f'<line x1="334" y1="56" x2="334" y2="450" stroke="#bbb" stroke-width="1"/>')
# calibragem
b.append(text(346, 62, "Como achar a marca do nível", 15, "#222", True))
def ground_seg(x0, y0, theta, span):
    th = math.radians(theta)
    x1, y1 = x0 + span * math.cos(th), y0 + span * math.sin(th)
    return (f'<line x1="{x0-12}" y1="{y0 - 12*math.tan(th):.1f}" x2="{x1+12:.1f}" y2="{y1 + 12*math.tan(th):.1f}" stroke="{DARKSOIL}" stroke-width="2"/>'
            f'<rect x="{x0-3}" y="{y0-2}" width="6" height="10" fill="#555"/><rect x="{x1-3:.1f}" y="{y1-2:.1f}" width="6" height="10" fill="#555"/>')
TH = 9
# passo 1: pernas E (esq.) e D (dir.)
b.append(num(352, 82, 1))
b.append(ground_seg(372, 150, TH, 96))
s1, off1 = aframe_rot(372, 150, 96, 76, TH, 5)
b.append(s1)
s1, _ = aframe_rot(372, 150, 96, 76, TH, 5, [(ORANGE, off1)])
b.append(s1)
b.append(text(380, 140, "E", 11, "#1e1e1e", True, "middle")); b.append(text(462, 148, "D", 11, "#1e1e1e", True, "middle"))
b.append(lines(486, 92, ["Ponha o A no chão e", "crave uma estaca em", "cada pé. Risque na", "travessa onde o fio", "passa: marca 1."], 12))
# passo 2: virado (D à esquerda); a marca 1 aparece espelhada
b.append(num(352, 202, 2))
b.append(ground_seg(372, 270, TH, 96))
s2, off2 = aframe_rot(372, 270, 96, 76, TH, 5, [(ORANGE, -off1), ("#7048e8", off1)])
b.append(s2)
b.append(text(380, 260, "D", 11, "#1e1e1e", True, "middle")); b.append(text(462, 268, "E", 11, "#1e1e1e", True, "middle"))
b.append(lines(486, 212, ["VIRE o A: o pé E vai", "para a estaca do D e", "vice-versa. O fio cai", "em outro ponto da", "travessa: marca 2."], 12))
# passo 3: travessa ampliada
b.append(num(352, 318, 3))
b.append(f'<rect x="372" y="334" width="200" height="20" rx="4" fill="#a0703a" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(f'<line x1="430" y1="328" x2="430" y2="360" stroke="{ORANGE}" stroke-width="3"/>')
b.append(f'<line x1="514" y1="328" x2="514" y2="360" stroke="#7048e8" stroke-width="3"/>')
b.append(f'<line x1="472" y1="322" x2="472" y2="366" stroke="{RED}" stroke-width="4"/>')
b.append(text(430, 378, "1", 12, ORANGE, True, "middle")); b.append(text(514, 378, "2", 12, "#7048e8", True, "middle"))
b.append(text(472, 394, "NÍVEL (meio)", 12.5, RED2, True, "middle"))
b.append(lines(584, 336, ["Marque o", "MEIO entre", "1 e 2.", "Pinte bem."], 12))
b.append(box(346, 404, 320, 46, "#eaf6ec", GREEN))
b.append(lines(358, 423, ["Fio na marca do meio = os dois pés", "estão na mesma altura (em nível)."], 12, "#1e5e2a", True))
open(D + "nivel-a.svg", "w").write(svg(680, 462, "Nível “A” (pé-de-galinha)", "\n".join(b)))

# =====================================================================
# 2. MARCAR CURVA DE NÍVEL E MEDIR DECLIVIDADE
# =====================================================================
b = []
b.append(text(20, 62, "1. Medir a declividade do terreno (vista de lado)", 14, "#222", True))
def gy(x): return 150 + (x - 20) * 0.2
b.append(f'<polygon points="20,{gy(20)} 420,{gy(420)} 420,250 20,250" fill="{SOIL}"/>')
b.append(f'<line x1="20" y1="{gy(20)}" x2="420" y2="{gy(420)}" stroke="{DARKSOIL}" stroke-width="3"/>')
fx1, fx2 = 150, 310
fy = gy(fx1)
s, _ = aframe_rot(fx1, fy, fx2 - fx1, 90, 0, 6, [(RED, 0)])
b.append(s)
b.append(f'<line x1="{fx2+12}" y1="{fy}" x2="{fx2+12}" y2="{gy(fx2)}" stroke="{RED}" stroke-width="2"/>')
b.append(f'<line x1="{fx2+6}" y1="{fy}" x2="{fx2+18}" y2="{fy}" stroke="{RED}" stroke-width="2"/>')
b.append(f'<line x1="{fx2+6}" y1="{gy(fx2)}" x2="{fx2+18}" y2="{gy(fx2)}" stroke="{RED}" stroke-width="2"/>')
b.append(text(fx2 + 22, (fy + gy(fx2)) / 2 + 5, "h", 15, RED2, True))
b.append(lines(440, 92, ["Apoie o pé de CIMA no chão.", "Levante o pé de BAIXO até o", "fio ficar na marca do nível.", "Meça a altura h (em cm)."], 12))
b.append(box(440, 160, 225, 62, "#fff4e5", ORANGE))
b.append(lines(452, 182, ["Declividade (%) = h ÷ 2", "Ex.: h = 20 cm → 10 %", "(vale para A de 2 m)"], 12.5, "#222", True))
# ---------- vista de cima ----------
b.append('<line x1="20" y1="266" x2="660" y2="266" stroke="#bbb" stroke-width="1"/>')
b.append(text(20, 290, "2. Marcar a curva de nível (vista de cima)", 14, "#222", True))
TY0, TY1 = 306, 530
b.append(f'<rect x="20" y="{TY0}" width="520" height="{TY1-TY0}" fill="#e6f0d6" stroke="#999" stroke-width="1"/>')
def cy_(x, base): return base + 22 * math.sin((x - 20) / 85.0) + 0.04 * (x - 20)
for base in (330, 366, 440, 476):
    pts = " ".join(f"{x},{cy_(x, base):.1f}" for x in range(20, 541, 10))
    b.append(f'<polyline points="{pts}" fill="none" stroke="#b9c7a5" stroke-width="1.5"/>')
CB = 402
pts = " ".join(f"{x},{cy_(x, CB):.1f}" for x in range(20, 541, 10))
b.append(f'<polyline points="{pts}" fill="none" stroke="{GREEN}" stroke-width="3" stroke-dasharray="8 5"/>')
stakes = list(range(50, 531, 60))
for i, x in enumerate(stakes):
    y = cy_(x, CB)
    if i == 2:
        x2 = stakes[i + 1]; y2 = cy_(x2, CB)
        b.append(f'<line x1="{x}" y1="{y:.1f}" x2="{x2}" y2="{y2:.1f}" stroke="{WOOD}" stroke-width="7" stroke-linecap="round"/>')
        b.append(text((x + x2) / 2 + 6, (y + y2) / 2 - 14, "o A", 12, WOOD, True, "middle"))
    b.append(f'<circle cx="{x}" cy="{y:.1f}" r="6" fill="#fff" stroke="#1e1e1e" stroke-width="2.5"/>')
    b.append(text(x, y + 22, str(i + 1), 11, "#1e1e1e", True, "middle"))
b.append(f'<line x1="560" y1="480" x2="560" y2="330" stroke="#555" stroke-width="3"/>')
b.append(f'<polygon points="560,318 552,334 568,334" fill="#555"/>')
b.append(lines(572, 340, ["morro", "acima"], 12, "#333", True))
b.append(lines(572, 480, ["morro", "abaixo"], 12, "#333", True))
b.append(lines(572, 396, ["linha", "verde =", "curva de", "nível"], 12, GREEN, True))
b.append(lines(20, 552, ["Crave a estaca 1. Ponha um pé do A nela e gire o outro pé, para cima ou para baixo do morro,",
                         "até o fio parar na marca do meio: crave a estaca 2. Leve o A para a frente e repita. Depois",
                         "acerte estacas fora da linha para a curva ficar suave. Plante e faça valas seguindo a linha."], 12.5))
open(D + "curva-de-nivel.svg", "w").write(svg(680, 604, "Curva de nível com o nível “A”", "\n".join(b)))

# =====================================================================
# 3. CARNEIRO HIDRÁULICO: O SISTEMA
# =====================================================================
b = []
ground = "0,190 120,196 200,250 300,310 380,322 460,300 560,170 660,100 680,96 680,390 0,390"
b.append(f'<polygon points="{ground}" fill="{SOIL}" stroke="{DARKSOIL}" stroke-width="2.5"/>')
b.append(f'<path d="M0 186 Q 50 194 100 188 L100 196 L0 196 Z" fill="{WATER}"/>')
b.append(lines(10, 150, ["fonte ou", "córrego"], 12, "#1e4e86", True))
b.append(f'<rect x="96" y="160" width="56" height="44" fill="#ddd" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<rect x="98" y="176" width="52" height="26" fill="{WATERL}"/>')
b.append(f'<line x1="98" y1="176" x2="150" y2="176" stroke="{WATER}" stroke-width="2"/>')
b.append(lines(100, 120, ["caixa de captação", "com tela (folhas)"], 11.5, "#333", True))
b.append(leader(124, 136, 124, 160))
# tubo de alimentação
b.append(f'<line x1="150" y1="198" x2="318" y2="306" stroke="#555" stroke-width="9" stroke-linecap="round"/>')
b.append(f'<line x1="150" y1="198" x2="318" y2="306" stroke="#bfbfbf" stroke-width="5" stroke-linecap="round"/>')
b.append(lines(20, 300, ["tubo de alimentação:", "RETO e rígido; comprimento", "de 5 a 10 vezes a queda"], 11.5, "#333", True))
b.append(leader(150, 296, 214, 240))
# carneiro
b.append(f'<rect x="312" y="300" width="56" height="14" fill="{PVC}" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<rect x="352" y="244" width="22" height="58" rx="5" fill="{PVC}" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<rect x="326" y="286" width="12" height="14" fill="#c08a2a" stroke="#1e1e1e" stroke-width="1.5"/>')
for dx in (-10, 0, 10):
    b.append(f'<path d="M332 284 q {dx} -14 {dx*1.8} -22" fill="none" stroke="{WATER}" stroke-width="2"/>')
b.append(text(345, 340, "CARNEIRO", 13, "#1e1e1e", True, "middle"))
b.append(f'<path d="M322 318 Q 370 326 440 312" fill="none" stroke="{WATER}" stroke-width="5"/>')
b.append(lines(470, 336, ["a sobra (80–90 % da", "água) volta ao córrego"], 11.5, "#1e4e86", True))
b.append(leader(468, 334, 436, 316, "#1e4e86"))
# recalque
b.append(f'<path d="M374 252 Q 420 250 470 290 L 560 166 L 604 132 L 604 90" fill="none" stroke="#2f2f2f" stroke-width="5" stroke-linejoin="round"/>')
b.append(f'<path d="M374 252 Q 420 250 470 290 L 560 166 L 604 132 L 604 90" fill="none" stroke="{WATER}" stroke-width="2" stroke-dasharray="6 6"/>')
b.append(lines(540, 262, ["tubo de recalque", "(mangueira ½\" ou ¾\")"], 11.5, "#333", True))
b.append(leader(538, 258, 515, 230))
b.append(f'<rect x="600" y="52" width="66" height="40" fill="#2f6aa8" stroke="#1e1e1e" stroke-width="2"/>')
b.append(text(633, 77, "caixa", 12, "#fff", True, "middle"))
# cotas H e h
b.append(f'<line x1="150" y1="176" x2="256" y2="176" stroke="#555" stroke-width="1" stroke-dasharray="4 3"/>')
b.append(f'<line x1="250" y1="314" x2="400" y2="314" stroke="#555" stroke-width="1" stroke-dasharray="4 3"/>')
b.append(dim_v(250, 176, 314, "", 15, RED2))
b.append(lines(258, 196, ["H = QUEDA", "(1 a 5 m)"], 12.5, RED2, True))
b.append(f'<line x1="400" y1="72" x2="596" y2="72" stroke="#555" stroke-width="1" stroke-dasharray="4 3"/>')
b.append(dim_v(400, 72, 314, "", 15, "#1e4e86"))
b.append(lines(410, 112, ["h = ALTURA que a", "água sobe (até", "cerca de 10 × H)"], 12.5, "#1e4e86", True))
b.append(box(20, 402, 640, 64, "#eef5ff", "#3f6d9e"))
b.append(lines(34, 423, ["Água que chega lá em cima ≈ água que entra × H ÷ h × 0,6",
                         "Ex.: entram 20 L/min, H = 2 m, h = 16 m → 20 × 2 ÷ 16 × 0,6 = 1,5 L/min ≈ 2.100 L por dia.",
                         "Funciona dia e noite, sem luz nem combustível. (Desenho fora de escala.)"], 12.5, "#222", True))
open(D + "carneiro-hidraulico.svg", "w").write(svg(680, 478, "Carneiro hidráulico: o sistema", "\n".join(b)))

# =====================================================================
# 4. CARNEIRO HIDRÁULICO: AS PEÇAS
# =====================================================================
b = []
PY = 300
def pipe_h(x1, x2, y, d=26, fill=PVC):
    return f'<rect x="{x1}" y="{y-d/2}" width="{x2-x1}" height="{d}" fill="{fill}" stroke="#1e1e1e" stroke-width="2"/>'
def pipe_v(x, y1, y2, d=26, fill=PVC):
    return f'<rect x="{x-d/2}" y="{y1}" width="{d}" height="{y2-y1}" fill="{fill}" stroke="#1e1e1e" stroke-width="2"/>'
def flow(x1, y1, x2, y2):
    return arrow(x1, y1, x2, y2, "#1c64b8", 3)
b.append(pipe_h(20, 150, PY, 26, "#cfcfcf"))
b.append(flow(36, PY, 92, PY))
b.append(text(85, PY + 34, "vem da fonte", 11.5, "#333", True, "middle"))
b.append(f'<rect x="150" y="{PY-17}" width="30" height="34" rx="3" fill="#c08a2a" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<line x1="165" y1="{PY-17}" x2="165" y2="{PY-36}" stroke="#1e1e1e" stroke-width="3"/>')
b.append(f'<rect x="153" y="{PY-42}" width="24" height="7" rx="3" fill="{RED}" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(pipe_h(180, 420, PY))
b.append(flow(196, PY, 250, PY))
VX = 290
b.append(pipe_v(VX, PY - 70, PY - 12, 26))
b.append(f'<rect x="{VX-20}" y="{PY-100}" width="40" height="32" rx="4" fill="#d9a441" stroke="#1e1e1e" stroke-width="2"/>')
for dx in (-14, 0, 14):
    b.append(f'<path d="M{VX} {PY-102} q {dx} -18 {dx*2.2} -34" fill="none" stroke="{WATER}" stroke-width="2.5"/>')
b.append(text(VX, PY - 150, "a água sai aqui", 11.5, "#1e4e86", True, "middle"))
CX = 400
b.append(pipe_v(CX, PY - 90, PY - 12, 26))
b.append(f'<rect x="{CX-20}" y="{PY-80}" width="40" height="30" rx="4" fill="#7fb36a" stroke="#1e1e1e" stroke-width="2"/>')
b.append(flow(CX, PY - 20, CX, PY - 76))
# câmara de ar
CT = PY - 238
b.append(f'<rect x="{CX-34}" y="{CT}" width="68" height="150" rx="10" fill="#fff" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<rect x="{CX-32}" y="{PY-150}" width="64" height="60" fill="{WATERL}"/>')
b.append(f'<line x1="{CX-32}" y1="{PY-150}" x2="{CX+32}" y2="{PY-150}" stroke="{WATER}" stroke-width="2"/>')
b.append(text(CX, CT + 40, "AR", 16, "#555", True, "middle"))
b.append(text(CX, CT + 56, "(mola)", 11, "#555", False, "middle"))
b.append(text(CX, PY - 112, "água", 12, "#1e4e86", True, "middle"))
b.append(pipe_h(CX + 34, 600, PY - 104, 16, "#3a3a3a"))
b.append(f'<rect x="520" y="{PY-118}" width="22" height="28" rx="3" fill="#c08a2a" stroke="#1e1e1e" stroke-width="2"/>')
b.append(flow(560, PY - 104, 650, PY - 104))
b.append(lines(560, PY - 134, ["para a caixa", "lá em cima"], 11.5, "#1e4e86", True))
b.append(f'<rect x="420" y="{PY-15}" width="10" height="30" fill="#bbb" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<rect x="170" y="{PY+16}" width="270" height="18" fill="#b5b5b5" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(text(305, PY + 52, "base firme (concreto ou estacas): ele vibra", 11.5, "#222", True, "middle"))
b.append(num(165, PY - 60, 1)); b.append(num(VX - 40, PY - 86, 2)); b.append(num(CX + 40, PY - 64, 3))
b.append(num(CX - 50, CT + 20, 4)); b.append(num(531, PY - 132, 5))
lx, ly = 20, 386
items = [(1, "Registro: abre e fecha a entrada de água."),
         (2, "Válvula de impulso (de escape): fica ABERTA parada; a água rápida a FECHA."),
         (3, "Válvula de retenção: deixa a água subir para a câmara e não deixa voltar."),
         (4, "Câmara de ar: tubo largo (75–100 mm), 60–100 cm, tampado em cima."),
         (5, "Saída para o tubo de recalque, com registro.")]
for i, (n, t) in enumerate(items):
    b.append(num(lx + 10, ly - 4 + i * 24, n)); b.append(text(lx + 28, ly + i * 24, t, 12.5))
b.append(box(20, 506, 640, 112, "#eef5ff", "#3f6d9e"))
b.append(text(34, 528, "Como funciona (repete 40 a 80 vezes por minuto):", 13, "#1e4e86", True))
b.append(lines(34, 548, ["a) A água desce pelo tubo e sai pela válvula de impulso (2), ganhando velocidade.",
                         "b) A água rápida fecha a válvula de uma vez (“tac”): a pancada (golpe de aríete) sobe a pressão.",
                         "c) A pressão abre a retenção (3) e empurra um pouco de água para a câmara (4); o ar",
                         "    comprimido empurra essa água morro acima, sem parar. A válvula (2) reabre e tudo recomeça."], 12.5))
open(D + "carneiro-hidraulico-pecas.svg", "w").write(svg(680, 630, "Carneiro hidráulico: as peças", "\n".join(b)))

# =====================================================================
# 5. GOTEJAMENTO POR GRAVIDADE
# =====================================================================
b = []
GY = 330
b.append(f'<rect x="0" y="{GY}" width="680" height="40" fill="{SOIL}"/>')
b.append(f'<line x1="0" y1="{GY}" x2="680" y2="{GY}" stroke="{DARKSOIL}" stroke-width="2"/>')
# estrado de madeira
for x in (52, 148):
    b.append(f'<rect x="{x}" y="180" width="12" height="{GY-180}" fill="{WOOD}" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(f'<rect x="40" y="172" width="136" height="12" fill="{WOOD}" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(f'<line x1="58" y1="300" x2="154" y2="210" stroke="{WOOD}" stroke-width="6"/>')
# tambor
b.append(f'<rect x="44" y="76" width="122" height="96" rx="6" fill="#2f6aa8" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<rect x="48" y="96" width="114" height="72" fill="#6aa6e0"/>')
b.append(f'<rect x="40" y="70" width="130" height="10" rx="3" fill="#24527f" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(text(105, 140, "tambor ou", 11.5, "#fff", True, "middle"))
b.append(text(105, 154, "caixa TAMPADA", 11, "#fff", True, "middle"))
# saída: filtro, registro, mangueira
b.append(f'<rect x="166" y="150" width="14" height="10" fill="#555"/>')
b.append(f'<rect x="180" y="144" width="20" height="22" rx="3" fill="#f2f2f2" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(f'<path d="M184 148 l12 14 M184 162 l12 -14" stroke="#999" stroke-width="1"/>')
b.append(f'<rect x="204" y="146" width="16" height="18" rx="2" fill="#c08a2a" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(f'<path d="M220 155 L240 155 Q 250 155 250 170 L250 {GY-14} Q 250 {GY-6} 262 {GY-6} L 640 {GY-6}" fill="none" stroke="#222" stroke-width="7" stroke-linejoin="round"/>')
b.append(f'<line x1="640" y1="{GY-14}" x2="652" y2="{GY+2}" stroke="#222" stroke-width="5"/>')
# plantas e gotas
for x in range(300, 630, 60):
    b.append(plant(x, GY - 10, 1.1))
    b.append(drop(x + 12, GY - 2, 0.9))
    b.append(f'<ellipse cx="{x+10}" cy="{GY+16}" rx="22" ry="12" fill="#2f86e0" fill-opacity="0.45"/>')
b.append(dim_v(30, 172, GY, "", 12))
b.append(lines(24, 244, ["1 a", "2 m"], 12.5, "#222", True, "end"))
# rótulos
b.append(lines(182, 104, ["filtro (pano ou tela)", "e registro na saída"], 11.5, "#333", True))
b.append(leader(188, 112, 190, 142))
b.append(lines(270, 218, ["mangueira preta ½\" (16 mm)", "ou fita gotejadora, EM NÍVEL"], 11.5, "#333", True))
b.append(leader(330, 226, 330, GY - 10))
b.append(lines(420, 262, ["furo de 1 mm (agulha quente) ou", "gotejador junto de cada planta"], 11.5, "#1e4e86", True))
b.append(lines(560, 384, ["ponta dobrada", "e amarrada"], 11.5, "#333", True))
b.append(leader(600, 372, 646, GY - 4))
b.append(box(20, 404, 640, 74, "#eef5ff", "#3f6d9e"))
b.append(lines(34, 425, ["Cada linha: até 15–20 m, sem subida. Quanto mais alto o tambor, mais forte e igual a vazão.",
                         "Quanto gastar: horta no calor ≈ 4–6 L por m² por dia. Um tambor de 200 L rega ~40 m²/dia.",
                         "Meça: ponha um copo sob 3 furos (começo, meio, fim) por 10 minutos e compare."], 12.5))
open(D + "gotejamento-gravidade.svg", "w").write(svg(680, 490, "Gotejamento por gravidade (sem bomba)", "\n".join(b)))

# =====================================================================
# 6. GARRAFA PET E POTE DE BARRO ENTERRADOS
# =====================================================================
b = []
GY = 196
for x0 in (20, 350):
    b.append(f'<rect x="{x0}" y="{GY}" width="310" height="190" fill="{SOIL}"/>')
    b.append(f'<line x1="{x0}" y1="{GY}" x2="{x0+310}" y2="{GY}" stroke="{DARKSOIL}" stroke-width="2"/>')
b.append(f'<line x1="340" y1="50" x2="340" y2="470" stroke="#bbb" stroke-width="1"/>')
b.append(text(175, 64, "A) Garrafa PET de cabeça para baixo", 13, "#222", True, "middle"))
# planta (tomate) e raízes
b.append(f'<line x1="100" y1="{GY}" x2="100" y2="{GY-90}" stroke="{GREEN}" stroke-width="4"/>')
for yy, dx in ((GY - 30, -1), (GY - 55, 1), (GY - 80, -1)):
    b.append(f'<ellipse cx="{100+dx*22}" cy="{yy}" rx="20" ry="8" fill="{LG}" stroke="{GREEN}" stroke-width="1.5"/>')
b.append(f'<circle cx="80" cy="{GY-44}" r="7" fill="#e03131" stroke="#1e1e1e" stroke-width="1"/>')
for dx in (-24, -10, 6, 20):
    b.append(f'<path d="M100 {GY} q {dx} 30 {dx*1.5} 70" fill="none" stroke="#7a5d3a" stroke-width="1.5"/>')
# umidade
b.append(f'<ellipse cx="180" cy="{GY+80}" rx="74" ry="56" fill="#2f86e0" fill-opacity="0.4"/>')
# garrafa: corpo acima, gargalo enterrado
gx = 180
b.append(f'<path d="M{gx-26} {GY-80} L{gx-26} {GY+10} Q {gx-26} {GY+30} {gx-8} {GY+40} L{gx-8} {GY+62} L{gx+8} {GY+62} L{gx+8} {GY+40} Q {gx+26} {GY+30} {gx+26} {GY+10} L{gx+26} {GY-80} Z" fill="#e8f3fd" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<path d="M{gx-24} {GY-50} L{gx-24} {GY+10} Q {gx-24} {GY+28} {gx-6} {GY+38} L{gx-6} {GY+60} L{gx+6} {GY+60} L{gx+6} {GY+38} Q {gx+24} {GY+28} {gx+24} {GY+10} L{gx+24} {GY-50} Z" fill="#9fc5ec"/>')
b.append(f'<rect x="{gx-10}" y="{GY+60}" width="20" height="10" fill="#3f6d9e" stroke="#1e1e1e" stroke-width="1.5"/>')
for dx in (-5, 0, 5):
    b.append(drop(gx + dx, GY + 74, 0.6))
# fundo cortado como tampa
b.append(f'<path d="M{gx-30} {GY-84} Q {gx} {GY-98} {gx+30} {GY-84}" fill="#e8f3fd" stroke="#1e1e1e" stroke-width="2"/>')
b.append(lines(214, 104, ["o fundo cortado", "vira tampa"], 11.5, "#333", True))
b.append(leader(232, 110, gx + 20, GY - 90))
b.append(lines(214, 160, ["garrafa de 2 L", "sem o fundo"], 11.5, "#333", True))
b.append(dim_v(232, GY, GY + 62, "", 11))
b.append(lines(240, GY + 24, ["enterre", "10–15 cm"], 11.5, "#333", True))
b.append(lines(30, GY + 150, ["Tampa com 2–3 furinhos de agulha", "quente, a 10 cm do pé da planta.", "Encha por cima: dura 1 a 3 dias."], 12))
# ---------- pote ----------
b.append(text(505, 64, "B) Pote de barro enterrado", 13, "#222", True, "middle"))
px, pcy = 505, GY + 52
b.append(f'<ellipse cx="{px}" cy="{pcy+10}" rx="104" ry="76" fill="#2f86e0" fill-opacity="0.4"/>')
b.append(f'<path d="M{px-18} {GY-6} L{px-18} {GY+8} Q {px-56} {GY+18} {px-56} {pcy+10} Q {px-56} {pcy+62} {px} {pcy+62} Q {px+56} {pcy+62} {px+56} {pcy+10} Q {px+56} {GY+18} {px+18} {GY+8} L{px+18} {GY-6} Z" fill="#c2693e" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<path d="M{px-48} {pcy-4} Q {px-48} {pcy+54} {px} {pcy+54} Q {px+48} {pcy+54} {px+48} {pcy-4} Z" fill="#6aa6e0" fill-opacity="0.85"/>')
b.append(f'<ellipse cx="{px}" cy="{GY-10}" rx="30" ry="6" fill="#bbb" stroke="#1e1e1e" stroke-width="2"/>')
for dx in (-90, 90):
    b.append(plant(px + dx, GY, 1.2))
    for k in (-12, 0, 12):
        b.append(f'<path d="M{px+dx} {GY} q {k} 26 {k*1.6+(-10 if dx>0 else 10)} 56" fill="none" stroke="#7a5d3a" stroke-width="1.5"/>')
b.append(lines(360, 104, ["tampa: prato", "ou telha"], 11.5, "#333", True))
b.append(leader(400, 110, px - 26, GY - 12))
b.append(lines(560, 104, ["pote de barro", "SEM verniz,", "enterrado até", "o pescoço"], 11.5, "#333", True))
b.append(leader(560, 154, px + 20, GY + 10))
b.append(dim_h(px - 90, px, GY - 52, "20–40 cm", 11))
b.append(lines(360, GY + 150, ["A terra seca puxa a água pela parede", "do pote. Encha a cada 2 a 5 dias.", "Gasta 50–70 % menos água que regador."], 12))
b.append(box(20, 400, 640, 58, "#fff4e5", ORANGE))
b.append(lines(34, 422, ["Os dois molham a raiz, não a superfície: quase nada evapora e não molha a folha (menos doença).",
                         "Sempre tampados: água parada aberta vira criadouro do mosquito da dengue."], 12.5))
open(D + "garrafa-pote-enterrados.svg", "w").write(svg(680, 470, "Irrigação com garrafa PET e pote de barro", "\n".join(b)))
print("ok agricultura2")
