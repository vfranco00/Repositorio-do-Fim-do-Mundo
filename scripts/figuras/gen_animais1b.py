import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
# Figuras de 05-animais: parto bovino, FAMACHA, maternidade suina, gaiola de coelho
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "05-animais", "img") + "/"
os.makedirs(D, exist_ok=True)
WOOD = "#8b5a2b"; SOIL = "#e8d3b0"; RED = "#d62828"; DRED = "#b3001b"; GREEN = "#2b8a3e"; BLUE = "#4a90d9"
CALF = "#c08a5a"; HOOF = "#3a2a1a"

def dim_h(x1, x2, y, color=DRED):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="1.6"/>'
            f'<line x1="{x1}" y1="{y-5}" x2="{x1}" y2="{y+5}" stroke="{color}" stroke-width="1.6"/>'
            f'<line x1="{x2}" y1="{y-5}" x2="{x2}" y2="{y+5}" stroke="{color}" stroke-width="1.6"/>')
def dim_v(x, y1, y2, color=DRED):
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{color}" stroke-width="1.6"/>'
            f'<line x1="{x-5}" y1="{y1}" x2="{x+5}" y2="{y1}" stroke="{color}" stroke-width="1.6"/>'
            f'<line x1="{x-5}" y1="{y2}" x2="{x+5}" y2="{y2}" stroke="{color}" stroke-width="1.6"/>')
def lead(x1, y1, x2, y2, color="#555"):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.2"/><circle cx="{x2}" cy="{y2}" r="2.5" fill="{color}"/>'

# =====================================================================
# 1) PARTO BOVINO: posicao normal e anormais
# =====================================================================
def leg(pts, w=7):
    s = limb(pts, w, CALF)
    x, y = pts[-1]
    return s + f'<circle cx="{x}" cy="{y}" r="4.5" fill="{HOOF}" stroke="{OUT}" stroke-width="1"/>'

def head_calf(cx, cy, face=1, rot=0):
    """cabeca de bezerro de perfil; face=1 focinho para a direita"""
    g = (f'<path d="M-6 -9 Q-14 -18 -22 -14 Q-16 -8 -8 -5 Z" fill="{CALF}" stroke="{OUT}" stroke-width="1.3"/>'
         f'<path d="M-17 -6 Q-12 -13 4 -10 L19 -4 Q24 0 20 6 L6 10 Q-12 13 -18 5 Z" fill="{CALF}" stroke="{OUT}" stroke-width="1.8"/>'
         f'<circle cx="-2" cy="-4" r="1.9" fill="{OUT}"/>'
         f'<ellipse cx="18" cy="1" rx="2" ry="1.5" fill="{OUT}"/>')
    return f'<g transform="translate({cx},{cy}) rotate({rot}) scale({face},1)">{g}</g>'

def body_calf(cx, cy, rx=44, ry=23, rot=0):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{CALF}" stroke="{OUT}" stroke-width="1.8" transform="rotate({rot} {cx} {cy})"/>'

def womb():
    P = "M166.5,58 L212,58 L212,102 L166.5,102 A84,62 0 1 1 166.5,58 Z"
    return (f'<path d="{P}" fill="#f6dede"/>'
            '<path d="M212,58 L166.5,58 A84,62 0 1 0 166.5,102 L212,102" fill="none" stroke="#b56576" stroke-width="2.5"/>'
            '<path d="M212 50 q7 8 0 16 M212 94 q7 8 0 16" fill="none" stroke="#b56576" stroke-width="4" stroke-linecap="round"/>')

