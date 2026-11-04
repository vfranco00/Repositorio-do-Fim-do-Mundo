import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
# Figuras de 05-animais (galinhas): galinheiro, ovoscopia, campanula, chocadeira
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "05-animais", "img") + "/"
os.makedirs(D, exist_ok=True)
WOOD = "#8b5a2b"; SOIL = "#e8d3b0"; RED = "#d62828"; DRED = "#b3001b"; GREEN = "#2b8a3e"; BLUE = "#4a90d9"

def dim_v(x, y1, y2, label, side="left", color="#b3001b", size=11.5):
    """cota vertical com tracinhos nas pontas"""
    s = (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{color}" stroke-width="1.6"/>'
         f'<line x1="{x-5}" y1="{y1}" x2="{x+5}" y2="{y1}" stroke="{color}" stroke-width="1.6"/>'
         f'<line x1="{x-5}" y1="{y2}" x2="{x+5}" y2="{y2}" stroke="{color}" stroke-width="1.6"/>')
    return s

def dim_h(x1, x2, y, color="#b3001b"):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="1.6"/>'
            f'<line x1="{x1}" y1="{y-5}" x2="{x1}" y2="{y+5}" stroke="{color}" stroke-width="1.6"/>'
            f'<line x1="{x2}" y1="{y-5}" x2="{x2}" y2="{y+5}" stroke="{color}" stroke-width="1.6"/>')

def lead(x1, y1, x2, y2, color="#555"):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.2"/><circle cx="{x2}" cy="{y2}" r="2.5" fill="{color}"/>'

def chicken(x, y, s=1.0, face=1, body="#c8743a", perched=False):
    """galinha de perfil; (x,y) = ponto dos pes; face=1 olha para a direita, -1 esquerda"""
    g = []
    leg = 4 if perched else 9
    by = -leg - 11
    g.append(f'<polygon points="-11,{by-4} -24,{by-20} -19,{by+2}" fill="#5b3a1e" stroke="{OUT}" stroke-width="1.5"/>')
    g.append(f'<ellipse cx="0" cy="{by}" rx="15" ry="11" fill="{body}" stroke="{OUT}" stroke-width="1.8"/>')
    g.append(f'<path d="M-8 {by-2} Q0 {by+8} 9 {by-1}" fill="none" stroke="{OUT}" stroke-width="1.3"/>')
    g.append(f'<path d="M7 {by-8} L11 {by-20} L17 {by-18} L14 {by-6} Z" fill="{body}" stroke="{OUT}" stroke-width="1.5"/>')
    g.append(f'<circle cx="14" cy="{by-22}" r="6" fill="{body}" stroke="{OUT}" stroke-width="1.6"/>')
    g.append(f'<path d="M9 {by-27} q2 -5 4 0 q2 -6 4 0 q2 -5 3 1" fill="{RED}" stroke="{OUT}" stroke-width="1"/>')
    g.append(f'<polygon points="19,{by-24} 25,{by-22} 19,{by-20}" fill="#f2b705" stroke="{OUT}" stroke-width="1"/>')
    g.append(f'<ellipse cx="18" cy="{by-16}" rx="2" ry="3" fill="{RED}"/>')
    g.append(f'<circle cx="15.5" cy="{by-23}" r="1.2" fill="{OUT}"/>')
    g.append(f'<line x1="-3" y1="{by+10}" x2="-3" y2="0" stroke="#d9a400" stroke-width="2.2"/>')
    g.append(f'<line x1="3" y1="{by+10}" x2="3" y2="0" stroke="#d9a400" stroke-width="2.2"/>')
    return f'<g transform="translate({x},{y}) scale({face*s},{s})">' + "".join(g) + '</g>'

def chick(x, y, r=5, face=1):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffd84d" stroke="{OUT}" stroke-width="1"/>'
            f'<polygon points="{x+face*r},{y-1.5} {x+face*(r+3)},{y} {x+face*r},{y+1.5}" fill="#ef8a2b"/>')

# =====================================================================
# 1) GALINHEIRO EM CORTE
# =====================================================================
b = []
GY = 440  # nivel do chao
b.append(f'<rect x="0" y="{GY}" width="680" height="40" fill="{SOIL}"/>')
b.append(f'<line x1="0" y1="{GY}" x2="680" y2="{GY}" stroke="#6b4f2a" stroke-width="3"/>')
L, R = 70, 440           # paredes
TOP = 180                 # topo das paredes
b.append(f'<rect x="{L}" y="{GY-10}" width="{R-L}" height="10" fill="#f1dfa6" stroke="#b89a50" stroke-width="1"/>')
for x in (L-10, R):
    b.append(f'<rect x="{x}" y="{GY-40}" width="10" height="40" fill="#b5651d" stroke="{OUT}" stroke-width="1.5"/>')
    b.append(f'<rect x="{x+2}" y="{TOP}" width="6" height="{GY-40-TOP}" fill="url(#tela)" stroke="#777" stroke-width="1"/>')
    b.append(f'<rect x="{x}" y="{TOP-6}" width="10" height="6" fill="{WOOD}" stroke="{OUT}" stroke-width="1"/>')
