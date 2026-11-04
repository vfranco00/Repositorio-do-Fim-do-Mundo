import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
# Figuras de 10-comunicacao-e-navegacao/04-tempo-clima-calendario.md
import math
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "10-comunicacao-e-navegacao", "img") + "/"
os.makedirs(D, exist_ok=True)
GREEN = "#2b8a3e"; RED = "#d62828"; DARK = "#1e1e1e"; BLUE = "#3f6d9e"; ORANGE = "#c26a00"; WOOD = "#8b5a2b"

def puffs(circles, fill="#ffffff", stroke="#7f8c99", base=None, sw=2):
    """Nuvem tipo cúmulo: união de círculos com contorno; base reta opcional."""
    s = "".join(f'<circle cx="{x}" cy="{y}" r="{r+sw}" fill="{stroke}"/>' for x, y, r in circles)
    s += "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>' for x, y, r in circles)
    if base is not None:
        xs = [x - r for x, y, r in circles] + [x + r for x, y, r in circles]
        s += f'<rect x="{min(xs)-sw-1}" y="{base}" width="{max(xs)-min(xs)+2*sw+2}" height="40" fill="BG"/>'
        s += f'<line x1="{min(xs)+6}" y1="{base}" x2="{max(xs)-6}" y2="{base}" stroke="{stroke}" stroke-width="{sw}"/>'
    return s

def sun(cx, cy, r=13, col="#ffd43b", st="#e8a400"):
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" stroke="{st}" stroke-width="2.5"/>'
    for k in range(8):
        a = k * math.pi / 4
        s += f'<line x1="{cx+(r+4)*math.cos(a):.1f}" y1="{cy+(r+4)*math.sin(a):.1f}" x2="{cx+(r+10)*math.cos(a):.1f}" y2="{cy+(r+10)*math.sin(a):.1f}" stroke="{st}" stroke-width="2.5"/>'
    return s

def rain(x0, x1, y0, y1, step=12, col=BLUE):
    return "".join(f'<line x1="{x}" y1="{y0}" x2="{x-6}" y2="{y1}" stroke="{col}" stroke-width="2"/>' for x in range(int(x0), int(x1), step))

def label(cx, y, name, l1, l2, col):
    return (text(cx, y, name, 13, "#222", True, "middle") + text(cx, y + 15, l1, 11.5, col, True, "middle")
            + text(cx, y + 29, l2, 11.5, col, True, "middle"))

# ---------- NUVENS ----------
b = []
SKY = ["#dcebf8", "#e7f1fa", "#f1f7fc"]
bands = [(48, 186, "NUVENS ALTAS (acima de 6 km, finas, de gelo)"), (186, 342, "NUVENS MÉDIAS (2 a 6 km)"), (342, 494, "NUVENS BAIXAS (até 2 km)")]
for i, (y0, y1, t) in enumerate(bands):
    b.append(f'<rect x="20" y="{y0}" width="640" height="{y1-y0}" fill="{SKY[i]}"/>')
    b.append(text(28, y0 + 16, t, 11.5, "#4a5a6a", True))
b.append('<rect x="20" y="494" width="640" height="14" fill="#8fbf6a"/>')
# ALTAS: cirros
for k, (x, y) in enumerate(((70, 122), (120, 110), (165, 126), (210, 114))):
    b.append(f'<path d="M{x} {y} q 30 -4 52 -22 q 6 -6 2 -10" fill="none" stroke="#8aa6c4" stroke-width="3" stroke-linecap="round"/>')
    b.append(f'<path d="M{x+6} {y+6} q 26 -2 44 -16" fill="none" stroke="#a9bfd6" stroke-width="2" stroke-linecap="round"/>')
