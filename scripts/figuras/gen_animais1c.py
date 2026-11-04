import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
# Figuras de 05-animais: silagem em tambor, pastejo rotacionado (piquetes), aprisco suspenso
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "05-animais", "img") + "/"
os.makedirs(D, exist_ok=True)
WOOD = "#8b5a2b"; SOIL = "#e8d3b0"; RED = "#d62828"; DRED = "#b3001b"; GREEN = "#2b8a3e"; BLUE = "#4a90d9"

def lead(x1, y1, x2, y2, color="#555"):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.2"/><circle cx="{x2}" cy="{y2}" r="2.5" fill="{color}"/>'
def dim_v(x, y1, y2, color=DRED):
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{color}" stroke-width="1.6"/>'
            f'<line x1="{x-5}" y1="{y1}" x2="{x+5}" y2="{y1}" stroke="{color}" stroke-width="1.6"/>'
            f'<line x1="{x-5}" y1="{y2}" x2="{x+5}" y2="{y2}" stroke="{color}" stroke-width="1.6"/>')

def drum(x, y, w=70, h=100, fill_level=1.0, layers=True, lid=False):
    """tambor visto de lado; (x,y) = canto superior esquerdo"""
    g = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#3f6d9e" stroke="{OUT}" stroke-width="2"/>']
    top = y + h*(1-fill_level)
    g.append(f'<rect x="{x+4}" y="{top+2}" width="{w-8}" height="{y+h-top-6}" fill="#9cbf5a"/>')
    if layers:
        yy = y + h - 20
        while yy > top + 6:
            g.append(f'<line x1="{x+4}" y1="{yy}" x2="{x+w-4}" y2="{yy}" stroke="#5d7f2a" stroke-width="1.5" stroke-dasharray="4 3"/>')
            yy -= 18
    for yy in (y+h*0.3, y+h*0.7):
        g.append(f'<line x1="{x}" y1="{yy}" x2="{x+w}" y2="{yy}" stroke="{OUT}" stroke-width="1.5"/>')
    if lid:
        g.append(f'<rect x="{x-4}" y="{y-8}" width="{w+8}" height="10" rx="2" fill="#2f5277" stroke="{OUT}" stroke-width="1.8"/>')
    return "".join(g)