PX = (L + R) // 2
b.append(f'<polygon points="15,{TOP+14} {PX-26},{TOP-74} {PX-26},{TOP-64} 15,{TOP+24}" fill="#a0522d" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<polygon points="{2*PX-15},{TOP+14} {PX+26},{TOP-74} {PX+26},{TOP-64} {2*PX-15},{TOP+24}" fill="#a0522d" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<polygon points="{PX-44},{TOP-82} {PX},{TOP-100} {PX+44},{TOP-82} {PX+44},{TOP-76} {PX},{TOP-94} {PX-44},{TOP-76}" fill="#a0522d" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<line x1="{PX-26}" y1="{TOP-72}" x2="{PX-26}" y2="{TOP-84}" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<line x1="{PX+26}" y1="{TOP-72}" x2="{PX+26}" y2="{TOP-84}" stroke="{OUT}" stroke-width="2"/>')
b.append(arrow(6, 240, 62, 240, BLUE, 3)); b.append(arrow(6, 270, 62, 270, BLUE, 3))
b.append(text(4, 226, "ar fresco", 11, "#1f5fa8", True))
b.append(arrow(PX, 150, PX, 92, "#f08c00", 3)); b.append(arrow(PX-50, 200, PX-10, 126, "#f08c00", 3))
b.append(text(PX+8, 160, "ar quente", 11, "#c06000", True))
# poleiros (mesma altura) com estrado de esterco embaixo
PY = GY - 75
b.append(f'<rect x="{L+6}" y="{PY+22}" width="140" height="6" fill="#c9b48a" stroke="{OUT}" stroke-width="1.2"/>')
b.append(f'<rect x="{L+10}" y="{PY+28}" width="5" height="{GY-10-PY-28}" fill="{WOOD}"/>')
b.append(f'<rect x="{L+136}" y="{PY+28}" width="5" height="{GY-10-PY-28}" fill="{WOOD}"/>')
for i, x in enumerate((L+30, L+74, L+118)):
    b.append(f'<line x1="{x}" y1="{PY+6}" x2="{x}" y2="{PY+22}" stroke="{WOOD}" stroke-width="3"/>')
    b.append(f'<circle cx="{x}" cy="{PY+4}" r="5" fill="{WOOD}" stroke="{OUT}" stroke-width="1.5"/>')
    b.append(chicken(x, PY-1, 1.15, 1, ["#c8743a", "#f4f1ea", "#7a4a2a"][i], perched=True))
