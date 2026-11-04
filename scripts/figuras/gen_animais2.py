import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
# Figuras de 05-animais (parte 2): abate (insensibilização), queijo, peixes, abelhas.
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "05-animais", "img") + "/"
os.makedirs(D, exist_ok=True)
RED = "#d62828"; DRED = "#b3001b"; GREEN = "#2b8a3e"; WOOD = "#8b5a2b"; SOIL = "#e8d3b0"
WATER = "#4a90d9"; WATERL = "#cfe6fb"

def target(x, y, r=11):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" fill-opacity="0.6" stroke="{RED}" stroke-width="3"/>'
            f'<line x1="{x-r-5}" y1="{y}" x2="{x+r+5}" y2="{y}" stroke="{RED}" stroke-width="2.5"/>'
            f'<line x1="{x}" y1="{y-r-5}" x2="{x}" y2="{y+r+5}" stroke="{RED}" stroke-width="2.5"/>')

def lines(x, y, rows, size=12, color="#222", bold=False, anchor="start", dy=15):
    return "".join(text(x, y + i * dy, r, size, color, bold, anchor) for i, r in enumerate(rows))

# ====================== INSENSIBILIZAÇÃO ======================
def insens():
    b = []
    for k in range(3):
        b.append(f'<rect x="{12+k*222}" y="48" width="212" height="394" rx="10" fill="#fafafa" stroke="#ccc"/>')
    b.append('<g transform="translate(0,26)">')
    # ---- BOVINO de frente ----
    HC = "#c99a6b"
    b.append(f'<path d="M80,104 C70,92 52,80 30,78 C42,86 58,98 72,112 Z" fill="#efe6d2" stroke="{OUT}" stroke-width="2"/>')
    b.append(f'<path d="M146,104 C156,92 174,80 196,78 C184,86 168,98 154,112 Z" fill="#efe6d2" stroke="{OUT}" stroke-width="2"/>')
    b.append(f'<ellipse cx="50" cy="138" rx="24" ry="10" transform="rotate(14 50 138)" fill="{HC}" stroke="{OUT}" stroke-width="2"/>')
    b.append(f'<ellipse cx="176" cy="138" rx="24" ry="10" transform="rotate(-14 176 138)" fill="{HC}" stroke="{OUT}" stroke-width="2"/>')
    b.append(f'<path d="M78,100 C96,94 130,94 148,100 C156,114 160,134 158,154 C154,194 142,228 140,252 '
             f'C142,272 132,288 113,290 C94,288 84,272 86,252 C84,228 72,194 68,154 C66,134 70,114 78,100 Z" fill="{HC}" stroke="{OUT}" stroke-width="2.5"/>')
    b.append(f'<ellipse cx="113" cy="266" rx="27" ry="20" fill="#e3b8a0" stroke="{OUT}" stroke-width="2"/>')
    b.append(f'<ellipse cx="101" cy="268" rx="5" ry="7" fill="{OUT}"/><ellipse cx="125" cy="268" rx="5" ry="7" fill="{OUT}"/>')
    b.append(f'<ellipse cx="82" cy="156" rx="7" ry="5" fill="{OUT}"/><ellipse cx="144" cy="156" rx="7" ry="5" fill="{OUT}"/>')
    b.append(f'<line x1="82" y1="156" x2="148" y2="102" stroke="#1f5fa8" stroke-width="2.5" stroke-dasharray="6 4"/>')
    b.append(f'<line x1="144" y1="156" x2="78" y2="102" stroke="#1f5fa8" stroke-width="2.5" stroke-dasharray="6 4"/>')
    b.append(target(113, 129))
    b.append('</g>')
    b.append(text(117, 72, "BOVINO (de frente)", 14, "#222", True, "middle"))
    b.append(lines(22, 340, ["Cruze duas linhas: de cada", "olho até a base do chifre", "do lado oposto. O alvo é o", "cruzamento, no meio da testa."], 12))
    b.append(lines(22, 406, ["Mire reto, de frente para", "o osso da testa."], 12, DRED, True))
    # ---- SUÍNO de frente ----
    PK = "#f3c1b4"; ox = 222
    b.append('<g transform="translate(0,26)">')
    b.append(f'<polygon points="{ox+68},{112} {ox+44},{66} {ox+98},{96}" fill="{PK}" stroke="{OUT}" stroke-width="2.5"/>')
    b.append(f'<polygon points="{ox+166},{112} {ox+190},{66} {ox+136},{96}" fill="{PK}" stroke="{OUT}" stroke-width="2.5"/>')
    b.append(f'<path d="M{ox+66},110 C{ox+80},92 {ox+154},92 {ox+168},110 C{ox+184},140 {ox+182},196 {ox+160},226 '
             f'C{ox+150},238 {ox+136},242 {ox+117},242 C{ox+98},242 {ox+84},238 {ox+74},226 C{ox+52},196 {ox+50},140 {ox+66},110 Z" fill="{PK}" stroke="{OUT}" stroke-width="2.5"/>')
    b.append(f'<ellipse cx="{ox+117}" cy="240" rx="32" ry="22" fill="#e89a8a" stroke="{OUT}" stroke-width="2.5"/>')
    b.append(f'<ellipse cx="{ox+105}" cy="240" rx="5" ry="8" fill="{OUT}"/><ellipse cx="{ox+129}" cy="240" rx="5" ry="8" fill="{OUT}"/>')
    b.append(f'<ellipse cx="{ox+92}" cy="160" rx="6" ry="4.5" fill="{OUT}"/><ellipse cx="{ox+142}" cy="160" rx="6" ry="4.5" fill="{OUT}"/>')
    b.append(f'<line x1="{ox+74}" y1="160" x2="{ox+160}" y2="160" stroke="#1f5fa8" stroke-width="2.5" stroke-dasharray="6 4"/>')
    b.append(target(ox + 117, 140))
    b.append(f'<line x1="{ox+170}" y1="160" x2="{ox+186}" y2="160" stroke="{OUT}" stroke-width="1.5"/>')
    b.append(f'<line x1="{ox+170}" y1="140" x2="{ox+186}" y2="140" stroke="{OUT}" stroke-width="1.5"/>')
    b.append(f'<line x1="{ox+180}" y1="140" x2="{ox+180}" y2="160" stroke="{OUT}" stroke-width="1.5"/>')
    b.append(text(ox + 186, 154, "2 cm", 11.5, "#222", True))
    b.append('</g>')
    b.append(text(ox + 117, 72, "PORCO (de frente)", 14, "#222", True, "middle"))
    b.append(lines(ox + 22, 330, ["Na linha do meio, 2 cm (um", "dedo) ACIMA da linha dos", "olhos. Porco grande ou", "cachaço: 3–4 cm acima."], 12))
    b.append(lines(ox + 22, 398, ["Mire na direção do rabo", "(ao longo da coluna)."], 12, DRED, True))
    # ---- OVELHA / CABRA de lado ----
    SH = "#efe9dc"; ox = 444
    b.append('<g transform="translate(0,26)">')
    b.append(f'<path d="M{ox+130},100 C{ox+160},110 {ox+190},150 {ox+204},200 L{ox+204},290 L{ox+150},290 C{ox+150},260 {ox+140},236 {ox+124},222 Z" fill="{SH}" stroke="{OUT}" stroke-width="2.5"/>')
    b.append(f'<path d="M{ox+128},98 C{ox+108},94 {ox+88},104 {ox+70},124 C{ox+54},144 {ox+40},170 {ox+30},194 '
             f'C{ox+26},206 {ox+30},214 {ox+42},218 C{ox+62},224 {ox+92},222 {ox+112},224 C{ox+128},226 {ox+140},216 {ox+144},196 '
             f'C{ox+150},160 {ox+148},120 {ox+128},98 Z" fill="{SH}" stroke="{OUT}" stroke-width="2.5"/>')
    b.append(f'<ellipse cx="{ox+156}" cy="128" rx="26" ry="9" transform="rotate(18 {ox+156} 128)" fill="{SH}" stroke="{OUT}" stroke-width="2"/>')
    b.append(f'<ellipse cx="{ox+100}" cy="140" rx="6" ry="4.5" fill="{OUT}"/>')
    b.append(f'<ellipse cx="{ox+38}" cy="196" rx="3" ry="4.5" fill="{OUT}"/>')
    b.append(f'<path d="M{ox+36},212 C{ox+48},216 {ox+62},214 {ox+70},210" fill="none" stroke="{OUT}" stroke-width="1.8"/>')
    # alvo no alto da cabeça e direção para a garganta
    b.append(arrow(ox + 130, 70, ox + 124, 214, RED, 3.5))
    b.append(target(ox + 128, 100))
    b.append(text(ox + 116, 240, "garganta", 11.5, DRED, True, "end"))
    b.append('</g>')
    b.append(text(ox + 108, 72, "OVELHA / CABRA", 14, "#222", True, "middle"))
    b.append(lines(ox + 22, 330, ["Sem chifre: no ALTO da", "cabeça (ponto mais alto).", "Com chifre (bode, carneiro):", "logo ATRÁS dos chifres."], 12))
    b.append(lines(ox + 22, 398, ["Nos dois casos, mire para", "a garganta (seta)."], 12, DRED, True))
    # regras
    y = 454
    b.append(box(12, y, 656, 156, "#fff4e5", "#ef8a2b"))
    b.append(lines(26, y + 22, [
        "Ferramenta: pistola de dardo cativo (a melhor); ou disparo por pessoa treinada e autorizada.",
        "Aves, coelhos e leitões pequenos: pancada forte e seca na nuca (veja o texto).",
        "Cabeça bem presa (brete, corda curta, ajudante). UM golpe, firme, encostado no ponto certo.",
        "Insensível = cai na hora, para a respiração ritmada, olho fixo que não pisca ao ser tocado,",
        "língua mole para fora, não tenta erguer a cabeça. Pernas podem pedalar: é reflexo.",
        "Piscou, gemeu ou tentou levantar? REPITA NA HORA, um pouco ao lado do primeiro ponto.",
        "SANGRE EM ATÉ 60 SEGUNDOS (quanto antes, melhor)."], 12.5, "#222", False, "start", 19))
    return svg(680, 620, "Onde insensibilizar antes da sangria (abate humanitário)", "\n".join(b))