def calf_variant(v):
    g = []
    if v == "normal":
        g.append(leg([(42, 96), (56, 116), (86, 110)])); g.append(leg([(50, 98), (66, 120), (94, 114)]))
        g.append(body_calf(70, 80)); g.append(limb([(104, 70), (140, 72)], 16, CALF))
        g.append(leg([(104, 90), (150, 92), (198, 88)])); g.append(leg([(106, 94), (152, 98), (202, 96)]))
        g.append(head_calf(160, 74, 1))
    elif v == "tras":
        g.append(leg([(60, 96), (80, 116), (40, 114)])); g.append(leg([(64, 100), (86, 120), (48, 120)]))
        g.append(head_calf(30, 70, -1, 20)); g.append(body_calf(84, 80))
        g.append(leg([(118, 88), (150, 76), (200, 74)])); g.append(leg([(120, 94), (154, 84), (204, 84)]))
        g.append(text(128, 50, "jarrete", 9.5, "#333", False, "middle"))
        g.append('<line x1="134" y1="53" x2="148" y2="72" stroke="#333" stroke-width="1"/>')
    elif v == "cabeca":
        g.append(leg([(42, 96), (56, 116), (86, 110)]))
        g.append(body_calf(76, 82)); g.append(limb([(108, 70), (98, 50)], 16, CALF))
        g.append(head_calf(74, 44, -1, 10))
        g.append(leg([(108, 92), (152, 92), (198, 88)])); g.append(leg([(110, 96), (154, 100), (202, 96)]))
    elif v == "joelho":
        g.append(leg([(42, 96), (56, 116), (86, 110)]))
        g.append(body_calf(70, 80)); g.append(limb([(104, 70), (140, 72)], 16, CALF))
        g.append(leg([(104, 92), (150, 104), (120, 118)]))
        g.append(leg([(106, 90), (152, 92), (200, 90)]))
        g.append(head_calf(160, 74, 1))
        g.append(text(158, 122, "joelho", 9.5, "#333", False, "middle"))
    elif v == "nadegas":
        g.append(head_calf(26, 74, -1, 15))
        g.append(leg([(56, 96), (72, 114), (34, 112)]))
        g.append(body_calf(90, 80, 46, 24))
        g.append(leg([(122, 92), (100, 112), (66, 112)])); g.append(leg([(126, 96), (108, 120), (74, 120)]))
        g.append('<path d="M136 76 q22 -2 40 6" fill="none" stroke="#5a3a20" stroke-width="3.5"/>')
        g.append(text(178, 74, "cauda", 9.5, "#333", False, "middle"))
    elif v == "costas":
        g.append(leg([(42, 66), (56, 46), (86, 50)])); g.append(leg([(50, 64), (66, 42), (94, 46)]))
        g.append(body_calf(70, 82)); g.append(limb([(104, 92), (140, 90)], 16, CALF))
        g.append(leg([(104, 72), (150, 70), (198, 72)])); g.append(leg([(106, 68), (152, 64), (202, 64)]))
        g.append(f'<g transform="translate(160,88) scale(1,-1)">{head_calf(0, 0, 1)}</g>')
    return "".join(g)

panels = [("normal", "1. NORMAL", GREEN, ["2 patas da FRENTE (sola do casco", "para baixo) e o focinho por cima.", "Espere. Só ajude se parar de", "avançar por 30 minutos."]),
          ("tras", "2. DE TRASEIRO", "#c06000", ["2 patas de TRÁS (sola para cima;", "o jarrete dobra ao contrário).", "Nasce assim, mas tire SEM", "demora: o umbigo fica apertado."]),
          ("cabeca", "3. CABEÇA VIRADA", DRED, ["Saem patas, mas não o focinho.", "Empurre o bezerro para dentro", "entre as forças da vaca e traga", "a cabeça pela boca/mandíbula."]),
          ("joelho", "4. PERNA DOBRADA", DRED, ["Sai a cabeça e só 1 pata (ou", "nenhuma). Empurre para dentro,", "pegue o casco com a mão em", "concha e estique a perna."]),
          ("nadegas", "5. DE NÁDEGAS", DRED, ["Só a cauda aparece (ou nada).", "Empurre o bezerro e traga uma", "perna de trás de cada vez, com o", "casco protegido na sua mão."]),
          ("costas", "6. DE COSTAS", DRED, ["Patas com sola para CIMA e", "focinho por baixo delas. Gire o", "bezerro de lado (90°) antes de", "puxar."])]