b.append(label(160, 148, "CIRROS (\"rabo de galo\")", "poucos e parados: tempo bom", "aumentando: mudança em 1–2 dias", ORANGE))
# cirrostratos com halo
b.append(sun(380, 100, 11))
b.append(f'<circle cx="380" cy="100" r="34" fill="none" stroke="#c8a2c8" stroke-width="3" stroke-opacity="0.9"/>')
b.append(f'<rect x="290" y="76" width="190" height="48" rx="24" fill="#ffffff" fill-opacity="0.55"/>')
b.append(label(390, 146, "CIRROESTRATOS (véu)", "halo no sol ou na lua:", "chuva provável em 12–24 h", ORANGE))
# MEDIAS: altocumulos
for row in range(3):
    for col in range(5):
        x = 46 + col * 24 + (row % 2) * 11; y = 222 + row * 15
        b.append(f'<ellipse cx="{x}" cy="{y}" rx="11" ry="6.5" fill="#fff" stroke="#8a98a6" stroke-width="1.5"/>')
b.append(label(95, 284, "ALTOCÚMULOS", "\"céu pedrento\":", "mudança de tempo", ORANGE))
# altostratos
b.append(f'<rect x="194" y="210" width="132" height="44" rx="10" fill="#b9c3cc" stroke="#8a98a6" stroke-width="1.5"/>')
b.append(f'<circle cx="260" cy="232" r="11" fill="#f3efe0" fill-opacity="0.85"/>')
b.append(label(260, 284, "ALTOESTRATOS", "sol de vidro fosco:", "chuva em horas", ORANGE))
# nimbostratos
b.append(f'<rect x="362" y="204" width="140" height="50" rx="12" fill="#6f7a86" stroke="#4d5660" stroke-width="1.5"/>')
b.append(rain(376, 502, 258, 276, 10))
b.append(label(432, 296, "NIMBOESTRATOS", "escura e grossa:", "chuva por horas", RED))
# BAIXAS: cumulos
b.append(puffs([(80, 410, 16), (102, 398, 22), (128, 404, 18), (148, 414, 12)], base=420).replace("BG", SKY[2]))
b.append(puffs([(200, 412, 12), (218, 404, 16), (236, 412, 11)], base=420).replace("BG", SKY[2]))
b.append(label(150, 446, "CÚMULOS (algodão)", "base reta, pequenos: BOM TEMPO", "crescendo muito à tarde: pancada", GREEN))
# estratos
b.append(f'<rect x="300" y="384" width="210" height="26" rx="12" fill="#c3c9cf" stroke="#9aa3ab" stroke-width="1.5"/>')
for x in range(312, 506, 16):
    b.append(f'<circle cx="{x}" cy="{418 + (x % 3) * 4}" r="1.6" fill="{BLUE}"/>')
b.append(label(405, 446, "ESTRATOS (neblina alta)", "garoa ou nada; costuma", "abrir no fim da manhã", BLUE))
# cumulonimbo atravessando tudo
cb = [(560, 452, 30), (598, 448, 34), (630, 456, 24), (572, 414, 30), (612, 408, 30), (566, 372, 26), (604, 362, 30),
      (580, 326, 28), (612, 310, 24), (574, 286, 24), (600, 256, 26), (582, 226, 22), (606, 214, 20)]
b.append(f'<path d="M530 168 Q 590 146 658 152 L 658 172 Q 626 182 612 206 L 576 206 Q 560 184 530 182 Z" fill="#ffffff" stroke="#7f8c99" stroke-width="2"/>')
b.append(puffs(cb, "#ffffff", "#7f8c99"))
b.append(f'<path d="M532 468 Q 594 494 652 470 L 648 484 L 538 484 Z" fill="#4d5660"/>')
b.append(rain(546, 646, 486, 504, 9, "#3f6d9e"))
b.append(f'<polygon points="606,474 594,496 604,494 596,512 616,486 606,488 614,474" fill="#ffd43b" stroke="#b38600" stroke-width="1.5"/>')
b.append(text(600, 64, "CUMULONIMBO", 13, RED, True, "middle"))
b.append(text(600, 80, "topo em bigorna", 11.5, RED, True, "middle"))
b.append(text(600, 96, "TEMPESTADE:", 11.5, RED, True, "middle"))
b.append(text(600, 110, "raios, ventania,", 11.5, RED, True, "middle"))
b.append(text(600, 124, "granizo", 11.5, RED, True, "middle"))
# legenda
b.append(f'<rect x="20" y="518" width="640" height="34" rx="6" fill="#f7f7f7" stroke="#ccc"/>')
b.append(f'<rect x="34" y="529" width="12" height="12" fill="{GREEN}"/>'); b.append(text(52, 540, "tempo bom", 12, "#222", True))
b.append(f'<rect x="150" y="529" width="12" height="12" fill="{ORANGE}"/>'); b.append(text(168, 540, "mudança / chuva chegando", 12, "#222", True))
b.append(f'<rect x="372" y="529" width="12" height="12" fill="{RED}"/>'); b.append(text(390, 540, "chuva ou tempestade agora", 12, "#222", True))
open(D + "nuvens.svg", "w").write(svg(680, 562, "Nuvens: o que cada uma anuncia", "\n".join(b)))

