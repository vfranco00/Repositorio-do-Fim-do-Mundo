import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
# Figuras de 10-comunicacao-e-navegacao/02-sinais-e-morse.md
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "10-comunicacao-e-navegacao", "img") + "/"
os.makedirs(D, exist_ok=True)
GREEN = "#2b8a3e"; RED = "#d62828"; DARK = "#1e1e1e"; BLUE = "#3f6d9e"

MORSE = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
         "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
         "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
         "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
         "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----"}

def code(x, y, c, dot=5.5, dash=24, h=10, adv_dot=15, adv_dash=30, color=DARK):
    """Desenha pontos (círculos) e traços (barras) a partir de x, centrado verticalmente em y."""
    s = []
    for ch in c:
        if ch == ".":
            s.append(f'<circle cx="{x+dot:.1f}" cy="{y}" r="{dot}" fill="{color}"/>'); x += adv_dot
        else:
            s.append(f'<rect x="{x:.1f}" y="{y-h/2}" width="{dash}" height="{h}" rx="{h/2}" fill="{color}"/>'); x += adv_dash
    return "".join(s), x

# ---------- TABELA MORSE ----------
b = []
b.append(f'<circle cx="40" cy="56" r="5.5" fill="{DARK}"/>')
b.append(text(52, 61, "ponto = sinal curto", 13))
b.append(f'<rect x="210" y="51" width="24" height="10" rx="5" fill="{DARK}"/>')
b.append(text(242, 61, "traço = sinal longo (dura 3 pontos)", 13))
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cols = [letters[0:9], letters[9:18], letters[18:26]]
y0 = 76; rh = 30
for ci, col in enumerate(cols):
    x0 = 20 + ci * 216
    for ri, L in enumerate(col):
        y = y0 + ri * rh
        if ri % 2 == 0:
            b.append(f'<rect x="{x0}" y="{y}" width="208" height="{rh}" fill="#eef3fa"/>')
        b.append(text(x0 + 12, y + 22, L, 20, BLUE, True))
        s, _ = code(x0 + 46, y + 15, MORSE[L]); b.append(s)
yl = y0 + 9 * rh
b.append(f'<rect x="20" y="{y0}" width="640" height="{9*rh}" fill="none" stroke="#9fb3cc" stroke-width="1.5"/>')
# numeros
yn = yl + 30
b.append(text(20, yn - 8, "NÚMEROS", 14, "#222", True))
b.append(text(110, yn - 8, "(1 a 5 começam com pontos; 6 a 0 começam com traços)", 12, "#444"))
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
for i, n in enumerate(nums):
    ci, ri = i // 4, i % 4
    x0 = 20 + ci * 216; y = yn + ri * rh
    if ri % 2 == 0:
        b.append(f'<rect x="{x0}" y="{y}" width="208" height="{rh}" fill="#f4f4f4"/>')
    b.append(text(x0 + 12, y + 22, n, 20, "#222", True))
    s, _ = code(x0 + 40, y + 15, MORSE[n]); b.append(s)
# sinais especiais na terceira coluna, linhas 3-4
x0 = 20 + 2 * 216
b.append(text(x0 + 10, yn + 2 * rh + 19, "Ponto (.)", 12.5, "#222", True))
s, _ = code(x0 + 92, yn + 2 * rh + 15, ".-.-.-", dot=4.5, dash=18, h=8, adv_dot=12, adv_dash=22); b.append(s)
b.append(text(x0 + 10, yn + 3 * rh + 19, "Pergunta (?)", 12.5, "#222", True))
s, _ = code(x0 + 104, yn + 3 * rh + 15, "..--..", dot=4.5, dash=18, h=8, adv_dot=12, adv_dash=22); b.append(s)
b.append(f'<rect x="20" y="{yn}" width="640" height="{4*rh}" fill="none" stroke="#bbb" stroke-width="1.5"/>')
# sinais de procedimento
ys = yn + 4 * rh + 22
b.append(box(20, ys, 640, 150, "#fff4e5", "#ef8a2b"))
b.append(text(34, ys + 22, "SINAIS IMPORTANTES", 14, "#222", True))
rows = [("SOS", "...---...", "SOCORRO — tudo junto, sem pausa entre as letras", RED),
        ("OK", "---  -.-", "entendido, tudo bem (letras O e K)", DARK),
        ("K", "-.-", "câmbio: \"pode falar\"   ·   R  (· — ·) = recebido", DARK),
        ("AR", ".-.-.", "fim da mensagem   ·   erro: 8 pontos (apague a palavra)", DARK)]
