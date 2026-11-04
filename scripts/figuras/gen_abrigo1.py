import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
# Figuras de 07-abrigo-e-construcao/01-abrigo-emergencial.md
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "07-abrigo-e-construcao", "img") + "/"
os.makedirs(D, exist_ok=True)
WOOD = "#8b5a2b"; SOLO = "#e8d3b0"; AGUA = "#4a90d9"; AGUA2 = "#cfe6fb"; VERDE = "#2b8a3e"; PERIGO = "#d62828"
LONA = "#3f7fbf"; LONA2 = "#2a5d91"; FOLHA = "#b5a04a"

# ---------- funções auxiliares (só deste gerador) ----------
def ln(x1, y1, x2, y2, c=OUT, w=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"{d}/>'
def rc(x, y, w, h, fill, stroke=OUT, sw=2, rx=0):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def pg(pts, fill, stroke=OUT, sw=2, op=None):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    o = f' fill-opacity="{op}"' if op is not None else ''
    return f'<polygon points="{p}" fill="{fill}"{o} stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'
def pl(pts, c=OUT, w=2, dash=None):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<polyline points="{p}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{d}/>'
def ci(cx, cy, r, fill, stroke=OUT, sw=2):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def tl(x, y, linhas, size=12, color="#222", bold=False, anchor="start", dy=None):
    dy = dy or size * 1.3
    return "".join(text(x, y + i * dy, s, size, color, bold, anchor) for i, s in enumerate(linhas))
def chuva(x0, y0, w, h, n=14, dx=-6, seed=3):
    import random; r = random.Random(seed); s = []
    for i in range(n):
        x = x0 + r.random() * w; y = y0 + r.random() * h
        s.append(ln(x, y, x + dx, y + 14, AGUA, 2))
    return "".join(s)
def arvore(x, ybase, h, r=34, morta=False):
    s = rc(x - 7, ybase - h, 14, h, WOOD)
    if not morta:
        s += ci(x, ybase - h - r * 0.6, r, "#5f9e4f") + ci(x - r * 0.7, ybase - h - r * 0.1, r * 0.7, "#6fae5c") + ci(x + r * 0.7, ybase - h - r * 0.1, r * 0.7, "#6fae5c")
    return s
def estaca(x, y, ang=1):  # ang=1 inclina para a direita (topo para fora)
    return ln(x - 8 * ang, y + 10, x + 6 * ang, y - 10, WOOD, 5)

# =====================================================================
# 1) ABRIGO DE LONA: EM "A" E MEIA-ÁGUA
# =====================================================================
b = []
# ---------------- painel 1: abrigo em A (perspectiva) ----------------
b.append(text(20, 58, '1. Abrigo em "A" — protege dos dois lados', 15, "#222", True))
S = 80; OX = 130; OY = 250; KX = -0.5; KY = 0.36
def P3(x, y, z):  # x ao longo da corda, y altura, z para quem olha
    return (OX + x * S + z * S * KX, OY - y * S + z * S * KY)
H = 1.0; Z = 1.12  # corda a 1 m; cada lado 1,5 m -> base 2,24 m
# chão
b.append(pg([P3(-0.85, 0, -1.3), P3(3.9, 0, -1.3), P3(3.9, 0, 1.45), P3(-0.85, 0, 1.45)], "#e4ecd2", "#b9c79a", 1.5))
# valeta (fora da linha onde a água pinga)
b.append(pl([P3(-0.15, 0, 1.3), P3(3.15, 0, 1.3), P3(3.15, 0, -1.27), P3(-0.15, 0, -1.27), P3(-0.15, 0, 1.3)], "#7a5a2a", 4, "8 5"))
# árvores
for xx in (3.6, -0.7):
    tx_, ty_ = P3(xx, 0, 0)
    b.append(arvore(tx_, ty_, 120, 28))
# estacas de trás (a da esquerda fica escondida)
for xx in (0, 3):
    px, py = P3(xx, 0, -Z); b.append(estaca(px + 4, py - 4, 1))
# face de trás (vista por dentro na ponta aberta)
b.append(pg([P3(0, H, 0), P3(3, H, 0), P3(3, 0, -Z), P3(0, 0, -Z)], LONA2))
# cama de folhas
b.append(pg([P3(0.3, 0.0, Z * 0.8), P3(3, 0, Z * 0.8), P3(3, 0.0, -Z * 0.8), P3(0.3, 0, -Z * 0.8)], FOLHA, OUT, 1.5))
# corda da cumeeira (de árvore a árvore)
ax, ay = P3(-0.7, 1.0, 0); bx, by = P3(3.6, 1.0, 0)
b.append(ln(ax, ay, bx, by, "#c47b12", 3))
# face da frente
b.append(pg([P3(0, H, 0), P3(3, H, 0), P3(3, 0, Z), P3(0, 0, Z)], LONA, OUT, 2.5))
b.append(pl([P3(0, H, 0), P3(0, 0, Z)], "#2a5d91", 1.5, "5 4"))
b.append(pl([P3(1.5, H, 0), P3(1.5, 0, Z)], "#2a5d91", 1.5, "5 4"))
b.append(pl([P3(3, 0, Z), P3(3, H, 0), P3(3, 0, -Z)], OUT, 3))
# estacas da frente
for (xx, sx) in ((0, -1), (3, 1)):
    px, py = P3(xx, 0, Z); b.append(estaca(px - 2, py + 2, -1))
# pingadeira
px, py = P3(3.3, 1.0, 0); b.append(ln(px, py, px - 2, py + 24, "#c47b12", 2)); b.append(ln(px - 2, py + 28, px - 2, py + 36, AGUA, 2.5))
# chuva
b.append(chuva(150, 116, 210, 36, 12))
# vento na ponta fechada
b.append(arrow(4, 236, 58, 236, "#555", 4)); b.append(text(4, 226, "VENTO", 11.5, "#555", True))
b += [tl(4, 254, ["feche", "esta", "ponta"], 10.5, "#444")]
# rótulos do painel 1
b.append(text(128, 100, "corda da cumeeira a 1–1,2 m do chão", 11.5, "#8a4f00", True))
b.append(ln(250, 104, 250, 166, "#8a4f00", 1.5))
b.append(text(440, 178, "pingadeira", 11, "#222", True))
b.append(ln(438, 175, 398, 188, "#555", 1.2))
b += [tl(432, 256, ["cama de", "folhas 20–30 cm"], 11, "#5a4a10", True)]
b.append(ln(430, 254, 392, 244, "#555", 1.2))
b.append(text(58, 314, "valeta de 10–15 cm em volta, levando a água morro abaixo", 11, "#7a5a2a", True))
# vista de frente com medidas (direita)
b.append(ln(522, 50, 522, 330, "#ccc", 1))
cx0 = 603; gy = 250; s2 = 55
apex = (cx0, gy - 1.0 * s2); L_ = (cx0 - 1.12 * s2, gy); R_ = (cx0 + 1.12 * s2, gy)
b.append(text(cx0, 70, "vista de frente", 12.5, "#222", True, "middle"))
b += [tl(534, 92, ["lona 3 × 3 m", "dobrada ao meio", "sobre a corda"], 11, "#222")]
b.append(ln(530, gy, 676, gy, "#6b4f2a", 3))
b.append(rc(L_[0] + 12, gy - 12, (R_[0] - L_[0]) - 24, 12, FOLHA, OUT, 1.2))
b.append(pg([apex, L_, R_], LONA, OUT, 0, 0.25))
b.append(pl([L_, apex, R_], LONA2, 5))
b.append(ci(apex[0], apex[1], 4, "#c47b12", OUT, 1.5))
b.append(ln(cx0, apex[1] + 4, cx0, gy - 12, "#444", 1.2, "4 3"))
b.append(text(cx0 + 4, gy - 22, "1 m", 11, "#222", True))
b.append(text(cx0 - 34, gy - 34, "1,5 m", 11, "#222", True, "end"))
b.append(ln(L_[0], gy + 10, R_[0], gy + 10, "#444", 1.2))
b.append(ln(L_[0], gy + 5, L_[0], gy + 15, "#444", 1.2)); b.append(ln(R_[0], gy + 5, R_[0], gy + 15, "#444", 1.2))
b.append(text(cx0, gy + 25, "~2,2 m", 11, "#222", True, "middle"))
b.append(text(cx0, gy + 46, "lados a ~42°", 11, "#b3001b", True, "middle"))
b += [tl(534, 318, ["cabem 2 pessoas deitadas"], 10.5, "#444")]
b.append(ln(14, 340, 666, 340, "#ccc", 1))

# ---------------- painel 2: meia-água (corte lateral) ----------------
b.append(text(20, 368, "2. Meia-água — costas para o vento, frente para o fogo", 15, "#222", True))
G = 640; s = 88
b.append(rc(0, G, 680, 24, SOLO, SOLO, 0))
b.append(ln(0, G, 680, G, "#6b4f2a", 3))
rx_ = 250; ry_ = G - 1.5 * s  # corda a 1,5 m
ex_ = rx_ + 2.6 * s           # lona de 3 m -> 2,6 m na horizontal (30°)
# árvore que segura a corda (vista de lado)
b.append(rc(rx_ - 7, G - 200, 14, 200, WOOD))
b.append(ci(rx_, G - 222, 30, "#5f9e4f") + ci(rx_ - 24, G - 204, 20, "#6fae5c") + ci(rx_ + 24, G - 204, 20, "#6fae5c"))
# cama de folhas e pessoa
b.append(rc(rx_ - 4, G - 22, 196, 22, FOLHA, OUT, 1.5))
b.append(limb([(rx_ + 30, G - 32), (rx_ + 140, G - 32)], 22, "#6f8aa3")); b.append(head(rx_ + 14, G - 34, 13, "#6f8aa3"))
# lona
b.append(ln(rx_, ry_, ex_, G, LONA2, 7)); b.append(ln(rx_, ry_, ex_, G, LONA, 4))
b.append(ci(rx_, ry_, 6, "#c47b12", OUT, 2))
b.append(estaca(ex_ + 10, G - 4, 1))
# valeta atrás
b.append(f'<path d="M{ex_+22:.0f} {G} q 11 18 24 0" fill="#9fc5ec" stroke="{OUT}" stroke-width="2"/>')
# água escorrendo sobre a lona
b.append(arrow(rx_ + 74, ry_ + 26, rx_ + 164, ry_ + 78, AGUA, 3))
# vento e chuva pelas costas
for yy in (G - 140, G - 100, G - 60):
    b.append(arrow(676, yy, 606, yy, "#555", 3.5))
b.append(text(676, G - 156, "VENTO", 12, "#555", True, "end"))
b.append(chuva(520, 392, 150, 40, 10, -10, 7))
# fogueira e refletor
fx = 140
b.append(f'<path d="M{fx-22} {G} q 6 -34 22 -48 q 4 22 12 26 q 6 -10 4 -22 q 14 18 6 44 Z" fill="#f08c00" stroke="{OUT}" stroke-width="2"/>')
b.append(ln(fx - 26, G - 3, fx + 26, G - 3, WOOD, 7))
for i in range(5):
    b.append(rc(26, G - 18 - i * 17, 30, 17, WOOD, OUT, 1.5, 6))
b.append(ln(22, G, 22, G - 102, "#5b3a1a", 4)); b.append(ln(60, G, 60, G - 102, "#5b3a1a", 4))
b.append(arrow(fx + 26, G - 26, rx_ - 14, G - 30, "#f08c00", 3))
b.append(arrow(64, G - 66, rx_ - 14, G - 58, "#f08c00", 3))
b.append(text(150, G - 70, "calor refletido", 10.5, "#a35a00", True))
b.append(text(170, G - 34, "direto", 10.5, "#a35a00", True))
# rótulos painel 2
b += [tl(300, 470, ["corda a 1,5 m: lona a ~30°", "corda a 2 m: ~40° (melhor em chuva forte)"], 11.5, "#8a4f00", True)]
b.append(ln(298, 476, 258, 503, "#8a4f00", 1.5))
b += [tl(16, 398, ["parede refletora: troncos", "entre estacas, ~1 m de altura"], 11, "#222")]
b.append(ln(40, 418, 40, 534, "#555", 1.2))
b += [tl(78, 462, ["fogo a 1,5–2 m", "da lona (ela", "derrete e pega fogo)"], 11, "#b3001b", True)]
b.append(text(232, 657, "cama de folhas 20–30 cm", 11, "#5a4a10", True))
b.append(text(412, 659, "borda presa no chão", 11, "#222", True))
b.append(text(ex_ + 50, G - 6, "valeta", 11, "#7a5a2a", True))

# ---------------- caixa: amarrações ----------------
b.append(box(14, 676, 652, 110, "#eef5ff", "#3f6d9e"))
b += [text(26, 696, "Amarrações", 13, "#1e3a5f", True),
      text(26, 715, "• Corda da cumeeira: lais de guia numa árvore e nó de caminhoneiro na outra (estica e solta fácil).", 11.5),
      text(26, 732, "• Estacas de 25–30 cm cravadas inclinadas 45°, com a cabeça para FORA do abrigo.", 11.5),
      text(26, 749, "• Lona sem ilhós: embrulhe uma pedrinha na ponta, amarre a corda por trás dela (não rasga).", 11.5),
      text(26, 766, "• Lona bem esticada, sem barriga: água empoçada pesa e rasga. Confira os nós antes de dormir.", 11.5)]
open(D + "abrigo-lona.svg", "w").write(svg(680, 796, 'Abrigos com uma lona de 3 × 3 m', "\n".join(b)))

# =====================================================================
# 2) ONDE MONTAR O ABRIGO (perfil do terreno)
# =====================================================================
b = []
terr = [(0, 110), (30, 118), (190, 330), (200, 334), (270, 334), (280, 330), (345, 330), (352, 334), (360, 346), (378, 346),
        (386, 334), (392, 330), (440, 282), (460, 272), (560, 272), (640, 150), (680, 140)]
b.append(pg(terr + [(680, 420), (0, 420)], SOLO, "#6b4f2a", 2.5))
# rio
b.append(f'<path d="M196 332 Q 235 368 274 332 Z" fill="{AGUA}" stroke="{OUT}" stroke-width="2"/>')
b.append(text(235, 350, "rio", 11, "#fff", True, "middle"))
# marca de cheia
b.append(ln(150, 298, 424, 298, AGUA, 2.5, "8 5"))
b.append(text(150, 292, "marca da última cheia", 11, "#1d5fa8", True))
# leito seco com pedras
for (x, y) in ((362, 342), (369, 343), (375, 341), (366, 337)):
    b.append(ci(x, y, 3, "#9a9a9a", OUT, 1))
# encosta: árvore torta, trincas, água brotando
b.append(f'<g transform="rotate(20 80 178)">{arvore(80, 178, 56, 18)}</g>')
b.append(pl([(116, 222), (124, 232), (118, 240), (128, 252)], OUT, 2.5))
b.append(pl([(140, 254), (147, 263), (142, 270), (150, 280)], OUT, 2.5))
b.append(f'<path d="M160 290 q 10 6 20 4" fill="none" stroke="{AGUA}" stroke-width="3"/>')
# árvore com galho seco na baixada
b.append(arvore(318, 330, 80, 24))
b.append(pl([(322, 268), (352, 250), (372, 252)], "#7b6a58", 5)); b.append(pl([(352, 250), (360, 234)], "#7b6a58", 4))
# patamar bom: barraca e mata atrás
b.append(pg([(470, 272), (500, 240), (530, 272)], LONA, OUT, 2)); b.append(ln(500, 240, 500, 272, LONA2, 2))
for (x, base, h) in ((622, 178, 40), (650, 145, 36), (672, 141, 34)):
    b.append(arvore(x, base, h, 18))
# vento por cima do morro
b.append(arrow(676, 70, 616, 70, "#555", 3)); b.append(text(574, 74, "vento", 11, "#555", True))

def marca_x(x, y):
    return ci(x, y, 10, PERIGO, OUT, 1.5) + ln(x - 4.5, y - 4.5, x + 4.5, y + 4.5, "#fff", 3) + ln(x - 4.5, y + 4.5, x + 4.5, y - 4.5, "#fff", 3)
def marca_ok(x, y):
    return ci(x, y, 10, VERDE, OUT, 1.5) + pl([(x - 5, y), (x - 1, y + 5), (x + 6, y - 5)], "#fff", 3)

b.append(marca_x(24, 60)); b += [tl(40, 58, ["encosta íngreme: trincas, árvores", "tortas, água brotando = deslizamento"], 11.5, "#b3001b", True)]
b.append(marca_x(180, 150)); b += [tl(196, 148, ["galho seco em cima", "(cai com vento ou chuva)"], 11.5, "#b3001b", True)]
b.append(ln(300, 168, 346, 246, "#b3001b", 1.2))
b.append(marca_x(396, 52)); b += [tl(412, 56, ["topo: vento forte e raio"], 11.5, "#b3001b", True)]
b.append(marca_ok(380, 170)); b += [tl(396, 168, ["BOM: plano, pouco elevado,", "acima da marca de cheia,", "a mais de 50 m da água,", "mata quebrando o vento"], 11.5, "#1f6b2e", True)]
b.append(ln(470, 222, 494, 246, "#1f6b2e", 1.2))
b.append(marca_x(100, 380)); b += [tl(116, 378, ["beira do rio e baixada:", "enche, junta ar frio e mosquito"], 11.5, "#b3001b", True)]
b.append(marca_x(372, 380)); b += [tl(388, 378, ["leito seco: enxurrada", "de repente (cabeça-d'água)"], 11.5, "#b3001b", True)]
open(D + "local-abrigo.svg", "w").write(svg(680, 420, "Onde montar (e onde NÃO montar) o abrigo", "\n".join(b)))
print("ok")
