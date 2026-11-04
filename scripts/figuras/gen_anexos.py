import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "anexos", "img") + "/"
os.makedirs(D, exist_ok=True)
WOOD = "#8b5a2b"; AGUA = "#4a90d9"; AGUA2 = "#cfe6fb"; SOLO = "#e8d3b0"; VERDE = "#2b8a3e"; PERIGO = "#d62828"

def darrow(x1, y1, x2, y2, color="#1e1e1e", w=2.5):
    """seta de cota com ponta nos dois lados"""
    return arrow(x1, y1, x2, y2, color, w) + arrow(x2, y2, x1, y1, color, w)

def dash(x1, y1, x2, y2, color="#888"):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.5" stroke-dasharray="5 4"/>'

def rect(x, y, w, h, fill, stroke="#1e1e1e", sw=2, rx=0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

# =====================================================================
# 1. MEDIDAS COM O CORPO
# =====================================================================
b = []
b.append('<line x1="345" y1="48" x2="345" y2="420" stroke="#ccc" stroke-width="2"/>')
b.append('<line x1="10" y1="432" x2="670" y2="432" stroke="#ccc" stroke-width="2"/>')
# --- figura de braços abertos (braça) ---
b.append(text(170, 62, "Braça (braços abertos)", 15, "#222", True, "middle"))
cx = 170
b.append(limb([(cx-10, 250), (cx-22, 372)], 20, SKIN))
b.append(limb([(cx+10, 250), (cx+22, 372)], 20, SKIN))
b.append(limb([(cx-20, 156), (44, 156)], 15, SKIN))
b.append(limb([(cx+20, 156), (296, 156)], 15, SKIN))
b.append(limb([(cx, 160), (cx, 248)], 46, SKIN))
b.append(head(cx, 122, 20, SKIN))
b.append(hand(36, 156, 9)); b.append(hand(304, 156, 9))
# cota da braça
b.append(dash(27, 146, 27, 92)); b.append(dash(313, 146, 313, 92))
b.append(darrow(29, 92, 311, 92))
b.append(text(170, 84, "ponta a ponta dos dedos", 12, "#222", False, "middle"))
# cota da altura
b.append(dash(196, 102, 330, 102)); b.append(dash(196, 380, 330, 380))
b.append(darrow(326, 104, 326, 378))
b.append(f'<text x="318" y="250" font-size="12" fill="#222" text-anchor="middle" transform="rotate(-90 318 250)">sua altura</text>')
b.append(f'<rect x="20" y="380" width="300" height="6" fill="{SOLO}"/>')
b += [text(170, 404, "Braça do corpo ≈ sua altura (1,6–1,8 m)", 12.5, "#222", True, "middle"),
      text(170, 422, "Braça ANTIGA de medir terra = 2,2 m", 12.5, "#b3001b", True, "middle")]
# --- mão aberta (palmo) ---
b.append(text(510, 62, "Palmo (mão bem aberta)", 15, "#222", True, "middle"))
hx, hy = 508, 178
fing = [((hx-28, hy+6), (418, hy-30), 20),     # polegar
        ((hx-18, hy-28), (hx-34, hy-94), 18),   # indicador
        ((hx, hy-30), (hx+2, hy-104), 18),      # medio
        ((hx+18, hy-28), (hx+34, hy-92), 18),   # anelar
        ((hx+30, hy-14), (596, hy-62), 16)]     # minimo
for p0, p1, w in fing:
    b.append(limb([p0, p1], w, SKIN))
b.append(f'<rect x="{hx-40}" y="{hy-36}" width="80" height="92" rx="24" fill="{SKIN}" stroke="{OUT}" stroke-width="2.5"/>')
b.append(f'<rect x="{hx-37}" y="{hy-33}" width="74" height="86" rx="22" fill="{SKIN}"/>')
# cota do palmo (abaixo da mão)
b.append(dash(412, hy-38, 412, 262)); b.append(dash(602, hy-66, 602, 262))
b.append(darrow(414, 262, 600, 262, "#b3001b"))
b.append(text(507, 254, "≈ 20–22 cm (adulto)", 13, "#b3001b", True, "middle"))
b.append(text(507, 282, "da ponta do polegar à ponta do mindinho", 12, "#222", False, "middle"))
# --- polegar (polegada) ---
tx, ty = 392, 318
b.append(f'<rect x="{tx}" y="{ty}" width="34" height="84" rx="17" fill="{SKIN}" stroke="{OUT}" stroke-width="2.5"/>')
b.append(f'<rect x="{tx+6}" y="{ty+7}" width="22" height="24" rx="8" fill="#fbe3d1" stroke="{OUT}" stroke-width="1.5"/>')
b.append(darrow(tx-2, ty+42, tx+36, ty+42, "#b3001b", 2))
b += [text(446, 330, "Polegada = largura do polegar", 12.5, "#222", True),
      text(446, 346, "na base da unha ≈ 2–2,5 cm", 12.5),
      text(446, 362, "(a polegada oficial = 2,54 cm)", 12),
      text(446, 386, "Dedo (largura do indicador)", 12.5, "#222", True),
      text(446, 402, "≈ 1,5–2 cm", 12.5)]
# --- passos (pegadas vistas de cima) ---
b.append(text(14, 456, "Passo (pegadas vistas de cima, andando →)", 14, "#222", True))
def pe(x, y, lado):
    # x = calcanhar; pegada horizontal de ~52 px
    s = f'<ellipse cx="{x+24}" cy="{y}" rx="26" ry="11" fill="#c9a26b" stroke="{OUT}" stroke-width="2"/>'
    dy = -1 if lado == "E" else 1
    for i, (ox, oy) in enumerate([(54, -6), (56, 0), (55, 6), (52, 11), (48, 15)]):
        s += f'<circle cx="{x+ox}" cy="{y+oy*dy*0.9:.1f}" r="{3.6-i*0.4:.1f}" fill="#c9a26b" stroke="{OUT}" stroke-width="1.2"/>'
    return s
P = [(40, 486, "E"), (175, 512, "D"), (310, 486, "E")]
for x, y, l in P:
    b.append(pe(x, y, l))
b += [text(64, 472, "pé esq.", 11, "#444", False, "middle"), text(199, 539, "pé dir.", 11, "#444", False, "middle"), text(334, 472, "pé esq.", 11, "#444", False, "middle")]
b.append(dash(40, 494, 40, 588)); b.append(dash(175, 524, 175, 560)); b.append(dash(310, 494, 310, 588))
b.append(darrow(42, 556, 173, 556, "#1e1e1e", 2))
b.append(text(108, 550, "passo ≈ 0,75 m", 12, "#222", True, "middle"))
b.append(darrow(42, 584, 308, 584, "#b3001b", 2))
b.append(text(175, 600, "passo duplo ≈ 1,5 m (conte só o pé esquerdo)", 12, "#b3001b", True, "middle"))
# --- caixa de calibragem ---
b.append(box(400, 446, 270, 160, "#eef5ff", "#3f6d9e"))
b += [text(414, 468, "MEÇA AS SUAS E ANOTE:", 13, "#1e3a5f", True),
      text(414, 492, "palmo: ........ cm", 13), text(414, 514, "polegar: ........ cm", 13),
      text(414, 536, "passo duplo: ........ m", 13), text(414, 558, "braça: ........ m", 13),
      text(414, 580, "Use trena, régua, cartão de", 11.5, "#444"),
      text(414, 595, "banco (8,56 cm) ou folha A4 (29,7 cm)", 11.5, "#444")]
open(D + "medidas-corpo.svg", "w").write(svg(680, 614, "Medidas com o corpo (calibre as suas)", "\n".join(b)))

# =====================================================================
# 2. MEDIDAS DE COZINHA
# =====================================================================
b = []
COLX = [130, 238, 346, 454, 562]; CW = 108
def colher(cx, cy, r):
    L = r * 3.2
    return (f'<line x1="{cx+r*0.6:.1f}" y1="{cy}" x2="{cx+r+L:.1f}" y2="{cy-r*0.9:.1f}" stroke="{OUT}" stroke-width="{max(3, r*0.45):.1f}" stroke-linecap="round"/>'
            f'<line x1="{cx+r*0.6:.1f}" y1="{cy}" x2="{cx+r+L:.1f}" y2="{cy-r*0.9:.1f}" stroke="#c8ccd2" stroke-width="{max(1.2, r*0.45-2.5):.1f}" stroke-linecap="round"/>'
            f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r*0.68:.1f}" fill="#c8ccd2" stroke="{OUT}" stroke-width="2"/>'
            f'<ellipse cx="{cx}" cy="{cy+1}" rx="{r*0.7:.1f}" ry="{r*0.42:.1f}" fill="{AGUA2}"/>')