b.append(dim_h(L+30, L+74, PY-68))
b.append(text(L+52, PY-74, "30–40 cm", 11, DRED, True, "middle"))
b.append(text(L+6, PY-108, "Poleiros na MESMA altura,", 11.5, "#222", True))
b.append(text(L+6, PY-94, "a 60–90 cm do chão", 11.5, "#222", True))
b.append(text(L+22, PY+40, "estrado: o esterco", 10, "#5a4630"))
b.append(text(L+22, PY+51, "cai aqui; limpe 1×", 10, "#5a4630"))
b.append(text(L+22, PY+62, "por semana", 10, "#5a4630"))
# ninho na parede direita
NB = GY - 55
b.append(f'<rect x="{R-40}" y="{NB-34}" width="40" height="34" fill="#5a4630" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<rect x="{R-46}" y="{NB-14}" width="6" height="14" fill="{WOOD}" stroke="{OUT}" stroke-width="1"/>')
b.append(f'<path d="M{R-36} {NB-2} q16 -10 32 0 Z" fill="#e8c96a"/>')
b.append(f'<ellipse cx="{R-20}" cy="{NB-6}" rx="5" ry="4" fill="#f6ecd8" stroke="{OUT}" stroke-width="1"/>')
b.append(f'<rect x="{R-58}" y="{NB}" width="58" height="5" fill="{WOOD}" stroke="{OUT}" stroke-width="1"/>')
b.append(f'<rect x="{R-6}" y="{NB+5}" width="5" height="{GY-10-NB-5}" fill="{WOOD}"/>')
b.append(f'<polygon points="{R-48},{NB-36} {R},{NB-54} {R},{NB-48} {R-48},{NB-30}" fill="{WOOD}" stroke="{OUT}" stroke-width="1.2"/>')
# comedouro tubular pendurado
CX = 290
b.append(f'<line x1="{CX}" y1="{TOP-40}" x2="{CX}" y2="{GY-84}" stroke="#555" stroke-width="1.5"/>')
b.append(f'<rect x="{CX-12}" y="{GY-84}" width="24" height="46" fill="#d9d9d9" stroke="{OUT}" stroke-width="1.6"/>')
b.append(f'<path d="M{CX-28} {GY-38} L{CX+28} {GY-38} L{CX+22} {GY-30} L{CX-22} {GY-30} Z" fill="#bdbdbd" stroke="{OUT}" stroke-width="1.6"/>')
# galinha comendo entre comedouro e bebedouro
b.append(chicken(345, GY-10, 1.1, -1, "#c8743a"))
# bebedouro (garrafao invertido sobre prato, em cima de tijolo)
BX = 236
b.append(f'<rect x="{BX-14}" y="{GY-24}" width="28" height="14" fill="#b5651d" stroke="{OUT}" stroke-width="1.2"/>')
b.append(f'<rect x="{BX-22}" y="{GY-30}" width="44" height="6" rx="2" fill="{BLUE}" stroke="{OUT}" stroke-width="1.2"/>')
b.append(f'<path d="M{BX-12} {GY-30} L{BX-12} {GY-62} Q{BX} {GY-74} {BX+12} {GY-62} L{BX+12} {GY-30} Z" fill="#cfe6fb" stroke="{OUT}" stroke-width="1.5"/>')
# rotulos (coluna direita)
X0 = 456
labels = [
    (TOP-82, "Lanternim: o ar quente", "sai pela abertura de cima"),
    (TOP-40, "Beiral de 50 cm a 1 m:", "a chuva não entra"),
    (TOP+42, "Pé-direito (altura da", "parede): 2,5 a 3 m"),
    (TOP+88, "Laterais de tela de arame", "(malha de até 2,5 cm)"),
    (NB-60, "Ninho 30 × 30 × 35 cm,", "a 40–60 cm do chão, escuro;"),
    (GY-30, "Mureta de 20–40 cm:", "segura a cama, corta vento"),
]
for y, l1, l2 in labels:
    b.append(text(X0, y, l1, 11.5, "#222", True)); b.append(text(X0, y+14, l2, 11.5, "#222"))
b.append(text(X0, NB-32, "1 ninho para 4–5 galinhas", 11.5, "#222"))
b.append(lead(X0-4, TOP-86, PX+34, TOP-88))
b.append(lead(X0-4, TOP-36, 2*PX-30, TOP+12))
b.append(lead(X0-4, TOP+46, R+5, TOP+50))
b.append(lead(X0-4, TOP+92, R+5, TOP+110))
b.append(lead(X0-4, NB-64, R-14, NB-24))
b.append(lead(X0-4, GY-34, R+10, GY-24))
b.append(text(CX+16, GY-92, "comedouro na", 10.5, "#222"))
b.append(text(CX+16, GY-80, "altura do dorso", 10.5, "#222"))
b.append(text(BX, GY-80, "água", 10.5, "#222", False, "middle"))
b.append(text(L+4, GY+26, "Cama seca de 5–10 cm (maravalha, palha, casca de arroz ou de café). Troque se empelotar.", 11.5, "#5a4630"))
b.append(box(20, 494, 640, 88, "#eef7ee", GREEN))
b += [text(34, 514, "Espaço: 1 m² de galinheiro para 3–5 galinhas + piquete de 3–5 m² por ave (ideal: 10 m²).", 11.8),
      text(34, 532, "Poleiro: 20–25 cm de vara por ave; vara de 4–5 cm de grossura, cantos arredondados.", 11.8),
      text(34, 550, "Galpão comprido no sentido leste-oeste (menos sol dentro). Telha de barro ou palha.", 11.8),
      text(34, 568, "Fibrocimento sem forro esquenta demais. Porta e tela que gambá e cachorro não abram.", 11.8)]
DEFS = ('<defs><pattern id="tela" width="6" height="6" patternUnits="userSpaceOnUse">'
        '<path d="M0 0 L6 6 M6 0 L0 6" stroke="#777" stroke-width="0.8"/></pattern></defs>')
open(D + "galinha-galinheiro.svg", "w").write(svg(680, 592, "Galinheiro em corte: medidas que importam", DEFS + "\n".join(b)))

# =====================================================================
# 2) OVOSCOPIA
# =====================================================================
def egg_path(cx, cy, a, h):
    y0, y1 = cy - h/2, cy + h/2
    return (f'M{cx},{y0} C{cx+1.5*a:.1f},{y0} {cx+1.17*a:.1f},{y1} {cx},{y1} '
            f'C{cx-1.17*a:.1f},{y1} {cx-1.5*a:.1f},{y0} {cx},{y0} Z')