b = []
for i, (v, t, col, lines) in enumerate(panels):
    px = 8 + (i % 3) * 224; py = 60 + (i // 3) * 254
    b.append(f'<rect x="{px}" y="{py}" width="216" height="246" rx="8" fill="#fff" stroke="{col}" stroke-width="2"/>')
    b.append(text(px+108, py+20, t, 13.5, col, True, "middle"))
    b.append(f'<g transform="translate({px+3},{py+28}) scale(0.96)">' + womb() + calf_variant(v) + '</g>')
    for j, s_ in enumerate(lines):
        b.append(text(px+8, py+178+j*15, s_, 10.8, "#222"))
b.append(text(340, 52, "Vaca vista de lado: a saída (vulva) fica à DIREITA de cada desenho.", 12, "#7a3a4a", True, "middle"))
b.append(box(8, 570, 664, 112, "#fff4e5", "#ef8a2b"))
tips = [("Como puxar:", " corda limpa com laço acima do boleto + meia-volta entre o boleto e o casco."),
        ("", "Puxe SÓ durante a força da vaca, em arco para BAIXO (em direção aos jarretes dela),"),
        ("", "alternando as patas. No máximo 2 pessoas. NUNCA trator, carro ou talha."),
        ("Frente ou trás?", " Pata da frente: as 2 juntas acima do casco dobram para o mesmo lado."),
        ("", "Pata de trás: a 2ª junta (jarrete) dobra para o lado contrário e tem uma ponta óssea.")]
for j, (k, s_) in enumerate(tips):
    b.append(text(20, 590 + j*19, f'<tspan font-weight="bold">{k}</tspan>{s_}' if k else s_, 11.6, "#222"))
open(D + "bovino-parto.svg", "w").write(svg(680, 692, "Parto da vaca: posição normal e as erradas mais comuns", "\n".join(b)))

# =====================================================================
# 2) CARTAO FAMACHA (cabras e ovelhas)
# =====================================================================
b = []
# olho com as palpebras abertas pelos polegares
b.append('<rect x="24" y="58" width="236" height="232" rx="18" fill="#e9dcc4" stroke="#b9a37a" stroke-width="1.5"/>')
b.append('<path d="M70 150 Q140 108 210 150 Q140 176 70 150 Z" fill="#fff" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append('<ellipse cx="140" cy="148" rx="24" ry="17" fill="#c99a2e" stroke="#1e1e1e" stroke-width="1.8"/>')
b.append('<rect x="122" y="143" width="36" height="10" rx="5" fill="#1e1e1e"/>')
b.append('<circle cx="150" cy="141" r="2.5" fill="#fff"/>')
# mucosa exposta
b.append('<path d="M76 158 Q140 182 204 158 Q206 172 196 186 Q140 214 84 186 Q74 172 76 158 Z" fill="#d9475a" stroke="#7a1020" stroke-width="2"/>')
b.append('<path d="M84 186 Q140 214 196 186" fill="none" stroke="#a78a5f" stroke-width="5"/>')
# polegares
b.append(f'<g transform="rotate(-8 140 84)"><rect x="104" y="58" width="74" height="54" rx="26" fill="{SKIN}" stroke="#1e1e1e" stroke-width="2"/>'
         f'<rect x="124" y="60" width="34" height="22" rx="9" fill="#f8e1cf" stroke="#1e1e1e" stroke-width="1.2"/></g>')
b.append(f'<g transform="rotate(6 140 232)"><rect x="102" y="204" width="76" height="56" rx="26" fill="{SKIN}" stroke="#1e1e1e" stroke-width="2"/>'
         f'<rect x="122" y="236" width="34" height="22" rx="9" fill="#f8e1cf" stroke="#1e1e1e" stroke-width="1.2"/></g>')
b.append(arrow(196, 70, 196, 98, "#555", 3)); b.append(arrow(196, 232, 196, 262, "#555", 3))
b.append(text(204, 82, "empurra", 10.5, "#333")); b.append(text(204, 246, "puxa", 10.5, "#333"))
b.append(text(204, 258, "para baixo", 10.5, "#333"))
b.append(text(140, 284, "a faixa rosa/vermelha é a MUCOSA", 11, DRED, True, "middle"))
steps = [("1.", "Segure o animal. Olhe à luz do dia, na"), ("", "sombra (nem sol direto, nem lanterna)."),
         ("2.", "Polegar de cima empurra a pálpebra de"), ("", "cima; o olho “afunda” um pouco."),
         ("3.", "Polegar de baixo puxa a pálpebra de"), ("", "baixo para baixo: aparece a mucosa."),
         ("4.", "Olhe o MEIO da mucosa (não o canto)"), ("", "e compare com o cartão em 1–2 segundos."),
         ("5.", "Repita a cada 15 dias nas chuvas e 30"), ("", "na seca. Anote o grau de cada animal.")]
for i, (n, s_) in enumerate(steps):
    b.append(text(276, 76 + i*20, f'<tspan font-weight="bold">{n}</tspan> {s_}' if n else "     " + s_, 12, "#222"))
# cartao
cols5 = [("1", "#b9182b", "#fff", "Vermelho vivo", "Ótimo", "NÃO vermifugar"),
         ("2", "#d9475a", "#fff", "Vermelho-rosado", "Bom", "NÃO vermifugar"),
         ("3", "#ee8996", "#222", "Rosa", "Limite", "Vermifugar se jovem, prenhe, parida, magra, ou se muitos estão em 3"),
         ("4", "#f6c4ca", "#222", "Rosa-pálido", "Anemia", "VERMIFUGAR já e reforçar a comida"),
         ("5", "#fbeeee", "#222", "Branco", "Anemia grave", "VERMIFUGAR, separar, comida boa, sem correr: risco de morte")]
b.append('<rect x="16" y="306" width="648" height="292" rx="10" fill="#fff" stroke="#1e1e1e" stroke-width="2"/>')
b.append(text(340, 328, "Cartão de cores (FAMACHA) — cor da mucosa e o que fazer", 13.5, "#222", True, "middle"))
for i, (n, c, tc, nome, cond, acao) in enumerate(cols5):
    y = 340 + i*50
    b.append(f'<rect x="28" y="{y}" width="120" height="44" rx="6" fill="{c}" stroke="#1e1e1e" stroke-width="1.5"/>')
    b.append(text(88, y+29, n, 20, tc, True, "middle"))
    b.append(text(160, y+18, nome, 12, "#222", True)); b.append(text(160, y+35, cond, 11.5, DRED if i >= 3 else ("#c06000" if i == 2 else GREEN), True))
    words = acao.split(" "); l1 = ""; l2 = ""
    for w in words:
        if len(l1 + " " + w) <= 40 and not l2: l1 = (l1 + " " + w).strip()
        else: l2 = (l2 + " " + w).strip()
    b.append(text(300, y+18 if l2 else y+27, l1, 12, "#222", i >= 3))
    if l2: b.append(text(300, y+35, l2, 12, "#222", i >= 3))
b.append(text(340, 616, "Cores impressas ou na tela variam: use como guia; o cartão oficial é mais confiável.", 11.2, "#444", False, "middle"))
b.append(text(340, 632, "Só detecta o verme que suga sangue (Haemonchus). Diarreia, magreza e papo inchado também pedem vermífugo.", 11.2, "#444", False, "middle"))
open(D + "cabra-famacha.svg", "w").write(svg(680, 644, "FAMACHA: a cor do olho diz quem precisa de vermífugo", "\n".join(b)))

# =====================================================================
# 3) MATERNIDADE SUINA (vista de cima + corte do protetor)
# =====================================================================
PIG = "#f0b3aa"
def num(x, y, n, col="#1f3f6e"):
    return f'<circle cx="{x}" cy="{y}" r="10" fill="{col}" stroke="#fff" stroke-width="1.5"/>' + text(x, y+4.5, str(n), 12, "#fff", True, "middle")
def piglet(x, y, rot=0, s=1.0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})">'
            f'<ellipse cx="0" cy="0" rx="10" ry="5.5" fill="{PIG}" stroke="{OUT}" stroke-width="1.2"/>'
            f'<ellipse cx="11" cy="0" rx="3" ry="3.2" fill="#e89a90" stroke="{OUT}" stroke-width="1"/></g>')