def xicara(cx, by):
    s = f'<ellipse cx="{cx}" cy="{by+4}" rx="40" ry="7" fill="#e8e8e8" stroke="{OUT}" stroke-width="2"/>'
    s += f'<path d="M{cx+24} {by-48} q22 4 18 18 q-3 12 -22 14" fill="none" stroke="{OUT}" stroke-width="5"/>'
    s += f'<path d="M{cx-30} {by-56} L{cx+30} {by-56} Q{cx+28} {by-4} {cx} {by-2} Q{cx-28} {by-4} {cx-30} {by-56} Z" fill="#fff" stroke="{OUT}" stroke-width="2.5"/>'
    s += f'<path d="M{cx-27} {by-46} L{cx+27} {by-46} Q{cx+24} {by-7} {cx} {by-5} Q{cx-24} {by-7} {cx-27} {by-46} Z" fill="{AGUA2}"/>'
    return s
def copo(cx, by):
    s = f'<path d="M{cx-26} {by-66} L{cx+26} {by-66} L{cx+19} {by} L{cx-19} {by} Z" fill="#eef6fc" stroke="{OUT}" stroke-width="2.5"/>'
    s += f'<path d="M{cx-24} {by-52} L{cx+24} {by-52} L{cx+18} {by-2} L{cx-18} {by-2} Z" fill="{AGUA2}"/>'
    for f in (-12, 0, 12):
        s += f'<line x1="{cx+f*1.05:.1f}" y1="{by-46}" x2="{cx+f*0.75:.1f}" y2="{by-3}" stroke="#7aa6cf" stroke-width="1.5"/>'
    s += f'<line x1="{cx-25}" y1="{by-54}" x2="{cx+25}" y2="{by-54}" stroke="{OUT}" stroke-width="1.5"/>'
    return s