# ---------- RELOGIO DE SOL (HORIZONTAL, HEMISFERIO SUL) ----------
b = []
LAT = 20; ang = math.radians(LAT)
# vista de cima (larga)
cx, cy = 340, 104
b.append(f'<rect x="20" y="48" width="640" height="320" rx="8" fill="#f6efe0" stroke="#d6c39b"/>')
b.append(text(30, 66, "Visto de cima — exemplo para latitude 20° S", 12, "#6b4f2a", True))
PX, PY = 290, 222
b.append(f'<rect x="{cx-PX}" y="{cy}" width="{2*PX}" height="{PY}" fill="#e8d3b0" stroke="{DARK}" stroke-width="2"/>')
for hr in range(6, 19):
    t = hr - 12
    th = math.atan(math.sin(ang) * math.tan(math.radians(15 * abs(t)))) if abs(t) < 6 else math.pi / 2
    sgn = -1 if t < 0 else 1  # manhã do lado OESTE (esquerda, com o norte para cima)
    dx, dy = sgn * math.sin(th), math.cos(th)
    lim = min((PX - 4) / abs(dx) if abs(dx) > 1e-6 else 1e9, (PY - 4) / dy if dy > 1e-6 else 1e9)
    ex, ey = cx + dx * lim, cy + dy * lim
    b.append(f'<line x1="{cx}" y1="{cy}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{"#b3001b" if hr == 12 else DARK}" stroke-width="{2.5 if hr == 12 else 1.5}"/>')
    if abs(dy) * lim >= PY - 6:   # linha termina embaixo: rótulo abaixo da placa
        b.append(text(ex, cy + PY + 16, str(hr), 12.5, "#b3001b" if hr == 12 else "#222", True, "middle"))
    elif hr in (6, 18):
        b.append(text(ex - sgn * 4, ey + 18, f"{hr} h", 12.5, "#222", True, "start" if sgn < 0 else "end"))
    else:
        b.append(text(ex + sgn * 6, ey + 4, str(hr), 12.5, "#222", True, "start" if sgn > 0 else "end"))