b = []
X1, Y1, X2, Y2 = 40, 74, 376, 350
b.append(f'<rect x="{X1}" y="{Y1}" width="{X2-X1}" height="{Y2-Y1}" fill="#d9d6cf"/>')
# paredes
for (x, y, w, h) in ((X1-8, Y1-8, X2-X1+16, 8), (X1-8, Y1, 8, Y2-Y1), (X2, Y1, 8, Y2-Y1)):
    b.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#6b6b6b" stroke="{OUT}" stroke-width="1"/>')
b.append(f'<rect x="{X1-8}" y="{Y2}" width="{250-X1+8}" height="8" fill="#6b6b6b" stroke="{OUT}" stroke-width="1"/>')
b.append(f'<rect x="330" y="{Y2}" width="{X2+8-330}" height="8" fill="#6b6b6b" stroke="{OUT}" stroke-width="1"/>')
b.append(f'<path d="M250 {Y2+4} L320 {Y2+40}" stroke="{WOOD}" stroke-width="5"/>')
b.append(f'<path d="M250 {Y2+4} A72 72 0 0 0 321 {Y2+0}" fill="none" stroke="#999" stroke-dasharray="4 3"/>')
# canaleta
b.append(f'<rect x="{X1-8}" y="{Y2+46}" width="{X2-X1+16}" height="12" fill="#9fb4c8" stroke="{OUT}" stroke-width="1"/>')
b.append(arrow(262, 250, 262, 342, "#3f6d9e", 2))
b.append(text(270, 300, "caimento", 10, "#1f3f6e", True)); b.append(text(270, 312, "3–5%", 10, "#1f3f6e", True))
# protetor (cano)
b.append(f'<path d="M{X1+2} {Y1+28} L{X2-40} {Y1+28}" stroke="#4d4d4d" stroke-width="6"/>')
b.append(f'<path d="M{X1+28} {Y1+28} L{X1+28} 262" stroke="#4d4d4d" stroke-width="6"/>')
b.append(f'<path d="M{X2-28} 196 L{X2-28} 300" stroke="#4d4d4d" stroke-width="6"/>')
for (x, y) in ((X1+28, Y1+28), (X2-40, Y1+28), (150, Y1+28), (260, Y1+28), (X1+28, 180), (X2-28, 200), (X2-28, 296)):
    b.append(f'<circle cx="{x}" cy="{y}" r="4" fill="#222"/>')
