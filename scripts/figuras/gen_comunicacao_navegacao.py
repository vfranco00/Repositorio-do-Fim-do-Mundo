import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
# Figuras de 10-comunicacao-e-navegacao/03-orientacao-e-navegacao.md
import math
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "10-comunicacao-e-navegacao", "img") + "/"
os.makedirs(D, exist_ok=True)
GREEN = "#2b8a3e"; RED = "#d62828"; DARK = "#1e1e1e"; BLUE = "#3f6d9e"; NAVY = "#1d2b4f"

def star(cx, cy, r, color=NAVY, ratio=0.45):
    pts = []
    for k in range(10):
        a = -math.pi / 2 + k * math.pi / 5
        rr = r if k % 2 == 0 else r * ratio
        pts.append(f"{cx + rr*math.cos(a):.1f},{cy + rr*math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{color}"/>'

def lines(x, y, rows, size=12.5, lh=17, color="#222"):
    out = []
    for i, r in enumerate(rows):
        bold = r.startswith("*")
        out.append(text(x, y + i * lh, r.lstrip("*"), size, color, bold))
    return "".join(out)

def sun(cx, cy, r=16):
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffd43b" stroke="#e8a400" stroke-width="3"/>'
    for k in range(8):
        a = k * math.pi / 4
        s += f'<line x1="{cx+(r+5)*math.cos(a):.1f}" y1="{cy+(r+5)*math.sin(a):.1f}" x2="{cx+(r+13)*math.cos(a):.1f}" y2="{cy+(r+13)*math.sin(a):.1f}" stroke="#e8a400" stroke-width="3"/>'
    return s

# ---------- CRUZEIRO DO SUL ----------
STARS = {  # nome: (AR em horas, declinação em graus, magnitude)
    "Acrux": (12.4433, -63.099, 0.8), "Mimosa": (12.7953, -59.689, 1.25), "Gacrux": (12.5194, -57.113, 1.6),
    "Pálida": (12.2524, -58.749, 2.8), "Intrometida": (12.3560, -60.401, 3.6),
    "Alfa Centauri": (14.6600, -60.835, -0.1), "Beta Centauri": (14.0637, -60.373, 0.6)}
def proj(ra, dec):  # azimutal equidistante centrada no polo sul celeste; Cruzeiro em pé
    phi = math.radians((ra - 12.48) * 15); r = 90 + dec
    return (-r * math.sin(phi), r * math.cos(phi))
P = {k: proj(v[0], v[1]) for k, v in STARS.items()}
# girar para o eixo Acrux->Gacrux ficar vertical
ax, ay = P["Acrux"]; gx, gy = P["Gacrux"]
rot = math.atan2(gx - ax, gy - ay)
def rotp(p):
    x, y = p; c, s = math.cos(rot), math.sin(rot)
    return (x * c - y * s, x * s + y * c)
P = {k: rotp(v) for k, v in P.items()}
ax, ay = P["Acrux"]; gx, gy = P["Gacrux"]
L = gy - ay
pole = (ax, ay - 4.5 * L)  # 4,5 vezes o comprimento do Cruzeiro, abaixo do pé
S = 7.6; CX = 250 - pole[0] * S; CY = 372 + pole[1] * S
def xy(p): return (CX + p[0] * S, CY - p[1] * S)
LAT = 23
b = []
hy = xy((pole[0], pole[1] - LAT))[1]
b.append(f'<rect x="20" y="46" width="430" height="{hy-46:.0f}" fill="#e9eef7"/>')
b.append(f'<rect x="20" y="{hy:.0f}" width="430" height="44" fill="#9fb98a"/>')
b.append(f'<path d="M20 {hy:.0f} q 40 -14 80 -4 q 50 -18 110 0 q 60 -10 100 2 q 50 -14 140 0 L450 {hy:.0f} Z" fill="#7d9c68"/>')
b.append(f'<line x1="20" y1="{hy:.0f}" x2="450" y2="{hy:.0f}" stroke="#4f7a35" stroke-width="2"/>')
# linha do Cruzeiro prolongada
A = xy(P["Acrux"]); G = xy(P["Gacrux"]); PO = xy(pole)
b.append(f'<line x1="{G[0]:.1f}" y1="{G[1]:.1f}" x2="{A[0]:.1f}" y2="{A[1]:.1f}" stroke="{NAVY}" stroke-width="2"/>')
b.append(f'<line x1="{A[0]:.1f}" y1="{A[1]:.1f}" x2="{PO[0]:.1f}" y2="{PO[1]:.1f}" stroke="{RED}" stroke-width="2.5" stroke-dasharray="7 5"/>')
for k in range(1, 5):
    yk = A[1] + k * L * S
    b.append(f'<line x1="{A[0]-7:.1f}" y1="{yk:.1f}" x2="{A[0]+7:.1f}" y2="{yk:.1f}" stroke="{RED}" stroke-width="2.5"/>')
    b.append(text(A[0] + 12, yk + 4, f"{k}×", 11.5, "#b3001b", True))
b.append(text(A[0] + 14, PO[1] + 4, "4,5×", 11.5, "#b3001b", True))
# guardas
AC = xy(P["Alfa Centauri"]); BC = xy(P["Beta Centauri"])
M = ((AC[0] + BC[0]) / 2, (AC[1] + BC[1]) / 2)
b.append(f'<line x1="{AC[0]:.1f}" y1="{AC[1]:.1f}" x2="{BC[0]:.1f}" y2="{BC[1]:.1f}" stroke="{BLUE}" stroke-width="2" stroke-dasharray="4 4"/>')
b.append(f'<line x1="{M[0]:.1f}" y1="{M[1]:.1f}" x2="{PO[0]:.1f}" y2="{PO[1]:.1f}" stroke="{BLUE}" stroke-width="2.5" stroke-dasharray="7 5"/>')
b.append(f'<circle cx="{M[0]:.1f}" cy="{M[1]:.1f}" r="3.5" fill="{BLUE}"/>')
# estrelas
for k, p in P.items():
    x, y = xy(p); mag = STARS[k][2]
    b.append(star(x, y, 9.5 - 1.7 * mag))
b.append(text(AC[0] - 4, AC[1] + 24, "Alfa", 11.5, BLUE, True, "middle")); b.append(text(AC[0] - 4, AC[1] + 37, "Centauri", 11.5, BLUE, True, "middle"))
b.append(text(BC[0] + 2, BC[1] - 14, "Beta Centauri", 11.5, BLUE, True, "middle"))
b.append(text(M[0] - 4, M[1] - 44, "AS GUARDAS", 12, BLUE, True, "middle"))
b.append(text(G[0] + 30, G[1] - 6, "CRUZEIRO", 12, NAVY, True))
b.append(text(G[0] + 30, G[1] + 8, "DO SUL", 12, NAVY, True))
# polo
b.append(f'<circle cx="{PO[0]:.1f}" cy="{PO[1]:.1f}" r="7" fill="none" stroke="{RED}" stroke-width="3"/>')
b.append(text(PO[0] + 14, PO[1] + 24, "Polo Sul Celeste", 12, "#b3001b", True))
b.append(text(PO[0] + 14, PO[1] + 38, "(ponto vazio do céu)", 11, "#b3001b"))
b.append(f'<line x1="{PO[0]:.1f}" y1="{PO[1]+8:.1f}" x2="{PO[0]:.1f}" y2="{hy-6:.1f}" stroke="{GREEN}" stroke-width="3"/>')
b.append(f'<polygon points="{PO[0]-8:.1f},{hy-16:.1f} {PO[0]+8:.1f},{hy-16:.1f} {PO[0]:.1f},{hy-2:.1f}" fill="{GREEN}"/>')
b.append(text(PO[0] + 10, (PO[1] + hy) / 2 + 14, "desça reto", 11.5, GREEN, True))
b.append(text(PO[0] + 10, (PO[1] + hy) / 2 + 28, "até o horizonte", 11.5, GREEN, True))
b.append(text(PO[0], hy + 30, "SUL", 20, "#fff", True, "middle"))
b.append(text(30, (PO[1] + hy) / 2 + 2, "altura do polo", 11, "#444"))
b.append(text(30, (PO[1] + hy) / 2 + 15, "= sua latitude", 11, "#444"))
b.append(text(30, (PO[1] + hy) / 2 + 28, f"(aqui {LAT}°)", 11, "#444"))
# detalhe ampliado
bx, by, bw, bh = 462, 46, 198, 236
b.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="8" fill="#e9eef7" stroke="#9fb3cc"/>')
b.append(text(bx + bw / 2, by + 18, "o Cruzeiro, ampliado", 12, NAVY, True, "middle"))
cxs = [P[k][0] for k in ("Acrux", "Mimosa", "Gacrux", "Pálida")]; cys = [P[k][1] for k in ("Acrux", "Mimosa", "Gacrux", "Pálida")]
mx, my = sum(cxs) / 4, sum(cys) / 4; Z = 23
def zz(k): return (bx + bw / 2 - 10 + (P[k][0] - mx) * Z, by + 128 - (P[k][1] - my) * Z)
za, zg, zm, zp = zz("Acrux"), zz("Gacrux"), zz("Mimosa"), zz("Pálida")
b.append(f'<line x1="{za[0]:.1f}" y1="{za[1]:.1f}" x2="{zg[0]:.1f}" y2="{zg[1]:.1f}" stroke="#9fb3cc" stroke-width="2"/>')
b.append(f'<line x1="{zm[0]:.1f}" y1="{zm[1]:.1f}" x2="{zp[0]:.1f}" y2="{zp[1]:.1f}" stroke="#9fb3cc" stroke-width="2"/>')
labels = {"Gacrux": ("Gacrux (topo,", "alaranjada)", 50, -4), "Acrux": ("Acrux (pé, a", "mais brilhante)", 56, -2),
          "Mimosa": ("Mimosa", "", -6, 22), "Pálida": ("Pálida", "", 6, 22), "Intrometida": ("Intrometida", "", 22, 20)}
for k in ("Acrux", "Mimosa", "Gacrux", "Pálida", "Intrometida"):
    x, y = zz(k); mag = STARS[k][2]
    b.append(star(x, y, 11 - 1.9 * mag, "#c0621a" if k == "Gacrux" else NAVY))
    l1, l2, dx, dy = labels[k]
    b.append(text(x + dx, y + dy, l1, 11, "#222", True, "middle"))
    if l2: b.append(text(x + dx, y + dy + 13, l2, 11, "#222", True, "middle"))
# passos
steps = ["*1. Ache o Cruzeiro: 4 estrelas", "em cruz + 1 menor (Intrometida)", "e, ao lado, 2 estrelas muito", "brilhantes: as Guardas.",
         "*2. Prolongue o braço maior,", "do topo para o pé, 4 vezes e", "meia o tamanho da cruz.",
         "*3. Confira: a linha que sai do", "meio das Guardas, em ângulo", "reto, chega ao mesmo ponto.",
         "*4. Desse ponto, desça reto até", "o horizonte: ali é o SUL.", "Marque com uma estaca e", "espere o dia para conferir."]
b.append(lines(466, 304, steps, 12, 16.5))
b.append(box(20, hy + 54, 640, 76, "#fff4e5", "#ef8a2b"))
b.append(lines(32, hy + 74, ["O Cruzeiro gira em volta do polo durante a noite (pode estar deitado ou de cabeça para baixo):",
                             "o método funciona em qualquer posição. Cuidado com o \"Falso Cruzeiro\": é maior, mais apagado,",
                             "sem a 5ª estrela e sem as Guardas ao lado. Punho fechado com o braço esticado ≈ 10° no céu."], 12, 17))
H = hy + 140
open(D + "cruzeiro-do-sul.svg", "w").write(svg(680, H, "Cruzeiro do Sul: como achar o SUL à noite", "\n".join(b)))

# ---------- METODO DO RELOGIO (HEMISFERIO SUL) ----------
def dial(cx, cy, r, hour, minute=0, label_n=True, big=True):
    s = [f'<circle cx="{cx}" cy="{cy}" r="{r+8}" fill="#cfd4da" stroke="{DARK}" stroke-width="3"/>',
         f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{DARK}" stroke-width="2"/>']
    for h in range(1, 13):
        a = math.radians(h * 30 - 90)
        s.append(f'<line x1="{cx+(r-2)*math.cos(a):.1f}" y1="{cy+(r-2)*math.sin(a):.1f}" x2="{cx+(r-10)*math.cos(a):.1f}" y2="{cy+(r-10)*math.sin(a):.1f}" stroke="{DARK}" stroke-width="3"/>')
        fs = 15 if big else 11
        s.append(text(cx + (r - 24 if big else r - 18) * math.cos(a), cy + (r - 24 if big else r - 18) * math.sin(a) + fs * 0.36, str(h), fs, "#222", True, "middle"))
    ah = math.radians((hour % 12 + minute / 60) * 30 - 90); am = math.radians(minute * 6 - 90)
    s.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+r*0.82*math.cos(am):.1f}" y2="{cy+r*0.82*math.sin(am):.1f}" stroke="#666" stroke-width="{4 if big else 3}" stroke-linecap="round"/>')
    s.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+r*0.55*math.cos(ah):.1f}" y2="{cy+r*0.55*math.sin(ah):.1f}" stroke="{DARK}" stroke-width="{9 if big else 7}" stroke-linecap="round"/>')
    # bissetriz
    hh = (hour % 12 + minute / 60)
    if hour < 12:  # manha: lado esquerdo (entre o ponteiro e o 12, passando pelo 11)
        bis = (hh * 30 + 360) / 2
    else:
        bis = (hh * 30) / 2
    ab = math.radians(bis - 90)
    L1 = r + (70 if big else 40)
    s.append(f'<line x1="{cx-(r+18)*math.cos(ab):.1f}" y1="{cy-(r+18)*math.sin(ab):.1f}" x2="{cx}" y2="{cy}" stroke="{GREEN}" stroke-width="2" stroke-dasharray="6 5"/>')
    s.append(arrow(cx, cy, cx + L1 * math.cos(ab), cy + L1 * math.sin(ab), GREEN, 5 if big else 4))
    s.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{DARK}"/>')
    return "".join(s), (cx + (L1 + 14) * math.cos(ab), cy + (L1 + 14) * math.sin(ab)), (cx - (r + 30) * math.cos(ab), cy - (r + 30) * math.sin(ab))