b.append(f'<polygon points="{cx-5},{cy} {cx+5},{cy} {cx+3},{cy+150} {cx-3},{cy+150}" fill="{WOOD}" stroke="{DARK}" stroke-width="1.5"/>')
b.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{DARK}"/>')
b.append(text(cx, cy - 8, "NORTE", 12, "#222", True, "middle"))
b.append(f'<text x="40" y="{cy+PY/2}" font-size="12" font-weight="bold" fill="#222" text-anchor="middle" transform="rotate(-90 40 {cy+PY/2})">OESTE</text>')
b.append(f'<text x="640" y="{cy+PY/2}" font-size="12" font-weight="bold" fill="#222" text-anchor="middle" transform="rotate(90 640 {cy+PY/2})">LESTE</text>')
b.append(f'<rect x="{cx+10}" y="{cy+108}" width="146" height="32" rx="4" fill="#f6efe0" stroke="{WOOD}"/>')
b.append(text(cx + 16, cy + 121, "gnômon", 11.5, WOOD, True)); b.append(text(cx + 16, cy + 135, "(ponta alta para o SUL)", 11, WOOD))
b.append(text(cx - 200, cy + 40, "MANHÃ", 13, "#6b4f2a", True, "middle")); b.append(text(cx + 200, cy + 40, "TARDE", 13, "#6b4f2a", True, "middle"))
b.append(text(cx, cy + PY + 32, "SUL", 12, "#222", True, "middle"))
# vista de lado
b.append(f'<rect x="20" y="380" width="300" height="170" rx="8" fill="#f4f8fc" stroke="#c6d4e3"/>')
b.append(text(170, 398, "De lado (olhando do leste)", 12, "#4a5a6a", True, "middle"))
gy = 504
b.append(f'<line x1="30" y1="{gy+12}" x2="310" y2="{gy+12}" stroke="#6b4f2a" stroke-width="3"/>')
b.append(f'<rect x="56" y="{gy}" width="200" height="12" fill="#d9c29a" stroke="{DARK}" stroke-width="2"/>')
x0 = 70; Lg = 170
xe, ye = x0 + Lg * math.cos(ang), gy - Lg * math.sin(ang)
b.append(f'<polygon points="{x0},{gy} {xe:.1f},{ye:.1f} {xe:.1f},{gy}" fill="{WOOD}" stroke="{DARK}" stroke-width="2"/>')
b.append(f'<line x1="{xe:.1f}" y1="{ye:.1f}" x2="{xe+60*math.cos(ang):.1f}" y2="{ye-60*math.sin(ang):.1f}" stroke="{RED}" stroke-width="2.5" stroke-dasharray="7 5"/>')
b.append(arrow(xe + 40 * math.cos(ang), ye - 40 * math.sin(ang), xe + 66 * math.cos(ang), ye - 66 * math.sin(ang), RED, 2.5))
b.append(text(186, 420, "aponta para o Polo", 11.5, "#b3001b", True)); b.append(text(186, 434, "Sul Celeste", 11.5, "#b3001b", True))
b.append(f'<path d="M{x0+50} {gy} A50 50 0 0 0 {x0+50*math.cos(ang):.1f} {gy-50*math.sin(ang):.1f}" fill="none" stroke="{BLUE}" stroke-width="2.5"/>')
b.append(text(36, 444, "ângulo = sua", 11.5, BLUE, True)); b.append(text(36, 458, f"latitude (ex.: {LAT}°)", 11.5, BLUE, True))
b.append(f'<line x1="90" y1="464" x2="{x0+46}" y2="{gy-8}" stroke="{BLUE}" stroke-width="1.5"/>')
b.append(text(34, gy + 30, "NORTE", 11.5, "#222", True)); b.append(text(306, gy + 30, "SUL", 11.5, "#222", True, "end"))
b.append(text(170, gy + 30, "placa NIVELADA", 11, "#444", False, "middle"))
# passos
b.append(box(332, 380, 328, 170, "#fff4e5", "#ef8a2b"))
rows = ["*1. Placa plana e nivelada.", "*2. Linha das 12 h no rumo norte–sul", "verdadeiro (sombra mais curta do dia).",
        "*3. Gnômon com ângulo = latitude.", "*4. Horas: use a tabela do texto, ou", "marque a sombra de hora em hora com", "um relógio que ainda funcione.",
        "*5. Marca a hora SOLAR: corrija com", "a tabela do texto. A sombra anda no", "sentido anti-horário."]
for i, r in enumerate(rows):
    b.append(text(344, 400 + i * 15.6, r.lstrip("*"), 12, "#222", r.startswith("*")))
open(D + "relogio-de-sol.svg", "w").write(svg(680, 560, "Relógio de sol (hemisfério sul)", "\n".join(b)))

# ---------- FASES DA LUA (VISTAS DO BRASIL) ----------
def moon(cx, cy, r, p):
    """p: 0 nova, 0.25 quarto crescente, 0.5 cheia, 0.75 quarto minguante. Hemisfério sul: crescente iluminada à ESQUERDA."""
    DK, LT = "#3a3f4b", "#f4e9b8"
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{DK}" stroke="{DARK}" stroke-width="2"/>'
    if abs(p - 0) < 1e-6 or abs(p - 1) < 1e-6:
        return s
    if abs(p - 0.5) < 1e-6:
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{LT}" stroke="{DARK}" stroke-width="2"/>'
    k = math.cos(2 * math.pi * p); rx = abs(k) * r
    waxing = p < 0.5
    if waxing:  # lado iluminado à esquerda
        limb_sweep = 0; term_sweep = 1 if p < 0.25 else 0
    else:
        limb_sweep = 1; term_sweep = 0 if p > 0.75 else 1
    d = f"M{cx} {cy-r} A{r} {r} 0 0 {limb_sweep} {cx} {cy+r} A{rx:.2f} {r} 0 0 {term_sweep} {cx} {cy-r} Z"
    return s + f'<path d="{d}" fill="{LT}"/>' + f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{DARK}" stroke-width="2"/>'