open(D + "abate-insensibilizacao.svg", "w").write(insens())

# ====================== QUEIJO MINAS FRESCAL ======================
def queijo():
    b = []
    steps = [
        ("Pasteurizar o leite", ["65 °C por 30 min mexendo (ou ferver).", "Coe num pano limpo e fervido."]),
        ("Esfriar a 35–37 °C", ["Morno no pulso. Mais quente que", "40 °C estraga o coalho."]),
        ("Pingar e misturar (10 L)", ["4–5 mL de cloreto de cálcio 50% +", "coalho na dose do rótulo. Mexa 1 min."]),
        ("Coagular 40–50 min", ["Tampado, parado, SEM mexer,", "enrolado num pano para não esfriar."]),
        ("Ponto de corte", ["Enfie a faca e levante: a massa", "racha limpa e sai soro verde-claro."]),
        ("Cortar em cubos de 1,5–2 cm", ["Faca comprida: cortes em pé nas", "duas direções e depois inclinados."]),
        ("Descansar e mexer", ["Espere 5 min. Mexa devagar por", "15–20 min: os grãos firmam."]),
        ("Tirar o soro", ["Retire 70–80% do soro com caneca.", "Guarde o soro para fazer ricota."]),
        ("Enformar", ["Formas furadas de 0,5 kg. Aperte", "de leve com a mão limpa."]),
        ("Virar", ["Vire o queijo 3 vezes na primeira", "hora (dentro da própria forma)."]),
        ("Salgar", ["Sal fino nas 2 faces: ~5 g por face", "(1 colher de chá) por queijo de 0,5 kg."]),
        ("Geladeira (4–8 °C)", ["12 h para firmar. Coma em até 10 dias.", "Rende ~1,5 kg por 10 L de leite."]),
    ]
    W, H, G = 316, 60, 16
    for i, (t, d) in enumerate(steps):
        col, row = i // 6, i % 6
        x = 16 + col * 336; y = 56 + row * (H + G)
        hot = i in (0, 1, 3)
        fill = "#fff4e5" if hot else "#eef5ff"
        stroke = "#ef8a2b" if hot else "#3f6d9e"
        b.append(box(x, y, W, H, fill, stroke))
        b.append(f'<circle cx="{x+20}" cy="{y+30}" r="14" fill="{stroke}"/>')
        b.append(text(x + 20, y + 35, str(i + 1), 14, "#fff", True, "middle"))
        b.append(text(x + 42, y + 20, t, 13.5, "#1e1e1e", True))
        b.append(text(x + 42, y + 37, d[0], 11.5, "#333"))
        b.append(text(x + 42, y + 52, d[1], 11.5, "#333"))
        if row < 5:
            b.append(arrow(x + W / 2, y + H + 1, x + W / 2, y + H + G - 1, "#555", 3))
    # seta do fim da coluna 1 para o início da coluna 2
    yb = 56 + 5 * (H + G) + H
    b.append(f'<path d="M174,{yb} L174,{yb+12} L342,{yb+12} L342,46 L510,46 L510,50" fill="none" stroke="#555" stroke-width="3"/>')
    b.append(f'<polygon points="510,56 504,46 516,46" fill="#555"/>')
    yt = yb + 30
    b.append(box(16, yt, 648, 70, "#f7f7f7", "#999"))
    b.append(lines(28, yt + 20, [
        "Tudo lavado e escaldado (panela, faca, formas, pano). Leite só de animal sadio.",
        "Termômetro de cozinha é o melhor amigo do queijeiro. Sem ele: 35 °C = morno, quase",
        "imperceptível no pulso; 65 °C = não dá para manter o dedo nem 1 segundo."], 12.5, "#222", False, "start", 18))
    b.append(text(28, yt + 92, "Laranja = etapas com temperatura. Queijo amargo = coalho demais; mole = cortou cedo.", 12, "#555"))
    return svg(680, yt + 102, "Queijo minas frescal passo a passo (10 L de leite)", "\n".join(b))

