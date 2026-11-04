import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
import math
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "08-ferramentas-e-mecanica", "img") + "/"
os.makedirs(D, exist_ok=True)
STEEL = "#b8c2cc"; STEEL_D = "#7d8a96"; STONE = "#8f8f8f"; RED = "#d62828"; DRED = "#b3001b"; GREEN = "#2b8a3e"


def lines(x, y, ls, size=12, color="#222", bold=False, anchor="start", lh=None):
    lh = lh or size * 1.3
    return "\n".join(text(x, y + i * lh, s, size, color, bold, anchor) for i, s in enumerate(ls))


def wrap(s, n):
    out, cur = [], ""
    for w in s.split():
        if len(cur) + len(w) + (1 if cur else 0) > n:
            out.append(cur); cur = w
        else:
            cur = (cur + " " + w) if cur else w
    if cur:
        out.append(cur)
    return out


def arc(cx, cy, r, a1, a2, color="#d62828", w=2.5):
    # angulos em graus, sentido matematico com y para baixo (0 = direita, -90 = cima)
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    x2, y2 = cx + r * math.cos(math.radians(a2)), cy + r * math.sin(math.radians(a2))
    sweep = 1 if a2 > a1 else 0
    return f'<path d="M{x1:.1f} {y1:.1f} A {r} {r} 0 0 {sweep} {x2:.1f} {y2:.1f}" fill="none" stroke="{color}" stroke-width="{w}"/>'


def badge(x, y, n, fill="#d62828", r=14):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="#fff" stroke-width="2.5"/>'
            f'<text x="{x}" y="{y+5.5}" font-size="16" font-weight="bold" fill="#fff" text-anchor="middle">{n}</text>')


# =====================================================================
# 1) ANGULOS DE AFIACAO
# =====================================================================
b = []
b.append(text(340, 56, "Ângulo do fio (corte da lâmina visto pela ponta)", 14, "#222", True, "middle"))


def painel(x0, titulo, cor_t="#222"):
    s = box(x0, 66, 210, 250, "#f7f7f7", "#999")
    s += text(x0 + 105, 88, titulo, 13.5, cor_t, True, "middle")
    return s