b = []
ph = [(0.0, "NOVA", "", "não aparece"), (0.12, "crescente", "", "fim de tarde"),
      (0.25, "QUARTO", "CRESCENTE", "tarde e noite"), (0.38, "crescente", "gibosa", "noite"),
      (0.5, "CHEIA", "", "a noite toda"), (0.62, "minguante", "gibosa", "noite e manhã"),
      (0.75, "QUARTO", "MINGUANTE", "manhã"), (0.88, "minguante", "", "madrugada")]
for i, (p, n1, n2, n3) in enumerate(ph):
    cx = 58 + i * 81; cy = 100
    b.append(moon(cx, cy, 30, p))
    big = n1.isupper()
    b.append(text(cx, 152, n1, 12 if big else 11.5, "#222", True, "middle"))
    if n2: b.append(text(cx, 166, n2, 11.5 if big else 11, "#222" if big else "#444", big, "middle"))
    b.append(text(cx, 184 if n2 else 168, n3, 10.5, "#2b6a1e", True, "middle"))
b.append(arrow(80, 200, 600, 200, "#888", 2.5))
b.append(text(340, 222, "cerca de 7,4 dias entre cada fase principal · ciclo completo: 29,5 dias", 12, "#222", True, "middle"))
# C e D
b.append(box(20, 240, 312, 170, "#eef5ff", BLUE))
b.append(text(176, 262, "No Brasil a Lua \"não mente\":", 13, "#222", True, "middle"))
b.append(moon(84, 316, 28, 0.15))
b.append(text(84, 366, "C", 22, BLUE, True, "middle")); b.append(text(84, 384, "Crescente", 12, BLUE, True, "middle"))
b.append(moon(240, 316, 28, 0.85))
b.append(text(240, 366, "D", 22, BLUE, True, "middle")); b.append(text(240, 384, "Decrescente", 12, BLUE, True, "middle"))
b.append(text(176, 402, "(no Norte e Nordeste ela aparece mais \"deitada\")", 10.5, "#444", False, "middle"))
b.append(box(346, 240, 314, 170, "#fff4e5", "#ef8a2b"))
b.append(text(503, 262, "Marés", 13, "#222", True, "middle"))
mr = ["*Lua NOVA e CHEIA: marés de sizígia", "(\"de lua\"): sobe mais e desce mais.",
      "*QUARTOS: marés de quadratura,", "as mais fracas.",
      "2 marés altas e 2 baixas por dia;", "atrasam ~50 min a cada dia.",
      "Anote a hora da maré alta na lua", "cheia: repete na próxima nova/cheia."]
for i, r in enumerate(mr):
    b.append(text(358, 284 + i * 15.5, r.lstrip("*"), 12, "#222", r.startswith("*")))
b.append(text(340, 430, "A Lua nasce cerca de 50 minutos mais tarde a cada dia.", 12.5, "#222", True, "middle"))
open(D + "fases-da-lua.svg", "w").write(svg(680, 444, "Fases da Lua vistas do Brasil", "\n".join(b)))

