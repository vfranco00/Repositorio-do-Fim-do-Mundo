import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "12-comunidade-e-seguranca", "img") + "/"
os.makedirs(D, exist_ok=True)
WOOD = "#8b5a2b"; AGUA = "#4a90d9"; AGUA_C = "#cfe6fb"; SOLO = "#e8d3b0"; VERDE = "#2b8a3e"; PERIGO = "#d62828"; PERIGO2 = "#b3001b"


def caixa(x, y, w, h, fill, stroke, titulo, linhas, tsize=13, lsize=11.5):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
    s += text(x + w / 2, y + 20, titulo, tsize, "#222", True, "middle")
    for i, l in enumerate(linhas):
        s += text(x + w / 2, y + 38 + i * 15, l, lsize, "#333", False, "middle")
    return s


# =====================================================================
# ORGANOGRAMA DO GRUPO
# =====================================================================
b = []
# assembleia
b.append(caixa(180, 48, 320, 62, "#ffe9c7", "#ef8a2b", "ASSEMBLEIA — todos os adultos",
               ["reunião semanal · decide as regras,", "elege e fiscaliza quem coordena"], 14))
# coordenacao
b.append(f'<line x1="340" y1="110" x2="340" y2="134" stroke="#555" stroke-width="2.5"/>')
b.append(caixa(220, 134, 240, 62, "#fff4e5", "#ef8a2b", "COORDENAÇÃO",
               ["2–3 pessoas eleitas, mandato de", "3 meses, com rodízio"]))
# mediacao (ligada a assembleia)
b.append(caixa(486, 134, 180, 62, "#f1e8ff", "#7b5cb8", "MEDIAÇÃO",
               ["3 pessoas eleitas;", "resolve conflitos"]))
b.append(f'<path d="M500 80 L576 80 L576 134" fill="none" stroke="#7b5cb8" stroke-width="2" stroke-dasharray="6 4"/>')
# almoxarifado (ligado a coordenacao)
b.append(caixa(14, 134, 180, 62, "#eeeeee", "#777", "ESTOQUE",
               ["2 chaves, 2 pessoas;", "livro de entrada e saída"]))
b.append(f'<line x1="194" y1="165" x2="220" y2="165" stroke="#555" stroke-width="2"/>')
# barramento
b.append(f'<line x1="340" y1="196" x2="340" y2="214" stroke="#555" stroke-width="2.5"/>')
b.append(f'<line x1="91" y1="214" x2="589" y2="214" stroke="#555" stroke-width="2.5"/>')
equipes = [
    ("Água e saneamento", AGUA_C, AGUA, ["captar e tratar água", "cisternas e filtros", "banheiros e lixo", "lavar as mãos"]),
    ("Comida e roça", "#d8f0d0", VERDE, ["horta e roça", "criação de animais", "cozinha coletiva", "conservar alimentos"]),
    ("Saúde", "#fde0e0", PERIGO, ["posto e farmácia", "primeiros socorros", "visita aos doentes", "partos, higiene"]),
    ("Segurança", "#e6e0f5", "#5a4a9a", ["vigia em turnos", "portões e alarmes", "combate a incêndio", "rotas de fuga"]),
    ("Energia e manutenção", "#fff1c2", "#c89a00", ["lenha e carvão", "solar e baterias", "ferramentas", "consertos e obras"]),
    ("Crianças e educação", "#fde7d0", "#ef8a2b", ["escola diária", "cuidar dos pequenos", "brincadeiras", "aprendizes de ofício"]),
    ("Registro e comunicação", "#e8e8e8", "#666", ["atas e diário", "inventário de tudo", "rádio e mural", "contato c/ vizinhos"]),
]
W = 154; G = 12
for i, (nome, fill, st, tarefas) in enumerate(equipes):
    if i < 4:
        x = 14 + i * (W + G); y = 232
    else:
        x = 14 + (i - 4) * (W + G); y = 372
    cx = x + W / 2
    if i < 4:
        b.append(f'<line x1="{cx}" y1="214" x2="{cx}" y2="{y}" stroke="#555" stroke-width="2"/>')
    b.append(f'<rect x="{x}" y="{y}" width="{W}" height="122" rx="8" fill="#fff" stroke="{st}" stroke-width="2"/>')
    b.append(f'<rect x="{x}" y="{y}" width="{W}" height="28" rx="8" fill="{fill}" stroke="{st}" stroke-width="2"/>')
    b.append(text(cx, y + 19, nome, 10.5 if len(nome) > 18 else 12.5, "#222", True, "middle"))
    for k, t in enumerate(tarefas):
        b.append(text(x + 10, y + 50 + k * 18, "• " + t, 11.5, "#333"))