b = []
cx, cy, r = 190, 300, 118
b.append(sun(cx, 70))
b.append(f'<line x1="{cx}" y1="94" x2="{cx}" y2="{cy-r-12}" stroke="#e8a400" stroke-width="3" stroke-dasharray="7 5"/>')
b.append(text(cx + 42, 72, "1. Aponte o 12", 13, "#8a6200", True)); b.append(text(cx + 42, 88, "para o SOL", 13, "#8a6200", True))
s, pn, ps = dial(cx, cy, r, 10, 0); b.append(s)
b.append(text(pn[0] - 22, pn[1] - 2, "NORTE", 17, GREEN, True, "middle"))
b.append(text(ps[0] + 2, ps[1] + 14, "SUL", 14, GREEN, True, "middle"))
b.append(text(40, cy + r + 46, "2. Exemplo: 10 h da manhã. A linha do", 12.5, "#222", True))
b.append(text(40, cy + r + 63, "MEIO entre o 12 e o ponteiro das horas", 12.5, "#222", True))
b.append(text(40, cy + r + 80, "(aqui, no 11) aponta o NORTE.", 12.5, "#222", True))
# exemplo da tarde
cx2, cy2, r2 = 540, 168, 66
b.append(sun(cx2, 58, 12))
b.append(f'<line x1="{cx2}" y1="76" x2="{cx2}" y2="{cy2-r2-10}" stroke="#e8a400" stroke-width="2.5" stroke-dasharray="6 4"/>')
s, pn2, ps2 = dial(cx2, cy2, r2, 16, 0, big=False); b.append(s)
b.append(text(pn2[0] + 2, pn2[1] - 2, "NORTE", 13, GREEN, True, "middle"))
b.append(text(cx2 - 10, cy2 + r2 + 32, "À tarde (16 h): a linha", 12, "#222", True, "middle"))
b.append(text(cx2 - 10, cy2 + r2 + 47, "do meio fica no 2.", 12, "#222", True, "middle"))
b.append(box(400, 300, 260, 216, "#fff4e5", "#ef8a2b"))
b.append(lines(412, 322, ["*Só vale no HEMISFÉRIO SUL.", "(No hemisfério norte é o ponteiro", "das horas que aponta para o sol, e a", "linha do meio indica o SUL.)",
                          "*Horário de verão: use o 1 no", "lugar do 12.",
                          "*Erro de 15° a 30°. Não use perto", "do meio-dia nem no Norte e", "Nordeste quando o sol está quase", "a pino; ali prefira a sombra."], 12, 18.5))
