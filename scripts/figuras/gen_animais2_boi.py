import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
# Figuras com bovino em vista lateral ESQUERDA (cabeça para a esquerda):
# cortes de carne, fita de peso, timpanismo (trocater) e locais de injeção.
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "05-animais", "img") + "/"
os.makedirs(D, exist_ok=True)
HIDE = "#d9c2a3"   # pelagem clara
HIDE2 = "#b89d7c"  # patas do lado oposto
RED = "#d62828"; DRED = "#b3001b"; GREEN = "#2b8a3e"

# contorno do corpo em coordenadas locais (0..520 x 0..340), cabeça à esquerda
BODY = ("M95,70 C80,66 62,74 50,86 C36,100 24,124 16,148 C12,160 12,170 22,180 "
        "C34,186 58,182 78,166 C88,162 96,164 102,176 C110,196 126,214 146,226 "
        "C154,232 158,236 160,240 C164,262 166,284 166,300 L168,368 C168,374 166,378 164,382 "
        "L196,382 C196,376 196,372 196,368 L198,300 C200,280 202,262 206,242 "
        "C240,248 300,250 340,246 C366,243 382,236 392,226 "
        "C400,246 408,262 414,282 C418,292 418,300 416,310 L414,368 C414,374 412,378 410,382 "
        "L442,382 C442,376 442,372 442,368 L444,322 C446,312 450,304 454,298 "
        "C460,272 468,248 472,228 C482,190 490,140 486,84 C484,76 482,72 478,68 "
        "C462,58 446,56 430,56 C390,56 350,54 300,52 C260,50 236,48 214,44 "
        "C196,34 180,30 166,34 C150,40 136,52 120,60 C110,64 102,68 95,70 Z")

def cow(tx, ty, s=1.0, cid="c", fill=HIDE, eye=True):
    """Desenha o boi; devolve o SVG. (tx,ty) = canto superior esquerdo; s = escala."""
    g = [f'<g transform="translate({tx},{ty}) scale({s})">']
    # patas do lado de lá (mais escuras)
    g.append(f'<path d="M206,240 L212,300 L214,368 C214,374 212,378 210,382 L240,382 L240,368 L238,300 L236,246 Z" fill="{HIDE2}" stroke="{OUT}" stroke-width="2"/>')
    g.append(f'<path d="M420,240 C428,262 432,282 434,300 L432,368 C432,374 430,378 428,382 L458,382 L458,368 L460,322 C462,312 466,304 468,296 L470,250 Z" fill="{HIDE2}" stroke="{OUT}" stroke-width="2"/>')
    # rabo
    g.append(f'<path d="M482,74 C496,100 500,160 498,232" fill="none" stroke="{OUT}" stroke-width="5" stroke-linecap="round"/>')
    g.append(f'<path d="M498,226 C490,240 492,262 500,272 C508,262 508,240 498,226 Z" fill="#6b5236" stroke="{OUT}" stroke-width="2"/>')
    # corpo
    g.append(f'<path d="{BODY}" fill="{fill}" stroke="{OUT}" stroke-width="2.5" stroke-linejoin="round"/>')
    # chifre e orelha
    g.append(f'<path d="M92,68 C90,56 92,46 100,38 C100,48 102,58 104,66 Z" fill="#efe6d2" stroke="{OUT}" stroke-width="2"/>')
    g.append(f'<path d="M104,74 C120,70 136,74 146,84 C132,90 116,88 104,82 Z" fill="{fill}" stroke="{OUT}" stroke-width="2"/>')
    if eye:
        g.append(f'<path d="M24,140 C16,150 14,166 22,178 C34,184 50,182 60,174 C50,160 38,146 24,140 Z" fill="#c9a98a" stroke="none"/>')
        g.append(f'<ellipse cx="68" cy="100" rx="6" ry="4.5" fill="{OUT}"/>')
        g.append(f'<ellipse cx="22" cy="156" rx="3.5" ry="5" fill="{OUT}"/>')
        g.append(f'<path d="M20,172 C30,176 44,176 52,172" fill="none" stroke="{OUT}" stroke-width="1.8"/>')
    # cascos
    for x1, x2 in ((164, 196), (410, 442)):
        g.append(f'<rect x="{x1}" y="374" width="{x2-x1}" height="8" fill="#3a2e22"/>')
    g.append('</g>')
    return "".join(g)