_eid = [0]
def candled_egg(cx, cy, kind, day):
    """kind: fertil, infertil, morto ; day: 4, 10, 18"""
    a, h = 26, 76
    _eid[0] += 1; cid = f"ov{_eid[0]}"
    p = egg_path(cx, cy, a, h)
    g = [f'<clipPath id="{cid}"><path d="{p}"/></clipPath>',
         f'<path d="{p}" fill="url(#luz)"/>', f'<g clip-path="url(#{cid})">']
    y0 = cy - h/2
    # camara de ar (aumenta com os dias)
    cam = {4: 9, 10: 14, 18: 24}[day]
    if kind == "fertil" and day == 18:
        g.append(f'<path d="M{cx-40},{y0} L{cx+40},{y0} L{cx+40},{y0+cam+8} Q{cx},{y0+cam-6} {cx-40},{y0+cam+2} Z" fill="#fffbe6"/>')
        g.append(f'<path d="M{cx-40},{y0+cam+2} Q{cx},{y0+cam-6} {cx+40},{y0+cam+8} L{cx+40},{y0+h} L{cx-40},{y0+h} Z" fill="#4a230c"/>')
        g.append(f'<path d="M{cx-40},{y0+cam+2} Q{cx},{y0+cam-6} {cx+40},{y0+cam+8}" fill="none" stroke="#2a1205" stroke-width="2"/>')
    else:
        g.append(f'<path d="M{cx-40},{y0} L{cx+40},{y0} L{cx+40},{y0+cam} Q{cx},{y0+cam+4} {cx-40},{y0+cam} Z" fill="#fffbe6"/>')
        g.append(f'<path d="M{cx-40},{y0+cam} Q{cx},{y0+cam+4} {cx+40},{y0+cam}" fill="none" stroke="#c98a3a" stroke-width="1.5"/>')
    if kind == "infertil":
        g.append(f'<circle cx="{cx}" cy="{cy+6}" r="17" fill="#e8962e" fill-opacity="0.55"/>')
    elif kind == "fertil" and day == 4:
        g.append(f'<circle cx="{cx}" cy="{cy+6}" r="18" fill="#e8962e" fill-opacity="0.45"/>')
        for ang, ln in ((0, 22), (50, 18), (110, 20), (170, 22), (220, 17), (280, 21), (330, 18)):
            import math
            ex = cx + ln*math.cos(math.radians(ang)); ey = cy + 6 + ln*math.sin(math.radians(ang))
            mx = cx + ln*0.5*math.cos(math.radians(ang+25)); my = cy + 6 + ln*0.5*math.sin(math.radians(ang+25))
            g.append(f'<path d="M{cx},{cy+6} Q{mx:.1f},{my:.1f} {ex:.1f},{ey:.1f}" fill="none" stroke="#c0181b" stroke-width="1.6"/>')
        g.append(f'<circle cx="{cx}" cy="{cy+6}" r="4.5" fill="#3a1206"/>')
    elif kind == "fertil" and day == 10:
        g.append(f'<ellipse cx="{cx+2}" cy="{cy+18}" rx="26" ry="22" fill="#4a230c"/>')
        for d in ("M{0},{1} q-14,-14 -26,-12", "M{0},{1} q4,-20 18,-26", "M{0},{1} q16,-6 26,-20", "M{0},{1} q-20,-2 -30,-22"):
            g.append(f'<path d="{d.format(cx, cy+2)}" fill="none" stroke="#c0181b" stroke-width="2.2"/>')
    elif kind == "morto" and day == 4:
        g.append(f'<circle cx="{cx}" cy="{cy+6}" r="15" fill="none" stroke="#c0181b" stroke-width="3.5"/>')
    elif kind == "morto" and day == 10:
        g.append(f'<ellipse cx="{cx-4}" cy="{cy+22}" rx="13" ry="9" fill="#5a2a10" fill-opacity="0.85"/>')
        g.append(f'<ellipse cx="{cx+8}" cy="{cy}" rx="8" ry="6" fill="#7a3a16" fill-opacity="0.6"/>')
    elif kind == "morto" and day == 18:
        g.append(f'<path d="{p}" fill="#4b5320" fill-opacity="0.75"/>')
        g.append(f'<ellipse cx="{cx-6}" cy="{cy+10}" rx="14" ry="16" fill="#2c2a10" fill-opacity="0.7"/>')
    g.append('</g>')
    g.append(f'<path d="{p}" fill="none" stroke="{OUT}" stroke-width="2"/>')
    return "".join(g)