icons = [colher(COLX[0]+34, 110, 9), colher(COLX[1]+32, 110, 12), colher(COLX[2]+30, 110, 15),
         xicara(COLX[3]+54, 128), copo(COLX[4]+54, 128)]
nomes = [("colher", "de chá"), ("colher de", "sobremesa"), ("colher", "de sopa"), ("xícara", "(de receita)"), ("copo", "americano")]
mls = ["5 mL", "10 mL", "15 mL", "240 mL", "190 mL"]
for i, x in enumerate(COLX):
    b.append(icons[i])
    b.append(text(x+CW/2, 150, nomes[i][0], 12, "#222", True, "middle"))
    b.append(text(x+CW/2, 164, nomes[i][1], 12, "#222", True, "middle"))
    b.append(text(x+CW/2, 188, mls[i], 17, AGUA if i < 5 else "#222", True, "middle"))
b.append(text(12, 188, "Volume:", 14, "#222", True))
rows = [("Água", ["5 g", "10 g", "15 g", "240 g", "190 g"]),
        ("Sal refinado", ["5–6 g", "10–12 g", "15–18 g", "≈ 290 g", "≈ 230 g"]),
        ("Açúcar refinado", ["4 g", "8 g", "12 g", "≈ 180 g", "≈ 145 g"]),
        ("Farinha de trigo", ["3 g", "5 g", "7–8 g", "≈ 120 g", "≈ 95 g"]),
        ("Arroz ou feijão cru", ["4 g", "8 g", "12 g", "≈ 185 g", "≈ 150 g"]),
        ("Óleo", ["4,5 g", "9 g", "13–14 g", "≈ 220 g", "≈ 175 g"]),
        ("Mel", ["7 g", "14 g", "21 g", "≈ 340 g", "≈ 270 g"])]
y0 = 212; RH = 30
b.append(text(12, y0, "Peso (gramas), medida rasa:", 12, "#555", True))
for j, (nome, vals) in enumerate(rows):
    y = y0 + 8 + RH * j + 6
    fill = "#f3f3f3" if j % 2 == 0 else "#fff"
    b.append(f'<rect x="10" y="{y}" width="660" height="{RH}" fill="{fill}" stroke="#ddd"/>')
    b.append(text(16, y+20, nome, 12.5, "#222", True))
    for i, v in enumerate(vals):
        b.append(text(COLX[i]+CW/2, y+20, v, 13, "#222", False, "middle"))