open(D + "relogio-hemisferio-sul.svg", "w").write(svg(680, 520, "Achar o NORTE com relógio de ponteiros (hemisfério sul)", "\n".join(b)))

# ---------- SOMBRA DO GRAVETO ----------
b = []
b.append('<rect x="20" y="50" width="420" height="380" rx="8" fill="#e8d3b0" stroke="#c9a978"/>')
b.append(text(230, 70, "vista de cima", 12, "#6b4f2a", False, "middle"))
st = (300, 112)
t1 = (140, 282); t2 = (232, 282)
b.append(f'<line x1="{st[0]}" y1="{st[1]}" x2="{t1[0]}" y2="{t1[1]}" stroke="#6b5a40" stroke-width="7" stroke-opacity="0.45" stroke-linecap="round"/>')
b.append(f'<line x1="{st[0]}" y1="{st[1]}" x2="{t2[0]}" y2="{t2[1]}" stroke="#6b5a40" stroke-width="7" stroke-opacity="0.75" stroke-linecap="round"/>')
b.append(f'<circle cx="{st[0]}" cy="{st[1]}" r="9" fill="#8b5a2b" stroke="{DARK}" stroke-width="2.5"/>')
b.append(text(st[0] - 16, st[1] - 10, "graveto reto,", 12, "#222", True, "end")); b.append(text(st[0] - 16, st[1] + 5, "~1 m, bem em pé", 12, "#222", True, "end"))
b.append(text(196, 196, "sombra 1", 11.5, "#444", True, "end")); b.append(text(196, 210, "(agora)", 11.5, "#444", False, "end"))
b.append(text(282, 200, "sombra 2", 11.5, "#444", True)); b.append(text(282, 214, "(15–20 min", 11.5, "#444")); b.append(text(282, 228, "depois)", 11.5, "#444"))
# linha O-L
b.append(f'<line x1="40" y1="282" x2="425" y2="282" stroke="{RED}" stroke-width="3"/>')
b.append(arrow(380, 282, 428, 282, RED, 3))
b.append(text(34, 270, "OESTE", 14, "#b3001b", True))
b.append(text(318, 270, "LESTE", 14, "#b3001b", True))
# linha N-S
NX = 395
b.append(f'<line x1="{NX}" y1="96" x2="{NX}" y2="410" stroke="{GREEN}" stroke-width="3"/>')
b.append(arrow(NX, 140, NX, 92, GREEN, 3))
b.append(text(NX - 8, 104, "NORTE", 14, GREEN, True, "end"))
b.append(text(NX - 8, 412, "SUL", 14, GREEN, True, "end"))
b.append(f'<rect x="{NX}" y="268" width="14" height="14" fill="none" stroke="{DARK}" stroke-width="1.5"/>')
# marcas
for i, t in enumerate((t1, t2)):
    b.append(f'<circle cx="{t[0]}" cy="{t[1]}" r="12" fill="#a8a29a" stroke="{DARK}" stroke-width="2"/>')
    b.append(text(t[0], t[1] + 5, str(i + 1), 13, "#fff", True, "middle"))