b = []
# como fazer (topo)
b.append('<rect x="40" y="96" width="44" height="70" rx="4" fill="#9a9a9a" stroke="#1e1e1e" stroke-width="2"/>')
b.append('<rect x="34" y="88" width="56" height="10" rx="3" fill="#6b6b6b" stroke="#1e1e1e" stroke-width="2"/>')
b.append('<ellipse cx="62" cy="88" rx="11" ry="3" fill="#fff6c8" stroke="#1e1e1e" stroke-width="1"/>')
b.append(f'<path d="{egg_path(62, 64, 15, 44)}" fill="url(#luz)" stroke="#1e1e1e" stroke-width="2" transform="rotate(180 62 64)"/>')
b.append(text(62, 184, "lanterna dentro", 10.5, "#333", False, "middle"))
b.append(text(62, 196, "de lata/tubo", 10.5, "#333", False, "middle"))
steps = [("1.", "Quarto escuro. Lanterna forte (serve a do celular) dentro de lata ou tubo"),
         ("", "de papelão, com furo de 2,5–3 cm em cima."),
         ("2.", "Encoste a ponta GROSSA do ovo no furo e gire devagar. Seja rápido:"),
         ("", "no máximo 10–20 segundos fora do calor por ovo."),
         ("3.", "Ovo branco: dá para ver no dia 4–5. Ovo marrom ou escuro: espere o dia 7."),
         ("4.", "Tire inférteis e mortos no dia 7–10: eles apodrecem e podem estourar.")]
for i, (n, s_) in enumerate(steps):
    b.append(text(112, 70 + i*18, f'<tspan font-weight="bold">{n}</tspan> {s_}' if n else "     " + s_, 12, "#222"))
cols = [(225, "Dia 4–5"), (385, "Dia 10"), (545, "Dia 18")]
for x, t in cols:
    b.append(text(x, 232, t, 14, "#222", True, "middle"))
rows = [(250, "fertil", "FÉRTIL", "(vivo)", GREEN, "#f3faf3",
         ["“aranha”: ponto escuro", "metade escura, veias", "quase todo escuro;"],
         ["com veias vermelhas", "grossas na parte clara", "câmara de ar grande"]),
        (385, "infertil", "INFÉRTIL", "(sem pinto)", "#666", "#f7f7f7",
         ["claro, só a sombra", "continua claro", "continua claro"],
         ["da gema", "", "(já devia ter saído)"]),
        (520, "morto", "MORTO", "(retire já)", DRED, "#fdf1f1",
         ["anel vermelho", "mancha escura solta,", "escuro-esverdeado,"],
         ["(anel de sangue)", "sem veias", "cheiro ruim: PODRE"])]
for y, kind, t1, t2, col, bg, l1, l2 in rows:
    b.append(f'<rect x="20" y="{y}" width="640" height="128" rx="8" fill="{bg}" stroke="#ddd"/>')
    b.append(text(34, y+52, t1, 14, col, True)); b.append(text(34, y+70, t2, 12, col))
    for (x, _), day, s1, s2 in zip(cols, (4, 10, 18), l1, l2):
        b.append(candled_egg(x, y + 52, kind, day))
        b.append(text(x, y + 107, s1, 11, "#222", False, "middle")); b.append(text(x, y + 120, s2, 11, "#222", False, "middle"))
b.append(text(340, 672, "A câmara de ar (parte clara de cima) cresce com os dias em todos os ovos.", 12, "#222", True, "middle"))
DEFS = ('<defs><radialGradient id="luz" cx="50%" cy="55%" r="60%"><stop offset="0" stop-color="#fff3c4"/>'
        '<stop offset="0.7" stop-color="#f6c065"/><stop offset="1" stop-color="#e08a2a"/></radialGradient></defs>')
open(D + "galinha-ovoscopia.svg", "w").write(svg(680, 686, "Ovoscopia: ver o que tem dentro do ovo", DEFS + "\n".join(b)))

# =====================================================================
# 3) PINTINHOS SOB A CAMPANULA (vista de cima)
# =====================================================================
import random, math
rnd = random.Random(7)
def pos_ring(cx, cy, n, r1, r2, a1=0, a2=360):
    pts = []
    tries = 0
    while len(pts) < n and tries < 5000:
        tries += 1
        a = math.radians(rnd.uniform(a1, a2)); r = rnd.uniform(r1, r2)
        x, y = cx + r*math.cos(a), cy + r*math.sin(a)
        if all((x-px)**2 + (y-py)**2 > 95 for px, py in pts):
            pts.append((x, y))
    return pts