open(D + "leite-queijo-minas.svg", "w").write(queijo())

# ====================== VIVEIRO ESCAVADO EM CORTE ======================
def viveiro():
    b = []
    GR = "#5aa04a"
    # solo
    b.append(f'<polygon points="0,170 110,170 190,275 470,312 505,312 565,170 615,170 660,330 668,346 680,346 680,370 0,370" fill="{SOIL}" stroke="#6b4f2a" stroke-width="2.5"/>')
    # água
    b.append(f'<polygon points="133,200 552,200 505,312 470,312 190,275" fill="{WATERL}" stroke="none"/>')
    b.append(f'<line x1="133" y1="200" x2="552" y2="200" stroke="{WATER}" stroke-width="3"/>')
    # grama nas cristas e talude externo
    b.append(f'<line x1="0" y1="170" x2="110" y2="170" stroke="{GR}" stroke-width="5"/>')
    b.append(f'<line x1="565" y1="170" x2="615" y2="170" stroke="{GR}" stroke-width="5"/>')
    b.append(f'<line x1="615" y1="170" x2="660" y2="330" stroke="{GR}" stroke-width="5"/>')
    # peixes
    for (fx, fy) in ((326, 228), (376, 252), (290, 262)):
        b.append(f'<ellipse cx="{fx}" cy="{fy}" rx="16" ry="7" fill="#7f8c99" stroke="{OUT}" stroke-width="1.5"/>'
                 f'<polygon points="{fx+14},{fy} {fx+26},{fy-7} {fx+26},{fy+7}" fill="#7f8c99" stroke="{OUT}" stroke-width="1.5"/>')
    # entrada: cano com tela e registro
    b.append(f'<rect x="0" y="176" width="150" height="10" fill="#9a9a9a" stroke="{OUT}" stroke-width="1.5"/>')
    b.append(f'<rect x="4" y="172" width="12" height="18" fill="none" stroke="{OUT}" stroke-width="1.5"/>')
    for k in range(3):
        b.append(f'<line x1="{6+k*4}" y1="172" x2="{6+k*4}" y2="190" stroke="{OUT}" stroke-width="1"/>')
    b.append(f'<line x1="70" y1="176" x2="70" y2="160" stroke="{OUT}" stroke-width="3"/><circle cx="70" cy="156" r="7" fill="#d62828" stroke="{OUT}" stroke-width="1.5"/>')
    b.append(f'<path d="M150,181 C160,184 162,192 162,200" fill="none" stroke="{WATER}" stroke-width="4"/>')
    b.append(lines(8, 74, ["ENTRADA: cano com TELA na boca", "e registro. A água cai de cima", "(areja e não deixa peixe subir)."], 12, "#222", False, "start", 15))
    b.append(f'<line x1="40" y1="118" x2="12" y2="170" stroke="#555" stroke-width="1.2"/>')
    # monge
    b.append(f'<rect x="478" y="160" width="30" height="152" fill="#bdbdbd" stroke="{OUT}" stroke-width="2"/>')
    for yy in range(206, 312, 13):
        b.append(f'<rect x="481" y="{yy}" width="11" height="12" fill="{WOOD}" stroke="{OUT}" stroke-width="1"/>')
    b.append(f'<rect x="494" y="200" width="11" height="112" fill="#e8f3fd" stroke="none"/>')
    b.append(arrow(486, 196, 500, 214, WATER, 2.5))
    b.append(f'<rect x="508" y="298" width="152" height="12" fill="#9a9a9a" stroke="{OUT}" stroke-width="1.5"/>')
    b.append(arrow(640, 304, 674, 340, WATER, 3))
    b.append(lines(300, 74, ["MONGE (saída): caixa com", "tábuas encaixadas. Tirar", "tábuas baixa o nível ou", "esvazia o viveiro."], 12, "#222", False, "start", 15))
    b.append(f'<line x1="430" y1="134" x2="488" y2="160" stroke="#555" stroke-width="1.2"/>')
    b.append(lines(560, 70, ["crista do dique:", "1,5 a 3 m,", "com grama"], 12, "#2b6a1e", True, "start", 15))
    b.append(lines(560, 122, ["borda livre:", "30 a 50 cm"], 12, "#1e1e1e", True, "start", 15))
    b.append(f'<line x1="556" y1="134" x2="542" y2="168" stroke="#555" stroke-width="1.2"/>')
    # cotas
    def vdim(x, y1, y2, lab, side=1):
        s = (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{OUT}" stroke-width="1.5"/>'
             f'<line x1="{x-6}" y1="{y1}" x2="{x+6}" y2="{y1}" stroke="{OUT}" stroke-width="1.5"/>'
             f'<line x1="{x-6}" y1="{y2}" x2="{x+6}" y2="{y2}" stroke="{OUT}" stroke-width="1.5"/>')
        return s + text(x + 8 * side, (y1 + y2) / 2 + 5, lab, 12.5, "#1e1e1e", True, "start" if side > 0 else "end")
    b.append(vdim(214, 200, 278, "1,0 m (raso)"))
    b.append(vdim(452, 200, 312, "1,5 m", -1))
    b.append(vdim(536, 170, 200, "", 1))
    b.append(f'<line x1="530" y1="170" x2="566" y2="170" stroke="{OUT}" stroke-width="1" stroke-dasharray="3 3"/>')
    b.append(text(226, 324, "fundo inclinado 0,5 a 1%  →", 12, "#5a4630", True))
    b.append(lines(12, 228, ["talude", "interno", "1:2 (barro)", "1:3 (arenoso)"], 11.5, "#5a4630", True, "start", 14))
    b.append(text(520, 342, "cano de saída 100–200 mm", 11.5, "#1e1e1e", True, "end"))
    b.append(text(12, 360, "Desenho fora de escala (altura exagerada).", 11, "#5a4630"))
    # cachimbo
    y0 = 384
    b.append(box(10, y0, 660, 150, "#f7f7f7", "#999"))
    b.append(lines(22, y0 + 26, ["CACHIMBO (mais barato", "que o monge): cano de", "PVC que passa por baixo", "do dique, com um joelho", "que gira dentro d'água."], 12, "#222", False, "start", 16))
    def cach(ox, deitado):
        s = (f'<rect x="{ox}" y="{y0+30}" width="90" height="80" fill="{WATERL}"/>'
             f'<line x1="{ox}" y1="{y0+30}" x2="{ox+90}" y2="{y0+30}" stroke="{WATER}" stroke-width="2.5"/>'
             f'<polygon points="{ox+90},{y0+20} {ox+130},{y0+20} {ox+150},{y0+110} {ox+90},{y0+110}" fill="{SOIL}" stroke="#6b4f2a" stroke-width="2"/>'
             f'<rect x="{ox+40}" y="{y0+96}" width="112" height="10" fill="#9a9a9a" stroke="{OUT}" stroke-width="1.5"/>')
        if not deitado:
            s += f'<rect x="{ox+40}" y="{y0+30}" width="10" height="70" fill="#9a9a9a" stroke="{OUT}" stroke-width="1.5"/>'
            s += arrow(ox + 24, y0 + 18, ox + 42, y0 + 34, WATER, 2.5)
        else:
            s += f'<rect x="{ox-26}" y="{y0+96}" width="66" height="10" fill="#9a9a9a" stroke="{OUT}" stroke-width="1.5"/>'
            s += arrow(ox - 20, y0 + 80, ox - 8, y0 + 96, WATER, 2.5)
        return s
    b.append(cach(222, False))
    b.append(text(297, y0 + 128, "EM PÉ: segura o nível", 12, "#222", True, "middle"))
    b.append(text(297, y0 + 143, "(boca do cano = nível da água)", 11.5, "#222", False, "middle"))
    b.append(cach(500, True))
    b.append(text(563, y0 + 128, "DEITADO: esvazia", 12, "#b3001b", True, "middle"))
    b.append(text(563, y0 + 143, "(gire o cano com uma vara)", 11.5, "#222", False, "middle"))
    return svg(680, y0 + 160, "Viveiro escavado em corte: entrada, saída e medidas", "\n".join(b))