def P(tx, ty, s, x, y):
    """converte ponto local do boi para coordenada da figura"""
    return tx + x * s, ty + y * s

def cleanup(path):
    return path

# ====================== 1) CORTES BOVINOS ======================
def cortes():
    tx, ty, s = 40, 50, 1.12
    b = []
    b.append(f'<defs><clipPath id="corpo"><path d="{BODY}"/></clipPath></defs>')
    b.append(cow(tx, ty, s, fill="#f4ead9", eye=False))
    MAC = "#8fd19e"; MED = "#ffe08a"; DUR = "#f6b38e"; CAB = "#eeeeee"
    # regiões em ordem de desenho (as de depois ficam por cima); recortadas pelo contorno
    reg = [
        ("0,0 103,0 104,62 100,178 60,400 0,400", CAB, 0, None),                         # cabeça
        ("103,0 150,0 150,200 110,200 100,178 104,62", DUR, 1, (128, 130)),              # pescoço
        ("100,178 110,200 252,200 252,400 100,400", DUR, 5, (230, 222)),                 # peito
        ("150,246 215,246 215,400 150,400", DUR, 16, (183, 318)),                        # músculo dianteiro
        ("150,0 236,0 236,45 150,50", MED, 3, (190, 42)),                                # cupim
        ("150,50 236,45 236,0 252,0 252,128 150,128", DUR, 2, (204, 92)),                # acém
        ("150,128 252,128 252,200 150,200", MED, 4, (204, 166)),                         # paleta
        ("252,0 352,0 352,128 252,128", MAC, 8, (302, 90)),                              # contrafilé
        ("252,128 352,128 352,210 252,210", DUR, 6, (302, 170)),                         # costela
        ("252,210 352,210 352,400 252,400", DUR, 7, (302, 229)),                         # ponta de agulha
        ("352,0 425,0 425,140 352,140", MAC, 9, (388, 98)),                              # alcatra
        ("352,140 425,140 425,198 352,198", MAC, 11, (388, 170)),                        # maminha
        ("352,198 425,198 405,400 352,400", MED, 12, (374, 222)),                        # fraldinha
        ("425,0 520,0 520,100 425,100", MAC, 10, (452, 78)),                             # picanha
        ("425,100 520,100 520,200 425,200", MED, 13, (456, 152)),                        # coxão duro/mole
        ("398,200 440,200 436,300 400,300", MED, 14, (418, 252)),                        # patinho
        ("440,200 520,200 470,300 436,300", MED, 15, (453, 252)),                        # lagarto
        ("380,300 520,300 520,400 380,400", DUR, 16, (428, 340)),                        # músculo traseiro
    ]
    g = [f'<g transform="translate({tx},{ty}) scale({s})" clip-path="url(#corpo)">']
    for pts, cor, n, _ in reg:
        g.append(f'<polygon points="{pts}" fill="{cor}" stroke="{OUT}" stroke-width="1.6"/>')
    g.append('</g>')
    b.append("".join(g))
    # contorno, olho, chifre e orelha por cima
    b.append(f'<g transform="translate({tx},{ty}) scale({s})"><path d="{BODY}" fill="none" stroke="{OUT}" stroke-width="2.5"/>'
             f'<ellipse cx="68" cy="100" rx="6" ry="4.5" fill="{OUT}"/><ellipse cx="22" cy="156" rx="3.5" ry="5" fill="{OUT}"/>'
             f'<path d="M104,74 C120,70 136,74 146,84 C132,90 116,88 104,82 Z" fill="{CAB}" stroke="{OUT}" stroke-width="2"/></g>')
    X, Y = P(tx, ty, s, 64, 128)
    b.append(text(round(X), round(Y), "cabeça", 12, "#555", True, "middle"))
    X, Y = P(tx, ty, s, 64, 143)
    b.append(text(round(X), round(Y), "(língua,", 11, "#555", False, "middle"))
    X, Y = P(tx, ty, s, 64, 155)
    b.append(text(round(X), round(Y), "bochecha)", 11, "#555", False, "middle"))
    for _, _, n, pos in reg:
        if not pos:
            continue
        X, Y = P(tx, ty, s, *pos)
        b.append(f'<circle cx="{X:.0f}" cy="{Y:.0f}" r="11" fill="#fff" stroke="{OUT}" stroke-width="1.5"/>')
        b.append(text(round(X), round(Y + 4.5), str(n), 12.5, "#111", True, "middle"))
    # filé mignon (por dentro)
    X1, Y1 = P(tx, ty, s, 318, 116); X2, Y2 = P(tx, ty, s, 408, 116)
    b.append(f'<line x1="{X1:.0f}" y1="{Y1:.0f}" x2="{X2:.0f}" y2="{Y2:.0f}" stroke="#7a1f1f" stroke-width="5" stroke-dasharray="8 5"/>')
    b.append(text(420, 58, "- - - filé mignon: fica por DENTRO,", 11.5, "#7a1f1f", True))
    b.append(text(420, 73, "embaixo do contrafilé e da alcatra", 11.5, "#7a1f1f", True))
    # legenda
    y0 = 500
    leg = [
        (1, "Pescoço", DUR), (2, "Acém", DUR), (3, "Cupim (boi zebu)", MED), (4, "Paleta", MED),
        (5, "Peito", DUR), (6, "Costela", DUR), (7, "Ponta de agulha", DUR), (8, "Contrafilé", MAC),
        (9, "Alcatra (miolo)", MAC), (10, "Picanha", MAC), (11, "Maminha", MAC), (12, "Fraldinha", MED),
        (13, "Coxão duro e mole", MED), (14, "Patinho", MED), (15, "Lagarto", MED), (16, "Músculo (canela)", DUR),
    ]
    for i, (n, nome, cor) in enumerate(leg):
        col, row = i // 6, i % 6
        x = 24 + col * 220; y = y0 + row * 24
        b.append(f'<rect x="{x}" y="{y-14}" width="26" height="19" rx="4" fill="{cor}" stroke="{OUT}" stroke-width="1.2"/>')
        b.append(text(x + 13, y, str(n), 12, "#111", True, "middle"))
        b.append(text(x + 34, y, nome, 12.5))
    x = 24 + 2 * 220; y = y0 + 4 * 24
    b.append(f'<line x1="{x}" y1="{y-5}" x2="{x+26}" y2="{y-5}" stroke="#7a1f1f" stroke-width="5" stroke-dasharray="7 4"/>')
    b.append(text(x + 34, y, "Filé mignon", 12.5))
    yb = y0 + 6 * 24 + 2
    b.append(box(20, yb, 640, 74, "#f7f7f7", "#999"))
    b.append(f'<rect x="34" y="{yb+12}" width="20" height="14" fill="{MAC}" stroke="{OUT}"/>')
    b.append(text(62, yb + 24, "MACIOS: grelhar, assar, bife, churrasco (fogo forte e rápido)", 12.5))
    b.append(f'<rect x="34" y="{yb+32}" width="20" height="14" fill="{MED}" stroke="{OUT}"/>')
    b.append(text(62, yb + 44, "MÉDIOS: bife fino, assado de panela, carne de sol, picadinho", 12.5))
    b.append(f'<rect x="34" y="{yb+52}" width="20" height="14" fill="{DUR}" stroke="{OUT}"/>')
    b.append(text(62, yb + 64, "DE PANELA: cozido longo, ensopado, carne moída, caldo, charque", 12.5))
    H = yb + 86
    return svg(680, H, "Cortes do boi (lado esquerdo, cabeça à esquerda)", "\n".join(b))