def panel(px, py, title, col, mode, l1, l2, l3):
    g = []
    g.append(f'<rect x="{px}" y="{py}" width="318" height="232" rx="10" fill="#fafafa" stroke="{col}" stroke-width="2"/>')
    g.append(text(px+159, py+22, title, 15, col, True, "middle"))
    cx, cy, R = px+100, py+128, 82
    g.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#f1dfa6" stroke="#8b5a2b" stroke-width="4"/>')
    g.append(f'<circle cx="{cx}" cy="{cy}" r="34" fill="#ffe680" fill-opacity="0.55"/>')
    g.append(f'<circle cx="{cx}" cy="{cy}" r="12" fill="#ffd21f" stroke="{OUT}" stroke-width="1.5"/>')
    if mode == "frio":
        pts = pos_ring(cx, cy, 26, 0, 24)
    elif mode == "calor":
        pts = pos_ring(cx, cy, 26, R-18, R-8)
    elif mode == "vento":
        pts = pos_ring(cx, cy, 26, 30, R-10, -60, 60)
        for yy in (cy-40, cy, cy+40):
            g.append(arrow(px+4, yy, px+44, yy, BLUE, 3))
        g.append(f'<path d="M{cx-R+2} {cy-60} A{R} {R} 0 0 0 {cx-R+2} {cy+60}" fill="none" stroke="{BLUE}" stroke-width="2" stroke-dasharray="5 4"/>')
    else:
        pts = pos_ring(cx, cy, 26, 20, R-12)
    for x, y in pts:
        if mode != "certo" and (x-cx)**2 + (y-cy)**2 < 14**2:
            continue
        if (x-cx)**2 + (y-cy)**2 < 14**2:
            continue
        g.append(chick(x, y, 5, 1 if x < cx else -1))
    if mode == "frio":
        for x, y in pos_ring(cx, cy, 6, 14, 26):
            g.append(chick(x, y, 5, 1 if x < cx else -1))
    if mode == "certo":
        g.append(f'<circle cx="{cx+52}" cy="{cy-48}" r="9" fill="#cfe6fb" stroke="{OUT}" stroke-width="1.5"/>')
        g.append(f'<rect x="{cx-70}" y="{cy+42}" width="30" height="10" rx="3" fill="#bdbdbd" stroke="{OUT}" stroke-width="1.5"/>')
    tx = px+194
    g.append(text(tx, py+86, l1[0], 11.5, "#222", True))
    for i, s_ in enumerate(l1[1:]):
        g.append(text(tx, py+101+i*14, s_, 11, "#222"))
    g.append(text(tx, py+160, l2, 11.5, col, True))
    for i, s_ in enumerate(l3):
        g.append(text(tx, py+175+i*14, s_, 11, "#222"))
    return "".join(g)

b = []
b.append(panel(16, 48, "FRIO", "#1f5fa8", "frio",
               ["Amontoados", "embaixo da luz,", "piando alto e", "sem parar"],
               "O que fazer:", ["abaixe a lâmpada", "ou ponha mais uma;", "feche as cortinas"]))
b.append(panel(346, 48, "CALOR", DRED, "calor",
               ["Afastados, na", "borda; bico aberto,", "asas abertas,", "ofegantes"],
               "O que fazer:", ["suba a lâmpada ou", "use uma mais fraca;", "abra a ventilação"]))
b.append(panel(16, 292, "CORRENTE DE AR", "#c06000", "vento",
               ["Todos de um lado", "só, longe do", "vento (seta azul)"],
               "O que fazer:", ["tape o lado do", "vento; círculo de", "40–50 cm de altura"]))
b.append(panel(346, 292, "CERTO", GREEN, "certo",
               ["Espalhados por", "todo o círculo,", "comendo, bebendo", "e dormindo soltos"],
               "Assim está bom:", ["pio baixinho,", "calmo; mantenha"]))
# tabela de temperatura
b.append(text(340, 556, "Temperatura na altura dos pintinhos, na borda da área aquecida", 13, "#222", True, "middle"))
wk = [("1ª semana", "32–35 °C"), ("2ª semana", "29–32 °C"), ("3ª semana", "26–29 °C"), ("4ª semana", "23–26 °C"), ("5ª em diante", "sem calor*")]
for i, (a_, t_) in enumerate(wk):
    x = 20 + i*128
    shade = ["#d62828", "#e8590c", "#f08c00", "#f2b705", "#8fbf6a"][i]
    b.append(f'<rect x="{x}" y="568" width="120" height="52" rx="6" fill="{shade}" stroke="{OUT}" stroke-width="1.2"/>')
    b.append(text(x+60, 589, a_, 12, "#fff" if i < 3 else "#222", True, "middle"))
    b.append(text(x+60, 609, t_, 13.5, "#fff" if i < 3 else "#222", True, "middle"))