# ligacao da segunda fileira
b.append(f'<line x1="{14 + W + G/2}" y1="214" x2="{14 + W + G/2}" y2="364" stroke="#555" stroke-width="2"/>')
b.append(f'<line x1="{14 + W/2}" y1="364" x2="{14 + 2*(W+G) + W/2}" y2="364" stroke="#555" stroke-width="2"/>')
for i in range(3):
    cx = 14 + i * (W + G) + W / 2
    b.append(f'<line x1="{cx}" y1="364" x2="{cx}" y2="372" stroke="#555" stroke-width="2"/>')
# nota
x = 14 + 3 * (W + G)
b.append(box(x, 380, W, 106, "#fff4e5", "#ef8a2b"))
b += [text(x + 10, 400, "Cada equipe tem", 11.5, "#222", True), text(x + 10, 415, "1 responsável e", 11.5, "#222", True),
      text(x + 10, 430, "ajudantes.", 11.5, "#222", True),
      text(x + 10, 450, "Todo adulto em pelo", 11.5), text(x + 10, 465, "menos 1 equipe.", 11.5), text(x + 10, 480, "Contas na assembleia.", 11.5)]
open(D + "organograma-grupo.svg", "w").write(svg(680, 500, "Como dividir as tarefas de um grupo comunitário", "\n".join(b)))


# =====================================================================
# BALANCA DE BRACO CASEIRA
# =====================================================================
def prato(cx, y):
    s = f'<path d="M{cx-46} {y} L{cx+46} {y} L{cx+38} {y+20} L{cx-38} {y+20} Z" fill="#c9c9c9" stroke="{OUT}" stroke-width="2.5"/>'
    return s


def garrafa1L(x, ybase, cheia=True):
    h = 62; w = 26
    s = (f'<path d="M{x} {ybase} L{x} {ybase-h+18} Q{x} {ybase-h+8} {x+8} {ybase-h+4} L{x+8} {ybase-h} L{x+w-8} {ybase-h} '
         f'L{x+w-8} {ybase-h+4} Q{x+w} {ybase-h+8} {x+w} {ybase-h+18} L{x+w} {ybase} Z" fill="#eef7ff" stroke="{OUT}" stroke-width="2"/>')
    if cheia:
        s += f'<rect x="{x+2}" y="{ybase-h+20}" width="{w-4}" height="{h-21}" fill="#9fc5ec"/>'
    s += f'<rect x="{x+7}" y="{ybase-h-6}" width="{w-14}" height="7" fill="#3f6d9e" stroke="{OUT}" stroke-width="1.5"/>'
    return s


b = []
P = (212, 128)  # pivo
yb = 400
b.append(f'<rect x="70" y="{yb}" width="290" height="16" rx="3" fill="{WOOD}" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<rect x="204" y="118" width="16" height="{yb-118}" fill="#a87442" stroke="{OUT}" stroke-width="2"/>')
# placa da marca
b.append(f'<rect x="198" y="186" width="28" height="26" rx="3" fill="#fff" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<line x1="212" y1="188" x2="212" y2="210" stroke="{PERIGO}" stroke-width="2"/>')
# braco (ripa)
b.append(f'<rect x="54" y="132" width="316" height="12" rx="3" fill="#c79a5a" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<circle cx="{P[0]}" cy="{P[1]+7}" r="4.5" fill="#555" stroke="{OUT}" stroke-width="1.5"/>')
# fiel (ponteiro para baixo)
b.append(f'<line x1="212" y1="144" x2="212" y2="204" stroke="#222" stroke-width="3"/>')
b.append(f'<polygon points="207,200 217,200 212,210" fill="#222"/>')
# ganchos e cordoes
for cx in (62, 362):
    b.append(f'<circle cx="{cx}" cy="138" r="3" fill="#555"/>')
    for dx in (-40, 0, 40):
        b.append(f'<line x1="{cx}" y1="140" x2="{cx+dx}" y2="296" stroke="#555" stroke-width="1.8"/>')
    b.append(prato(cx, 296))