open(D + "abate-cortes-bovino.svg", "w").write(cortes())

# ====================== 2) FITA DE PESO ======================
def fita():
    tx, ty, s = 14, 64, 0.82
    b = [cow(tx, ty, s)]
    # fita: anel logo atrás das patas dianteiras (x local ~ 214)
    xa, ya = P(tx, ty, s, 214, 44); xb, yb_ = P(tx, ty, s, 214, 246)
    b.append(f'<ellipse cx="{xa:.0f}" cy="{(ya+yb_)/2:.0f}" rx="15" ry="{(yb_-ya)/2:.0f}" fill="none" stroke="{RED}" stroke-width="7" stroke-opacity="0.35"/>')
    b.append(f'<path d="M{xa:.0f},{ya:.0f} C{xa+20:.0f},{ya+50:.0f} {xa+20:.0f},{yb_-50:.0f} {xb:.0f},{yb_:.0f}" fill="none" stroke="{RED}" stroke-width="7"/>')
    b.append(text(xa + 6, ya - 26, "A = perímetro torácico", 13, DRED, True, "middle"))
    b.append(text(xa + 6, ya - 11, "(fita justa, logo atrás das patas da frente)", 11.5, DRED, False, "middle"))
    # comprimento: ponta da paleta -> ponta da nádega
    x1, y1 = P(tx, ty, s, 150, 200); x2, y2 = P(tx, ty, s, 484, 112)
    b.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#1f5fa8" stroke-width="3" stroke-dasharray="9 5"/>')
    b.append(f'<circle cx="{x1:.0f}" cy="{y1:.0f}" r="6" fill="#1f5fa8"/><circle cx="{x2:.0f}" cy="{y2:.0f}" r="6" fill="#1f5fa8"/>')
    b.append(text(x1 - 10, y1 + 22, "ponta da paleta", 11.5, "#1f5fa8", True, "middle"))
    b.append(text(x2 - 30, y2 - 26, "ponta da", 11.5, "#1f5fa8", True, "middle"))
    b.append(text(x2 - 30, y2 - 12, "nádega", 11.5, "#1f5fa8", True, "middle"))
    b.append(text(236, 232, "B = comprimento", 13, "#1f5fa8", True))
    # tabela
    tbx, tby = 470, 70
    b.append(box(tbx - 8, tby - 18, 206, 330, "#fff", "#888"))
    b.append(text(tbx + 95, tby, "Bovino: só a fita (A)", 12.5, "#222", True, "middle"))
    b.append(text(tbx + 30, tby + 22, "A (cm)", 12, "#555", True, "middle"))
    b.append(text(tbx + 132, tby + 22, "peso aprox. (kg)", 12, "#555", True, "middle"))
    rows = [(100, 70), (110, 95), (120, 120), (130, 155), (140, 190), (150, 235), (160, 285),
            (170, 345), (180, 410), (190, 480), (200, 560), (210, 650)]
    for i, (a, p) in enumerate(rows):
        y = tby + 44 + i * 22
        if i % 2 == 0:
            b.append(f'<rect x="{tbx-4}" y="{y-15}" width="198" height="21" fill="#f1f1f1"/>')
        b.append(text(tbx + 30, y, str(a), 13, "#222", True, "middle"))
        b.append(text(tbx + 132, y, f"{p}", 13, "#222", False, "middle"))
    # fórmulas
    fy = 400
    b.append(box(16, fy, 440, 150, "#eef5ff", "#3f6d9e"))
    b += [text(28, fy + 22, "Mais preciso (fita A e comprimento B, em cm):", 12.5, "#222", True),
          text(28, fy + 46, "Bovino:   peso (kg) = A × A × B ÷ 10.840", 13, "#1e1e1e", True),
          text(28, fy + 68, "Cavalo:   peso (kg) = A × A × B ÷ 11.880", 13, "#1e1e1e", True),
          text(28, fy + 90, "Porco:     peso (kg) = A × A × B ÷ 14.400", 13, "#1e1e1e", True),
          text(28, fy + 108, "(no porco, B vai do meio das orelhas até a raiz do rabo)", 11.5, "#444"),
          text(28, fy + 132, "Ex.: A = 190, B = 150 → 190×190×150 ÷ 10.840 = 500 kg", 12, "#2b6a1e", True)]
    b.append(box(466, fy, 198, 150, "#f7f7f7", "#999"))
    b += [text(478, fy + 22, "Sem fita métrica:", 12.5, "#222", True),
          text(478, fy + 42, "dê a volta com um", 12),
          text(478, fy + 58, "barbante, marque com", 12),
          text(478, fy + 74, "um nó e meça depois", 12),
          text(478, fy + 90, "numa trena ou régua.", 12),
          text(478, fy + 114, "Cabra, ovelha, cão:", 12.5, "#222", True),
          text(478, fy + 130, "suba na balança com", 12),
          text(478, fy + 146, "ele no colo e desconte.", 12)]
    b.append(box(16, fy + 160, 648, 50, "#fff4e5", "#ef8a2b"))
    b += [text(28, fy + 180, "Animal em pé, parado, cabeça na altura normal. Meça 2 vezes e use a média.", 12.5),
          text(28, fy + 198, "Erro de ±10% (gordo, magro e prenhe variam). Serve para dose de remédio e ganho de peso.", 12.5)]
    return svg(680, fy + 220, "Estimar o peso com fita (sem balança)", "\n".join(b))