b.append(text(20, 642, "*Retire o aquecimento quando estiverem empenados e o ambiente passar de 20 °C; em noites frias, ligue à noite.", 11.2, "#222"))
b.append(text(20, 658, "Círculo de 1 m de diâmetro abriga 30–40 pintos na 1ª semana. Aumente o círculo toda semana.", 11.2, "#222"))
b.append(text(20, 674, "Desenhos vistos de cima: o círculo amarelo do centro é a lâmpada (campânula).", 11.2, "#222"))
b.append(text(20, 692, "Vale mais o comportamento dos pintos que o termômetro: olhe várias vezes ao dia e à noite.", 11.2, "#222", True))
open(D + "galinha-campanula.svg", "w").write(svg(680, 704, "Pintinhos sob a campânula: o que eles mostram", "\n".join(b)))

# =====================================================================
# 4) CHOCADEIRA CASEIRA (corte)
# =====================================================================
b = []
X1, X2, Y1, Y2, T = 50, 400, 92, 382, 18   # caixa de isopor
b.append(f'<rect x="{X1}" y="{Y1}" width="{X2-X1}" height="{Y2-Y1}" fill="#f4f4f4" stroke="{OUT}" stroke-width="2.5"/>')
b.append(f'<rect x="{X1+T}" y="{Y1+T}" width="{X2-X1-2*T}" height="{Y2-Y1-2*T}" fill="#fffdf6" stroke="{OUT}" stroke-width="1.5"/>')
# tampa com visor
b.append(f'<line x1="{X1}" y1="{Y1+T}" x2="{X2}" y2="{Y1+T}" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<rect x="200" y="{Y1}" width="90" height="{T}" fill="#cfe6fb" stroke="{OUT}" stroke-width="1.5"/>')
# furos de ventilacao
for (x, y) in ((X1, 350), (X2-T, 128)):
    b.append(f'<rect x="{x}" y="{y}" width="{T}" height="8" fill="#fffdf6" stroke="none"/>')
b.append(arrow(22, 354, 62, 354, BLUE, 2.5)); b.append(arrow(392, 132, 432, 132, "#f08c00", 2.5))
# lampada presa na tampa
b.append(f'<rect x="112" y="{Y1+T}" width="20" height="14" fill="#9a9a9a" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<circle cx="122" cy="{Y1+T+30}" r="17" fill="#ffe066" stroke="{OUT}" stroke-width="1.8"/>')
b.append(f'<circle cx="122" cy="{Y1+T+30}" r="28" fill="#ffd21f" fill-opacity="0.18"/>')
# ventilador
FX, FY = 178, Y1+T+30
b.append(f'<circle cx="{FX}" cy="{FY}" r="18" fill="#dcdcdc" stroke="{OUT}" stroke-width="1.8"/>')
for ang in (0, 120, 240):
    b.append(f'<ellipse cx="{FX+8*math.cos(math.radians(ang)):.1f}" cy="{FY+8*math.sin(math.radians(ang)):.1f}" rx="8" ry="3.5" fill="#888" transform="rotate({ang} {FX+8*math.cos(math.radians(ang)):.1f} {FY+8*math.sin(math.radians(ang)):.1f})"/>')
b.append(f'<circle cx="{FX}" cy="{FY}" r="3" fill="{OUT}"/>')
# bandeja de agua
b.append(f'<rect x="110" y="322" width="230" height="40" fill="#ddd" stroke="{OUT}" stroke-width="1.8"/>')
b.append(f'<rect x="112" y="334" width="226" height="26" fill="{BLUE}" fill-opacity="0.7"/>')
# tela dos ovos
b.append(f'<line x1="{X1+T}" y1="300" x2="{X2-T}" y2="300" stroke="#555" stroke-width="3" stroke-dasharray="2 3"/>')
for i in range(7):
    ex = 100 + i*42
    b.append(f'<ellipse cx="{ex}" cy="286" rx="18" ry="13" fill="#f3e1c4" stroke="{OUT}" stroke-width="1.6"/>')