yb = y0 + 14 + RH * len(rows) + 12
b.append(box(10, yb, 660, 92, "#fff4e5", "#ef8a2b"))
b += [text(22, yb+22, "Medidas RASAS: encha e passe as costas de uma faca por cima. Colher CHEIA ≈ 1,5 a 2 rasas.", 12),
      text(22, yb+42, "1 xícara = 16 colheres de sopa = 48 colheres de chá.  Farinha: solta, sem apertar na xícara.", 12),
      text(22, yb+62, "A xícara de beber da sua casa pode ter 150 a 200 mL e as colheres variam: meça as suas", 12, "#b3001b", True),
      text(22, yb+80, "uma vez com água numa seringa ou mamadeira graduada e anote.", 12, "#b3001b", True)]
open(D + "medidas-cozinha.svg", "w").write(svg(680, yb + 102, "Medidas de cozinha: volume e peso", "\n".join(b)))

# =====================================================================
# 3. CALENDARIO ANUAL DE MANUTENCAO
# =====================================================================
CAT = {"A": ("#4a90d9", "Água"), "N": ("#8b5a2b", "Animais"), "H": ("#2b8a3e", "Horta/roça"),
       "C": ("#6c757d", "Casa/fogo"), "E": ("#f2b705", "Energia"), "S": ("#d62828", "Estoque/saúde")}
MESES = [
 ("JANEIRO", "chuva", [("C", "Calhas e telhado", "após temporais"), ("N", "Bicheira, mosca", "e carrapato"), ("H", "Capina e", "cobertura morta"), ("S", "Água parada:", "ronda semanal")]),
 ("FEVEREIRO", "chuva", [("H", "Colher feijão;", "plantar o da seca"), ("C", "Valetas e", "drenagem"), ("S", "Ratos e enchente:", "leptospirose"), ("S", "Grãos: conferir", "umidade e caruncho")]),
 ("MARÇO", "chuva", [("A", "Encher cisternas", "e caixas"), ("N", "Fazer silagem e", "feno para a seca"), ("H", "Semear horta de", "outono-inverno")]),
 ("ABRIL", "seca", [("N", "Vacina leptospirose", "(1ª do ano)"), ("A", "Cisterna: tampa,", "tela e ladrão"), ("H", "Secar e guardar", "sementes"), ("C", "Cortar e empilhar", "lenha (seca 6 meses)")]),
 ("MAIO", "seca", [("N", "Vermífugo bovinos", "(1ª dose: 5-7-9)"), ("N", "Vacinas anuais", "do rebanho"), ("C", "Fazer aceiros", "(contra fogo)"), ("E", "Painel: ângulo", "e limpeza")]),
 ("JUNHO", "seca", [("N", "Frio: abrigar", "filhotes do vento"), ("H", "Geada (Sul):", "cobrir mudas"), ("C", "Chaminé e", "fogão a lenha"), ("S", "Inventário de", "comida e remédios")]),
 ("JULHO", "seca", [("N", "Vermífugo bovinos", "(2ª dose)"), ("H", "Poda de", "frutíferas"), ("C", "Cercas, currais", "e porteiras"), ("C", "Limpar mato em", "volta da casa")]),
 ("AGOSTO", "seca", [("C", "Fogo e vento:", "aceiros prontos"), ("C", "Consertar telhado", "e calhas"), ("H", "Calagem e teste", "de germinação"), ("E", "Painéis: tirar", "a poeira")]),
 ("SETEMBRO", "seca", [("N", "Vermífugo bovinos", "(3ª dose)"), ("A", "Lavar e desinfetar", "a cisterna vazia"), ("N", "Carrapato: início", "do controle"), ("C", "Podar galhos", "sobre a casa")]),
 ("OUTUBRO", "chuva", [("A", "Desviar a 1ª água", "do telhado"), ("H", "Plantar milho,", "feijão, mandioca"), ("N", "Vacina lepto (2ª)", "e dos cavalos"), ("C", "Revoada de", "cupins: vistoriar")]),
 ("NOVEMBRO", "chuva", [("S", "Dengue: ronda", "toda semana"), ("H", "Capina e adubo", "de cobertura"), ("N", "Umbigo de bezerro:", "iodo 10%"), ("E", "Aterramento e", "para-raios")]),
 ("DEZEMBRO", "chuva", [("S", "Inventário de", "comida e remédios"), ("C", "Telhado após", "temporais"), ("S", "Documentos e este", "manual: atualizar"), ("N", "Bicheira e", "carrapato")]),
]
b = []
b.append(text(340, 54, "Modelo para o Centro-Sul (chuvas de outubro a março). Ajuste para a sua região.", 12.5, "#444", False, "middle"))
CWm, CHm, GX, GY = 160, 168, 6, 8
x0, y0 = 10, 66
for k, (mes, est, tarefas) in enumerate(MESES):
    c, r = k % 4, k // 4
    x = x0 + c * (CWm + GX); y = y0 + r * (CHm + GY)
    hdr = "#cfe6fb" if est == "chuva" else "#f1e2c4"
    b.append(f'<rect x="{x}" y="{y}" width="{CWm}" height="{CHm}" rx="6" fill="#fff" stroke="#1e1e1e" stroke-width="1.5"/>')
    b.append(f'<path d="M{x} {y+6} q0 -6 6 -6 h{CWm-12} q6 0 6 6 v20 h-{CWm} Z" fill="{hdr}" stroke="#1e1e1e" stroke-width="1.5"/>')
    b.append(text(x+8, y+18, mes, 12.5, "#1e1e1e", True))
    b.append(text(x+CWm-8, y+18, est, 11, "#1e5aa0" if est == "chuva" else "#8a5a12", True, "end"))
    for t, (cat, l1, l2) in enumerate(tarefas):
        ty = y + 46 + t * 33
        b.append(f'<rect x="{x+7}" y="{ty-10}" width="10" height="10" rx="2" fill="{CAT[cat][0]}" stroke="#1e1e1e" stroke-width="1"/>')
        b.append(text(x+22, ty, l1, 11, "#222", True))
        b.append(text(x+22, ty+13, l2, 11, "#333"))