b.append(piglet(110, Y1+14, 0, 0.9))
# porca deitada de lado
b.append(f'<ellipse cx="205" cy="150" rx="108" ry="38" fill="{PIG}" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<path d="M110 150 Q205 192 300 150" fill="none" stroke="#c98a80" stroke-width="1.5"/>')
for tx in range(140, 290, 18):
    b.append(f'<circle cx="{tx}" cy="176" r="2.4" fill="#c0605a"/>')
b.append(f'<ellipse cx="322" cy="146" rx="24" ry="22" fill="{PIG}" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<polygon points="308,128 300,112 322,124" fill="#e89a90" stroke="{OUT}" stroke-width="1.4"/>')
b.append(f'<ellipse cx="346" cy="148" rx="6" ry="9" fill="#e89a90" stroke="{OUT}" stroke-width="1.4"/>')
b.append(f'<circle cx="330" cy="138" r="2" fill="{OUT}"/>')
b.append(f'<path d="M97 150 q-12 -4 -10 -14" fill="none" stroke="{OUT}" stroke-width="2"/>')
for i, px in enumerate(range(148, 290, 22)):
    b.append(piglet(px, 196, -90 + (i % 2) * 14, 0.95))
# comedouro e bebedouro
b.append(f'<rect x="{X2-30}" y="{Y1+40}" width="26" height="40" rx="4" fill="#bdbdbd" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<circle cx="{X2-10}" cy="{Y1+104}" r="5" fill="{BLUE}" stroke="{OUT}" stroke-width="1.2"/>')
# escamoteador
EX1, EY1, EX2, EY2 = X1, 266, 190, Y2
b.append(f'<rect x="{EX1}" y="{EY1}" width="{EX2-EX1}" height="{EY2-EY1}" fill="#c9a26b" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<rect x="{EX1+6}" y="{EY1+6}" width="{EX2-EX1-12}" height="{EY2-EY1-12}" fill="#f1dfa6" stroke="{OUT}" stroke-width="1"/>')
b.append(f'<rect x="150" y="{EY1-2}" width="30" height="8" fill="#f1dfa6"/>')
b.append(f'<circle cx="100" cy="310" r="30" fill="#ffd21f" fill-opacity="0.35"/>')
b.append(f'<circle cx="100" cy="310" r="9" fill="#ffd21f" stroke="{OUT}" stroke-width="1.5"/>')
for (x, y, r) in ((74, 294, 20), (80, 330, -10), (126, 300, 70), (128, 330, 160), (66, 314, 100)):
    b.append(piglet(x, y, r, 0.85))
# cotas
b.append(dim_h(X1-8, X2+8, 54)); b.append(text((X1+X2)/2, 48, "2,4 m", 11.5, DRED, True, "middle"))
b.append(dim_v(394, Y1-8, Y2+8)); b.append(text(400, 216, "2,0 m", 11.5, DRED, True))
# numeros
for (x, y, n) in ((200, Y1+28, 1), (90, 282, 2), (165, 252, 3), (X2-17, Y1+60, 4), (X2-30, Y1+104, 5), (290, Y2+28, 6), (60, Y2+52, 7)):
    b.append(num(x, y, n))