open(D + "vet-fita-peso.svg", "w").write(fita())

# ====================== 3) TIMPANISMO / TROCATER ======================
def timpanismo():
    tx, ty, s = 10, 70, 0.84
    b = [cow(tx, ty, s, fill="#dcc6a6")]
    loc = lambda x, y: P(tx, ty, s, x, y)
    # rúmen (recortado pelo contorno), última costela, fossa e ponta do quadril
    b.append(f'<defs><clipPath id="corpoT"><path d="{BODY}"/></clipPath></defs>')
    b.append(f'<g transform="translate({tx},{ty}) scale({s})">'
             f'<path clip-path="url(#corpoT)" d="M236,72 C280,62 380,60 430,70 C412,130 400,190 360,236 C300,252 250,246 226,238 C214,170 216,112 236,72 Z" fill="#a8d5f0" fill-opacity="0.55" stroke="#1f5fa8" stroke-width="2.5" stroke-dasharray="8 5"/>'
             f'<path d="M352,62 C346,110 338,160 326,214" fill="none" stroke="#6b4f2a" stroke-width="3" stroke-dasharray="6 4"/>'
             f'<path d="M356,74 L428,74 L368,150 Z" fill="#ffd2d2" fill-opacity="0.85" stroke="{RED}" stroke-width="2"/>'
             f'<circle cx="434" cy="66" r="6" fill="#6b4f2a"/></g>')
    Xx, Xy = loc(388, 98)
    b.append(f'<line x1="{Xx-9:.0f}" y1="{Xy-9:.0f}" x2="{Xx+9:.0f}" y2="{Xy+9:.0f}" stroke="{DRED}" stroke-width="5"/>'
             f'<line x1="{Xx-9:.0f}" y1="{Xy+9:.0f}" x2="{Xx+9:.0f}" y2="{Xy-9:.0f}" stroke="{DRED}" stroke-width="5"/>')
    lx, ly = loc(282, 150)
    b.append(text(lx, ly, "rúmen (pança)", 12.5, "#1f5fa8", True, "middle"))
    b.append(text(lx, ly + 15, "cheio de gás", 12.5, "#1f5fa8", True, "middle"))
    rx, ry = loc(326, 214)
    b.append(f'<line x1="{rx:.0f}" y1="{ry:.0f}" x2="{rx-20:.0f}" y2="{ry+60:.0f}" stroke="#6b4f2a" stroke-width="1.5"/>')
    b.append(text(rx - 20, ry + 74, "última costela", 11.5, "#6b4f2a", True, "middle"))
    hx, hy = loc(434, 66)
    b.append(f'<line x1="{hx:.0f}" y1="{hy:.0f}" x2="{hx+40:.0f}" y2="{hy-26:.0f}" stroke="#6b4f2a" stroke-width="1.5"/>')
    b.append(text(hx + 44, hy - 30, "ponta do quadril", 11.5, "#6b4f2a", True))
    b.append(f'<line x1="{Xx+8:.0f}" y1="{Xy-10:.0f}" x2="{Xx+40:.0f}" y2="{Xy-72:.0f}" stroke="{DRED}" stroke-width="1.5"/>')
    b.append(text(Xx + 14, Xy - 92, "X = vão do flanco ESQUERDO", 12.5, DRED, True))
    b.append(text(Xx + 14, Xy - 77, "(atrás da última costela)", 11.5, DRED))
    b.append(text(14, 60, "Lado ESQUERDO do boi", 12.5, "#222", True))
    b.append(text(14, 76, "(cabeça à esquerda)", 11.5, "#444"))
    b.append(box(14, 410, 652, 70, "#ffecec", DRED))
    b.append(text(26, 431, "Onde: no meio entre a última costela e a ponta do quadril, um palmo (10 cm)", 12.5, "#222", True))
    b.append(text(26, 450, "abaixo da linha do lombo, no ponto mais estufado (soa como tambor).", 12.5, "#222", True))
    b.append(text(26, 469, "NUNCA do lado direito (lá ficam intestinos, coagulador e fígado).", 12.5, DRED, True))
    ox, oy = 462, 300
    b.append(text(ox, oy - 18, "Trocater (trocarte):", 12.5, "#222", True))
    b.append(f'<rect x="{ox}" y="{oy}" width="22" height="20" rx="4" fill="#8b5a2b" stroke="{OUT}" stroke-width="2"/>')
    b.append(f'<rect x="{ox+22}" y="{oy+7}" width="140" height="6" fill="#bbb" stroke="{OUT}" stroke-width="1.5"/>')
    b.append(f'<polygon points="{ox+162},{oy+7} {ox+180},{oy+10} {ox+162},{oy+13}" fill="#bbb" stroke="{OUT}" stroke-width="1.5"/>')
    b.append(text(ox, oy + 36, "1. estilete pontudo por dentro", 11.5))
    b.append(f'<rect x="{ox}" y="{oy+48}" width="10" height="20" fill="#ccc" stroke="{OUT}" stroke-width="1.5"/>')
    b.append(f'<rect x="{ox+10}" y="{oy+53}" width="112" height="10" fill="#e6e6e6" stroke="{OUT}" stroke-width="1.5"/>')
    b.append(text(ox, oy + 86, "2. tira o estilete: a cânula", 11.5))
    b.append(text(ox, oy + 100, "(tubo) fica e o gás sai", 11.5))
    # passos
    y = 504
    st = [("1.", "Tire do pasto. Faça andar com as patas da frente mais ALTAS (barranco).", "#222"),
          ("2.", "Pau atravessado na boca, amarrado atrás dos chifres: faz salivar e arrotar.", "#222"),
          ("3.", "Sonda: mangueira lisa de 2 cm pela boca até o rúmen. Saiu gás = resolveu.", "#222"),
          ("", "Se for espuma: 250–500 mL de óleo de cozinha pela sonda (ovelha/cabra: 50–100 mL).", "#222"),
          ("4.", "ÚLTIMO CASO (caindo, língua roxa, sufocando): trocater no X, firme, mirando", DRED),
          ("", "o cotovelo do lado DIREITO. Deixe a cânula; solte o gás aos poucos.", DRED)]
    for n, t, c in st:
        b.append(text(22, y, n, 12.5, c, True))
        b.append(text(44, y, t, 12.5, c, n == "4." or c == DRED))
        y += 20
    return svg(680, y + 6, "Timpanismo (boi estufado): onde furar em último caso", "\n".join(b))

open(D + "vet-timpanismo-trocater.svg", "w").write(timpanismo())