# ---------- CALENDARIO PELO SOL ----------
b = []
# painel esquerdo: nascer do sol no horizonte (olhando para o leste)
b.append(f'<rect x="20" y="48" width="320" height="316" rx="8" fill="#f4f8fc" stroke="#c6d4e3"/>')
b.append(text(180, 68, "Onde o sol NASCE (olhando para o leste)", 12, "#4a5a6a", True, "middle"))
hy = 220
b.append(f'<path d="M20 {hy} L60 {hy-20} L92 {hy-8} L130 {hy-34} L160 {hy-14} L200 {hy-22} L246 {hy-6} L282 {hy-28} L340 {hy-10} L340 {hy+60} L20 {hy+60} Z" fill="#9fb98a" stroke="#4f7a35" stroke-width="2"/>')
pos = [(80, "JUNHO", "solstício", "de inverno", ORANGE), (180, "MAR e SET", "equinócios:", "leste exato", GREEN), (280, "DEZEMBRO", "solstício", "de verão", RED)]
for x, a1, a2, a3, col in pos:
    b.append(sun(x, hy - 50, 12))
    b.append(f'<line x1="{x}" y1="{hy-30}" x2="{x}" y2="{hy+6}" stroke="{col}" stroke-width="2" stroke-dasharray="4 3"/>')
    b.append(text(x, 104, a1, 12, col, True, "middle")); b.append(text(x, 118, a2, 11, "#444", False, "middle")); b.append(text(x, 131, a3, 11, "#444", False, "middle"))
b.append(f'<path d="M98 {hy-74} Q 180 {hy-92} 262 {hy-74}" fill="none" stroke="#888" stroke-width="2"/>')
b.append(arrow(240, hy - 79, 264, hy - 74, "#888", 2)); b.append(arrow(120, hy - 79, 96, hy - 74, "#888", 2))
b.append(text(40, hy + 26, "esquerda = NORTE", 11, "#222", True)); b.append(text(320, hy + 26, "direita = SUL", 11, "#222", True, "end"))
b.append(text(180, hy + 52, "até 23° a 28° para cada lado", 11.5, "#222", True, "middle"))
b.append(text(30, 296, "Marque, do mesmo lugar, onde o sol nasce", 11.5, "#222"))
b.append(text(30, 311, "(estaca, árvore, morro). Nos extremos ele", 11.5, "#222"))
b.append(text(30, 326, "\"para\" uns dias e volta: é o solstício.", 11.5, "#222"))
# painel direito: sombra do meio-dia
b.append(f'<rect x="350" y="48" width="310" height="316" rx="8" fill="#f6efe0" stroke="#d6c39b"/>')
b.append(text(505, 68, "Sombra ao MEIO-DIA de uma vara de 1 m", 12, "#6b4f2a", True, "middle"))
b.append(text(505, 84, "(exemplo: Brasília, 16° S)", 11, "#6b4f2a", False, "middle"))
gx, gy, S = 470, 262, 130
b.append(f'<line x1="360" y1="{gy}" x2="650" y2="{gy}" stroke="#6b4f2a" stroke-width="3"/>')
b.append(f'<line x1="{gx}" y1="{gy}" x2="{gx}" y2="{gy-S}" stroke="{WOOD}" stroke-width="6"/>')
b.append(text(gx - 8, gy - S / 2, "1 m", 12, "#222", True, "end"))
for L, lab, col, dy in ((0.82, "junho: 82 cm", ORANGE, 20), (0.28, "mar/set: 28 cm", GREEN, 38), (-0.13, "dez: 13 cm", RED, 20)):
    xe = gx + L * S
    b.append(f'<line x1="{gx}" y1="{gy-S}" x2="{xe:.1f}" y2="{gy}" stroke="{col}" stroke-width="1.6" stroke-dasharray="5 4"/>')
    b.append(f'<line x1="{gx}" y1="{gy+4+ (0 if L>0 else 0)}" x2="{xe:.1f}" y2="{gy+4}" stroke="{col}" stroke-width="5"/>')
    b.append(f'<circle cx="{xe:.1f}" cy="{gy}" r="4.5" fill="{col}"/>')
    b.append(text(xe + (0 if L > 0 else 4), gy + dy + 4, lab, 11.5, col, True, "middle" if L > 0 else "end"))
b.append(text(368, gy - 6, "NORTE", 11, "#444", True)); b.append(text(646, gy - 6, "SUL", 11, "#444", True, "end"))
b.append(text(505, 324, "A sombra mais longa do ano é em junho e", 11.5, "#222", False, "middle"))
b.append(text(505, 339, "a mais curta em dezembro. Ao norte de", 11.5, "#222", False, "middle"))
b.append(text(505, 354, "~23° S, em dezembro ela aponta para o norte.", 11.5, "#222", False, "middle"))
b.append(box(20, 376, 640, 76, "#fff4e5", "#ef8a2b"))
b.append(text(34, 398, "Solstício de inverno: ~21 de junho (dia mais curto do ano).", 12.5, "#222", True))
b.append(text(34, 416, "Equinócios: ~20 de março e ~22 de setembro (dia = noite; o sol nasce no leste exato).", 12.5, "#222", True))
b.append(text(34, 434, "Solstício de verão: ~21 de dezembro (dia mais longo do ano).", 12.5, "#222", True))
open(D + "calendario-pelo-sol.svg", "w").write(svg(680, 462, "Descobrir a época do ano pelo sol", "\n".join(b)))