# conteudo: esquerda = saco + garrafa vazia; direita = garrafa cheia
b.append('<path d="M30 296 Q 26 262 40 254 L 70 254 Q 82 262 78 296 Z" fill="#e9dcb8" stroke="#1e1e1e" stroke-width="2"/>')
b.append(text(54, 284, "arroz", 10.5, "#5a4a2a", True, "middle"))
b.append(garrafa1L(80, 296, False))
b.append(garrafa1L(349, 296, True))
# cotas
b.append(f'<line x1="62" y1="104" x2="210" y2="104" stroke="{VERDE}" stroke-width="2"/>')
b.append(f'<line x1="214" y1="104" x2="362" y2="104" stroke="{VERDE}" stroke-width="2"/>')
for x in (62, 212, 362):
    b.append(f'<line x1="{x}" y1="96" x2="{x}" y2="112" stroke="{VERDE}" stroke-width="2"/>')
b.append(text(137, 96, "45 cm", 12.5, VERDE, True, "middle")); b.append(text(287, 96, "45 cm", 12.5, VERDE, True, "middle"))
b.append(text(212, 66, "distâncias IGUAIS (meça com barbante)", 12, VERDE, True, "middle"))
# rotulos
b += [text(196, 230, "fiel (ponteiro)", 11, "#222", True, "end"), text(196, 244, "na marca =", 11, "#222", True, "end"), text(196, 258, "equilíbrio", 11, "#222", True, "end")]
b += [text(230, 164, "prego (eixo) num", 11), text(230, 178, "furo um pouco", 11), text(230, 192, "ACIMA do meio", 11, "#222", True), text(230, 206, "da ripa", 11, "#222", True)]
b += [text(16, 330, "garrafa vazia IGUAL", 11, "#333"), text(16, 343, "(desconta o plástico)", 11, "#333")]
b += [text(318, 330, "garrafa de 1 L", 11, "#333"), text(318, 343, "cheia d'água", 11, "#333")]
b += [text(14, 438, "arroz + garrafa vazia = garrafa cheia: 1 kg de arroz", 12, "#222", True),
      text(14, 455, "Ripa reta de madeira dura (~1 m), pratos iguais, 3 cordões iguais.", 11.5, "#444")]
# coluna direita
x = 418
b.append(box(x, 52, 248, 196, "#eef7ff", "#3f6d9e"))
b += [text(x + 12, 74, "Como conferir", 13.5, "#222", True),
      text(x + 12, 96, "1. Vazia: o fiel para na", 11.5, "#222", True), text(x + 12, 111, "marca. Se não, cole fita,", 11.5),
      text(x + 12, 126, "massa ou um prego no", 11.5), text(x + 12, 141, "lado mais leve.", 11.5),
      text(x + 12, 163, "2. Pese algo e TROQUE os", 11.5, "#222", True), text(x + 12, 178, "pratos de lado. Tem que", 11.5),
      text(x + 12, 193, "equilibrar igual. Se não,", 11.5), text(x + 12, 208, "os braços estão desiguais:", 11.5),
      text(x + 12, 223, "refaça os furos.", 11.5)]