EY = 236  # y do fio
# --- faca
x0 = 15; cx = x0 + 105; ang = 20; L = 70
dx, dy = L * math.sin(math.radians(ang)), L * math.cos(math.radians(ang))
b.append(painel(x0, "FACA"))
b.append(f'<polygon points="{cx-dx:.1f},104 {cx+dx:.1f},104 {cx+dx:.1f},{EY-dy:.1f} {cx},{EY} {cx-dx:.1f},{EY-dy:.1f}" fill="{STEEL}" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<line x1="{cx}" y1="140" x2="{cx}" y2="{EY+8}" stroke="#555" stroke-width="1.5" stroke-dasharray="5 4"/>')
b.append(arc(cx, EY, 46, -90, -90 + ang))
b.append(text(cx + 22, EY - 50, "20°", 14, DRED, True))
b.append(text(cx, EY + 22, "fio", 11, "#555", False, "middle"))
b.append(lines(cx, 280, ["15–20° de cada lado", "(30–40° no total)"], 12, "#222", False, "middle"))
b.append(text(cx, 308, "corta fino, lasca se bater", 11, "#555", False, "middle"))
# --- facao / machado
x0 = 235; cx = x0 + 105; ang = 28; L = 66
dx, dy = L * math.sin(math.radians(ang)), L * math.cos(math.radians(ang))
b.append(painel(x0, "FACÃO e MACHADO"))
b.append(f'<polygon points="{cx-48},104 {cx+48},104 {cx+dx:.1f},{EY-dy:.1f} {cx},{EY} {cx-dx:.1f},{EY-dy:.1f}" fill="{STEEL}" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<line x1="{cx}" y1="140" x2="{cx}" y2="{EY+8}" stroke="#555" stroke-width="1.5" stroke-dasharray="5 4"/>')
b.append(arc(cx, EY, 44, -90, -90 + ang))
b.append(text(cx + 26, EY - 46, "25–30°", 14, DRED, True))
b.append(text(cx, EY + 22, "fio", 11, "#555", False, "middle"))
b.append(lines(cx, 280, ["25–30° de cada lado", "(50–60° no total)"], 12, "#222", False, "middle"))
b.append(text(cx, 308, "fio mais grosso aguenta pancada", 11, "#555", False, "middle"))
# --- enxada (chanfro de um lado so)
x0 = 455; cx = x0 + 105; ang = 35; T = 34
rise = T / math.tan(math.radians(ang))
b.append(painel(x0, "ENXADA e PÁ"))
xl, xr = cx - T / 2, cx + T / 2
b.append(f'<polygon points="{xl},104 {xr},104 {xr},{EY-rise:.1f} {xl},{EY}" fill="{STEEL}" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<line x1="{xl}" y1="140" x2="{xl}" y2="{EY+8}" stroke="#555" stroke-width="1.5" stroke-dasharray="5 4"/>')
b.append(arc(xl, EY, 52, -90, -90 + ang))
b.append(text(xr + 6, EY - 22, "30–40°", 14, DRED, True))
b.append(lines(xl - 8, 150, ["lado", "liso"], 11, "#555", False, "end"))
b.append(lines(xr + 8, 118, ["chanfro", "(lado", "de dentro,", "do cabo)"], 11, "#555"))
b.append(text(xl, EY + 22, "fio", 11, "#555", False, "middle"))
b.append(lines(cx, 280, ["30–40° num lado só", "(siga o chanfro de fábrica)"], 12, "#222", False, "middle"))
b.append(text(cx, 308, "lime só o chanfro", 11, "#555", False, "middle"))

# --- como segurar na pedra
b.append(text(20, 344, "Como segurar a faca na pedra (visto pela ponta da faca)", 14, "#222", True))
SY = 440  # topo da pedra
b.append(f'<rect x="30" y="{SY}" width="370" height="38" rx="4" fill="{STONE}" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<rect x="30" y="{SY}" width="370" height="8" fill="#a8a8a8"/>')
b.append(text(215, SY + 28, "pedra molhada (água ou óleo)", 12, "#fff", True, "middle"))
ex, ey = 150, SY  # fio encostado
W = 150; ang = 20
sx, sy = ex + W * math.cos(math.radians(ang)), ey - W * math.sin(math.radians(ang))
nx, ny = -math.sin(math.radians(ang)) * 6, -math.cos(math.radians(ang)) * 6
b.append(f'<polygon points="{ex},{ey} {sx+nx:.1f},{sy+ny:.1f} {sx-nx*0.2:.1f},{sy-ny*0.2:.1f}" fill="{STEEL}" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<line x1="{ex}" y1="{ey}" x2="{ex+170}" y2="{ey}" stroke="#555" stroke-width="1.5" stroke-dasharray="5 4"/>')
b.append(arc(ex, ey, 78, -ang, 0))
b.append(text(ex + 86, ey - 8, "20°", 14, DRED, True))
# altura do dorso
b.append(f'<line x1="{sx+14:.1f}" y1="{sy:.1f}" x2="{sx+14:.1f}" y2="{ey}" stroke="{GREEN}" stroke-width="2"/>')
b.append(f'<line x1="{sx+8:.1f}" y1="{sy:.1f}" x2="{sx+20:.1f}" y2="{sy:.1f}" stroke="{GREEN}" stroke-width="2"/>')
b.append(lines(sx + 24, sy + 8, ["dorso levantado", "≈ 1/3 da largura", "da lâmina"], 11.5, "#1d6b2c", True))
b.append(lines(40, 372, ["fio", "encostado"], 11.5, "#555"))
b.append(f'<line x1="70" y1="392" x2="{ex-4}" y2="{ey-4}" stroke="#555" stroke-width="1.5"/>')
b.append(arrow(150, 500, 60, 500, "#555", 3))
b.append(lines(160, 498, ["empurre o fio, como quem tira", "uma fatia fina da pedra"], 11.5, "#333"))