# corte do protetor (direita)
CX0 = 452
b.append(text(560, 72, "Corte do protetor", 13, "#222", True, "middle"))
b.append(f'<rect x="{CX0}" y="86" width="14" height="190" fill="#6b6b6b" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<rect x="{CX0}" y="276" width="216" height="12" fill="#bcb6aa" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<path d="M{CX0+14} 214 L{CX0+46} 214 L{CX0+46} 222" fill="none" stroke="#4d4d4d" stroke-width="4"/>')
b.append(f'<circle cx="{CX0+46}" cy="226" r="7" fill="#4d4d4d" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<path d="M{CX0+66} 276 Q{CX0+50} 196 {CX0+120} 172 Q{CX0+200} 160 {CX0+214} 210 L{CX0+214} 276 Z" fill="{PIG}" stroke="{OUT}" stroke-width="2"/>')
b.append(text(CX0+140, 236, "porca", 12, "#7a3a30", True, "middle"))
b.append(piglet(CX0+34, 268, -90, 0.9))
b.append(f'<line x1="{CX0+46}" y1="226" x2="{CX0+46}" y2="276" stroke="{DRED}" stroke-width="1.6" stroke-dasharray="3 2"/>')
b.append(text(CX0+53, 262, "B", 13, DRED, True))
b.append(dim_h(CX0+14, CX0+46, 200)); b.append(text(CX0+30, 194, "A", 13, DRED, True, "middle"))
b.append(text(CX0+82, 120, "A (da parede) e", 11.5, DRED, True)); b.append(text(CX0+82, 134, "B (do chão):", 11.5, DRED, True))
b.append(text(CX0+82, 148, "20–25 cm", 11.5, DRED, True))
b.append(text(CX0, 306, "Ao deitar, a porca encosta", 11, "#222", True))
b.append(text(CX0, 320, "no cano e não esmaga o", 11, "#222", True))
b.append(text(CX0, 334, "leitão que está junto à", 11, "#222", True))
b.append(text(CX0, 348, "parede: ele foge por baixo.", 11, "#222", True))
# legenda
leg = [(1, "Protetor: cano ou caibro forte, a 20–25 cm do chão e da parede"),
       (2, "Escamoteador: caixa só para leitões, com lâmpada; 30–32 °C na 1ª semana"),
       (3, "Entrada dos leitões (15–20 cm): a porca não passa"),
       (4, "Comedouro da porca"), (5, "Água: chupeta ou cocho sempre cheio"),
       (6, "Porta"), (7, "Canaleta: piso com caimento de 3–5% leva urina e esterco")]
b.append(box(16, 420, 648, 160, "#f6f9ff", "#3f6d9e"))
for i, (n, s_) in enumerate(leg):
    b.append(num(34, 440 + i*20, n)); b.append(text(52, 444 + i*20, s_, 11.6, "#222"))
b.append(text(340, 600, "Porca: 18–22 °C é o ideal (ela sofre com calor). Leitão: precisa de 30–34 °C nos primeiros dias.", 11.4, "#222", True, "middle"))
open(D + "suino-maternidade.svg", "w").write(svg(680, 612, "Baia de maternidade da porca (vista de cima)", "\n".join(b)))

# =====================================================================
# 4) GAIOLA DE COELHO (vista de frente)
# =====================================================================
def rabbit(x, y, s=1.0, col="#f4f1ea"):
    """coelho sentado de perfil, olhando para a direita; (x,y) = chao sob o corpo"""
    g = [f'<ellipse cx="-30" cy="-16" rx="7" ry="7" fill="#fff" stroke="{OUT}" stroke-width="1.4"/>',
         f'<ellipse cx="-4" cy="-20" rx="30" ry="20" fill="{col}" stroke="{OUT}" stroke-width="1.8"/>',
         f'<ellipse cx="-18" cy="-12" rx="14" ry="12" fill="{col}" stroke="{OUT}" stroke-width="1.4"/>',
         f'<ellipse cx="6" cy="-58" rx="5.5" ry="18" fill="{col}" stroke="{OUT}" stroke-width="1.6" transform="rotate(-18 6 -58)"/>',
         f'<ellipse cx="16" cy="-56" rx="5.5" ry="18" fill="{col}" stroke="{OUT}" stroke-width="1.6" transform="rotate(-6 16 -56)"/>',
         f'<ellipse cx="17" cy="-36" rx="14" ry="12" fill="{col}" stroke="{OUT}" stroke-width="1.8"/>',
         f'<circle cx="21" cy="-38" r="2.4" fill="#c0181b"/>',
         f'<circle cx="30" cy="-33" r="2" fill="#e89a90"/>',
         f'<ellipse cx="14" cy="-2" rx="9" ry="3" fill="{col}" stroke="{OUT}" stroke-width="1.3"/>']
    return f'<g transform="translate({x},{y}) scale({s})">' + "".join(g) + '</g>'