b.append(box(x, 260, 248, 196, "#fff4e5", "#ef8a2b"))
b += [text(x + 12, 282, "Pesos-padrão", 13.5, "#222", True),
      text(x + 12, 304, "1 litro de água = 1 kg", 12, "#222", True),
      text(x + 12, 320, "2 L = 2 kg · 500 mL = 500 g", 11.5),
      text(x + 12, 340, "Moeda de R$ 1 (dourada e", 11.5), text(x + 12, 355, "prateada) = 7 g; 10 moedas", 11.5), text(x + 12, 370, "= 70 g", 11.5),
      text(x + 12, 392, "Faça pesos de pedra: pese", 11.5), text(x + 12, 407, "contra a garrafa e marque", 11.5),
      text(x + 12, 422, "(1 kg, 500 g, 250 g, 100 g).", 11.5), text(x + 12, 442, "Precisão: ~1 a 2%.", 11.5, "#444")]
open(D + "balanca-braco.svg", "w").write(svg(680, 466, "Balança de braço caseira (pesos justos na feira)", "\n".join(b)))


# =====================================================================
# CAMADAS DE SEGURANCA (vista de cima)
# =====================================================================
b = []
# vizinhanca
b.append(f'<rect x="14" y="52" width="652" height="430" rx="10" fill="#eef1ea" stroke="#aab59a" stroke-dasharray="6 4"/>')
b.append(text(26, 74, "1. VIZINHANÇA: vizinhos que se conhecem e avisam", 12.5, "#4a5a3a", True))
for (hx, hy) in ((30, 140), (30, 300), (610, 120), (610, 330), (470, 444)):
    b.append(f'<rect x="{hx}" y="{hy}" width="34" height="26" fill="#d9cbb0" stroke="{OUT}" stroke-width="1.5"/>')
# terreno
X0, Y0, X1, Y1 = 90, 96, 580, 420
b.append(f'<rect x="{X0}" y="{Y0}" width="{X1-X0}" height="{Y1-Y0}" fill="#f6f0e1" stroke="#6b4f2a" stroke-width="3"/>')
# cerca viva espinhosa por dentro da cerca
zz = []
x = X0 + 8
while x < X1 - 8:
    zz.append(f"{x},{Y0+8}"); zz.append(f"{x+5},{Y0+16}"); x += 10
b.append(f'<polyline points="{" ".join(zz)}" fill="none" stroke="{VERDE}" stroke-width="3"/>')
zz = []
y = Y0 + 8
while y < Y1 - 8:
    zz.append(f"{X0+8},{y}"); zz.append(f"{X0+16},{y+5}"); y += 10
b.append(f'<polyline points="{" ".join(zz)}" fill="none" stroke="{VERDE}" stroke-width="3"/>')
b += [text(X0 + 24, Y0 + 36, "2. CERCA + cerca viva", 12, "#222", True), text(X0 + 24, Y0 + 51, "espinhosa por dentro", 12)]
# latas no arame (lado direito)
for y in range(Y0 + 40, Y1 - 30, 36):
    b.append(f'<rect x="{X1-7}" y="{y}" width="12" height="15" rx="2" fill="#bbb" stroke="{OUT}" stroke-width="1.5"/>')
b += [text(X1 - 14, 336, "latas com", 11, "#222", True, "end"), text(X1 - 14, 350, "pedrinhas no", 11, "#222", True, "end"), text(X1 - 14, 364, "arame (barulho)", 11, "#222", False, "end")]
# luzes nos cantos apontando para FORA
for (lx, ly, dx, dy) in ((X0, Y0, -1, -1), (X1, Y0, 1, -1), (X0, Y1, -1, 1), (X1, Y1, 1, 1)):
    if dy > 0:
        b.append(f'<polygon points="{lx},{ly} {lx+dx*44},{ly+dy*16} {lx+dx*16},{ly+dy*44}" fill="#ffe066" fill-opacity="0.75" stroke="#c89a00"/>')
    b.append(f'<circle cx="{lx}" cy="{ly}" r="6" fill="#ffd43b" stroke="{OUT}" stroke-width="1.5"/>')
