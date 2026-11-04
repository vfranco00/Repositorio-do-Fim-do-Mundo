import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
import math
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "04-agricultura", "img") + "/"
os.makedirs(D, exist_ok=True)
# Figuras de 04-agricultura (parte 3): enxertia por garfagem, enxertia por borbulhia,
# estratos da agrofloresta.

SOIL = "#e8d3b0"; DARKSOIL = "#6b4f2a"; GREEN = "#2b8a3e"; LG = "#8fd19e"
RED = "#d62828"; RED2 = "#b3001b"; ORANGE = "#ef8a2b"
BARK = "#8b6b4a"; WOODC = "#f3e3c0"; CAMB = "#5cb85c"

def lines(x, y, txts, size=12, color="#222", bold_first=False, anchor="start", lh=None):
    lh = lh or size + 3
    return "".join(text(x, y + i * lh, t, size, color, bold_first and i == 0, anchor) for i, t in enumerate(txts))

def num(x, y, n, color=ORANGE):
    return (f'<circle cx="{x}" cy="{y}" r="11" fill="{color}" stroke="#1e1e1e" stroke-width="1.5"/>'
            + text(x, y + 4.5, str(n), 13, "#fff", True, "middle"))

def leaf(x, y, ang, s=1.0):
    return f'<ellipse cx="{x}" cy="{y}" rx="{14*s}" ry="{6*s}" fill="{LG}" stroke="{GREEN}" stroke-width="1.5" transform="rotate({ang} {x} {y})"/>'

def bud(x, y, side=1):
    """gema na lateral de um ramo (side=1 direita, -1 esquerda)"""
    return f'<path d="M{x} {y} q {7*side} -2 {9*side} -10 q {-6*side} 2 {-9*side} 2 Z" fill="#6b8e23" stroke="#1e1e1e" stroke-width="1.2"/>'

def ground(x0, w, y):
    return (f'<rect x="{x0}" y="{y}" width="{w}" height="16" fill="{SOIL}"/>'
            f'<line x1="{x0}" y1="{y}" x2="{x0+w}" y2="{y}" stroke="{DARKSOIL}" stroke-width="2"/>')

def stock(cx, ytop, ybot, w=26, cut=True):
    """porta-enxerto (cavalo): caule com casca; topo cortado mostra a madeira"""
    s = f'<rect x="{cx-w/2}" y="{ytop}" width="{w}" height="{ybot-ytop}" fill="{BARK}" stroke="#1e1e1e" stroke-width="2"/>'
    if cut:
        s += f'<ellipse cx="{cx}" cy="{ytop}" rx="{w/2}" ry="4" fill="{WOODC}" stroke="#1e1e1e" stroke-width="1.5"/>'
    return s

def panel_frame(x, y, w, h):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#fbfbf8" stroke="#ccc" stroke-width="1.2"/>'

def wrap_band(cx, y1, y2, w):
    s = f'<rect x="{cx-w/2-2}" y="{y1}" width="{w+4}" height="{y2-y1}" fill="#dfe9f5" fill-opacity="0.9" stroke="#1e1e1e" stroke-width="1.5"/>'
    yy = y1 + 4
    while yy < y2 - 2:
        s += f'<line x1="{cx-w/2-2}" y1="{yy+6}" x2="{cx+w/2+2}" y2="{yy}" stroke="#6d8fb3" stroke-width="1.5"/>'
        yy += 8
    return s

# =====================================================================
# 1. ENXERTIA POR GARFAGEM (FENDA CHEIA)
# =====================================================================
b = []
PW, PH = 208, 250
pos = [(14, 50), (236, 50), (458, 50), (14, 312), (236, 312), (458, 312)]
GYo = 196   # chão relativo ao topo do painel
for i, (px, py) in enumerate(pos):
    b.append(panel_frame(px, py, PW, PH))
    b.append(num(px + 18, py + 18, i + 1))
    if i != 2:
        b.append(ground(px + 6, PW - 12, py + GYo))