b = []
K = 3.6                         # px por cm
GX1, GY1 = 40, 110              # canto superior esquerdo da gaiola
GW, GH = 80*K, 45*K             # 288 x 162
GX2, GY2 = GX1 + GW, GY1 + GH
NW, NH = 30*K, 25*K             # ninho externo (frente) 108 x 90
FLOOR = 470
# pes
for x in (GX1+6, GX2-6, GX2+NW-6):
    b.append(f'<rect x="{x-4}" y="{GY2}" width="8" height="{FLOOR-GY2}" fill="#9a9a9a" stroke="{OUT}" stroke-width="1"/>')
# minhocario
b.append(f'<rect x="{GX1-10}" y="{FLOOR-56}" width="{GW+NW+20}" height="56" fill="{WOOD}" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<rect x="{GX1-4}" y="{FLOOR-50}" width="{GW+NW+8}" height="44" fill="#5a4630"/>')
for i in range(9):
    x = GX1 + 18 + i*44
    b.append(f'<path d="M{x} {FLOOR-34} q6 -7 12 0 q6 7 12 0" fill="none" stroke="#e8a0a0" stroke-width="3" stroke-linecap="round"/>')
for i in range(14):
    x = GX1 + 20 + i*27
    b.append(f'<circle cx="{x}" cy="{FLOOR-46 + (i%3)*2}" r="2.4" fill="#2a1d10"/>')
for i in range(4):
    x = GX1 + 50 + i*70
    b.append(f'<line x1="{x}" y1="{GY2+44}" x2="{x}" y2="{FLOOR-64}" stroke="#7a5a30" stroke-width="1.5" stroke-dasharray="2 8"/>')
# gaiola: fundo de tela
b.append(f'<rect x="{GX1}" y="{GY1}" width="{GW}" height="{GH}" fill="url(#telac)" stroke="{OUT}" stroke-width="2.5"/>')
# ninho externo
b.append(f'<rect x="{GX2}" y="{GY2-NH}" width="{NW}" height="{NH}" fill="#c9a26b" stroke="{OUT}" stroke-width="2.5"/>')
b.append(f'<rect x="{GX2+6}" y="{GY2-NH+6}" width="{NW-12}" height="{NH-6}" fill="#f1dfa6"/>')
b.append(f'<rect x="{GX2-3}" y="{GY2-15*K}" width="6" height="{15*K-10*K}" fill="#f1dfa6" stroke="{OUT}" stroke-width="1" stroke-dasharray="3 2"/>')
b.append(f'<path d="M{GX2+10} {GY2-4} q20 -26 44 -10 q20 10 40 -4 L{GX2+NW-6} {GY2} L{GX2+6} {GY2} Z" fill="#e3c98a" stroke="#a0824a"/>')
for (x, y) in ((GX2+40, GY2-10), (GX2+58, GY2-12), (GX2+74, GY2-8)):
    b.append(f'<ellipse cx="{x}" cy="{y}" rx="8" ry="4.5" fill="#f2c9c0" stroke="{OUT}" stroke-width="1"/>')