for i, (lab, c, desc, col) in enumerate(rows):
    y = ys + 50 + i * 26
    b.append(text(34, y + 5, lab, 15, col, True))
    xx = 82
    for part in c.split("  "):
        s, xx = code(xx, y, part.strip(), dot=5, dash=22, h=9, adv_dot=14, adv_dash=28, color=col); b.append(s); xx += 14
    b.append(text(250 if lab != "SOS" else 250, y + 5, desc, 12.5, "#222"))
# regra de tempo
yt = ys + 172
b.append(text(20, yt, "TEMPO (1 unidade = duração de 1 ponto)", 14, "#222", True))
u = 26; xs = 40; yb = yt + 22
seq = [("on", 1, "E"), ("off", 3, "entre letras: 3"), ("on", 3, "T"), ("off", 7, "entre palavras: 7"),
       ("on", 1, ""), ("off", 1, "dentro: 1"), ("on", 3, "")]
x = xs
for i in range(21):
    b.append(f'<rect x="{xs + i*u}" y="{yb}" width="{u}" height="22" fill="none" stroke="#ccc"/>')
for kind, n, lab in seq:
    if kind == "on":
        b.append(f'<rect x="{x+1}" y="{yb+3}" width="{n*u-2}" height="16" rx="6" fill="{DARK}"/>')
    else:
        b.append(f'<line x1="{x+3}" y1="{yb+34}" x2="{x+n*u-3}" y2="{yb+34}" stroke="{RED}" stroke-width="2"/>')
        b.append(f'<line x1="{x+3}" y1="{yb+29}" x2="{x+3}" y2="{yb+39}" stroke="{RED}" stroke-width="2"/>')
        b.append(f'<line x1="{x+n*u-3}" y1="{yb+29}" x2="{x+n*u-3}" y2="{yb+39}" stroke="{RED}" stroke-width="2"/>')
        b.append(text(x + n * u / 2, yb + 54, lab, 11.5, "#b3001b", True, "middle"))
    x += n * u
b.append(text(xs + 0.5 * u, yb - 6, "E", 12, BLUE, True, "middle"))
b.append(text(xs + 5.5 * u, yb - 6, "T", 12, BLUE, True, "middle"))
b.append(text(xs + 16 * u, yb - 6, "A (nova palavra)", 12, BLUE, True, "middle"))
b += [text(20, yb + 82, "Lanterna ou apito, devagar: ponto ≈ meio segundo, traço ≈ 1,5 segundo.", 12.5),
      text(20, yb + 100, "Escreva sem acentos e sem Ç (CAO = cão). Para batidas em cano ou parede, use o", 12.5),
      text(20, yb + 118, "código de batidas (quadro de letras) explicado no texto.", 12.5)]
H = yb + 130
open(D + "morse-tabela.svg", "w").write(svg(680, H, "Código Morse internacional", "\n".join(b)))

# ---------- SINAIS TERRA-AR ----------
b = []
b.append(text(340, 56, "Monte no chão, em lugar aberto, com material que CONTRASTE com o fundo", 13, "#222", False, "middle"))
GRASS = "#8fbf6a"; STRIP = "#f7f3e6"
def strip(x1, y1, x2, y2, w=13):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{DARK}" stroke-width="{w+4}" stroke-linecap="square"/>'
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{STRIP}" stroke-width="{w}" stroke-linecap="square"/>')
panels = [("V", "PRECISO DE", "AJUDA", RED), ("X", "PRECISO DE", "MÉDICO", RED), ("N", "NÃO", "(negativo)", DARK),
          ("Y", "SIM", "(afirmativo)", GREEN), ("→", "FUI NESTA", "DIREÇÃO", BLUE)]