open(D + "peixes-viveiro-corte.svg", "w").write(viveiro())

# ====================== CAIXA LANGSTROTH EXPLODIDA ======================
WOODL = "#e2b97f"; WOODD = "#c9965a"
def caixa3d(x, y, w, h, dx=56, dy=-30, front=WOODL, top=WOODD, side="#b9854a"):
    return (f'<polygon points="{x},{y} {x+dx},{y+dy} {x+w+dx},{y+dy} {x+w},{y}" fill="{top}" stroke="{OUT}" stroke-width="2"/>'
            f'<polygon points="{x+w},{y} {x+w+dx},{y+dy} {x+w+dx},{y+h+dy} {x+w},{y+h}" fill="{side}" stroke="{OUT}" stroke-width="2"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{front}" stroke="{OUT}" stroke-width="2"/>')

def quadros_topo(x, y, w, n=10, dx=56, dy=-30):
    s = ""
    for k in range(n):
        t = (k + 0.5) / n
        x1 = x + 6 + (w - 12) * t
        s += f'<line x1="{x1:.0f}" y1="{y-3}" x2="{x1+dx*0.9:.0f}" y2="{y+dy*0.9:.0f}" stroke="#7a5230" stroke-width="3"/>'
    return s

def langstroth():
    b = []
    X, W = 40, 240
    # tampa
    b.append(caixa3d(X - 6, 78, W + 12, 18, front="#9aa7b0", top="#c3ccd2", side="#7f8c96"))
    # melgueira
    b.append(caixa3d(X, 132, W, 56))
    b.append(quadros_topo(X, 132, W))
    b.append(f'<rect x="{X+20}" y="{150}" width="40" height="8" rx="3" fill="#a97b45"/>')
    # tela excluidora (opcional)
    b.append(f'<polygon points="{X},{216} {X+56},{186} {X+W+56},{186} {X+W},{216}" fill="none" stroke="#555" stroke-width="2" stroke-dasharray="5 4"/>')
    # ninho
    b.append(caixa3d(X, 252, W, 92))
    b.append(quadros_topo(X, 252, W))
    b.append(f'<rect x="{X+20}" y="{272}" width="40" height="8" rx="3" fill="#a97b45"/>')
    # fundo com alvado
    b.append(caixa3d(X, 378, W, 16, front=WOODL))
    b.append(f'<rect x="{X+30}" y="{380}" width="{W-60}" height="8" fill="#3a2e22"/>')
    b.append(f'<polygon points="{X},{394} {X+W},{394} {X+W-10},{410} {X+10},{410}" fill="{WOODD}" stroke="{OUT}" stroke-width="2"/>')
    # cavalete
    for lx in (X + 20, X + W - 34):
        b.append(f'<rect x="{lx}" y="410" width="14" height="44" fill="{WOOD}" stroke="{OUT}" stroke-width="2"/>')
    b.append(f'<line x1="0" y1="454" x2="380" y2="454" stroke="#6b4f2a" stroke-width="3"/>')
    # linhas de montagem
    for xx in (X + 10, X + W - 10):
        b.append(f'<line x1="{xx}" y1="98" x2="{xx}" y2="378" stroke="#888" stroke-width="1" stroke-dasharray="3 5"/>')
    # rótulos à direita
    lab = [
        (96, "TAMPA (com chapa de zinco", "ou lata por cima: chuva)"),
        (160, "MELGUEIRA: onde fica o mel", "que você colhe. 14,5 cm de altura"),
        (204, "tela excluidora (opcional):", "a rainha não sobe para o mel"),
        (296, "NINHO: cria + reserva das", "abelhas (NUNCA colha daqui). 24 cm"),
        (392, "FUNDO com ALVADO (entrada)", "voltado para o nascente"),
        (436, "CAVALETE: 40–50 cm do chão", "(longe de sapo, formiga, umidade)"),
    ]
    for y, l1, l2 in lab:
        b.append(f'<line x1="{X+W+60}" y1="{y-5}" x2="{X+W+70}" y2="{y-5}" stroke="#555" stroke-width="1.5"/>')
        b.append(text(X + W + 74, y - 2, l1, 12, "#1e1e1e", True))
        b.append(text(X + W + 74, y + 13, l2, 11.5, "#333"))
    # quadro avulso
    qx, qy = 468, 470
    b.append(text(qx - 120, qy - 4, "QUADRO de ninho", 12.5, "#1e1e1e", True))
    b.append(f'<rect x="{qx-120}" y="{qy+4}" width="180" height="8" fill="{WOOD}" stroke="{OUT}" stroke-width="1.5"/>')
    b.append(f'<rect x="{qx-106}" y="{qy+12}" width="152" height="78" fill="#f6e3a6" stroke="{OUT}" stroke-width="1.5"/>')
    for r in range(5):
        for c in range(12):
            cx = qx - 98 + c * 12.5 + (6 if r % 2 else 0); cy = qy + 22 + r * 14
            if cx < qx + 42:
                b.append(f'<polygon points="{cx-5},{cy} {cx-2.5},{cy-4.3} {cx+2.5},{cy-4.3} {cx+5},{cy} {cx+2.5},{cy+4.3} {cx-2.5},{cy+4.3}" fill="none" stroke="#c9a24a" stroke-width="1"/>')
    for k in range(4):
        yy = qy + 24 + k * 19
        b.append(f'<line x1="{qx-106}" y1="{yy}" x2="{qx+46}" y2="{yy}" stroke="#555" stroke-width="1.2"/>')
    b.append(f'<rect x="{qx-106}" y="{qy+90}" width="152" height="6" fill="{WOOD}" stroke="{OUT}" stroke-width="1.5"/>')
    b.append(lines(qx + 70, qy + 18, ["48 × 23 cm", "cera alveolada", "presa em 4 fios", "de arame"], 11.5, "#333", False, "start", 15))
    # medidas
    my = 590
    b.append(box(12, my, 656, 100, "#eef5ff", "#3f6d9e"))
    b.append(lines(24, my + 22, [
        "Medidas INTERNAS (padrão Langstroth): 46,5 cm × 37 cm. Ninho com 24 cm de altura;",
        "melgueira com 14,5 cm. Madeira de 2 a 2,5 cm. Cabem 10 quadros, 3,5 cm de centro a centro.",
        "ESPAÇO-ABELHA: 6 a 9 mm entre quadros, paredes e tampa. Menos que isso elas colam com",
        "própolis; mais que isso elas enchem de favo. É a medida mais importante da caixa."], 12.5, "#222", False, "start", 20))
    return svg(680, my + 110, "Colmeia Langstroth desmontada (abelha africanizada)", "\n".join(b))

