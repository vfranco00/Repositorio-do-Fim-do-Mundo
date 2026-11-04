import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
# Figuras de 07-abrigo-e-construcao/05-telhados-e-conforto.md
import math
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "07-abrigo-e-construcao", "img") + "/"
os.makedirs(D, exist_ok=True)
WOOD = "#8b5a2b"; SOLO = "#e8d3b0"; AGUA = "#4a90d9"; VERDE = "#2b8a3e"; PERIGO = "#d62828"
TELHA = "#c8553d"; PAREDE = "#f3ece0"; SOL = "#f2b705"; QUENTE = "#e8590c"

def ln(x1, y1, x2, y2, c=OUT, w=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"{d}/>'
def rc(x, y, w, h, fill, stroke=OUT, sw=2, rx=0):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def pg(pts, fill, stroke=OUT, sw=2, op=None):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    o = f' fill-opacity="{op}"' if op is not None else ''
    return f'<polygon points="{p}" fill="{fill}"{o} stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'
def ci(cx, cy, r, fill, stroke=OUT, sw=2):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def tl(x, y, linhas, size=12, color="#222", bold=False, anchor="start", dy=None):
    dy = dy or size * 1.3
    return "".join(text(x, y + i * dy, s, size, color, bold, anchor) for i, s in enumerate(linhas))
def sol(x, y, r=16):
    s = ""
    for i in range(8):
        a = i * math.pi / 4
        s += ln(x + math.cos(a) * (r + 4), y + math.sin(a) * (r + 4), x + math.cos(a) * (r + 11), y + math.sin(a) * (r + 11), SOL, 3)
    return s + ci(x, y, r, SOL, "#b07d00", 2)
def curva(d, cor, w=3):
    return f'<path d="{d}" fill="none" stroke="{cor}" stroke-width="{w}" stroke-linecap="round"/>'

# =====================================================================
# 1) CASA FRESCA EM CORTE
# =====================================================================
b = []
GY = 440
b.append(rc(0, GY, 680, 34, SOLO, "none", 0)); b.append(ln(0, GY, 680, GY, "#6b4f2a", 3))
b.append(text(16, 64, "NORTE", 13, "#555", True)); b.append(text(664, 64, "SUL", 13, "#555", True, "end"))
# árvore (lado direito)
b.append(rc(616, 320, 16, GY - 320, WOOD, OUT, 2))
b.append(ci(624, 300, 36, "#5f9e4f") + ci(596, 318, 24, "#6fae5c") + ci(652, 318, 24, "#6fae5c"))
# embasamento e calçada
WL, WR, WT = 200, 480, 262
b.append(rc(WL - 6, 418, WR - WL + 26, 22, "#b5b5b5", OUT, 2))
b.append(pg([(WL - 60, GY - 1), (WL - 6, GY - 5), (WL - 6, GY), (WL - 60, GY + 3)], "#bbb", OUT, 1.5))
b.append(pg([(WR + 20, GY - 5), (WR + 74, GY - 1), (WR + 74, GY + 3), (WR + 20, GY)], "#bbb", OUT, 1.5))
# interior
b.append(rc(WL + 14, WT, WR - WL - 14, 418 - WT, "#fffaf0", "none", 0))
# paredes com janelas
def parede(x, jy1, jy2):
    s = rc(x, WT, 14, jy1 - WT, PAREDE, OUT, 2) + rc(x, jy2, 14, 418 - jy2, PAREDE, OUT, 2)
    s += rc(x + 2, jy1, 10, jy2 - jy1, "#cfe6fb", OUT, 1.2)
    return s
b.append(parede(WL, 318, 384)); b.append(parede(WR, 276, 322))
# forro
b.append(rc(WL, WT - 6, WR - WL + 14, 8, "#d8b98a", OUT, 1.5))
# telhado com lanternim
ap = (347, 166); eL = (128, 274); eR = (566, 274)
def roof_pt(p1, p2, t):
    return (p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t)
gL = roof_pt(eL, ap, 0.86); gR = roof_pt(eR, ap, 0.86)
b.append(pg([eL, gL, (gL[0], gL[1] + 10), (eL[0], eL[1] + 10)], "#f4efe6", OUT, 2.5))
b.append(pg([eR, gR, (gR[0], gR[1] + 10), (eR[0], eR[1] + 10)], "#f4efe6", OUT, 2.5))
b.append(pg([(ap[0] - 50, ap[1] + 18), (ap[0], ap[1] - 14), (ap[0] + 50, ap[1] + 18), (ap[0] + 50, ap[1] + 26), (ap[0], ap[1] - 6), (ap[0] - 50, ap[1] + 26)], "#f4efe6", OUT, 2.5))
# manta refletora sob a telha
b.append(curva(f"M{eL[0]+70} {eL[1]-24} L{gL[0]-6} {gL[1]+16}", "#9aa5b1", 3))
# ar do sótão: entra no beiral, sai no lanternim
b.append(arrow(WL - 30, 286, WL + 40, 250, QUENTE, 2.5))
b.append(arrow(WR + 44, 286, WR - 26, 250, QUENTE, 2.5))
for dx in (-16, 16):
    b.append(arrow(ap[0] + dx, 214, ap[0] + dx * 1.8, 154, QUENTE, 3))
# ventilação cruzada
b.append(arrow(70, 352, WL - 8, 352, AGUA, 4))
b.append(curva(f"M{WL+20} 352 C {WL+120} 352, {WR-120} 300, {WR-6} 298", AGUA, 4))
b.append(arrow(WR + 20, 298, WR + 70, 290, AGUA, 4))
b.append(text(24, 344, "vento", 12, "#1d5fa8", True))
# sol de inverno (baixo) e de verão (alto)
b.append(sol(54, 214, 14))
b.append(ln(72, 228, 238, 404, SOL, 3, "8 5"))
b.append(sol(158, 84, 14))
b.append(ln(159, 106, 166, 250, SOL, 3, "8 5"))
b.append(pg([(128, 285), (200, 285), (200, 330)], "#000", "none", 0, 0.12))
b += [tl(178, 80, ["sol de verão (alto): bate no", "telhado; o beiral faz sombra"], 11.5, "#8a6100", True)]
b += [tl(10, 170, ["sol de inverno (baixo):", "entra pela janela"], 11.5, "#8a6100", True)]
# rótulos
b += [tl(400, 104, ["ar quente sai pelo", "lanternim (topo)"], 11.5, QUENTE, True)]
b.append(ln(398, 112, 372, 150, "#555", 1.2))
b += [tl(452, 172, ["telhado claro"], 11.5, "#222", True)]
b += [tl(232, 304, ["forro + colchão de ar ventilado;", "manta refletora sob a telha"], 11, "#444")]
b.append(ln(300, 288, 290, 252, "#555", 1.2))
b += [tl(232, 392, ["janelas grandes do lado do vento,", "saída alta do lado oposto"], 11, "#1d5fa8", True)]
b += [tl(WR - 122, 284, ["pé-direito 2,8–3 m"], 11, "#444")]
b += [tl(10, 268, ["beiral largo"], 11.5, "#222", True)]
b.append(ln(80, 264, eL[0] + 6, eL[1] + 4, "#555", 1.2))
b += [tl(560, 220, ["árvore e", "varanda:", "sombra"], 11.5, VERDE, True)]
b += [tl(420, 466, ["piso acima do chão, calçada em volta"], 11, "#222")]
b += [tl(10, 466, ["paredes claras (cal)"], 11, "#222")]
# caixa por clima
b.append(box(14, 486, 652, 92, "#eef5ff", "#3f6d9e"))
b += [text(26, 506, "Calor úmido (litoral, Norte): casa leve, aberta, sombreada, piso elevado; paredes grossas ajudam pouco.", 11.5),
      text(26, 524, "Calor de dia e frio à noite (sertão, cerrado, serras): paredes grossas de terra ou pedra (massa térmica).", 11.5),
      text(26, 542, "Inverno frio (Sul, serras): janelas para o NORTE, frestas vedadas, forro isolado, fogão a lenha no centro.", 11.5),
      text(26, 562, "Do Sudeste ao Sul o sol fica ao norte quase o ano todo; perto do Equador, quase a pino.", 11.5, "#1e3a5f", True)]
open(D + "casa-conforto.svg", "w").write(svg(680, 588, "Casa fresca e confortável (corte, sul do Equador)", "\n".join(b)))

# =====================================================================
# 2) INCLINAÇÃO MÍNIMA DE CADA COBERTURA
# =====================================================================
b = []
ox, oy, Lr = 70, 330, 330
b.append(ln(ox, oy, ox + Lr + 30, oy, "#444", 2))
b.append(text(ox + Lr + 34, oy + 4, "0%", 11.5, "#444", True))
tipos = [(10, "10% (~6°): telha metálica", "#6c757d"), (15, "15% (~9°): fibrocimento ondulada", "#495057"),
         (30, "30–35% (17–19°): telha cerâmica", TELHA), (45, "45% (~24°): tabuinhas de madeira", WOOD),
         (100, "100% (45°) ou mais: sapé e palha", "#a68a2c")]
for pct, lab, cor in tipos:
    a = math.atan(pct / 100)
    ex, ey = ox + Lr * math.cos(a), oy - Lr * math.sin(a)
    b.append(ln(ox, oy, ex, ey, cor, 5))
    yy = ey + 4
    if pct == 10: yy = ey + 10
    if pct == 15: yy = ey - 2
    b.append(text(ex + 10, yy, lab, 12, cor, True))
b.append(ci(ox, oy, 5, OUT, OUT, 1))
b.append(text(ox, oy + 22, "Mínimos usuais. Mais inclinado escorre melhor; siga o fabricante da telha.", 11.5, "#444"))
# como medir a porcentagem
b.append(box(14, 372, 652, 108, "#eef5ff", "#3f6d9e"))
tx0, ty0 = 40, 458
b.append(pg([(tx0, ty0), (tx0 + 200, ty0), (tx0 + 200, ty0 - 60)], "#f6d7cf", OUT, 2))
b.append(text(tx0 + 100, ty0 + 16, "1 m na horizontal", 11, "#222", True, "middle"))
b.append(text(tx0 + 206, ty0 - 26, "sobe 30 cm", 11, "#b3001b", True))
b.append(text(tx0 + 120, ty0 - 46, "= 30%", 13, "#b3001b", True, "end"))
b += [tl(330, 396, ["% = quanto o telhado sobe para cada 1 m deitado.", "Ex.: meia-água com 4 m de largura a 30%:", "sobe 4 × 0,30 = 1,20 m.", "Meça com régua de 1 m + nível de bolha."], 11.5, "#1e3a5f")]
open(D + "inclinacao-telhados.svg", "w").write(svg(680, 490, "Inclinação mínima de cada tipo de cobertura", "\n".join(b)))
print("ok")