b.append(text(X0 + 4, Y1 + 30, "luz virada para FORA", 11, "#8a6a00", True))
# portao principal (embaixo) e saida de fuga (em cima, a direita)
gx = 300
b.append(f'<rect x="{gx}" y="{Y1-5}" width="60" height="10" fill="#fff" stroke="{OUT}" stroke-width="2"/>')
b.append(text(gx + 30, Y1 + 22, "portão principal", 11.5, "#222", True, "middle"))
b.append(text(gx + 30, Y1 + 36, "(um só, vigiado)", 11, "#444", False, "middle"))
b.append(f'<rect x="460" y="{Y0-5}" width="34" height="10" fill="#fff" stroke="{VERDE}" stroke-width="2.5"/>')
# casa e comodo seguro
b.append(f'<rect x="250" y="180" width="200" height="140" fill="#e9dcc6" stroke="{OUT}" stroke-width="3"/>')
b.append(text(270, 202, "3. CASA: trancas, janelas", 12, "#222", True))
b.append(text(270, 217, "com cortina grossa à noite", 11.5))
b.append(f'<rect x="360" y="250" width="80" height="60" fill="#d0c4f0" stroke="#5a4a9a" stroke-width="2.5"/>')
b += [text(400, 272, "4. CÔMODO", 11, "#3a2a7a", True, "middle"), text(400, 286, "SEGURO", 11, "#3a2a7a", True, "middle"),
      text(400, 300, "água, rádio", 10, "#3a2a7a", False, "middle")]
# posto de vigia
b.append(f'<rect x="120" y="340" width="26" height="26" fill="#a87442" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<path d="M146 340 L 230 300 L 210 380 Z" fill="#9ad0f5" fill-opacity="0.4" stroke="#4a90d9" stroke-dasharray="4 3"/>')
b += [text(120, 386, "vigia (ponto alto,", 11.5, "#222", True), text(120, 400, "sem luz atrás)", 11.5, "#222", True)]
# caes e gansos perto do portao
for (ax, ay) in ((250, 380), (270, 392), (380, 388)):
    b.append(f'<ellipse cx="{ax}" cy="{ay}" rx="9" ry="6" fill="#fff" stroke="{OUT}" stroke-width="1.5"/><circle cx="{ax+9}" cy="{ay-5}" r="4" fill="#fff" stroke="{OUT}" stroke-width="1.5"/>')
b.append(text(400, 384, "cães, gansos e", 11, "#222", True)); b.append(text(400, 397, "galinhas-d'angola", 11, "#222", True))
b.append(text(400, 410, "(alarme vivo)", 11, "#444"))
# horta
b.append(f'<rect x="470" y="180" width="80" height="110" fill="#d8f0d0" stroke="{VERDE}" stroke-width="1.5"/>')
for yy in range(192, 290, 14):
    b.append(f'<line x1="476" y1="{yy}" x2="544" y2="{yy}" stroke="{VERDE}" stroke-width="2" stroke-dasharray="3 4"/>')
b.append(text(510, 306, "horta", 11, "#2b6a1e", True, "middle"))
# rota de fuga -> ponto de encontro
b.append(f'<path d="M440 180 L 477 130 L 477 {Y0} L 500 72" fill="none" stroke="{VERDE}" stroke-width="3.5" stroke-dasharray="9 6"/>')
b.append(arrow(492, 86, 502, 68, VERDE, 3.5))
b.append(f'<line x1="508" y1="84" x2="508" y2="54" stroke="{OUT}" stroke-width="2"/><polygon points="508,54 528,60 508,66" fill="{VERDE}" stroke="{OUT}"/>')
b += [text(448, 132, "rota de fuga", 11, VERDE, True, "end"), text(448, 145, "pelos fundos", 11, VERDE, True, "end")]
b += [text(534, 66, "ponto de", 11, VERDE, True), text(534, 79, "encontro", 11, VERDE, True)]
b.append(box(14, 494, 652, 46, "#fff4e5", "#ef8a2b"))
b += [text(28, 513, "Cada camada AVISA e ATRASA. O objetivo é ver o problema cedo, não brigar:", 12.5, "#222", True),
      text(28, 531, "quem vê primeiro dá o alarme, todos vão para os lugares combinados ou saem pela rota.", 12.5)]
open(D + "camadas-seguranca.svg", "w").write(svg(680, 548, "Segurança em camadas (vista de cima)", "\n".join(b)))