# --- truque do angulo
b.append(box(425, 356, 240, 156, "#eef5ff", "#3f6d9e"))
b.append(text(545, 376, "Truque para achar 20°", 12.5, "#1e3f66", True, "middle"))
for i, (a, lab) in enumerate([(90, "90°"), (45, "metade: 45°"), (22, "metade: ~22°")]):
    bx = 445 + i * 76; by = 452
    b.append(f'<line x1="{bx-6}" y1="{by}" x2="{bx+64}" y2="{by}" stroke="#555" stroke-width="5"/>')
    tx, ty = bx + 50 * math.cos(math.radians(a)), by - 50 * math.sin(math.radians(a))
    b.append(f'<line x1="{bx}" y1="{by}" x2="{tx:.1f}" y2="{ty:.1f}" stroke="#1e1e1e" stroke-width="4" stroke-linecap="round"/>')
    b.append(text(bx + 28, by + 22, lab, 10.5, "#222", False, "middle"))
b.append(text(545, 498, "baixe só mais um pouquinho = 20°", 11.5, "#1e3f66", True, "middle"))
# --- caixa de passos
b.append(box(15, 524, 650, 76))
b.append(lines(28, 545, [
    "1. Lado GROSSO da pedra até sentir rebarba (fio de arame) em TODO o comprimento, do lado oposto.",
    "2. Vire e repita do outro lado. 3. Lado FINO, mesmo ângulo, passadas leves e alternadas.",
    "4. Tire a rebarba com 3–5 passadas bem leves de cada lado. Mantenha SEMPRE o mesmo ângulo."], 12, "#222", False, "start", 18))
open(D + "afiacao-angulos.svg", "w").write(svg(680, 610, "Afiação: ângulos e como segurar na pedra", "\n".join(b)))

# =====================================================================
# 2) CHUPETA
# =====================================================================
b = []


def bateria(x, y, rotulo, sub, pos_mais_dir):
    s = f'<rect x="{x}" y="{y}" width="200" height="104" rx="6" fill="#4d4d4d" stroke="#1e1e1e" stroke-width="2.5"/>'
    s += f'<rect x="{x}" y="{y}" width="200" height="16" rx="4" fill="#666" stroke="#1e1e1e" stroke-width="2"/>'
    s += text(x + 100, y + 58, rotulo, 15, "#fff", True, "middle")
    s += text(x + 100, y + 80, sub, 11.5, "#ddd", False, "middle")
    xm = x + 160 if pos_mais_dir else x + 40
    xn = x + 40 if pos_mais_dir else x + 160
    s += f'<rect x="{xm-12}" y="{y-14}" width="24" height="16" fill="#d62828" stroke="#1e1e1e" stroke-width="2"/>'
    s += f'<rect x="{xn-12}" y="{y-14}" width="24" height="16" fill="#9a9a9a" stroke="#1e1e1e" stroke-width="2"/>'
    s += text(xm, y + 34, "+", 22, "#ff8a8a", True, "middle")
    s += text(xn, y + 34, "−", 22, "#ddd", True, "middle")
    return s, xm, xn


def garra(x, y, cor):
    return (f'<rect x="{x-9}" y="{y-12}" width="18" height="20" rx="3" fill="{cor}" stroke="#1e1e1e" stroke-width="2"/>'
            f'<line x1="{x-5}" y1="{y+8}" x2="{x-5}" y2="{y+14}" stroke="#1e1e1e" stroke-width="3"/>'
            f'<line x1="{x+5}" y1="{y+8}" x2="{x+5}" y2="{y+14}" stroke="#1e1e1e" stroke-width="3"/>')