yl = y0 + 3 * (CHm + GY) + 4
# legenda
lx = 10
for k in "ANHCES":
    col, nome = CAT[k]
    b.append(f'<rect x="{lx}" y="{yl}" width="12" height="12" rx="2" fill="{col}" stroke="#1e1e1e" stroke-width="1"/>')
    b.append(text(lx+17, yl+11, nome, 12))
    lx += 17 + len(nome) * 6.4 + 12
b.append(f'<rect x="{lx+4}" y="{yl}" width="22" height="12" fill="#cfe6fb" stroke="#1e1e1e" stroke-width="1"/>')
b.append(text(lx+30, yl+11, "chuva", 12))
b.append(f'<rect x="{lx+80}" y="{yl}" width="22" height="12" fill="#f1e2c4" stroke="#1e1e1e" stroke-width="1"/>')
b.append(text(lx+106, yl+11, "seca", 12))
yt = yl + 24
b.append(box(10, yt, 660, 78, "#eef5ff", "#3f6d9e"))
b += [text(22, yt+20, "TODO MÊS:", 12.5, "#1e3a5f", True),
      text(112, yt+20, "testar lanternas e rádio · rodar o gerador 30 min · usar e repor", 12),
      text(112, yt+37, "o estoque (o mais velho primeiro) · baterias e painéis · vela do filtro", 12),
      text(22, yt+58, "Nordeste semiárido: chuvas de fevereiro a maio. Norte: chuvas de dezembro a maio.", 12, "#b3001b", True),
      text(22, yt+73, "Sul: frio e geada de junho a agosto. Desloque as tarefas para a SUA estação.", 12, "#b3001b", True)]
open(D + "calendario-manutencao.svg", "w").write(svg(680, yt + 88, "Calendário anual de manutenção", "\n".join(b)))

# =====================================================================
# 4. BACKUP 3-2-1
# =====================================================================
def celular(x, y):
    return (rect(x, y, 38, 70, "#3a3f47", rx=6) + rect(x+4, y+8, 30, 50, "#cfe6fb", sw=1, rx=2)
            + f'<circle cx="{x+19}" cy="{y+64}" r="3" fill="#ddd"/>')
def pendrive(x, y):
    return (rect(x+8, y, 22, 16, "#c8ccd2", rx=2) + rect(x+13, y+4, 4, 5, "#555", sw=0) + rect(x+21, y+4, 4, 5, "#555", sw=0)
            + rect(x, y+15, 38, 56, "#d62828", rx=7) + text(x+19, y+50, "USB", 10, "#fff", True, "middle"))
def hd(x, y):
    return (rect(x, y, 62, 74, "#2f3640", rx=8) + f'<circle cx="{x+31}" cy="{y+33}" r="20" fill="#9aa3ad" stroke="#1e1e1e" stroke-width="1.5"/>'
            + f'<circle cx="{x+31}" cy="{y+33}" r="4" fill="#2f3640"/>' + rect(x+24, y+62, 14, 5, "#7ed957", sw=0, rx=2))