pw = 124; gap = 5
for i, (sym, l1, l2, col) in enumerate(panels):
    x0 = 20 + i * (pw + gap); y0 = 70
    b.append(f'<rect x="{x0}" y="{y0}" width="{pw}" height="120" rx="6" fill="{GRASS}" stroke="#4f7a35" stroke-width="2"/>')
    cx, cy = x0 + pw / 2, y0 + 60
    if sym == "V":
        b.append(strip(cx - 32, cy - 38, cx, cy + 38)); b.append(strip(cx + 32, cy - 38, cx, cy + 38))
    elif sym == "X":
        b.append(strip(cx - 32, cy - 38, cx + 32, cy + 38)); b.append(strip(cx + 32, cy - 38, cx - 32, cy + 38))
    elif sym == "N":
        b.append(strip(cx - 28, cy + 38, cx - 28, cy - 38)); b.append(strip(cx - 28, cy - 38, cx + 28, cy + 38)); b.append(strip(cx + 28, cy + 38, cx + 28, cy - 38))
    elif sym == "Y":
        b.append(strip(cx - 32, cy - 38, cx, cy)); b.append(strip(cx + 32, cy - 38, cx, cy)); b.append(strip(cx, cy, cx, cy + 38))
    else:
        b.append(strip(cx - 44, cy, cx + 34, cy)); b.append(strip(cx + 34, cy, cx + 10, cy - 24)); b.append(strip(cx + 34, cy, cx + 10, cy + 24))
    b.append(text(cx, y0 + 146, l1, 13, col, True, "middle"))
    b.append(text(cx, y0 + 163, l2, 13, col, True, "middle"))
b.append(text(20 + 4 * (pw + gap) + pw / 2, 70 + 180, "(aponte para onde foi)", 11, "#444", False, "middle"))
# tamanho
yb = 270
b.append(f'<rect x="20" y="{yb}" width="300" height="200" rx="8" fill="#f6f1e4" stroke="#c9bba0"/>')
b.append(text(170, yb + 22, "Tamanho mínimo (letra V)", 13.5, "#222", True, "middle"))
gx, gy = 60, yb + 46
b.append(f'<rect x="{gx-20}" y="{gy-8}" width="160" height="134" fill="{GRASS}" rx="4"/>')
b.append(strip(gx + 10, gy, gx + 60, gy + 116, 16)); b.append(strip(gx + 110, gy, gx + 60, gy + 116, 16))
b.append(f'<line x1="{gx+156}" y1="{gy}" x2="{gx+156}" y2="{gy+116}" stroke="{DARK}" stroke-width="1.5"/>')
b.append(f'<line x1="{gx+150}" y1="{gy}" x2="{gx+162}" y2="{gy}" stroke="{DARK}" stroke-width="1.5"/><line x1="{gx+150}" y1="{gy+116}" x2="{gx+162}" y2="{gy+116}" stroke="{DARK}" stroke-width="1.5"/>')
b += [text(gx + 166, gy + 46, "3 m no", 12, "#222", True), text(gx + 166, gy + 62, "mínimo;", 12, "#222", True), text(gx + 166, gy + 78, "melhor", 12), text(gx + 166, gy + 94, "6 a 10 m", 12)]
b.append(text(170, yb + 191, "faixa com ~1/6 do comprimento (1 m)", 12, "#222", False, "middle"))
# dicas
b.append(box(334, yb, 326, 200, "#eef5ff", BLUE))
tips = ["Lugar aberto: clareira, praia, topo,", "campo, telhado, banco de areia.",
        "Linhas RETAS e cantos vivos: não", "existem na natureza e chamam atenção.",
        "Contraste: pano claro, pedras claras ou", "capim cortado sobre fundo escuro; galhos",
        "e terra revirada sobre fundo claro.", "Valas cavadas ou montes fazem SOMBRA",
        "e aparecem melhor com sol baixo.", "Avião BALANÇA AS ASAS (ou pisca as luzes",
        "2 vezes à noite) = mensagem entendida."]
for i, t in enumerate(tips):
    bold = i in (0, 2, 4, 7, 9)
    b.append(text(346, yb + 24 + i * 16.4, t, 12, "#222", bold))
# sinais com o corpo
yc = 502
b.append(text(340, yc + 4, "Com o corpo, de frente para o avião ou helicóptero", 14, "#222", True, "middle"))
def person(cx, base, arms):
    s = []
    s.append(limb([(cx - 9, base - 70), (cx - 12, base)], 12, SOC)); s.append(limb([(cx + 9, base - 70), (cx + 12, base)], 12, SOC))
    s.append(limb([(cx, base - 132), (cx, base - 70)], 30, SOC))
    for a in arms:
        s.append(limb(a, 10, SOC))
    s.append(head(cx, base - 152, 15, SOC))
    return "".join(s)