BY = 130
s1, m1, n1 = bateria(30, BY, "DESCARREGADA", "no carro PARADO", True)
s2, m2, n2 = bateria(450, BY, "BOA", "no carro que vai ajudar", False)
b += [s1, s2]
# motor do carro parado (massa)
b.append(f'<rect x="30" y="300" width="230" height="74" rx="8" fill="#a0a0a0" stroke="#1e1e1e" stroke-width="2.5"/>')
for i in range(4):
    b.append(f'<rect x="{48+i*40}" y="286" width="26" height="16" rx="3" fill="#8a8a8a" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append(text(128, 330, "MOTOR do carro parado", 13, "#1e1e1e", True, "middle"))
b.append(text(128, 348, "parafuso ou suporte de metal", 11, "#1e1e1e", False, "middle"))
b.append(text(128, 362, "SEM tinta, longe da bateria", 11, "#1e1e1e", False, "middle"))
b.append(f'<rect x="232" y="318" width="22" height="22" fill="#cfcfcf" stroke="#1e1e1e" stroke-width="2"/>')
# cabo vermelho: + descarregada -> + boa
b.append(f'<path d="M{m1} {BY-26} C {m1+40} 52, {m2-40} 52, {m2} {BY-26}" fill="none" stroke="#1e1e1e" stroke-width="11" stroke-linecap="round"/>')
b.append(f'<path d="M{m1} {BY-26} C {m1+40} 52, {m2-40} 52, {m2} {BY-26}" fill="none" stroke="{RED}" stroke-width="7" stroke-linecap="round"/>')
# cabo preto: - boa -> motor
pth = f"M{n2} {BY-26} C {n2+60} 70, 662 250, 560 300 C 470 334, 360 330, 262 330"
b.append(f'<path d="{pth}" fill="none" stroke="#777" stroke-width="11" stroke-linecap="round"/>')
b.append(f'<path d="{pth}" fill="none" stroke="#1e1e1e" stroke-width="7" stroke-linecap="round"/>')
b.append(garra(m1, BY - 20, RED)); b.append(garra(m2, BY - 20, RED))
b.append(garra(n2, BY - 20, "#333"))
b.append(f'<rect x="254" y="320" width="20" height="18" rx="3" fill="#333" stroke="#1e1e1e" stroke-width="2"/>')
b.append(badge(m1 - 30, BY - 34, 1)); b.append(badge(m2 + 30, BY - 34, 2))
b.append(badge(n2 - 32, BY - 34, 3, "#1e1e1e")); b.append(badge(284, 308, 4, "#1e1e1e"))
b.append(text(340, 108, "cabo VERMELHO", 12.5, DRED, True, "middle"))
b.append(text(450, 296, "cabo PRETO", 12.5, "#1e1e1e", True, "middle"))
# passos
b.append(box(15, 392, 650, 168, "#fff4e5", "#ef8a2b"))
P = [("1", RED, "VERMELHO no + da bateria DESCARREGADA."),
     ("2", RED, "Outra ponta do vermelho no + da bateria BOA."),
     ("3", "#1e1e1e", "PRETO no − da bateria BOA."),
     ("4", "#1e1e1e", "Outra ponta do preto em METAL SEM TINTA do motor do carro parado")]
for i, (n, c, t) in enumerate(P):
    y = 414 + i * 25
    b.append(badge(36, y - 4, n, c, 10).replace('font-size="16"', 'font-size="12"').replace(f'y="{y-4+5.5}"', f'y="{y-4+4.5}"'))
    b.append(text(54, y + 1, t, 12.5, "#222", i in (0, 1, 2, 3)))
b.append(text(54, 514 - 6, "(não no − da fraca: a faísca pode explodir o gás que sai da bateria).", 11.5, "#555"))
b.append(text(28, 530, "Ligue o carro bom, espere 3–5 min, dê partida no parado (máx. 10 s, 1 min entre tentativas).", 12, "#222"))
b.append(text(28, 550, "Para TIRAR: ordem inversa  4 → 3 → 2 → 1.  Nunca deixe as garras se encostarem.", 12.5, DRED, True))
b.append(text(340, 580, "Bateria estufada, rachada, vazando ou congelada: NÃO faça chupeta. Use óculos.", 12.5, DRED, True, "middle"))
open(D + "chupeta.svg", "w").write(svg(680, 594, "Chupeta: ordem certa dos cabos", "\n".join(b)))

# =====================================================================
# 3) CARRO NAO PEGA - FLUXOGRAMA
# =====================================================================
b = []


def node(x, y, w, ls, kind="q", size=12):
    lh = size * 1.3
    h = len(ls) * lh + 14
    fill, st = {"q": ("#eef5ff", "#3f6d9e"), "a": ("#fff4e5", "#ef8a2b"), "r": ("#fdecec", "#d62828"), "g": ("#eaf6ec", "#2b8a3e")}[kind]
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h:.0f}" rx="9" fill="{fill}" stroke="{st}" stroke-width="2"/>'
    s += lines(x + w / 2, y + 7 + size, ls, size, "#1e1e1e", kind == "q", "middle", lh)
    return s, y + h