# piso: tela + tabua de descanso
b.append(f'<line x1="{GX1}" y1="{GY2}" x2="{GX2}" y2="{GY2}" stroke="#444" stroke-width="5" stroke-dasharray="3 3"/>')
b.append(f'<rect x="{GX1+40}" y="{GY2-6}" width="110" height="6" fill="{WOOD}" stroke="{OUT}" stroke-width="1"/>')
# coelho
b.append(rabbit(GX1+100, GY2-6, 1.25))
# comedouro (na porta) e bebedouro
b.append(f'<path d="M{GX1+210} {GY2-70} L{GX1+250} {GY2-70} L{GX1+246} {GY2-18} L{GX1+226} {GY2-4} L{GX1+210} {GY2-4} Z" fill="#bdbdbd" stroke="{OUT}" stroke-width="1.8"/>')
b.append(f'<rect x="{GX1+18}" y="{GY1+10}" width="22" height="46" rx="5" fill="#cfe6fb" stroke="{OUT}" stroke-width="1.6"/>')
b.append(f'<line x1="{GX1+29}" y1="{GY1+56}" x2="{GX1+29}" y2="{GY1+70}" stroke="#555" stroke-width="4"/>')
# porta
b.append(f'<rect x="{GX1+170}" y="{GY1+6}" width="110" height="{GH-14}" fill="none" stroke="#1f5fa8" stroke-width="2" stroke-dasharray="7 4"/>')
# cotas
b.append(dim_h(GX1, GX2, GY1-14)); b.append(text(GX1+GW/2, GY1-20, "80 cm de largura (60 cm de fundo)", 11.5, DRED, True, "middle"))
b.append(dim_h(GX2, GX2+NW, GY2-NH-14)); b.append(text(GX2+NW/2, GY2-NH-20, "30 cm", 11, DRED, True, "middle"))
b.append(dim_v(GX1-14, GY1, GY2)); b.append(text(GX1-18, GY1+GH/2, "45", 11, DRED, True, "end")); b.append(text(GX1-18, GY1+GH/2+13, "cm", 11, DRED, True, "end"))
b.append(dim_v(GX2+NW+14, GY2, FLOOR-56)); b.append(text(GX2+NW+20, GY2+40, "70–90 cm", 11, DRED, True))
b.append(text(GX2+NW+20, GY2+54, "do chão", 11, DRED, True))
# rotulos
X0 = 456
lab = [(GY1+4, ["Bebedouro: chupeta com", "garrafa, ou pote pesado"]),
       (GY1+52, ["Porta na frente (tracejado)"]),
       (GY1+82, ["Comedouro de chapa na", "porta: enche por fora"]),
       (GY2-NH-46, ["Ninho 40 × 30 × 25 cm,", "entrada de 15 cm, borda", "de 10 cm; entra no dia 26–28"]),
       ]
b.append(text(X0, GY1-2, "Bebedouro: chupeta com", 11.3, "#222", True)); b.append(text(X0, GY1+12, "garrafa, ou pote pesado", 11.3, "#222"))
b.append(lead(X0-4, GY1-6, GX1+40, GY1+20))
b.append(text(X0, GY1+34, "Comedouro de chapa na", 11.3, "#222", True)); b.append(text(X0, GY1+48, "porta: abastece por fora", 11.3, "#222"))
b.append(lead(X0-4, GY1+30, GX1+250, GY2-60))
b.append(text(X0, GY1+70, "Ninho 40 × 30 × 25 cm", 11.3, "#222", True)); b.append(text(X0, GY1+84, "(comprimento × largura ×", 11.3, "#222"))
b.append(text(X0, GY1+98, "altura), passagem de 15 cm,", 11.3, "#222")); b.append(text(X0, GY1+112, "borda de 10 cm; coloque", 11.3, "#222"))
b.append(text(X0, GY1+126, "no dia 26–28 da gestação", 11.3, "#222"))
b.append(lead(X0-4, GY1+66, GX2+NW-20, GY2-NH+10))
b.append(text(GX1+40, GY2+18, "tábua de descanso sobre a tela", 10.5, "#5a4630", True))
b.append(text(GX1+40, GY2+30, "(evita ferida nas patas)", 10.5, "#5a4630"))
b.append(text(GX1+(GW+NW)/2, FLOOR-11, "minhocário ou esterqueira: o esterco cai pela tela e vira adubo", 11, "#fff", True, "middle"))
b.append(box(16, 484, 648, 94, "#eef7ee", GREEN))
b += [text(30, 504, "Matriz: 80 × 60 × 45 cm · Macho: 60 × 60 × 45 cm · Engorda: 80 × 60 cm para 6–8 coelhos.", 11.8),
      text(30, 522, "Piso de tela galvanizada de malha 1,3 × 2,5 cm, arame grosso (fio 14). Laterais: malha 2,5 × 5 cm.", 11.8),
      text(30, 540, "Galpão com sombra, ventilado, protegido de chuva, ratos, cães e cobras. Ideal: 15–21 °C;", 11.8),
      text(30, 558, "acima de 30 °C o coelho sofre e pode morrer.", 11.8, DRED, True)]
DEFS = ('<defs><pattern id="telac" width="9" height="9" patternUnits="userSpaceOnUse">'
        '<rect width="9" height="9" fill="#fbfbf7"/><path d="M0 0 L9 0 M0 0 L0 9" stroke="#9a9a9a" stroke-width="0.8"/></pattern></defs>')
open(D + "coelho-gaiola.svg", "w").write(svg(680, 590, "Gaiola de coelha com ninho (vista de frente)", DEFS + "\n".join(b)))