# pes
def foot(x, y, rot):
    return f'<ellipse cx="{x}" cy="{y}" rx="9" ry="20" fill="#f2c9a5" stroke="{DARK}" stroke-width="2" transform="rotate({rot} {x} {y})"/>'
b.append(foot(t1[0], t1[1] + 40, 0)); b.append(foot(t2[0], t2[1] + 40, 0))
b.append(text(186, 372, "pé esquerdo na 1, pé direito na 2:", 11.5, "#222", True, "middle"))
b.append(text(186, 388, "você fica de frente para o NORTE", 11.5, GREEN, True, "middle"))
b.append(box(452, 50, 208, 380, "#fff4e5", "#ef8a2b"))
b.append(lines(464, 74, ["*1. Finque o graveto em", "chão plano e marque a", "ponta da sombra com", "uma pedra (marca 1).",
                         "*2. Espere 15 a 20", "minutos. Marque a nova", "ponta da sombra", "(marca 2).",
                         "*3. A linha da marca 1", "para a 2 vai de OESTE", "para LESTE.",
                         "*4. Uma linha em ângulo", "reto com ela dá o", "NORTE–SUL.",
                         "Funciona em qualquer", "lugar e época, com", "qualquer sol que faça", "sombra. Mais preciso", "perto do meio-dia."], 12, 17.4))