def tag(x, y, s, c="#333"):
    return text(x, y, s, 11.5, c, True, "middle")


s, yb = node(170, 46, 340, ["Gire a chave para dar partida.", "O motor de arranque gira o motor?"], "q", 13)
b.append(s)
# tres ramos
cols = [(12, 200), (226, 186), (426, 242)]
yr = 132
labels = ["NÃO gira (silêncio", "Gira DEVAGAR", "Gira NORMAL"]
labels2 = ["ou só um \"clique\")", "(rrrr... rrrr...)", "mas não pega"]
for (x, w), l1, l2 in zip(cols, labels, labels2):
    cx = x + w / 2
    b.append(f'<path d="M340 {yb:.0f} L340 {yb+12:.0f} L{cx} {yb+12:.0f} L{cx} {yr-4}" fill="none" stroke="#555" stroke-width="2.5"/>')
    b.append(f'<polygon points="{cx-6},{yr-10} {cx+6},{yr-10} {cx},{yr}" fill="#555"/>')
    s, _ = node(x, yr, w, [l1, l2], "q" if cx < 300 or cx > 500 else "q")
    b.append(s.replace("#eef5ff", "#f2f2f2").replace("#3f6d9e", "#777"))
yA = yr + 52
# coluna A
x, w = cols[0]; cx = x + w / 2
b.append(arrow(cx, yA, cx, yA + 18, "#555", 2.5))
s, y2 = node(x, yA + 22, w, ["Acenda o farol.", "A luz fica forte?"], "q"); b.append(s)
b.append(f'<line x1="{x+50}" y1="{y2}" x2="{x+50}" y2="{y2+24}" stroke="#555" stroke-width="2.5"/>')
b.append(f'<line x1="{x+150}" y1="{y2}" x2="{x+150}" y2="{y2+24}" stroke="#555" stroke-width="2.5"/>')
b.append(tag(x + 22, y2 + 16, "fraca", DRED)); b.append(tag(x + 176, y2 + 16, "forte", GREEN))
s, y3 = node(x, y2 + 26, 98, ["BATERIA", "fraca ou", "terminal", "solto/sujo:", "limpe,", "aperte,", "chupeta"], "a", 11.5); b.append(s)
s, y3b = node(x + 102, y2 + 26, 98, ["MOTOR DE", "ARRANQUE,", "relé ou cabo", "de massa:", "bata de leve", "nele com o", "cabo do", "martelo"], "a", 11.5); b.append(s)
s, _ = node(x, max(y3, y3b) + 8, w, ["Carro manual: tente", "pegar no TRANCO"], "g", 11.5); b.append(s)
# coluna B
x, w = cols[1]; cx = x + w / 2
b.append(arrow(cx, yA, cx, yA + 18, "#555", 2.5))
s, _ = node(x, yA + 22, w, ["Bateria fraca ou", "terminal com zinabre", "(pó branco/verde):", "limpe com água e", "bicarbonato, aperte,", "faça chupeta.", "", "No frio, óleo grosso", "e gasolina velha", "pioram a partida."], "a"); b.append(s)
# coluna C
x, w = cols[2]; cx = x + w / 2
b.append(arrow(cx, yA, cx, yA + 18, "#555", 2.5))
s, y2 = node(x, yA + 22, w, ["Tem COMBUSTÍVEL?", "(marcador; cheiro de gasolina no", "escapamento; a bomba zumbe 2 s", "ao ligar a chave)"], "q"); b.append(s)
b.append(f'<line x1="{x+40}" y1="{y2}" x2="{x+40}" y2="{y2+22}" stroke="#555" stroke-width="2.5"/>')
b.append(f'<line x1="{x+175}" y1="{y2}" x2="{x+175}" y2="{y2+22}" stroke="#555" stroke-width="2.5"/>')
b.append(tag(x + 16, y2 + 15, "não", DRED)); b.append(tag(x + 200, y2 + 15, "sim", GREEN))
s, y3 = node(x, y2 + 24, 92, ["Abasteça.", "Fusível e", "relé da", "bomba.", "Filtro.", "Água no", "tanque?"], "a", 11.5); b.append(s)
s, y4 = node(x + 98, y2 + 24, 144, ["Tem FAÍSCA?", "(teste da vela", "encostada no", "metal do motor)"], "q", 11.5); b.append(s)
yy = max(y3 + 16, y4 + 22)
b.append(f'<path d="M{x+130} {y4} L{x+130} {yy-4} L{x+58} {yy-4} L{x+58} {yy+1}" fill="none" stroke="#555" stroke-width="2.5"/>')
b.append(f'<polygon points="{x+52},{yy} {x+64},{yy} {x+58},{yy+7}" fill="#555"/>')
b.append(f'<line x1="{x+200}" y1="{y4}" x2="{x+200}" y2="{yy+1}" stroke="#555" stroke-width="2.5"/>')
b.append(f'<polygon points="{x+194},{yy} {x+206},{yy} {x+200},{yy+7}" fill="#555"/>')
b.append(tag(x + 146, y4 + 14, "não", DRED)); b.append(tag(x + 218, y4 + 14, "sim", GREEN))
s, y5 = node(x, yy + 8, 116, ["SEM FAÍSCA:", "bobina, cabos", "de vela, vela,", "platinado,", "sensor de", "rotação,", "fusível"], "a", 11.5); b.append(s)
s, y6 = node(x + 122, yy + 8, 120, ["COM FAÍSCA:", "afogado? (pise", "o acelerador", "todo e dê", "partida 5 s)", "alarme ou", "imobilizador?"], "a", 11.5); b.append(s)
yb2 = max(y5, y6, 520)
b.append(box(12, yb2 + 10, 656, 74, "#f7f7f7", "#999"))
b.append(lines(24, yb2 + 30, [
    "Flex com álcool no frio: encha o tanquinho de partida (gasolina). Diesel: troque o filtro e sangre o ar.",
    "Teste de faísca: segure o cabo com alicate de cabo isolado, a rosca da vela encostada no motor.",
    "Faísca AZUL e forte = boa; amarela, fraca ou nenhuma = problema na ignição."], 11.5, "#222", False, "start", 18))
H = yb2 + 96
open(D + "carro-nao-pega.svg", "w").write(svg(680, H, "Carro não pega: o que verificar", "\n".join(b)))
print("ok gen_mecanica1")