open(D + "abelhas-langstroth.svg", "w").write(langstroth())

# ====================== CAIXA RACIONAL INPA (SEM FERRÃO) + DIVISÃO ======================
def inpa():
    b = []
    X, W = 40, 150
    def modulo(y, h, nome, conteudo=None, furo=False):
        s = caixa3d(X, y, W, h, dx=44, dy=-24)
        if furo:
            s += f'<circle cx="{X+W/2}" cy="{y+h-14}" r="5" fill="#3a2e22"/>'
            s += f'<path d="M{X+W/2-6},{y+h-14} l-10,10 M{X+W/2+6},{y+h-14} l10,10" stroke="#8a6a3a" stroke-width="3"/>'
        return s
    b.append(text(160, 62, "Módulos empilhados (vista desmontada)", 12.5, "#1e1e1e", True, "middle"))
    # tampa
    b.append(caixa3d(X - 6, 92, W + 12, 14, dx=44, dy=-24, front="#9aa7b0", top="#c3ccd2", side="#7f8c96"))
    # melgueira com potes
    b.append(modulo(140, 40, "melgueira"))
    for k, px in enumerate(range(X + 14, X + W - 10, 22)):
        b.append(f'<ellipse cx="{px+6}" cy="{168}" rx="9" ry="10" fill="#f4c542" stroke="#8a6a1a" stroke-width="1.5"/>')
    # sobreninho
    b.append(modulo(214, 56, "sobreninho"))
    # ninho com discos de cria
    b.append(modulo(304, 70, "ninho", furo=True))
    for k in range(5):
        yy = 222 + k * 10
        b.append(f'<ellipse cx="{X+W/2}" cy="{yy}" rx="{48-k*4}" ry="3.5" fill="#e9d6a8" stroke="#8a6a3a" stroke-width="1.2"/>')
    for k in range(4):
        yy = 314 + k * 10
        b.append(f'<ellipse cx="{X+W/2}" cy="{yy}" rx="{36+k*4}" ry="3.5" fill="#e9d6a8" stroke="#8a6a3a" stroke-width="1.2"/>')
    # rótulos
    lab = [(98, "TAMPA", []), (150, "MELGUEIRA", ["potes de mel", "e de pólen"]),
           (226, "SOBRENINHO", ["sem fundo;", "discos de cria"]), (318, "NINHO", ["fundo fechado", "e entrada"])]
    for y, l1, l2 in lab:
        b.append(text(X + W + 52, y, l1, 12, "#1e1e1e", True))
        for i, t in enumerate(l2):
            b.append(text(X + W + 52, y + 15 + 14 * i, t, 11.5, "#333"))
    # tabela de medidas
    ty = 404
    b.append(box(12, ty, 318, 152, "#eef5ff", "#3f6d9e"))
    b.append(text(24, ty + 20, "Medidas internas aproximadas", 12.5, "#1e1e1e", True))
    b.append(text(150, ty + 40, "pequenas*", 11.5, "#1e1e1e", True, "middle"))
    b.append(text(258, ty + 40, "grandes**", 11.5, "#1e1e1e", True, "middle"))
    rows = [("largura", "13 × 13", "20 × 20"), ("ninho", "7 cm", "10 cm"), ("sobreninho", "5 cm", "7 cm"), ("melgueira", "4 cm", "5 cm")]
    for i, (a, p, g) in enumerate(rows):
        y = ty + 60 + i * 18
        b.append(text(24, y, a, 11.5)); b.append(text(150, y, p, 11.5, "#222", False, "middle")); b.append(text(258, y, g, 11.5, "#222", False, "middle"))
    b.append(text(24, ty + 134, "* jataí, iraí   ** mandaçaia, uruçu, tiúba", 11, "#444"))
    b.append(text(24, ty + 148, "Parede de 2,5–3 cm (protege do calor e do frio)", 11, "#444"))
    # divisão (lado direito)
    dx0 = 350
    b.append(f'<line x1="{dx0-8}" y1="48" x2="{dx0-8}" y2="556" stroke="#ccc" stroke-width="1.5"/>')
    b.append(text(dx0 + 160, 62, "Divisão (multiplicar colônias)", 12.5, "#1e1e1e", True, "middle"))
    def mini(x, y, discos_cima, discos_baixo, cor_cima="#fff", rainha=False, vazio_cima=False):
        s = f'<rect x="{x}" y="{y}" width="80" height="44" fill="{"#fafafa" if vazio_cima else WOODL}" stroke="{OUT}" stroke-width="2"/>'
        s += f'<rect x="{x}" y="{y+44}" width="80" height="44" fill="{WOODL}" stroke="{OUT}" stroke-width="2"/>'
        for k in range(discos_cima):
            s += f'<ellipse cx="{x+40}" cy="{y+40-k*9}" rx="{30-k*3}" ry="3" fill="#e9d6a8" stroke="#8a6a3a" stroke-width="1.2"/>'
        for k in range(discos_baixo):
            s += f'<ellipse cx="{x+40}" cy="{y+50+k*9}" rx="{30-k*2}" ry="3" fill="#e9d6a8" stroke="#8a6a3a" stroke-width="1.2"/>'
        if rainha:
            s += f'<circle cx="{x+66}" cy="{y+70}" r="6" fill="#d62828" stroke="{OUT}" stroke-width="1"/>'
        return s
    # passo 1
    b.append(text(dx0, 90, "1. Caixa FORTE: discos de cria", 12, "#1e1e1e", True))
    b.append(text(dx0, 105, "enchem ninho e sobreninho.", 11.5))
    b.append(mini(dx0 + 210, 74, 4, 4, rainha=True))
    # passo 2
    b.append(text(dx0, 200, "2. Corte entre os módulos com", 12, "#1e1e1e", True))
    b.append(text(dx0, 215, "fio ou espátula: cada parte fica", 11.5))
    b.append(text(dx0, 230, "com cria. Confira a cria NOVA", 11.5))
    b.append(text(dx0, 245, "(clara, quase nascendo) em cima.", 11.5))
    b.append(f'<rect x="{dx0+210}" y="178" width="80" height="44" fill="{WOODL}" stroke="{OUT}" stroke-width="2"/>')
    for k in range(4):
        b.append(f'<ellipse cx="{dx0+250}" cy="{218-k*9}" rx="{30-k*3}" ry="3" fill="#f6eed6" stroke="#8a6a3a" stroke-width="1.2"/>')
    b.append(f'<rect x="{dx0+210}" y="236" width="80" height="44" fill="{WOODL}" stroke="{OUT}" stroke-width="2"/>')
    for k in range(4):
        b.append(f'<ellipse cx="{dx0+250}" cy="{242+k*9}" rx="{30-k*2}" ry="3" fill="#e9d6a8" stroke="#8a6a3a" stroke-width="1.2"/>')
    b.append(f'<circle cx="{dx0+276}" cy="266" r="6" fill="#d62828" stroke="{OUT}" stroke-width="1"/>')
    b.append(f'<line x1="{dx0+200}" y1="229" x2="{dx0+300}" y2="229" stroke="{RED}" stroke-width="2" stroke-dasharray="5 3"/>')
    # passo 3
    b.append(text(dx0, 316, "3. Cada parte ganha um módulo", 12, "#1e1e1e", True))
    b.append(text(dx0, 331, "vazio e vira uma colônia:", 11.5))
    b.append(mini(dx0 + 10, 350, 0, 4, vazio_cima=True, rainha=True))
    b.append(text(dx0 + 50, 456, "COM rainha:", 11.5, "#1e1e1e", True, "middle"))
    b.append(text(dx0 + 50, 471, "vai para um", 11.5, "#222", False, "middle"))
    b.append(text(dx0 + 50, 486, "LUGAR NOVO", 11.5, "#222", False, "middle"))
    b.append(f'<rect x="{dx0+210}" y="350" width="80" height="44" fill="{WOODL}" stroke="{OUT}" stroke-width="2"/>')
    for k in range(4):
        b.append(f'<ellipse cx="{dx0+250}" cy="{390-k*9}" rx="{30-k*3}" ry="3" fill="#f6eed6" stroke="#8a6a3a" stroke-width="1.2"/>')
    b.append(f'<rect x="{dx0+210}" y="394" width="80" height="44" fill="#fafafa" stroke="{OUT}" stroke-width="2"/>')
    b.append(text(dx0 + 250, 456, "SEM rainha:", 11.5, "#1e1e1e", True, "middle"))
    b.append(text(dx0 + 250, 471, "fica no LUGAR da", 11.5, "#222", False, "middle"))
    b.append(text(dx0 + 250, 486, "caixa-mãe (recebe", 11.5, "#222", False, "middle"))
    b.append(text(dx0 + 250, 501, "as campeiras)", 11.5, "#222", False, "middle"))
    b.append(f'<circle cx="{dx0+14}" cy="530" r="6" fill="#d62828" stroke="{OUT}" stroke-width="1"/>')
    b.append(text(dx0 + 26, 534, "= rainha. Divida só caixas", 11.5))
    b.append(text(dx0 + 26, 549, "fortes, na época de florada.", 11.5))
    return svg(680, 566, "Caixa racional (modelo INPA) para abelha sem ferrão", "\n".join(b))

open(D + "abelhas-caixa-inpa.svg", "w").write(inpa())