def sdcard(x, y):
    return (f'<path d="M{x} {y} h20 l10 10 v34 h-30 Z" fill="#1f4e8c" stroke="#1e1e1e" stroke-width="2"/>' + text(x+15, y+32, "SD", 10, "#fff", True, "middle"))
def papel(x, y):
    s = ""
    for i in range(3):
        s += rect(x+i*5, y-i*5, 46, 60, "#fff", sw=1.5)
    for i in range(5):
        s += f'<line x1="{x+16}" y1="{y-2+i*10}" x2="{x+52}" y2="{y-2+i*10}" stroke="#999" stroke-width="2"/>'
    return s
def casa(x, y, fill="#f1e2c4"):
    return (f'<polygon points="{x-5},{y+28} {x+32},{y} {x+69},{y+28}" fill="#a0522d" stroke="#1e1e1e" stroke-width="2"/>'
            + rect(x, y+28, 64, 54, fill) + rect(x+23, y+50, 18, 32, WOOD, sw=1.5))
b = []
PX = [10, 234, 458]; PW = 212
heads = [("3", "CÓPIAS", "dos mesmos arquivos"), ("2", "TIPOS DE MÍDIA", "diferentes"), ("1", "FORA DE CASA", "em outro lugar")]
for i, x in enumerate(PX):
    b.append(box(x, 48, PW, 260, "#fafafa", "#999"))
    b.append(f'<circle cx="{x+36}" cy="{88}" r="26" fill="{["#4a90d9", "#2b8a3e", "#ef8a2b"][i]}" stroke="#1e1e1e" stroke-width="2"/>')
    b.append(text(x+36, 99, heads[i][0], 30, "#fff", True, "middle"))
    b.append(text(x+70, 84, heads[i][1], 15, "#222", True))
    b.append(text(x+70, 102, heads[i][2], 12.5, "#444"))
# painel 1: tres aparelhos
b.append(celular(30, 140)); b.append(pendrive(96, 140)); b.append(hd(152, 138))
b += [text(49, 232, "celular", 11.5, "#222", False, "middle"), text(115, 232, "pendrive", 11.5, "#222", False, "middle"), text(183, 232, "HD externo", 11.5, "#222", False, "middle")]
b += [text(116, 262, "Se um quebrar ou sumir,", 12, "#222", False, "middle"), text(116, 278, "sobram dois.", 12, "#222", True, "middle")]
# painel 2: memoria x disco
b.append(pendrive(254, 140)); b.append(sdcard(298, 154))
b.append(text(360, 182, "≠", 34, "#2b8a3e", True, "middle"))
b.append(hd(380, 138))
b += [text(290, 232, "memória", 11.5, "#222", True, "middle"), text(290, 246, "(pendrive, cartão)", 11, "#444", False, "middle"),
      text(411, 232, "disco", 11.5, "#222", True, "middle"), text(411, 246, "(HD, notebook)", 11, "#444", False, "middle")]
b += [text(340, 270, "Um defeito ou calor que estraga", 12, "#222", False, "middle"), text(340, 286, "um tipo pode poupar o outro.", 12, "#222", False, "middle")]
# painel 3: duas casas
b.append(casa(474, 144)); b.append(casa(586, 144, "#e2ecf7"))
b.append(arrow(546, 190, 578, 190, "#ef8a2b", 4))
b += [text(506, 244, "sua casa", 11.5, "#222", True, "middle"), text(618, 244, "parente, vizinho,", 11, "#222", False, "middle"), text(618, 258, "sítio, igreja", 11, "#222", False, "middle")]
b += [text(564, 280, "Incêndio, enchente ou roubo", 12, "#222", False, "middle"), text(564, 296, "não levam tudo.", 12, "#222", True, "middle")]
# caixa metalica (gaiola de Faraday) em corte
yb = 326
b.append(text(170, yb+18, "Caixa metálica fechada (em corte)", 14, "#222", True, "middle"))
b.append(rect(30, yb+40, 280, 150, "#9aa3ad", sw=2.5, rx=4))
b.append(rect(22, yb+30, 296, 16, "#b8c0c8", sw=2.5, rx=3))
b.append(rect(42, yb+54, 256, 126, "#fff8e1", "#8a5a12", 2, 6))
b.append(f'<rect x="42" y="{yb+54}" width="256" height="126" rx="6" fill="none" stroke="#8a5a12" stroke-width="2" stroke-dasharray="7 5"/>')
b.append(celular(62, yb+80)); b.append(pendrive(118, yb+82)); b.append(sdcard(170, yb+96)); b.append(rect(214, yb+72, 64, 92, "#4b4f57", rx=6)); b.append(rect(220, yb+80, 52, 66, "#e9e6dc", sw=1, rx=2))
b.append(text(246, yb+118, "e-reader", 10, "#444", False, "middle"))
b.append(text(326, yb+42, "tampa justa + fita de alumínio na junta", 11.5, "#222"))
b.append(text(326, yb+100, "dentro: saco plástico ou papelão,", 11.5, "#8a5a12", True))
b.append(text(326, yb+116, "nada encosta no metal", 11.5, "#8a5a12", True))
b.append(text(326, yb+176, "lata de biscoito, caixa de ferramentas", 11.5, "#222"))
b.append(text(326, yb+192, "de aço ou panela com tampa", 11.5, "#222"))
b.append(box(326, yb+206, 344, 104, "#fff4e5", "#ef8a2b"))
b += [text(338, yb+226, "A CADA 6 MESES:", 12.5, "#222", True),
      text(338, yb+243, "ligue, abra 3 arquivos ao acaso, recarregue", 12),
      text(338, yb+260, "as baterias e confira todas as cópias.", 12),
      text(338, yb+277, "A cada 3–5 anos: copie tudo para mídia nova.", 12),
      text(338, yb+296, "Tenha o principal IMPRESSO em papel.", 12.5, "#b3001b", True)]