open(D + "sombra-graveto.svg", "w").write(svg(680, 440, "Método da sombra do graveto", "\n".join(b)))

# ---------- BUSSOLA: PARTES E COMO TIRAR UM RUMO ----------
b = []
# placa base
bx0, by0 = 70, 70
b.append(f'<rect x="{bx0}" y="{by0}" width="180" height="330" rx="16" fill="#e6f0f7" stroke="{DARK}" stroke-width="2.5"/>')
for i in range(0, 21):  # regua
    yy = by0 + 150 + i * 8.5
    b.append(f'<line x1="{bx0}" y1="{yy}" x2="{bx0 + (14 if i % 5 == 0 else 8)}" y2="{yy}" stroke="{DARK}" stroke-width="1.5"/>')
# seta de direcao
b.append(f'<polygon points="{bx0+90},{by0+10} {bx0+78},{by0+40} {bx0+86},{by0+40} {bx0+86},{by0+76} {bx0+94},{by0+76} {bx0+94},{by0+40} {bx0+102},{by0+40}" fill="{DARK}"/>')
# limbo
ccx, ccy, cr = bx0 + 90, by0 + 190, 74
b.append(f'<circle cx="{ccx}" cy="{ccy}" r="{cr+12}" fill="#d9dde2" stroke="{DARK}" stroke-width="2.5"/>')
b.append(f'<circle cx="{ccx}" cy="{ccy}" r="{cr}" fill="#f8fbff" stroke="{DARK}" stroke-width="1.5"/>')
for d in range(0, 360, 10):
    a = math.radians(d - 90)
    l = 8 if d % 30 == 0 else 5
    b.append(f'<line x1="{ccx+(cr+12)*math.cos(a):.1f}" y1="{ccy+(cr+12)*math.sin(a):.1f}" x2="{ccx+(cr+12-l)*math.cos(a):.1f}" y2="{ccy+(cr+12-l)*math.sin(a):.1f}" stroke="{DARK}" stroke-width="1.5"/>')