# ---------- BAROMETRO CASEIRO ----------
b = []
# pote
b.append(f'<path d="M110 150 L110 330 Q110 350 130 350 L250 350 Q270 350 270 330 L270 150 Z" fill="#e8f3fd" stroke="{DARK}" stroke-width="3"/>')
b.append(f'<rect x="102" y="136" width="176" height="16" rx="4" fill="#cfe6fb" stroke="{DARK}" stroke-width="2.5"/>')
b.append(f'<path d="M100 136 Q 190 118 280 136" fill="#e86a6a" stroke="#9b2c2c" stroke-width="2.5"/>')
b.append(f'<rect x="98" y="138" width="184" height="8" fill="#555"/>')
b.append(text(190, 250, "pote de vidro", 12, "#222", True, "middle")); b.append(text(190, 266, "bem fechado", 12, "#222", True, "middle"))
b.append(text(190, 290, "(o ar de dentro", 11, "#444", False, "middle")); b.append(text(190, 304, "fica preso)", 11, "#444", False, "middle"))
# canudo apoiado na borda
b.append(f'<line x1="190" y1="127" x2="470" y2="140" stroke="#2b8a3e" stroke-width="5" stroke-linecap="round"/>')
b.append(f'<rect x="182" y="120" width="16" height="10" fill="#ddd" stroke="#555"/>')
b.append(text(140, 96, "bexiga esticada e", 11.5, "#9b2c2c", True)); b.append(text(140, 110, "presa com elástico", 11.5, "#9b2c2c", True))
b.append(text(284, 162, "canudo colado no centro", 11.5, GREEN, True)); b.append(text(284, 176, "da bexiga, apoiado na borda", 11.5, GREEN))
# escala
b.append(f'<rect x="480" y="60" width="16" height="170" fill="#fffbe6" stroke="{DARK}" stroke-width="2"/>')
for i in range(9):
    yy = 72 + i * 18
    b.append(f'<line x1="480" y1="{yy}" x2="{490 if i % 2 else 496}" y2="{yy}" stroke="{DARK}" stroke-width="1.5"/>')
b.append(text(506, 82, "PRESSÃO SUBINDO", 12, GREEN, True)); b.append(text(506, 97, "(ponta sobe)", 11.5, GREEN))
b.append(text(506, 112, "tempo firme", 11.5, GREEN))
b.append(text(506, 196, "PRESSÃO CAINDO", 12, RED, True)); b.append(text(506, 211, "(ponta desce)", 11.5, RED))
b.append(text(506, 226, "chuva ou vento", 11.5, RED))
b.append(arrow(470, 156, 470, 196, RED, 3)); b.append(arrow(470, 124, 470, 84, GREEN, 3))
b.append(box(20, 370, 640, 112, "#eef5ff", BLUE))
rows = ["*O que importa é a TENDÊNCIA, não o número. Anote 2 vezes por dia, nas mesmas horas.",
        "Queda lenta e contínua por 1–2 dias: tempo piorando, frente chegando.",
        "*Queda rápida em poucas horas: tempestade ou ventania próxima. Prepare-se.",
        "Subida depois da chuva: tempo melhorando (no Sul e Sudeste, frio chegando com vento sul).",
        "*Deixe na sombra, longe do fogão e do sol: o calor também mexe o ponteiro."]
for i, r in enumerate(rows):
    b.append(text(34, 392 + i * 19, r.lstrip("*"), 12.2, "#222", r.startswith("*")))
open(D + "barometro-caseiro.svg", "w").write(svg(680, 492, "Barômetro caseiro de pote e bexiga", "\n".join(b)))
print("ok")