base = yc + 214
b.append(person(170, base, [[(cx, base - 126), (cx + dx, base - 186)] for cx, dx in ((160, -32), (180, 32))]))
b.append(hand(128, base - 188, 7)); b.append(hand(212, base - 188, 7))
b.append(text(170, base + 22, "Y — braços para cima em V:", 12.5, GREEN, True, "middle"))
b.append(text(170, base + 38, "\"SIM, PRECISAMOS DE AJUDA\"", 12.5, GREEN, True, "middle"))
b.append(person(500, base, [[(510, base - 126), (512, base - 200)], [(490, base - 126), (474, base - 66)]]))
b.append(hand(512, base - 202, 7)); b.append(hand(474, base - 62, 7))
b.append(text(500, base + 22, "N — um braço para cima, outro para", 12.5, DARK, True, "middle"))
b.append(text(500, base + 38, "baixo: \"NÃO PRECISAMOS DE AJUDA\"", 12.5, DARK, True, "middle"))
b.append(text(340, base + 64, "Agite um pano claro ou colorido na mão para ser visto de mais longe.", 12.5, "#444", False, "middle"))
open(D + "sinais-terra-ar.svg", "w").write(svg(680, base + 78, "Sinais terra-ar (para aviões e helicópteros)", "\n".join(b)))

# ---------- ESPELHO DE SINALIZACAO ----------
b = []
b.append('<circle cx="70" cy="80" r="22" fill="#ffd43b" stroke="#e8a400" stroke-width="3"/>')
for k in range(8):
    import math
    a = k * math.pi / 4
    b.append(f'<line x1="{70+28*math.cos(a):.1f}" y1="{80+28*math.sin(a):.1f}" x2="{70+38*math.cos(a):.1f}" y2="{80+38*math.sin(a):.1f}" stroke="#e8a400" stroke-width="3"/>')
b.append(text(70, 132, "SOL", 12, "#8a6200", True, "middle"))
# pessoa (cabeca de perfil) e espelho
b.append(limb([(150, 312), (150, 236)], 34, SOC))
b.append(head(150, 206, 24, SOC, 1, 0))
b.append(f'<rect x="178" y="190" width="8" height="34" fill="#cfe6fb" stroke="{DARK}" stroke-width="2" transform="rotate(-25 182 207)"/>')
b.append(text(176, 296, "espelho junto ao olho", 11.5, "#222", True))
b.append(f'<line x1="200" y1="284" x2="186" y2="222" stroke="#555" stroke-width="1.5"/>')
# braco estendido com dedos em V
b.append(limb([(160, 250), (250, 228), (330, 214)], 11, SOC))
b.append(hand(336, 212, 8))
b.append(limb([(340, 206), (352, 178)], 5, SKIN)); b.append(limb([(343, 209), (368, 190)], 5, SKIN))
b.append(text(352, 152, "dedos em V", 12, "#222", True, "middle"))
b.append(text(352, 166, "(o alvo fica entre eles)", 11, "#444", False, "middle"))
# raios
b.append(f'<line x1="90" y1="98" x2="180" y2="204" stroke="#e8a400" stroke-width="3" stroke-dasharray="8 5"/>')
b.append(f'<line x1="184" y1="204" x2="600" y2="175" stroke="#e8a400" stroke-width="3" stroke-dasharray="8 5"/>')
b.append(f'<circle cx="358" cy="192" r="6" fill="#fff3a0" stroke="#e8a400" stroke-width="2"/>')
# aviao
b.append(f'<path d="M600 175 l40 -6 l8 -12 l6 2 l-4 14 l18 -2 l2 6 l-18 4 l6 14 l-6 2 l-12 -12 l-38 6 Z" fill="#9aa5b1" stroke="{DARK}" stroke-width="2"/>')
b.append(text(612, 216, "alvo", 12, "#222", True, "middle"))
b.append(box(20, 330, 640, 186, "#fff4e5", "#ef8a2b"))
steps = ["1. Segure o espelho junto ao olho, com a face brilhante virada para o sol.",
         "2. Estique o outro braço e faça um V com os dedos. Enquadre o alvo (avião, barco,",
         ">casa, morro) entre os dedos.",
         "3. Incline o espelho até o reflexo (ponto de luz) aparecer na sua mão ou nos dedos.",
         "4. Mova o espelho devagar para o ponto de luz passar pelo V, de um lado para o outro:",
         ">o alvo recebe flashes.",
         "Espelho com furo no meio: olhe o alvo pelo furo e mova até o ponto de luz cair sobre ele.",
         "Alcance: dezenas de km com sol. Varra o horizonte mesmo sem ver ninguém. Serve CD,",
         "lata polida, tela de celular apagado. Quando o piloto responder, não mire mais no rosto dele."]