# ---- 1: cortar o cavalo
px, py = pos[0]; cx = px + 104
b.append(stock(cx, py + 110, py + GYo, 26))
b.append(f'<rect x="{cx-13}" y="{py+44}" width="26" height="62" fill="none" stroke="#999" stroke-width="1.5" stroke-dasharray="5 4"/>')
b.append(f'<line x1="{cx-30}" y1="{py+110}" x2="{cx+30}" y2="{py+110}" stroke="{RED}" stroke-width="3"/>')
b.append(leaf(cx - 26, py + 150, -30)); b.append(leaf(cx + 26, py + 168, 30))
b.append(f'<line x1="{px+56}" y1="{py+110}" x2="{px+56}" y2="{py+GYo}" stroke="#333" stroke-width="1.5"/>')
b.append(f'<line x1="{px+50}" y1="{py+110}" x2="{px+62}" y2="{py+110}" stroke="#333" stroke-width="1.5"/>')
b.append(f'<line x1="{px+50}" y1="{py+GYo}" x2="{px+62}" y2="{py+GYo}" stroke="#333" stroke-width="1.5"/>')
b.append(lines(px + 48, py + 150, ["15–25", "cm"], 11, "#333", True, "end"))
b.append(lines(px + 104, py + 226, ["Corte o cavalo", "(porta-enxerto) reto"], 12, "#222", True, "middle"))
# ---- 2: fenda
px, py = pos[1]; cx = px + 104
b.append(stock(cx, py + 110, py + GYo, 26))
b.append(f'<line x1="{cx}" y1="{py+110}" x2="{cx}" y2="{py+146}" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(leaf(cx - 26, py + 160, -30)); b.append(leaf(cx + 26, py + 180, 30))
# canivete
b.append(f'<polygon points="{cx-2},{py+112} {cx+4},{py+112} {cx+10},{py+70} {cx-2},{py+66}" fill="#c9c9c9" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(f'<rect x="{cx-6}" y="{py+40}" width="18" height="28" rx="4" fill="#7a4a2a" stroke="#1e1e1e" stroke-width="1.5" transform="rotate(8 {cx} {py+54})"/>')
b.append(f'<line x1="{cx+16}" y1="{py+112}" x2="{cx+16}" y2="{py+146}" stroke="#333" stroke-width="1.5"/>')
b.append(text(cx + 22, py + 134, "3–4 cm", 11.5, "#333", True))
b.append(lines(px + 104, py + 226, ["Abra uma fenda de", "3–4 cm no meio"], 12, "#222", True, "middle"))
# ---- 3: garfo em cunha
px, py = pos[2]; cx = px + 104
gt, gb = py + 50, py + 196
b.append(f'<path d="M{cx-11} {gt} L{cx+11} {gt} L{cx+11} {gb-40} L{cx} {gb} L{cx-11} {gb-40} Z" fill="{BARK}" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<path d="M{cx-9} {gb-38} L{cx} {gb-4} L{cx+9} {gb-38} Z" fill="{WOODC}" stroke="#1e1e1e" stroke-width="1"/>')
b.append(f'<ellipse cx="{cx}" cy="{gt}" rx="11" ry="3.5" fill="{WOODC}" stroke="#1e1e1e" stroke-width="1.5"/>')
for yy, sd in ((gt + 26, 1), (gt + 60, -1), (gt + 94, 1)):
    b.append(bud(cx + 11 * sd, yy, sd))
b.append(f'<line x1="{cx+28}" y1="{gb-40}" x2="{cx+28}" y2="{gb}" stroke="#333" stroke-width="1.5"/>')
b.append(text(cx + 34, gb - 16, "cunha", 11.5, "#333", True)); b.append(text(cx + 34, gb - 2, "3 cm", 11.5, "#333", True))
b.append(lines(px + 152, gt + 30, ["2–3", "gemas"], 11.5, GREEN, True))
b.append(lines(px + 104, py + 210, ["Garfo de 10–15 cm, da", "planta boa; base em cunha"], 12, "#222", True, "middle"))
# ---- 4: encaixar
px, py = pos[3]; cx = px + 104
b.append(stock(cx, py + 120, py + GYo, 26))
gx = cx - 3   # garfo mais fino, encostado do lado esquerdo
b.append(f'<path d="M{gx-10} {py+54} L{gx+10} {py+54} L{gx+10} {py+120} L{gx-10} {py+120} Z" fill="{BARK}" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<path d="M{gx-10} {py+120} L{gx-10} {py+132} L{gx} {py+160} L{gx+10} {py+132} L{gx+10} {py+120}" fill="none" stroke="#1e1e1e" stroke-width="1.5" stroke-dasharray="4 3"/>')
b.append(f'<ellipse cx="{gx}" cy="{py+54}" rx="10" ry="3" fill="{WOODC}" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(bud(gx + 10, py + 80, 1)); b.append(bud(gx - 10, py + 100, -1))
b.append(f'<line x1="{cx-13}" y1="{py+112}" x2="{cx-13}" y2="{py+150}" stroke="{CAMB}" stroke-width="4"/>')
b.append(f'<line x1="{cx-34}" y1="{py+131}" x2="{cx-17}" y2="{py+131}" stroke="{GREEN}" stroke-width="2"/>')
b.append(lines(px + 14, py + 160, ["casca", "com", "casca"], 11.5, GREEN, True))
b.append(lines(px + 104, py + 226, ["Encaixe alinhando a casca", "(a linha verde por baixo)"], 12, "#222", True, "middle"))
# ---- 5: amarrar
px, py = pos[4]; cx = px + 104
b.append(stock(cx, py + 120, py + GYo, 26, cut=False))
b.append(f'<path d="M{cx-13} {py+54} L{cx+7} {py+54} L{cx+7} {py+120} L{cx-13} {py+120} Z" fill="{BARK}" stroke="#1e1e1e" stroke-width="2"/>')
b.append(bud(cx + 7, py + 76, 1)); b.append(bud(cx - 13, py + 96, -1))
b.append(wrap_band(cx, py + 108, py + 168, 26))
b.append(f'<path d="M{cx+30} {py+170} L{cx+30} {py+112}" stroke="{RED}" stroke-width="2.5"/>')
b.append(f'<polygon points="{cx+30},{py+104} {cx+24},{py+116} {cx+36},{py+116}" fill="{RED}"/>')
b.append(lines(cx + 38, py + 140, ["de baixo", "para cima"], 11, RED2, True))
b.append(lines(px + 104, py + 226, ["Amarre firme com fita", "plástica, cobrindo o corte"], 12, "#222", True, "middle"))
# ---- 6: saquinho
px, py = pos[5]; cx = px + 104
b.append(stock(cx, py + 120, py + GYo, 26, cut=False))
b.append(f'<path d="M{cx-13} {py+70} L{cx+7} {py+70} L{cx+7} {py+120} L{cx-13} {py+120} Z" fill="{BARK}" stroke="#1e1e1e" stroke-width="2"/>')
b.append(wrap_band(cx, py + 108, py + 168, 26))
b.append(f'<line x1="{cx+7}" y1="{py+86}" x2="{cx+22}" y2="{py+70}" stroke="{GREEN}" stroke-width="2.5"/>')
b.append(leaf(cx + 30, py + 64, -30, 0.7))
b.append(f'<path d="M{cx-16} {py+176} Q {cx-46} {py+120} {cx-34} {py+60} Q {cx} {py+30} {cx+40} {py+56} Q {cx+48} {py+120} {cx+16} {py+176} Z" fill="#e8f3fd" fill-opacity="0.55" stroke="#4a90d9" stroke-width="2"/>')
b.append(f'<line x1="{cx-18}" y1="{py+176}" x2="{cx+18}" y2="{py+176}" stroke="#1e1e1e" stroke-width="3"/>')
# broto ladrão a tirar
b.append(f'<line x1="{cx+13}" y1="{py+196}" x2="{cx+34}" y2="{py+186}" stroke="{GREEN}" stroke-width="2.5"/>')
b.append(leaf(cx + 42, py + 184, -10, 0.6))
b.append(f'<path d="M{cx+30} {py+178} l14 14 M{cx+44} {py+178} l-14 14" stroke="{RED}" stroke-width="3"/>')
b.append(lines(px + 104, py + 226, ["Saquinho plástico por cima.", "Tire os brotos do cavalo."], 12, "#222", True, "middle"))
b.append(box(14, 574, 652, 92, "#eaf6ec", GREEN))
b.append(lines(28, 595, ["Pegou: as gemas incham e brotam em 15–40 dias. Tire o saquinho aos poucos (abra, depois tire).",
                         "Não pegou: garfo seco e escuro em 30 dias. Corte a fita 60–90 dias depois, antes que estrangule.",
                         "Canivete limpo e afiado; cada corte de um golpe só; não toque nos cortes; faça na sombra.",
                         "Cavalo e garfo da mesma espécie (ou parentes), com a grossura de um lápis a um dedo."], 12.5))
open(D + "enxertia-garfagem.svg", "w").write(svg(680, 678, "Enxertia por garfagem (fenda cheia), passo a passo", "\n".join(b)))

# =====================================================================
# 2. ENXERTIA POR BORBULHIA (T)
# =====================================================================
b = []
PW, PH = 208, 240
pos = [(14, 50), (236, 50), (458, 50), (14, 302), (236, 302)]
GYo = 184
def shield(cx, cy, s=1.0, fill=BARK):
    return (f'<path d="M{cx} {cy-26*s} Q {cx+11*s} {cy} {cx} {cy+26*s} Q {cx-11*s} {cy} {cx} {cy-26*s} Z" fill="{fill}" stroke="#1e1e1e" stroke-width="1.5"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{4*s}" fill="#6b8e23" stroke="#1e1e1e" stroke-width="1"/>')
for i, (px, py) in enumerate(pos):
    b.append(panel_frame(px, py, PW, PH))
    b.append(num(px + 18, py + 18, i + 1))
    if i != 1:
        b.append(ground(px + 6, PW - 12, py + GYo))
# ---- 1: corte em T
px, py = pos[0]; cx = px + 104
b.append(stock(cx, py + 40, py + GYo, 30, cut=False))
b.append(leaf(cx - 30, py + 60, -30)); b.append(leaf(cx + 30, py + 54, 30))
b.append(f'<line x1="{cx-9}" y1="{py+100}" x2="{cx+9}" y2="{py+100}" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<line x1="{cx}" y1="{py+100}" x2="{cx}" y2="{py+134}" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<line x1="{px+56}" y1="{py+100}" x2="{px+56}" y2="{py+GYo}" stroke="#333" stroke-width="1.5"/>')
b.append(lines(px + 50, py + 140, ["15–25", "cm"], 11, "#333", True, "end"))
b.append(lines(cx + 22, py + 104, ["1,5 cm", "atravessado", "+ 2–3 cm", "para baixo"], 11, "#333", True))
b.append(lines(px + 104, py + 210, ["Faça um T na casca", "do cavalo (só a casca)"], 12, "#222", True, "middle"))
# ---- 2: tirar a borbulha
px, py = pos[1]; cx = px + 70
b.append(f'<rect x="{cx-10}" y="{py+40}" width="20" height="150" fill="{BARK}" stroke="#1e1e1e" stroke-width="2"/>')
for yy, sd in ((py + 70, 1), (py + 160, 1)):
    b.append(bud(cx + 10, yy, sd))
b.append(f'<path d="M{cx+10} {py+90} Q {cx+20} {py+116} {cx+10} {py+142}" fill="none" stroke="{RED}" stroke-width="2" stroke-dasharray="4 3"/>')
b.append(f'<line x1="{cx+10}" y1="{py+116}" x2="{cx+24}" y2="{py+110}" stroke="{GREEN}" stroke-width="2"/>')
b.append(shield(cx + 86, py + 112, 1.4, "#a98a64"))
b.append(f'<line x1="{cx+86}" y1="{py+112}" x2="{cx+108}" y2="{py+100}" stroke="{GREEN}" stroke-width="2.5"/>')
b.append(lines(cx + 58, py + 168, ["escudo de", "2–3 cm com", "a gema"], 11, "#333", True))
b.append(lines(cx + 92, py + 64, ["pecíolo", "de 1 cm"], 11, GREEN, True))
b.append(lines(px + 104, py + 210, ["Tire a gema (borbulha)", "do galho da planta boa"], 12, "#222", True, "middle"))
# ---- 3: inserir
px, py = pos[2]; cx = px + 104
b.append(stock(cx, py + 40, py + GYo, 30, cut=False))
b.append(f'<path d="M{cx} {py+100} L{cx-14} {py+104} L{cx-14} {py+136} L{cx} {py+134} Z" fill="{WOODC}" stroke="#1e1e1e" stroke-width="1.2"/>')
b.append(f'<path d="M{cx} {py+100} L{cx+14} {py+104} L{cx+14} {py+136} L{cx} {py+134} Z" fill="{WOODC}" stroke="#1e1e1e" stroke-width="1.2"/>')
b.append(shield(cx, py + 120, 0.9, "#a98a64"))
b.append(f'<line x1="{cx-9}" y1="{py+100}" x2="{cx+9}" y2="{py+100}" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(arrow(cx + 40, py + 70, cx + 40, py + 120, RED, 3))
b.append(lines(cx + 48, py + 86, ["empurre", "para", "baixo"], 11, RED2, True))
b.append(lines(px + 104, py + 210, ["Abra as abas do T e", "enfie o escudo"], 12, "#222", True, "middle"))
# ---- 4: amarrar
px, py = pos[3]; cx = px + 104
b.append(stock(cx, py + 40, py + GYo, 30, cut=False))
b.append(wrap_band(cx, py + 92, py + 112, 30))
b.append(wrap_band(cx, py + 128, py + 150, 30))
b.append(shield(cx, py + 120, 0.5, "#a98a64"))
b.append(lines(cx + 24, py + 124, ["gema de fora", "(ou coberta de", "leve)"], 11, "#333", True))
b.append(lines(px + 104, py + 210, ["Amarre com fita, de", "baixo para cima"], 12, "#222", True, "middle"))
# ---- 5: pegou, cortar acima
px, py = pos[4]; cx = px + 104
b.append(stock(cx, py + 40, py + GYo, 30, cut=False))
b.append(shield(cx, py + 120, 0.9, "#7fb36a"))
b.append(f'<line x1="{cx}" y1="{py+116}" x2="{cx+18}" y2="{py+96}" stroke="{GREEN}" stroke-width="3"/>')
b.append(leaf(cx + 28, py + 90, -35, 0.8))
b.append(f'<line x1="{cx-24}" y1="{py+80}" x2="{cx+24}" y2="{py+70}" stroke="{RED}" stroke-width="3"/>')
b.append(lines(px + 124, py + 38, ["corte 5–10", "cm acima", "da gema"], 11, RED2, True))
b.append(lines(px + 104, py + 210, ["15–21 dias: verde = pegou.", "Corte o cavalo acima."], 12, "#222", True, "middle"))
# dicas
b.append(box(458, 302, 208, 240, "#eaf6ec", GREEN))
b.append(lines(470, 324, ["Quando: com a planta", "crescendo e a casca", "soltando fácil (teste", "com a ponta do canivete).", "",
                          "Em lugar de muita chuva,", "faça o T de cabeça para", "baixo (⊥): a água não", "entra no corte.", "",
                          "Usada em citros, pêssego,", "abacate, rosa, seringueira."], 12, "#1e5e2a"))
open(D + "enxertia-borbulhia.svg", "w").write(svg(680, 556, "Enxertia por borbulhia (em T), passo a passo", "\n".join(b)))

# =====================================================================
# 3. AGROFLORESTA: ESTRATOS
# =====================================================================
b = []
GY = 420
b.append(f'<rect x="0" y="{GY}" width="680" height="60" fill="{SOIL}"/>')
b.append(f'<line x1="0" y1="{GY}" x2="680" y2="{GY}" stroke="{DARKSOIL}" stroke-width="2.5"/>')
def tree(x, h, cw, ch, fill, trunk=8):
    top = GY - h
    return (f'<rect x="{x-trunk/2}" y="{top+ch*0.6}" width="{trunk}" height="{h-ch*0.6}" fill="#7a5233" stroke="#1e1e1e" stroke-width="1.5"/>'
            f'<ellipse cx="{x}" cy="{top+ch/2}" rx="{cw/2}" ry="{ch/2}" fill="{fill}" stroke="#1e1e1e" stroke-width="1.5"/>')
# emergente
b.append(tree(70, 340, 120, 80, "#2f7d32", 12))
# alto
b.append(tree(190, 250, 110, 90, "#43a047", 10))
# médio: citros + banana
b.append(tree(290, 150, 70, 60, "#66bb6a", 7))
def banana(x, h):
    s = f'<rect x="{x-7}" y="{GY-h}" width="14" height="{h}" fill="#9ccc65" stroke="#1e1e1e" stroke-width="1.5"/>'
    for ang in (-165, -130, -95, -60, -20):
        a = math.radians(ang)
        ex, ey = x + 34 * math.cos(a), GY - h + 6 + 34 * math.sin(a) * 0.7
        s += f'<ellipse cx="{ex:.0f}" cy="{ey:.0f}" rx="34" ry="9" fill="#7cb342" stroke="#1e1e1e" stroke-width="1.2" transform="rotate({ang if ang > -90 else ang + 180} {ex:.0f} {ey:.0f})"/>'
    return s
b.append(banana(370, 150))
# baixo: mandioca e abacaxi
def mandioca(x, h):
    s = f'<line x1="{x}" y1="{GY}" x2="{x}" y2="{GY-h}" stroke="#8d6e63" stroke-width="4"/>'
    for ang in (-160, -120, -90, -60, -20):
        a = math.radians(ang)
        s += f'<ellipse cx="{x+14*math.cos(a):.0f}" cy="{GY-h+14*math.sin(a):.0f}" rx="13" ry="4" fill="#689f38" stroke="#1e1e1e" stroke-width="1" transform="rotate({ang} {x+14*math.cos(a):.0f} {GY-h+14*math.sin(a):.0f})"/>'
    return s
b.append(mandioca(424, 70)); b.append(mandioca(452, 60))
def abacaxi(x):
    s = ""
    for ang in (-150, -125, -100, -80, -55, -30):
        a = math.radians(ang)
        s += f'<line x1="{x}" y1="{GY}" x2="{x+30*math.cos(a):.0f}" y2="{GY+30*math.sin(a):.0f}" stroke="#558b2f" stroke-width="4" stroke-linecap="round"/>'
    return s
b.append(abacaxi(486))
# rasteiro: abóbora
b.append(f'<path d="M300 {GY-4} Q 340 {GY-12} 380 {GY-4} Q 420 {GY+2} 440 {GY-6}" fill="none" stroke="#3d7a2a" stroke-width="3"/>')
for x in (320, 360, 410):
    b.append(f'<ellipse cx="{x}" cy="{GY-8}" rx="10" ry="6" fill="#7cc47f" stroke="#2b6a1e" stroke-width="1"/>')
b.append(f'<ellipse cx="392" cy="{GY-9}" rx="11" ry="8" fill="#f08c00" stroke="#1e1e1e" stroke-width="1.5"/>')
# trepadeira (maracujá no tronco do alto)
b.append(f'<path d="M196 {GY} Q 210 {GY-40} 192 {GY-80} Q 176 {GY-120} 196 {GY-160}" fill="none" stroke="#2e7d32" stroke-width="2.5"/>')
b.append(f'<circle cx="206" cy="{GY-100}" r="6" fill="#ffd54f" stroke="#1e1e1e" stroke-width="1"/>')
# raízes
for x in (424, 452):
    b.append(f'<ellipse cx="{x+6}" cy="{GY+22}" rx="20" ry="6" fill="#d7b98e" stroke="#1e1e1e" stroke-width="1.2" transform="rotate(25 {x+6} {GY+22})"/>')
# rótulos à direita, na altura de cada andar
RX = 532
labs = [(GY - 316, GY - 300, 130, "EMERGENTE (20 m +)", ["castanha, jatobá, ipê,", "cajá, eucalipto, cedro"], "#2f7d32"),
        (GY - 216, GY - 205, 245, "ALTO (10–20 m)", ["manga, jaca, abacate,", "ingá, pequi"], "#43a047"),
        (GY - 144, GY - 120, 325, "MÉDIO (3–10 m)", ["citros, goiaba, banana,", "mamão, café, cacau"], "#5a9a3a"),
        (GY - 76, GY - 70, 466, "BAIXO (até 3 m)", ["mandioca, abacaxi,", "guandu, milho"], "#558b2f"),
        (GY - 22, GY - 10, 404, "RASTEIRO", ["abóbora, batata-doce"], "#b05a00")]
for y, yl, x0, t, sub, c in labs:
    b.append(f'<line x1="{x0}" y1="{yl}" x2="{RX-6}" y2="{y-4}" stroke="#999" stroke-width="1" stroke-dasharray="3 3"/>')
    b.append(text(RX, y, t, 11.5, c, True, "start"))
    b.append(lines(RX, y + 14, sub, 10.5, "#333"))
b.append(lines(20, GY + 24, ["raízes: mandioca, batata-doce, inhame, cará", "trepadeiras: maracujá, chuchu, cará, feijão"], 11.5, "#5a4630", True))
# régua de altura (sem escala)
b.append(lines(150, 76, ["Cada andar aproveita uma faixa de luz: as plantas", "de cima pegam sol pleno, as de baixo aguentam meia-sombra."], 12, "#1e5e2a", True))
b.append(box(20, 486, 640, 70, "#fff4e5", ORANGE))
b.append(lines(34, 507, ["Plante tudo junto e bem denso. Colhe primeiro o rápido (milho, feijão, abóbora: meses);",
                         "depois mandioca, banana, mamão (1–2 anos); frutíferas (3–8 anos); madeira (15 anos ou +).",
                         "Pode as árvores de serviço várias vezes por ano: a rama vira adubo no chão e abre luz."], 12.5))
open(D + "agrofloresta-estratos.svg", "w").write(svg(680, 568, "Agrofloresta: os andares (estratos)", "\n".join(b)))
print("ok agricultura3")