b.append(papel(56, yb+236)); b.append(text(126, yb+258, "+ papel: não precisa", 12, "#222", True))
b.append(text(126, yb+274, "de energia nem de", 12, "#222", True)); b.append(text(126, yb+290, "aparelho nenhum", 12, "#222", True))
open(D + "backup-3-2-1.svg", "w").write(svg(680, yb + 320, "Regra 3-2-1 para não perder a biblioteca", "\n".join(b)))

# =====================================================================
# 5. FORMULAS DE AREA E VOLUME
# =====================================================================
b = []
GW, GH = 216, 236
cells = [(10, 46), (232, 46), (454, 46), (10, 290), (232, 290), (454, 290)]
for (x, y) in cells:
    b.append(box(x, y, GW, GH, "#fff", "#bbb"))
def tit(i, s):
    x, y = cells[i]; return text(x+GW/2, y+22, s, 13, "#222", True, "middle")
def lines(i, y0, ls):
    x, y = cells[i]; out = []
    for k, (s, bold, col) in enumerate(ls):
        out.append(text(x+GW/2, y+y0+k*16, s, 12, col, bold, "middle"))
    return out
# 1 retangulo
x, y = cells[0]
b.append(tit(0, "Retângulo (canteiro, piso)"))
b.append(rect(x+40, y+44, 136, 70, "#cdeccf", sw=2.5))
b.append(darrow(x+40, y+128, x+176, y+128, "#1e1e1e", 2)); b.append(text(x+108, y+146, "comprimento", 11.5, "#222", False, "middle"))
b.append(darrow(x+188, y+44, x+188, y+114, "#1e1e1e", 2)); b.append(f'<text x="{x+204}" y="{y+79}" font-size="11.5" fill="#222" text-anchor="middle" transform="rotate(-90 {x+204} {y+79})">largura</text>')
b += lines(0, 172, [("Área = comprimento × largura", True, "#1e3a5f"), ("Ex.: canteiro 10 m × 1,2 m", False, "#222"), ("= 12 m²", True, "#b3001b")])
# 2 triangulo
x, y = cells[1]
b.append(tit(1, "Triângulo"))
b.append(f'<polygon points="{x+34},{y+124} {x+182},{y+124} {x+130},{y+44}" fill="#f6e3b5" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(dash(x+130, y+44, x+130, y+124, "#b3001b"))
b.append(text(x+124, y+112, "altura", 11.5, "#b3001b", True, "end"))
b.append(darrow(x+34, y+138, x+182, y+138, "#1e1e1e", 2)); b.append(text(x+108, y+156, "base", 11.5, "#222", False, "middle"))
b += lines(1, 180, [("Área = base × altura ÷ 2", True, "#1e3a5f"), ("Ex.: 30 m × 20 m ÷ 2", False, "#222"), ("= 300 m²", True, "#b3001b")])
# 3 circulo
x, y = cells[2]
b.append(tit(2, "Círculo (roda, tanque)"))
ccx, ccy = x+108, y+92
b.append(f'<circle cx="{ccx}" cy="{ccy}" r="50" fill="{AGUA2}" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<circle cx="{ccx}" cy="{ccy}" r="3" fill="#1e1e1e"/>')
b.append(arrow(ccx, ccy, ccx+48, ccy, "#b3001b", 2.5)); b.append(text(ccx+24, ccy-6, "raio", 11.5, "#b3001b", True, "middle"))
b.append(text(ccx, ccy+68, "diâmetro = 2 × raio", 11.5, "#444", False, "middle"))
b += lines(2, 182, [("Área = 3,14 × raio × raio", True, "#1e3a5f"), ("Volta = 3,14 × diâmetro", True, "#1e3a5f"), ("Ex.: raio 2 m → 12,6 m²", False, "#b3001b")])
# 4 cilindro
x, y = cells[3]
b.append(tit(3, "Cilindro (tambor, cisterna)"))
cx2, top, bot = x+108, y+62, y+146
b.append(f'<path d="M{cx2-50} {top} L{cx2-50} {bot} A50 12 0 0 0 {cx2+50} {bot} L{cx2+50} {top}" fill="{AGUA2}" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<ellipse cx="{cx2}" cy="{top}" rx="50" ry="12" fill="#e6f2fd" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(arrow(cx2, top, cx2+48, top, "#b3001b", 2.5)); b.append(text(cx2+56, top+4, "raio", 11.5, "#b3001b", True))
b.append(darrow(cx2-64, top, cx2-64, bot, "#1e1e1e", 2)); b.append(f'<text x="{cx2-74}" y="{(top+bot)/2}" font-size="11.5" fill="#222" text-anchor="middle" transform="rotate(-90 {cx2-74} {(top+bot)/2})">altura</text>')
b += lines(3, 172, [("Volume = 3,14 × r × r × altura", True, "#1e3a5f"), ("em metros → × 1.000 = litros", False, "#222"), ("Ex.: r 1 m, alt. 2 m = 6.280 L", True, "#b3001b")])
# 5 monte (cone)
x, y = cells[4]
b.append(tit(4, "Monte (grão, areia, adubo)"))
b.append(f'<polygon points="{x+38},{y+136} {x+178},{y+136} {x+108},{y+56}" fill="{SOLO}" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(f'<ellipse cx="{x+108}" cy="{y+136}" rx="70" ry="10" fill="#d9bf92" stroke="#1e1e1e" stroke-width="2"/>')
b.append(dash(x+108, y+56, x+108, y+136, "#b3001b")); b.append(dash(x+110, y+56, x+196, y+56, "#888"))
b.append(darrow(x+192, y+58, x+192, y+134, "#b3001b", 2)); b.append(f'<text x="{x+205}" y="{y+96}" font-size="11.5" font-weight="bold" fill="#b3001b" text-anchor="middle" transform="rotate(-90 {x+205} {y+96})">altura</text>')
b.append(arrow(x+108, y+136, x+176, y+136, "#1e3a5f", 2.5)); b.append(text(x+148, y+156, "raio", 11.5, "#1e3a5f", True, "middle"))
b += lines(4, 180, [("Vol. = 3,14 × r × r × alt. ÷ 3", True, "#1e3a5f"), ("Ex.: r 1 m, alt. 0,9 m", False, "#222"), ("≈ 0,94 m³ ≈ 940 L", True, "#b3001b")])
# 6 esquadro 3-4-5
x, y = cells[5]
b.append(tit(5, "Canto reto: regra 3-4-5"))
ax, ay = x+46, y+150
b.append(f'<polygon points="{ax},{ay} {ax+128},{ay} {ax},{ay-96}" fill="#eee4f7" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append(rect(ax, ay-14, 14, 14, "none", "#b3001b", 2))
b.append(text(ax+64, ay+18, "4 m", 13, "#222", True, "middle"))
b.append(text(ax-24, ay-44, "3 m", 13, "#222", True, "middle"))
b.append(text(ax+76, ay-56, "5 m", 13, "#b3001b", True, "middle"))
b += lines(5, 190, [("Se a diagonal der 5, o canto", False, "#222"), ("é reto (90°). Vale 0,6-0,8-1,0 m.", False, "#222")])
open(D + "formulas-geometria.svg", "w").write(svg(680, 536, "Fórmulas de área e volume (com exemplos)", "\n".join(b)))

print("ok:", sorted(os.listdir(D)))