for d, lab in ((0, "N"), (90, "L"), (180, "S"), (270, "O")):
    a = math.radians(d - 90)
    b.append(text(ccx + (cr - 10) * math.cos(a), ccy + (cr - 10) * math.sin(a) + 5, lab, 13, RED if lab == "N" else DARK, True, "middle"))
# linhas meridianas e seta de orientacao
for dx in (-40, -20, 20, 40):
    hh = math.sqrt(cr * cr - dx * dx) - 4
    b.append(f'<line x1="{ccx+dx}" y1="{ccy-hh:.1f}" x2="{ccx+dx}" y2="{ccy+hh:.1f}" stroke="#d62828" stroke-width="1" stroke-opacity="0.6"/>')
b.append(f'<polygon points="{ccx},{ccy-58} {ccx-12},{ccy-30} {ccx-5},{ccy-30} {ccx-5},{ccy+40} {ccx+5},{ccy+40} {ccx+5},{ccy-30} {ccx+12},{ccy-30}" fill="none" stroke="{RED}" stroke-width="2.5"/>')
# agulha
b.append(f'<polygon points="{ccx},{ccy-52} {ccx-7},{ccy} {ccx+7},{ccy}" fill="{RED}" stroke="{DARK}" stroke-width="1.5"/>')
b.append(f'<polygon points="{ccx},{ccy+52} {ccx-7},{ccy} {ccx+7},{ccy}" fill="#fff" stroke="{DARK}" stroke-width="1.5"/>')
b.append(f'<circle cx="{ccx}" cy="{ccy}" r="4" fill="{DARK}"/>')
# indice
b.append(f'<line x1="{ccx}" y1="{ccy-cr-24}" x2="{ccx}" y2="{ccy-cr-12}" stroke="{DARK}" stroke-width="3"/>')
# rotulos
def lab(x1, y1, x2, y2, t1, t2=""):
    s = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#555" stroke-width="1.3"/><circle cx="{x1}" cy="{y1}" r="2.5" fill="#555"/>'
    s += text(x2 + 5, y2 + 4, t1, 12, "#222", True)
    if t2: s += text(x2 + 5, y2 + 19, t2, 11.5, "#444")
    return s
b.append(lab(ccx + 6, by0 + 30, 262, 86, "seta de direção", "(aponte para o alvo)"))
b.append(lab(ccx + 2, ccy - cr - 20, 262, 128, "índice", "(leia o rumo aqui)"))
b.append(lab(ccx + 60, ccy - 50, 262, 168, "limbo giratório", "(graus de 0 a 360)"))
b.append(lab(ccx + 3, ccy - 40, 262, 212, "agulha: parte VERMELHA", "aponta o norte magnético"))
b.append(lab(ccx - 10, ccy + 20, 262, 256, "seta de orientação", "(no fundo do limbo)"))
b.append(lab(ccx + 40, ccy + 40, 262, 300, "linhas meridianas", "(alinhe com o norte do mapa)"))
b.append(lab(bx0 + 10, by0 + 300, 262, 346, "régua (para o mapa)"))
# passos
b.append(box(470, 60, 190, 340, "#eef5ff", BLUE))
b.append(lines(480, 84, ["*Tirar um rumo:", "*1. Segure a bússola", "na altura do peito,", "bem na horizontal, com", "a seta de direção", "apontando para o alvo.",
                         "*2. Gire o limbo até a", "seta de orientação", "ficar embaixo da parte", "VERMELHA da agulha", "(\"vermelho na casinha\").",
                         "*3. Leia o número no", "índice: é o rumo", "magnético (ex.: 120°).",
                         "*4. Para seguir: mantenha", "o vermelho na casinha e", "ande para onde a seta", "de direção aponta."], 12, 17.5))
b.append(text(340, 428, "Longe de ferro, carro, cerca de arame, celular, rádio e fios: tudo isso desvia a agulha.", 12.5, "#b3001b", True, "middle"))
open(D + "bussola-rumo.svg", "w").write(svg(680, 442, "Bússola: partes e como tirar um rumo", "\n".join(b)))