b.append(text(100, 291, "X", 10, "#555", True, "middle")); b.append(text(142, 291, "O", 10, "#555", True, "middle"))
# termometro/higrometro na parede do fundo
b.append(f'<rect x="76" y="200" width="62" height="40" rx="4" fill="#fff" stroke="{OUT}" stroke-width="1.6"/>')
b.append(text(107, 216, "37,7 °C", 11, "#222", True, "middle")); b.append(text(107, 232, "UR 55%", 11, "#1f5fa8", True, "middle"))
b.append(text(107, 254, "termômetro e", 10, "#222", False, "middle")); b.append(text(107, 265, "higrômetro", 10, "#222", False, "middle"))
# sensor do termostato
b.append(f'<path d="M{X2+20} 222 L300 222 L300 258" fill="none" stroke="#333" stroke-width="2"/>')
b.append(f'<rect x="294" y="256" width="12" height="12" rx="2" fill="#333"/>')
b.append(f'<line x1="250" y1="270" x2="350" y2="270" stroke="{DRED}" stroke-width="1.2" stroke-dasharray="4 3"/>')
# termostato fora da caixa
b.append(f'<rect x="{X2+20}" y="196" width="78" height="52" rx="6" fill="#3a3a3a" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<rect x="{X2+28}" y="204" width="62" height="22" rx="3" fill="#0b2a12"/>')
b.append(text(X2+59, 221, "37.7", 15, "#3cff6a", True, "middle"))
b.append(text(X2+59, 242, "termostato", 9.5, "#fff", False, "middle"))
b.append(f'<path d="M{X2+59} 196 L{X2+59} 64 L122 64 L122 {Y1}" fill="none" stroke="#333" stroke-width="2"/>')
# rotulos
lab = [(62, 60, "Visor de vidro na tampa: olhe sem abrir"),
       ]
b.append(text(290, 84, "visor de vidro (olhe sem abrir)", 11, "#222", True, "middle"))
b.append(text(122, 172, "lâmpada", 10.5, "#222", False, "middle")); b.append(text(122, 184, "25–40 W", 10.5, "#222", True, "middle"))
b.append(text(FX, 172, "ventoinha", 10.5, "#222", False, "middle")); b.append(text(FX, 184, "de PC 12 V", 10.5, "#222", False, "middle"))
b.append(text(10, 344, "ar", 10.5, "#1f5fa8", True))
b.append(text(410, 120, "ar", 10.5, "#c06000", True))
b.append(text(225, 316, "tela de arame (o pinto não cai na água)", 10.5, "#222", True, "middle"))
b.append(text(225, 376, "bandeja de água: mais área = mais umidade", 10.5, "#1f5fa8", True, "middle"))
b.append(text(288, 246, "sensor na altura", 10.5, DRED, True, "end"))
b.append(text(288, 258, "do TOPO dos ovos", 10.5, DRED, True, "end"))
b.append(text(X2+20, 266, "liga e desliga a", 10.5, "#222")); b.append(text(X2+20, 278, "lâmpada sozinho", 10.5, "#222"))
b.append(text(X2+20, 300, "Caixa de isopor de", 11.5, "#222", True)); b.append(text(X2+20, 314, "40–60 L, ou de madeira", 11.5, "#222"))
b.append(text(X2+20, 328, "forrada; dentro de um", 11.5, "#222")); b.append(text(X2+20, 342, "cômodo sem sol e sem", 11.5, "#222"))
b.append(text(X2+20, 356, "vento", 11.5, "#222"))
b.append(text(X2+20, 380, "Marque X e O nos ovos", 11.5, "#222", True)); b.append(text(X2+20, 394, "para saber se virou todos", 11.5, "#222"))
# tabela
rows_ = [("Temperatura", "37,5–37,8 °C com ventoinha. Sem ventoinha: 38,3 °C no topo dos ovos."),
         ("Umidade", "50–55% do dia 1 ao 18; 65–70% do dia 19 ao 21 (encha mais a bandeja)."),
         ("Virar", "3 a 5 vezes por dia (número ímpar) do dia 1 ao 18. Do dia 18 em diante: NÃO vire."),
         ("Ovos", "Limpos, sem rachar, com até 7 dias, guardados a 15–18 °C de ponta fina para baixo."),
         ("Antes", "Ligue a chocadeira vazia 24–48 h e só ponha os ovos com a temperatura estável.")]
b.append(box(20, 410, 640, 128, "#f6f9ff", "#3f6d9e"))
for i, (k, v) in enumerate(rows_):
    b.append(text(34, 432 + i*22, k, 12, "#1f3f6e", True)); b.append(text(128, 432 + i*22, v, 11.6, "#222"))
b.append(text(340, 558, "Calor demais mata mais que frio: 40 °C por algumas horas mata os embriões.", 11.5, DRED, True, "middle"))
b.append(text(340, 574, "Faltou luz? Esfriar 1–2 h quase sempre não mata: tampe a caixa com um cobertor.", 11.5, "#222", False, "middle"))
open(D + "galinha-chocadeira.svg", "w").write(svg(680, 588, "Chocadeira caseira (corte) — 21 dias para galinha", "\n".join(b)))