# =====================================================================
# 1) SILAGEM EM TAMBOR - passo a passo
# =====================================================================
b = []
def pan(i, title, lines, art):
    px = 8 + (i % 3) * 224; py = 46 + (i // 3) * 262
    s = [f'<rect x="{px}" y="{py}" width="216" height="254" rx="8" fill="#fff" stroke="#2b8a3e" stroke-width="1.8"/>',
         f'<circle cx="{px+20}" cy="{py+20}" r="13" fill="{GREEN}"/>', text(px+20, py+25, str(i+1), 14, "#fff", True, "middle"),
         text(px+40, py+25, title, 13, "#1e5a2a", True)]
    s.append(f'<g transform="translate({px},{py})">{art}</g>')
    for j, l in enumerate(lines):
        s.append(text(px+10, py+160+j*15, l, 10.8, "#222", l.startswith("!")) if not l.startswith("!") else text(px+10, py+160+j*15, l[1:], 10.8, DRED, True))
    return "".join(s)

# arte 1: pe de milho
a1 = ('<rect x="0" y="136" width="216" height="8" fill="#e8d3b0"/>'
      '<line x1="80" y1="136" x2="80" y2="44" stroke="#4f8a2b" stroke-width="6"/>'
      '<path d="M80 120 q-30 -6 -46 6 M80 100 q32 -10 50 0 M80 78 q-28 -12 -44 -2 M80 60 q22 -16 40 -12" fill="none" stroke="#4f8a2b" stroke-width="5" stroke-linecap="round"/>'
      '<ellipse cx="94" cy="88" rx="8" ry="18" fill="#f2c94c" stroke="#1e1e1e" stroke-width="1.6" transform="rotate(20 94 88)"/>'
      '<path d="M86 104 q4 -24 18 -30" fill="none" stroke="#7aa63c" stroke-width="3"/>'
      '<line x1="150" y1="136" x2="150" y2="50" stroke="#3d7a2b" stroke-width="5"/>'
      '<path d="M150 120 q-20 -14 -24 -40 M150 110 q22 -16 26 -44 M150 90 q-14 -20 -10 -40 M150 80 q16 -18 14 -36" fill="none" stroke="#3d7a2b" stroke-width="4" stroke-linecap="round"/>'
      '<text x="80" y="38" font-size="10" text-anchor="middle" fill="#333">milho</text><text x="152" y="44" font-size="10" text-anchor="middle" fill="#333">capim</text>')
b.append(pan(0, "Corte no ponto", ["Milho ou sorgo: grão farináceo", "(a unha marca, mas não sai", "leite), uns 90–110 dias.", "Capim-elefante: 70–90 dias,", "1,5 a 2 m de altura.", "Pode ser cana + capim também."], a1))
# arte 2: picar
a2 = ('<rect x="40" y="100" width="140" height="24" rx="10" fill="#9cbf5a" stroke="#1e1e1e" stroke-width="1.5"/>'
      + "".join(f'<rect x="{50+(i%10)*13}" y="{88+(i//10)*8 - (i%3)*2}" width="9" height="5" fill="#7aa63c" stroke="#3d5a1a" stroke-width="0.8" transform="rotate({(i*37)%60-30} {54+(i%10)*13} {90+(i//10)*8})"/>' for i in range(20))
      + '<g transform="rotate(-30 120 62)"><rect x="80" y="56" width="80" height="12" rx="3" fill="#c0c0c0" stroke="#1e1e1e" stroke-width="1.5"/>'
      '<rect x="158" y="54" width="30" height="16" rx="4" fill="#8b5a2b" stroke="#1e1e1e" stroke-width="1.5"/></g>'
      '<text x="110" y="140" font-size="10.5" text-anchor="middle" fill="#b3001b" font-weight="bold">pedaços de 1–2 cm</text>')
b.append(pan(1, "Pique miúdo", ["Picadeira, ou facão em cepo.", "Pedaço pequeno compacta", "melhor e expulsa o ar.", "Pique e ensile no MESMO dia", "(no máximo em 1–2 dias para", "encher e fechar o tambor)."], a2))
# arte 3: socar em camadas
a3 = (drum(60, 62, 80, 84, 0.75) +
      '<rect x="94" y="40" width="12" height="44" fill="#8b5a2b" stroke="#1e1e1e" stroke-width="1.5"/>'
      '<rect x="84" y="82" width="32" height="12" rx="3" fill="#8b5a2b" stroke="#1e1e1e" stroke-width="1.5"/>'
      + arrow(160, 50, 160, 86, "#b3001b", 3) +
      '<text x="150" y="104" font-size="10" fill="#333">camadas</text><text x="150" y="116" font-size="10" fill="#333">de 10–15 cm</text>')
b.append(pan(2, "Encha e soque", ["Camadas de 10–15 cm: soque", "ou pise cada uma com força.", "O segredo é tirar o AR.", "Tambor de 200 L leva", "120–150 kg; saco grosso", "(200 micra) leva 40–60 kg."], a3))
# arte 4: fechar
a4 = (drum(60, 74, 80, 72, 1.0, True, True) +
      '<path d="M54 68 q46 -16 92 0 l0 8 q-46 -10 -92 0 Z" fill="#dfe8f0" fill-opacity="0.8" stroke="#555"/>'
      '<rect x="78" y="40" width="44" height="26" rx="8" fill="#e8d3b0" stroke="#1e1e1e" stroke-width="1.6"/>'
      '<text x="100" y="58" font-size="9.5" text-anchor="middle" fill="#5a4630">areia</text>')
b.append(pan(3, "Feche sem ar", ["Plástico por cima, encostado", "na massa; tampa bem presa", "e peso em cima (saco de", "areia, pedra). Saco: aperte", "para sair o ar e amarre.", "!Furo = mofo. Tape com fita."], a4))
# arte 5: esperar
a5 = ('<rect x="60" y="44" width="96" height="96" rx="6" fill="#fff" stroke="#1e1e1e" stroke-width="2"/>'
      '<rect x="60" y="44" width="96" height="22" rx="6" fill="#d62828" stroke="#1e1e1e" stroke-width="2"/>'
      + "".join(f'<rect x="{66+(i%7)*12.5:.1f}" y="{72+(i//7)*13}" width="9" height="9" fill="{"#9cbf5a" if i < 30 else "#eee"}" stroke="#999" stroke-width="0.6"/>' for i in range(35))
      + '<text x="108" y="60" font-size="11" text-anchor="middle" fill="#fff" font-weight="bold">30 DIAS</text>')
b.append(pan(4, "Espere fermentar", ["No mínimo 3–4 semanas", "fechado, à sombra, longe de", "ratos e de furos.", "Bem fechada, a silagem", "dura mais de 1 ano: é a", "comida da seca."], a5))
# arte 6: abrir e usar
a6 = (drum(30, 72, 70, 74, 0.85, False) +
      '<path d="M130 100 L176 100 L170 146 L136 146 Z" fill="#c0c0c0" stroke="#1e1e1e" stroke-width="1.8"/>'
      '<ellipse cx="153" cy="100" rx="23" ry="6" fill="#9cbf5a" stroke="#1e1e1e" stroke-width="1.5"/>'
      '<path d="M58 66 q4 -10 0 -18 M72 66 q4 -10 0 -18" fill="none" stroke="#2b8a3e" stroke-width="2"/>'
      '<text x="88" y="60" font-size="10" fill="#2b8a3e" font-weight="bold">cheiro azedinho</text>')
b.append(pan(5, "Abra e use rápido", ["Boa: verde-amarelada, cheiro", "azedo agradável (de fruta).", "Gaste o tambor aberto em", "2–4 dias; tampe entre usos.", "!Mofada, preta, gosmenta ou", "!cheiro de podre: JOGUE FORA."], a6))
b.append(box(8, 574, 664, 100, "#fff4e5", "#ef8a2b"))
b += [text(20, 594, '<tspan font-weight="bold">Teste do punho (umidade certa):</tspan> aperte um punhado da massa picada por 30 segundos e abra a mão.', 11.4),
      text(20, 612, "• Escorre caldo, ou a bola fica firme e a mão molhada: úmido demais. Deixe murchar 4–6 h ao sol", 11.4),
      text(20, 628, "   ou misture 5–10% de fubá ou farelo.  • A bola se abre devagar e a mão fica só úmida: PONTO CERTO.", 11.4),
      text(20, 644, "• Desmancha na hora: seco demais (compacta mal e mofa); corte a lavoura mais cedo da próxima vez.", 11.4),
      text(20, 664, "Vaca adulta: 20–30 kg de silagem/dia. Cabra ou ovelha: 2–4 kg. Sempre com algum capim.", 11.6, "#222", True)]
open(D + "silagem-tambor.svg", "w").write(svg(680, 684, "Silagem em tambor ou saco, passo a passo", "\n".join(b)))

# =====================================================================
# 2) PASTEJO ROTACIONADO (vista de cima)
# =====================================================================
def cow_top(x, y, rot=0, col="#f4f1ea"):
    return (f'<g transform="translate({x},{y}) rotate({rot})">'
            f'<ellipse cx="0" cy="0" rx="12" ry="6.5" fill="{col}" stroke="{OUT}" stroke-width="1.2"/>'
            f'<ellipse cx="-3" cy="-1" rx="4" ry="3" fill="#5a3a20"/>'
            f'<ellipse cx="14" cy="0" rx="4.5" ry="3.5" fill="{col}" stroke="{OUT}" stroke-width="1.1"/></g>')
b = []
greens = ["#dce9b8", "#cfe3a2", "#bcd98a", "#a6cd70", "#8fbf58", "#78b046", "#62a03a", "#4f8f32", "#3e7f2a"]
PX0, PY0, PW, PH = 30, 60, 470, 300
CW = PW / 5
# corredor central
b.append(f'<rect x="{PX0}" y="{PY0}" width="{PW}" height="{PH}" fill="#fff" stroke="{OUT}" stroke-width="2"/>')
order = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (3, 1), (2, 1), (1, 1), (0, 1)]
LANE = 34
rowh = (PH - LANE) / 2
for k, (c, r) in enumerate(order):
    x = PX0 + c*CW; y = PY0 + (0 if r == 0 else rowh + LANE)
    if k == 0:
        fill = "#9db86b"
    else:
        fill = greens[(k - 1)] if k - 1 < len(greens) else greens[-1]
    # o piquete 2 (k=1) acabou de sair: mais baixo; o 10 (k=9) esta pronto
    order_age = [None, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    if k > 0:
        fill = greens[order_age[k] - 1]
    b.append(f'<rect x="{x}" y="{y}" width="{CW}" height="{rowh}" fill="{fill}" stroke="#6b4f2a" stroke-width="2"/>')
    b.append(f'<circle cx="{x+16}" cy="{y+16}" r="11" fill="#fff" stroke="{OUT}" stroke-width="1.2"/>')
    b.append(text(x+16, y+20.5, str(k+1), 11.5, "#222", True, "middle"))
b.append(f'<rect x="{PX0}" y="{PY0+rowh}" width="{PW}" height="{LANE}" fill="#e8d3b0" stroke="#6b4f2a" stroke-width="1.5"/>')
b.append(text(PX0+PW/2-30, PY0+rowh+21, "corredor (leva à água)", 11, "#5a4630", True, "middle"))
# porteiras (aberturas no corredor)
for c in range(5):
    for r in (0, 1):
        gx = PX0 + c*CW + CW/2 - 12
        gy = PY0 + rowh if r == 0 else PY0 + rowh + LANE
        b.append(f'<line x1="{gx}" y1="{gy}" x2="{gx+24}" y2="{gy}" stroke="#fff" stroke-width="4"/>')
# bebedouro e cocho de sal no fim do corredor
b.append(f'<rect x="{PX0+PW+6}" y="{PY0+rowh-22}" width="60" height="78" rx="6" fill="#e8d3b0" stroke="#6b4f2a" stroke-width="1.5"/>')
b.append(f'<circle cx="{PX0+PW+36}" cy="{PY0+rowh+2}" r="16" fill="{BLUE}" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<rect x="{PX0+PW+18}" y="{PY0+rowh+28}" width="36" height="14" rx="3" fill="#fff" stroke="{OUT}" stroke-width="1.5"/>')
b.append(text(PX0+PW+70, PY0+rowh-2, "água", 11, "#1f5fa8", True))
b.append(text(PX0+PW+70, PY0+rowh+40, "sal mineral", 11, "#222", True))
b.append(text(PX0+PW+70, PY0+rowh+54, "(cocho coberto)", 10.5, "#222"))
# vacas no piquete 1
for (x, y, r) in ((62, 104, 10), (96, 128, -20), (70, 156, 30), (112, 96, 80), (120, 150, 160), (58, 130, 200)):
    b.append(cow_top(x, y, r, "#f4f1ea" if r % 20 == 0 else "#c08a5a"))
# seta de rotacao
b.append(f'<path d="M{PX0+CW*0.5} {PY0-8} L{PX0+CW*4.5} {PY0-8}" fill="none" stroke="{DRED}" stroke-width="2.5"/>')
b.append(arrow(PX0+CW*4.3, PY0-8, PX0+CW*4.6, PY0-8, DRED, 2.5))
b.append(text(PX0+CW*2.5, PY0-14, "o gado muda de piquete na ordem 1 → 2 → 3 … → 10 → 1", 11, DRED, True, "middle"))
b.append(text(PX0+CW*0.5, PY0+rowh-10, "gado aqui", 11, "#222", True, "middle"))
b.append(text(PX0+CW*0.5, PY0+rowh-10+rowh+LANE, "acabou de sair", 10.5, "#222", True, "middle"))
b.append(text(PX0+CW*1.5, PY0+rowh-24, "o próximo:", 10.5, "#fff", True, "middle"))
b.append(text(PX0+CW*1.5, PY0+rowh-10, "pronto", 10.5, "#fff", True, "middle"))
# legenda de cores
b.append(text(580, 80, "Altura do capim", 11.5, "#222", True, "middle"))
for i, g_ in enumerate((greens[0], greens[4], greens[8])):
    b.append(f'<rect x="530" y="{92+i*26}" width="22" height="18" fill="{g_}" stroke="{OUT}"/>')
b.append(text(558, 105, "baixo (descansando)", 10.5, "#222")); b.append(text(558, 131, "crescendo", 10.5, "#222")); b.append(text(558, 157, "alto: pronto", 10.5, "#222"))
b.append(box(16, 376, 648, 72, "#eef7ee", GREEN))
b += [text(30, 396, '<tspan font-weight="bold">Ocupação:</tspan> 1 a 3 dias por piquete (no máximo 7).  <tspan font-weight="bold">Descanso:</tspan> 25–35 dias nas águas, mais na seca.', 11.6),
      text(30, 414, '<tspan font-weight="bold">Quantos piquetes?</tspan> descanso ÷ ocupação + 1. Ex.: 27 dias ÷ 3 dias + 1 = 10 piquetes (este desenho).', 11.6),
      text(30, 432, "Água e sal em todos os piquetes, ou no corredor. Sombra (árvores) em cada piquete se possível.", 11.6)]
# tabela de alturas
b.append(text(340, 470, "Quando entrar e quando tirar o gado (altura do capim)", 13, "#222", True, "middle"))
tab = [("Capim", "Entrar com", "Tirar com"),
       ("Braquiarão (Marandu)", "25–30 cm", "15 cm"),
       ("Braquiária decumbens", "20 cm", "10 cm"),
       ("Mombaça", "90 cm", "30–50 cm"),
       ("Tanzânia", "70 cm", "30–35 cm"),
       ("Capim-elefante", "100 cm", "40–50 cm"),
       ("Tifton, coastcross, estrela", "25 cm", "10–15 cm")]
for i, (c1, c2, c3) in enumerate(tab):
    y = 482 + i*21
    bg = "#2b8a3e" if i == 0 else ("#f3faf3" if i % 2 else "#fff")
    b.append(f'<rect x="100" y="{y}" width="480" height="21" fill="{bg}" stroke="#cfd8cf"/>')
    col = "#fff" if i == 0 else "#222"
    b.append(text(112, y+15, c1, 11.5, col, i == 0)); b.append(text(400, y+15, c2, 11.5, col, True, "middle")); b.append(text(510, y+15, c3, 11.5, col, i == 0, "middle"))
b.append(text(340, 646, "Nunca rape o pasto até o chão: a planta perde a reserva, demora a rebrotar e o mato invade.", 11.5, DRED, True, "middle"))
open(D + "pastejo-piquetes.svg", "w").write(svg(680, 658, "Pastejo rotacionado em piquetes (vista de cima)", "\n".join(b)))

# =====================================================================
# 3) APRISCO SUSPENSO (corte) para cabras e ovelhas
# =====================================================================
def goat(x, y, s=1.0, face=1, col="#f4f1ea", head_down=False):
    """cabra de perfil; (x,y) = chao sob as patas; face=1 olha para a direita"""
    g = []
    for lx in (-22, -14, 14, 22):
        g.append(f'<line x1="{lx}" y1="-26" x2="{lx}" y2="0" stroke="{OUT}" stroke-width="5" stroke-linecap="round"/>')
        g.append(f'<line x1="{lx}" y1="-26" x2="{lx}" y2="0" stroke="{col}" stroke-width="2.6" stroke-linecap="round"/>')
    g.append(f'<path d="M-30 -40 q-6 -10 -2 -14" fill="none" stroke="{OUT}" stroke-width="3"/>')
    g.append(f'<ellipse cx="0" cy="-38" rx="32" ry="15" fill="{col}" stroke="{OUT}" stroke-width="1.8"/>')
    if head_down:
        g.append(f'<path d="M24 -44 L42 -30 L36 -22 L20 -32 Z" fill="{col}" stroke="{OUT}" stroke-width="1.6"/>')
        hx, hy, rot = 46, -24, 40
    else:
        g.append(f'<path d="M22 -46 L32 -66 L40 -62 L32 -38 Z" fill="{col}" stroke="{OUT}" stroke-width="1.6"/>')
        hx, hy, rot = 40, -68, 20
    g.append(f'<g transform="translate({hx},{hy}) rotate({rot})">'
             f'<path d="M-4 -6 q-8 -12 -16 -10" fill="none" stroke="#7a6a50" stroke-width="3.5" stroke-linecap="round"/>'
             f'<ellipse cx="0" cy="0" rx="13" ry="7" fill="{col}" stroke="{OUT}" stroke-width="1.6"/>'
             f'<ellipse cx="-6" cy="4" rx="7" ry="3" fill="{col}" stroke="{OUT}" stroke-width="1.2" transform="rotate(30 -6 4)"/>'
             f'<path d="M8 5 l2 9 l3 -8" fill="#9a8a70" stroke="{OUT}" stroke-width="1"/>'
             f'<circle cx="2" cy="-2" r="1.5" fill="{OUT}"/></g>')
    return f'<g transform="translate({x},{y}) scale({face*s},{s})">' + "".join(g) + '</g>'

b = []
GY = 470; PL = 360; BX1, BX2 = 150, 470
b.append(f'<rect x="0" y="{GY}" width="680" height="30" fill="{SOIL}"/>')
b.append(f'<line x1="0" y1="{GY}" x2="680" y2="{GY}" stroke="#6b4f2a" stroke-width="3"/>')
# esterco
b.append(f'<path d="M{BX1+20} {GY} Q{BX1+80} {GY-34} {BX1+160} {GY-26} Q{BX1+240} {GY-36} {BX2-20} {GY} Z" fill="#6b4a2a" stroke="#3a2614" stroke-width="1.5"/>')
for i in range(26):
    b.append(f'<circle cx="{BX1+40+i*11}" cy="{GY-8-(i*7)%14}" r="3" fill="#3a2614"/>')
# pilares
for x in (BX1+4, (BX1+BX2)//2, BX2-4):
    b.append(f'<rect x="{x-6}" y="{PL}" width="12" height="{GY-PL}" fill="{WOOD}" stroke="{OUT}" stroke-width="1.5"/>')
    b.append(f'<rect x="{x-5}" y="200" width="10" height="{PL-200}" fill="{WOOD}" stroke="{OUT}" stroke-width="1.2"/>')
# piso ripado
b.append(f'<rect x="{BX1}" y="{PL-2}" width="{BX2-BX1}" height="12" fill="#5a4630"/>')
x = BX1
while x < BX2:
    b.append(f'<rect x="{x}" y="{PL-2}" width="7" height="12" fill="#c49a62" stroke="{OUT}" stroke-width="0.8"/>')
    x += 10
# paredes de ripas (laterais) ate 1,2 m acima do piso
for xw in (BX1, BX2-8):
    for yy in range(PL-118, PL-2, 12):
        b.append(f'<rect x="{xw}" y="{yy}" width="8" height="8" fill="#c49a62" stroke="{OUT}" stroke-width="0.6"/>')
# canzil (abertura para a cabeca) e comedouro externo a esquerda
b.append(f'<rect x="{BX1-1}" y="{PL-70}" width="10" height="40" fill="#fff"/>')
b.append(f'<path d="M{BX1-56} {PL-36} L{BX1} {PL-36} L{BX1-6} {PL-4} L{BX1-50} {PL-4} Z" fill="#c49a62" stroke="{OUT}" stroke-width="1.8"/>')
b.append(f'<path d="M{BX1-52} {PL-34} q24 -10 48 0" fill="#9cbf5a" stroke="#4f7a2a"/>')
b.append(f'<rect x="{BX1-34}" y="{PL-4}" width="8" height="{GY-PL+4}" fill="{WOOD}" stroke="{OUT}" stroke-width="1"/>')
# telhado
b.append(f'<polygon points="{BX1-34},{214} {(BX1+BX2)//2},{120} {BX2+34},{214} {BX2+34},{224} {(BX1+BX2)//2},{130} {BX1-34},{224}" fill="#a0522d" stroke="{OUT}" stroke-width="2"/>')
# animais
b.append(goat(BX1+50, PL-2, 1.0, -1, "#f4f1ea", True))
b.append(goat(BX1+170, PL-2, 1.0, 1, "#c08a5a"))
b.append(goat(BX1+250, PL-2, 0.6, -1, "#f4f1ea"))
# rampa a direita
b.append(f'<polygon points="{BX2},{PL} {BX2+176},{GY} {BX2+176},{GY+0} {BX2+160},{GY} {BX2},{PL+12}" fill="#c49a62" stroke="{OUT}" stroke-width="1.8"/>')
ang = math.degrees(math.atan2(110, 176))
for i in range(1, 9):
    tx = BX2 + i*19; ty = PL + i*19*110/176
    b.append(f'<rect x="{tx-4}" y="{ty-5}" width="8" height="5" fill="{WOOD}" stroke="{OUT}" stroke-width="1" transform="rotate({ang:.1f} {tx} {ty})"/>')
# cotas
b.append(dim_v(BX1-80, PL, GY)); b.append(text(BX1-86, PL+50, "1,0–1,2 m", 11, DRED, True, "end"))
b.append(dim_v(BX2+48, 224, PL)); b.append(text(BX2+54, 300, "2,0–2,5 m", 11, DRED, True))
# rotulos
b.append(text(8, 250, "Comedouro por fora,", 11.3, "#222", True)); b.append(text(8, 264, "com canzil (vão para", 11.3, "#222"))
b.append(text(8, 278, "a cabeça): o animal", 11.3, "#222")); b.append(text(8, 292, "não pisa nem suja", 11.3, "#222"))
b.append(text(8, 306, "a comida", 11.3, "#222"))
b.append(lead(64, 312, BX1-36, PL-34))
b.append(text(BX2+48, 140, "Telhado com beiral;", 11.3, "#222", True)); b.append(text(BX2+48, 154, "laterais de ripas: ventila", 11.3, "#222"))
b.append(text(BX2+48, 168, "e protege do vento frio", 11.3, "#222"))
b.append(text(BX2+104, 372, "Rampa com", 11.3, "#222", True)); b.append(text(BX2+104, 386, "travessas a", 11.3, "#222"))
b.append(text(BX2+104, 400, "cada 20 cm", 11.3, "#222"))
b.append(text(322, 384, "Piso de ripas:", 11.3, "#222", True)); b.append(text(322, 398, "4–5 cm de largura,", 11.3, "#222"))
b.append(text(322, 412, "vão de 1,5–2 cm", 11.3, "#222")); b.append(text(322, 426, "(o casco não entra)", 11.3, "#222"))
b.append(text((BX1+BX2)//2, GY+20, "O esterco cai pelo piso: limpeza fácil, adubo bom e menos verme, casco podre e piolho", 11, "#5a4630", True, "middle"))
b.append(box(16, 504, 648, 76, "#eef7ee", GREEN))
b += [text(30, 524, "Espaço por animal: cabra ou ovelha adulta 0,8–1,2 m²; fêmea com cria 1,5–2 m²; cabrito ou", 11.6),
      text(30, 542, "cordeiro 0,3–0,5 m²; bode ou carneiro em baia separada de 2–3 m². Comprimento leste-oeste.", 11.6),
      text(30, 560, "Bebedouro e saleiro (cocho de sal coberto) também por fora ou em altura que não sujem.", 11.6)]
open(D + "cabra-aprisco.svg", "w").write(svg(680, 540, "Aprisco suspenso (corte) para cabras e ovelhas", '<g transform="translate(0,-50)">' + "\n".join(b) + '</g>'))