# ---------- DECLINACAO MAGNETICA ----------
b = []
ox, oy = 170, 330
b.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="80" stroke="{DARK}" stroke-width="3"/>')
b.append(star(ox, 70, 12, DARK))
b.append(text(ox, 52, "NORTE VERDADEIRO", 12.5, "#222", True, "middle")); b.append(text(ox, 66 - 30, "", 1))
dec = 22; a = math.radians(-dec)
mx_, my_ = ox + 250 * math.sin(a), oy - 250 * math.cos(a)
b.append(f'<line x1="{ox}" y1="{oy}" x2="{mx_:.1f}" y2="{my_:.1f}" stroke="{RED}" stroke-width="3"/>')
b.append(f'<polygon points="{mx_:.1f},{my_-6:.1f} {mx_-7:.1f},{my_+12:.1f} {mx_+7:.1f},{my_+12:.1f}" fill="{RED}" transform="rotate({-dec} {mx_:.1f} {my_:.1f})"/>')
b.append(text(mx_ - 6, my_ - 30, "NORTE DA", 12.5, "#b3001b", True, "middle")); b.append(text(mx_ - 6, my_ - 15, "BÚSSOLA", 12.5, "#b3001b", True, "middle"))
b.append(f'<path d="M{ox} {oy-150} A150 150 0 0 0 {ox+150*math.sin(a):.1f} {oy-150*math.cos(a):.1f}" fill="none" stroke="{BLUE}" stroke-width="2.5"/>')
b.append(text(ox - 92, oy - 168, f"{dec}°", 15, BLUE, True, "middle"))
b.append(text(ox - 92, oy - 152, "oeste", 12, BLUE, True, "middle"))
# alvo leste
b.append(f'<line x1="{ox}" y1="{oy}" x2="{ox+170}" y2="{oy}" stroke="{GREEN}" stroke-width="3"/>')
b.append(arrow(ox + 140, oy, ox + 178, oy, GREEN, 3))
b.append(text(ox + 110, oy + 22, "alvo a LESTE", 12.5, GREEN, True, "middle"))
b.append(f'<path d="M{ox} {oy-60} A60 60 0 0 1 {ox+60} {oy}" fill="none" stroke="#222" stroke-width="1.5"/>')
b.append(text(ox + 46, oy - 50, "90° no mapa", 11.5, "#222", True))
b.append(f'<path d="M{ox+100*math.sin(a):.1f} {oy-100*math.cos(a):.1f} A100 100 0 0 1 {ox+100} {oy}" fill="none" stroke="{RED}" stroke-width="1.5" stroke-dasharray="5 4"/>')
b.append(text(ox + 72, oy - 104, "112° na bússola", 11.5, "#b3001b", True))
b.append(f'<circle cx="{ox}" cy="{oy}" r="5" fill="{DARK}"/>')
b.append(box(380, 60, 280, 280, "#fff4e5", "#ef8a2b"))
b.append(lines(392, 84, ["*No Brasil a agulha aponta", "*8° a 24° A OESTE do norte", "*verdadeiro (do mapa).",
                         "", "*MAPA → BÚSSOLA: SOME", "Rumo no mapa 90° + 22° =", "112° na bússola.",
                         "", "*BÚSSOLA → MAPA: SUBTRAIA", "Rumo na bússola 112° − 22° =", "90° no mapa.",
                         "", "Errar 20° faz você sair 350 m", "do alvo a cada 1 km andado.", "Valores de cada cidade: tabela", "no texto. Muda ~0,1° por ano."], 12, 16.5))
b.append(text(340, 370, "Exemplo para São Paulo (declinação 22° oeste em 2026).", 12.5, "#444", False, "middle"))
open(D + "declinacao-magnetica.svg", "w").write(svg(680, 384, "Declinação magnética: corrigir a bússola", "\n".join(b)))

# ---------- CURVAS DE NIVEL ----------
b = []
def h(x):  # perfil de um morro: lado esquerdo íngreme, direito suave (x de 0 a 1)
    if x < 0.35: return max(0, 1 - ((0.35 - x) / 0.22) ** 1.4) if x > 0.13 else 0
    return max(0, 1 - ((x - 0.35) / 0.55) ** 1.2)
X0, X1 = 80, 420; Ybase, Htop = 220, 140
pts = [(X0 + (X1 - X0) * i / 200, Ybase - Htop * h(i / 200)) for i in range(201)]
b.append('<path d="M' + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + f' L{X1} {Ybase} L{X0} {Ybase} Z" fill="#c9b48a" stroke="{DARK}" stroke-width="2.5"/>')
levels = [0.2, 0.4, 0.6, 0.8]; names = ["100 m", "120 m", "140 m", "160 m"]
mapy0 = 286
def crossings(lv):
    xs = [i / 1000 for i in range(1001)]
    left = next(x for x in xs if h(x) >= lv); right = next(x for x in reversed(xs) if h(x) >= lv)
    return X0 + (X1 - X0) * left, X0 + (X1 - X0) * right