for i, t in enumerate(steps):
    b.append(text(52 if t.startswith(">") else 34, 352 + i * 18.5, t.lstrip(">"), 12.5, "#222"))
open(D + "espelho-sinalizacao.svg", "w").write(svg(680, 528, "Espelho de sinalização: como mirar", "\n".join(b)))

# ---------- MARCAS DE TRILHA ----------
b = []
STONE = "#a8a29a"; STICK = "#8b5a2b"
def stone(cx, cy, rx=14, ry=10, f=STONE):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{f}" stroke="{DARK}" stroke-width="2"/>'
def stick(x1, y1, x2, y2, w=7):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{DARK}" stroke-width="{w+3}" stroke-linecap="round"/>'
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{STICK}" stroke-width="{w}" stroke-linecap="round"/>')
cells = []
# 1 seta
s = stick(30, 60, 120, 60) + stick(120, 60, 98, 42) + stick(120, 60, 98, 78)
cells.append((s, "SIGA POR AQUI", "seta de galhos ou pedras", GREEN))
s = stick(45, 30, 105, 90) + stick(105, 30, 45, 90)
cells.append((s, "NÃO VÁ POR AQUI", "X de galhos sobre a trilha", RED))
s = stone(75, 76, 22, 13) + stone(75, 54, 15, 10)
cells.append((s, "ESTA É A TRILHA", "pedra sobre pedra", GREEN))
s = stone(65, 76, 22, 13) + stone(65, 54, 15, 10) + stone(108, 78, 10, 8)
cells.append((s, "VIRE À DIREITA", "pedrinha do lado da curva", BLUE))
s = stone(75, 80, 24, 13) + stone(75, 60, 18, 11) + stone(75, 42, 11, 8)
cells.append((s, "ATENÇÃO / PERIGO", "três pedras empilhadas", RED))
s = f'<circle cx="75" cy="60" r="36" fill="none" stroke="{DARK}" stroke-width="9"/><circle cx="75" cy="60" r="36" fill="none" stroke="{STONE}" stroke-width="5"/>' + stone(75, 60, 9, 7)
cells.append((s, "FIM / FUI PARA CASA", "círculo com pedra no meio", DARK))
s = stick(40, 30, 40, 100, 9) + stick(40, 50, 92, 78, 5) + f'<polygon points="92,78 100,86 102,72" fill="{STICK}" stroke="{DARK}" stroke-width="1.5"/>'
cells.append((s, "FUI POR AQUI", "galho quebrado apontando", BLUE))
s = (f'<rect x="40" y="32" width="70" height="56" rx="4" fill="#fffbe6" stroke="{DARK}" stroke-width="2"/>'
     + "".join(f'<line x1="48" y1="{44+i*10}" x2="{100-(i%2)*14}" y2="{44+i*10}" stroke="#555" stroke-width="2"/>' for i in range(4)))
cells.append((s, "BILHETE", "data, hora, para onde foi", DARK))
for i, (s, t1, t2, col) in enumerate(cells):
    cx0 = 20 + (i % 4) * 162; cy0 = 50 + (i // 4) * 186
    b.append(f'<rect x="{cx0}" y="{cy0}" width="154" height="176" rx="8" fill="#f1ead8" stroke="#c9bba0"/>')
    b.append(f'<g transform="translate({cx0+2},{cy0+8})">{s}</g>')
    b.append(text(cx0 + 77, cy0 + 136, t1, 12.5, col, True, "middle"))
    b.append(text(cx0 + 77, cy0 + 154, t2, 11, "#444", False, "middle"))
b.append(text(340, 440, "Marque sempre do mesmo lado da trilha, bem à vista, a cada 50–100 m e em toda bifurcação.", 12.5, "#222", False, "middle"))
b.append(text(340, 458, "Combine os sinais ANTES com o grupo.", 12.5, "#222", True, "middle"))
b.append(text(340, 476, "Bilhete: dentro de saco plástico, preso num galho à altura dos olhos.", 12.5, "#222", False, "middle"))
open(D + "marcas-de-trilha.svg", "w").write(svg(680, 490, "Marcas de trilha (para quem vem atrás)", "\n".join(b)))
print("ok")