# =====================================================================
# CONTAR COM PALITOS (unidade, dezena, centena)
# =====================================================================
def palito(x, y, h=56, w=5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{min(2, w/2)}" fill="#e8c88a" stroke="#8a6a3a" stroke-width="{1 if w >= 4 else 0.6}"/>')


def dezena(x, y, h=56, w=5, gap=5.5):
    s = "".join(palito(x + i * gap, y, h, w) for i in range(10))
    larg = 9 * gap + w
    s += f'<rect x="{x-2}" y="{y+h/2-max(2, h/14)}" width="{larg+4}" height="{max(4, h/7)}" rx="2" fill="{PERIGO}" stroke="{OUT}" stroke-width="0.8"/>'
    return s


def centena(x, y, h, w, gap, dx, dy):
    """10 dezenas em 2 fileiras de 5, cercadas por um cordao azul."""
    s = ""
    for i in range(10):
        s += dezena(x + (i % 5) * dx, y + (i // 5) * dy, h, w, gap)
    larg = 4 * dx + 9 * gap + w
    s += f'<rect x="{x-6}" y="{y-5}" width="{larg+12}" height="{dy+h+10}" rx="6" fill="none" stroke="#1e5aa8" stroke-width="3"/>'
    return s


b = []
b.append(palito(60, 70))
b += [text(62, 148, "1 palito", 13, "#222", True, "middle"), text(62, 164, "= 1 UNIDADE", 12.5, "#2b6a1e", True, "middle")]
b.append(dezena(170, 70))
b += [text(198, 148, "10 palitos amarrados", 13, "#222", True, "middle"), text(198, 164, "= 1 DEZENA", 12.5, "#2b6a1e", True, "middle")]
b.append(centena(370, 62, 30, 3, 3.6, 56, 38))
b += [text(500, 148, "10 dezenas amarradas", 13, "#222", True, "middle"), text(500, 164, "= 1 CENTENA (100)", 12.5, "#2b6a1e", True, "middle")]
b.append(f'<line x1="14" y1="180" x2="666" y2="180" stroke="#ccc" stroke-width="2"/>')
# quadro valor de lugar com 234
b.append(text(20, 204, "Quadro de valor: o número 234", 14, "#222", True))
cols = [("C", "centenas"), ("D", "dezenas"), ("U", "unidades")]
x0 = 20; cw = 200; y0 = 216
for i, (c, nome) in enumerate(cols):
    x = x0 + i * (cw + 10)
    b.append(f'<rect x="{x}" y="{y0}" width="{cw}" height="150" rx="6" fill="#fafafa" stroke="#777" stroke-width="1.5"/>')
    b.append(f'<rect x="{x}" y="{y0}" width="{cw}" height="26" rx="6" fill="#e8e8e8" stroke="#777" stroke-width="1.5"/>')
    b.append(text(x + cw / 2, y0 + 18, f"{c} — {nome}", 12.5, "#222", True, "middle"))
for k in range(2):
    b.append(centena(34 + k * 98, 256, 22, 1.4, 1.75, 17, 28))
for k in range(3):
    b.append(dezena(238 + k * 64, 254, 44))
for k in range(4):
    b.append(palito(450 + k * 18, 254, 44))
for i, n in enumerate("234"):
    b.append(text(x0 + i * (cw + 10) + cw / 2, 352, n, 34, "#1e5aa8", True, "middle"))
b.append(box(14, 380, 652, 64, "#eef7ff", "#3f6d9e"))
b += [text(28, 401, "\"Vai um\": 8 + 5 = 13 palitos soltos. Amarre 10 (vira 1 dezena) e sobram 3 soltos:", 12.5),
      text(28, 419, "1 dezena e 3 unidades = 13. Pegar emprestado é o contrário: desamarre uma dezena.", 12.5),
      text(28, 437, "Serve também com feijão em copinhos, pedrinhas ou tampinhas.", 12.5, "#444")]
open(D + "palitos-dezena.svg", "w").write(svg(680, 452, "Contar com palitos: unidade, dezena, centena", "\n".join(b)))
print("ok")