cyc = mapy0 + 104
b.append(f'<rect x="{X0-20}" y="{mapy0}" width="{X1-X0+40}" height="204" rx="6" fill="#f5f0e1" stroke="#c9bba0"/>')
for lv, nm in zip(levels, names):
    yl = Ybase - Htop * lv; xl, xr = crossings(lv)
    b.append(f'<line x1="{X0-20}" y1="{yl:.1f}" x2="{X1+8}" y2="{yl:.1f}" stroke="#6b4f2a" stroke-width="1" stroke-dasharray="4 4"/>')
    b.append(text(X1 + 12, yl + 4, nm, 11.5, "#6b4f2a", True))
    b.append(f'<line x1="{xl:.1f}" y1="{yl:.1f}" x2="{xl:.1f}" y2="{cyc:.1f}" stroke="#999" stroke-width="1" stroke-dasharray="2 4"/>')
    b.append(f'<line x1="{xr:.1f}" y1="{yl:.1f}" x2="{xr:.1f}" y2="{cyc:.1f}" stroke="#999" stroke-width="1" stroke-dasharray="2 4"/>')
    rx = (xr - xl) / 2; ry = 22 + 50 * (1 - lv)
    b.append(f'<ellipse cx="{(xl+xr)/2:.1f}" cy="{cyc}" rx="{rx:.1f}" ry="{ry:.1f}" fill="none" stroke="#8a5a2b" stroke-width="2.2"/>')
b.append(text(X0 - 12, mapy0 + 18, "o mesmo morro no mapa (visto de cima)", 12, "#6b4f2a", True))
b.append(text(X0 - 14, 70, "o morro de lado (corte)", 12, "#6b4f2a", True))
xl, _ = crossings(0.2)
b.append(text(X0 - 12, mapy0 + 184, "linhas JUNTAS =", 11.5, "#b3001b", True))
b.append(text(X0 - 12, mapy0 + 198, "subida ÍNGREME", 11.5, "#b3001b", True))
b.append(text(X1 + 14, mapy0 + 184, "linhas SEPARADAS =", 11.5, GREEN, True, "end"))
b.append(text(X1 + 14, mapy0 + 198, "subida suave", 11.5, GREEN, True, "end"))
b.append(f'<line x1="{X0-20}" y1="{Ybase}" x2="{X1+8}" y2="{Ybase}" stroke="#6b4f2a" stroke-width="2"/>')
# painel do vale
px0 = 518
b.append(f'<rect x="{px0-18}" y="60" width="160" height="430" rx="6" fill="#f5f0e1" stroke="#c9bba0"/>')
b.append(text(px0 + 62, 82, "VALE com rio", 12.5, "#222", True, "middle"))
b.append(text(px0 + 62, 100, "(nascente no alto)", 11, "#444", False, "middle"))
for i, yv in enumerate((128, 170, 212, 254)):
    b.append(f'<path d="M{px0} {yv+30} L{px0+62} {yv-6} L{px0+124} {yv+30}" fill="none" stroke="#8a5a2b" stroke-width="2.2"/>')
b.append(f'<path d="M{px0+62} 116 L{px0+62} 296" stroke="{BLUE}" stroke-width="3" fill="none"/>')
b.append(arrow(px0 + 62, 270, px0 + 62, 302, BLUE, 3))
b.append(text(px0 + 62, 324, "o V aponta para a", 11.5, "#222", True, "middle"))
b.append(text(px0 + 62, 338, "nascente (rio acima);", 11.5, "#222", True, "middle"))
b.append(text(px0 + 62, 352, "a água desce para", 11.5, "#222", True, "middle"))
b.append(text(px0 + 62, 366, "o lado aberto do V", 11.5, "#222", True, "middle"))
b.append(text(px0 + 62, 398, "CRISTA (espigão):", 11.5, "#222", True, "middle"))
b.append(text(px0 + 62, 412, "o V aponta para", 11.5, "#222", False, "middle"))
b.append(text(px0 + 62, 426, "baixo do morro", 11.5, "#222", False, "middle"))
b.append(text(px0 + 62, 458, "Cada linha liga", 11.5, "#444", False, "middle"))
b.append(text(px0 + 62, 472, "pontos de mesma altura", 10.5, "#444", False, "middle"))
open(D + "curvas-de-nivel.svg", "w").write(svg(680, 502, "Curvas de nível: ler o relevo no mapa", "\n".join(b)))
print("ok")
