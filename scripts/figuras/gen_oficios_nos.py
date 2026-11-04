import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
# Diagramas de nos e cordas (09-quimica-e-oficios). Corda desenhada como faixa larga com
# contorno; cruzamentos por camadas (z): o trecho de z maior passa POR CIMA.
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "09-quimica-e-oficios", "img") + "/"
os.makedirs(D, exist_ok=True)
import math

LAR = ("#f08c2b", "#b8600f")   # laranja: ponta de trabalho
AZU = ("#6aa4dc", "#2f6ea8")   # azul: parte firme
WOOD = "#8b5a2b"

def lbl(x, y, s, size=12, color="#222", bold=False, anchor="start"):
    b = ' font-weight="bold"' if bold else ''
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}"{b} text-anchor="{anchor}" '
            f'stroke="#fff" stroke-width="4" stroke-linejoin="round" paint-order="stroke">{s}</text>')

def _bez(P):
    n = len(P); out = []
    for i in range(n - 1):
        p0, p1 = P[i], P[i + 1]
        pm = P[i - 1] if i > 0 else p0
        p2 = P[i + 2] if i + 2 < n else p1
        c1 = (p0[0] + (p1[0] - pm[0]) / 6, p0[1] + (p1[1] - pm[1]) / 6)
        c2 = (p1[0] - (p2[0] - p0[0]) / 6, p1[1] - (p2[1] - p0[1]) / 6)
        out.append((p0, c1, c2, p1))
    return out

class Cena:
    """Junta cordas e objetos e desenha na ordem de z."""
    def __init__(self, fantasma=False):
        self.items = []; self.seq = 0; self.fantasma = fantasma
    def add(self, z, s):
        self.items.append((z, self.seq, s)); self.seq += 1
    def corda(self, legs, w=12, ox=0, oy=0, fim=True, inicio=False, dobras=()):
        """legs: lista de (z, cor, [(x,y),...]); o ultimo ponto de um trecho e o primeiro do seguinte.
        dobras: indices de juncoes entre trechos onde a corda dobra (borda de poste): desenha contorno."""
        P = []; spans = []
        for k, (z, cor, pts) in enumerate(legs):
            pts = [(x + ox, y + oy) for x, y in pts]
            if k == 0:
                P.append(pts[0])
            for p in pts[1:]:
                P.append(p); spans.append((z, cor, k))
        B = _bez(P)
        # agrupa trechos consecutivos de mesmo leg
        groups = []
        for i, (z, cor, k) in enumerate(spans):
            if groups and groups[-1][2] == k:
                groups[-1][3].append(B[i])
            else:
                groups.append([z, cor, k, [B[i]]])
        W = w + 4.5
        for gi, (z, cor, k, segs) in enumerate(groups):
            d = "M%.1f %.1f" % segs[0][0]
            for (p0, c1, c2, p1) in segs:
                d += " C%.1f %.1f %.1f %.1f %.1f %.1f" % (c1 + c2 + p1)
            s = f'<path d="{d}" fill="none" stroke="{OUT}" stroke-width="{W}" stroke-linecap="butt" stroke-linejoin="round"/>'
            ends = []
            if gi == 0 and inicio: ends.append(segs[0][0])
            if gi == len(groups) - 1 and fim: ends.append(segs[-1][3])
            if gi in dobras: ends.append(segs[0][0])
            if gi + 1 in dobras: ends.append(segs[-1][3])
            for (x, y) in ends:
                s += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{W/2:.1f}" fill="{OUT}"/>'
            s += f'<path d="{d}" fill="none" stroke="{cor[0]}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
            s += f'<path d="{d}" fill="none" stroke="{cor[1]}" stroke-width="{w-3}" stroke-dasharray="1.6 5" stroke-opacity="0.55"/>'
            self.add(z, s)
            if z < 0 and self.fantasma:   # trecho escondido: desenha "fantasma" tracejado por cima do poste
                self.add(0.5, f'<path d="{d}" fill="none" stroke="{cor[0]}" stroke-width="{w}" stroke-opacity="0.35" stroke-linecap="round"/>'
                              f'<path d="{d}" fill="none" stroke="{OUT}" stroke-width="1.6" stroke-dasharray="4 4"/>')
    def svg(self):
        return "\n".join(s for z, q, s in sorted(self.items, key=lambda t: (t[0], t[1])))

def painel(x, y, w, h, n, linhas, clip_id):
    s = f'<clipPath id="{clip_id}"><rect x="{x}" y="{y+66}" width="{w}" height="{h-66}" rx="8"/></clipPath>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#f6f3ee" stroke="#c9bba0" stroke-width="1.5"/>'
    s += f'<circle cx="{x+18}" cy="{y+20}" r="12" fill="#1e1e1e"/>' + text(x + 18, y + 25, str(n), 14, "#fff", True, "middle")
    for i, t in enumerate(linhas):
        s += text(x + 36 if i == 0 else x + 12, y + 25 + 16 * i, t, 12.5 if i == 0 else 12, "#222", i == 0)
    return s

PX = [8, 232, 456]; PW = 216

# =====================================================================
# VOLTA DO FIEL (clove hitch) em poste vertical
# =====================================================================
def poste(c, cx, top, bot, R):
    c.add(0, f'<rect x="{cx-R}" y="{top}" width="{2*R}" height="{bot-top}" fill="{WOOD}" stroke="{OUT}" stroke-width="2.5"/>'
             f'<rect x="{cx-R+6}" y="{top}" width="7" height="{bot-top}" fill="#a87443" opacity="0.7"/>'
             f'<ellipse cx="{cx}" cy="{top}" rx="{R}" ry="7" fill="#c89a62" stroke="{OUT}" stroke-width="2.5"/>')

def fiel(etapa, ox, oy):
    c = Cena(fantasma=True); R = 24; w = 13
    poste(c, ox, oy - 108, oy + 92, R)
    legs = [
        (1, AZU, [(-140, 12), (-70, 12), (-R - 6, 12), (0, 12), (R + 7, 13)]),     # parte firme pela frente
        (-1, AZU, [(R + 7, 13), (R - 4, 19), (0, 23), (-R + 4, 27), (-R - 7, 31)]),  # por tras
    ]
    if etapa == 1:
        legs.append((1, LAR, [(-R - 7, 31), (-R - 20, 40), (-56, 58), (-68, 74)]))
        c.corda(legs, w=w, ox=ox, oy=oy, dobras=(1,))
    else:
        legs.append((2, LAR, [(-R - 7, 31), (-R + 4, 33), (0, 4), (R - 4, -25), (R + 7, -29)]))  # diagonal por cima
        legs.append((-1, LAR, [(R + 7, -29), (R - 4, -24), (0, -18), (-R + 4, -14), (-R - 7, -12)]))
        if etapa == 2:
            legs.append((1, LAR, [(-R - 7, -12), (-R - 20, -16), (-56, -30), (-68, -46)]))
        else:
            legs.append((1, LAR, [(-R - 7, -12), (-R + 4, -12), (0, -12), (R + 8, -12), (60, -13), (84, -16)]))
        c.corda(legs, w=w, ox=ox, oy=oy, dobras=(1, 2, 3, 4))
    return c.svg()

b = []
oy = 222
txt = [["Dê uma volta", "no poste."],
       ["Cruze POR CIMA,", "em diagonal, e dê", "outra volta."],
       ["Passe a ponta POR", "BAIXO da diagonal.", "Puxe as duas pontas."]]
for i in range(3):
    b.append(painel(PX[i], 44, PW, 300, i + 1, txt[i], f"cf{i}"))
    b.append(f'<g clip-path="url(#cf{i})">' + fiel(i + 1, PX[i] + 108, oy) + '</g>')
for i in (0, 2):
    b.append(lbl(PX[i] + 10, oy - 6, "parte firme", 11.5, "#1d4f80", True))
b.append(lbl(PX[0] + 12, oy + 92, "ponta", 11.5, "#a04d00", True))
b.append(lbl(PX[2] + 160, oy - 24, "ponta", 11.5, "#a04d00", True))
b.append(lbl(PX[2] + 108, oy + 62, "a diagonal prende", 11, "#222", True, "middle"))
b.append(lbl(PX[2] + 108, oy + 76, "as duas pontas", 11, "#222", True, "middle"))
b.append(text(PX[1] + 108, 336, "tracejado = por trás do poste", 11, "#555", False, "middle"))
b.append(box(8, 354, 664, 50, "#eef5ff", "#3f6d9e"))
b.append(text(20, 374, "Usos: começar e terminar amarrações de bambu/varas, prender corda a poste ou estaca.", 12.5))
b.append(text(20, 392, "Pode escorregar se a carga balança ou gira: para carga séria, use volta redonda com dois cotes.", 12.5, "#b3001b"))
open(D + "volta-do-fiel.svg", "w").write(svg(680, 412, "Volta do fiel (prender corda em poste)", "\n".join(b)))

# =====================================================================
# LAIS DE GUIA (bowline)
# =====================================================================
def lais(etapa, ox, oy):
    c = Cena(); k = 1.3
    L = [
        (0, AZU, [(0, -150), (0, -100), (0, -70)]),
        (-1, AZU, [(0, -70), (0, -48), (-4, -36), (-14, -24)]),
        (0, AZU, [(-14, -24), (-24, -10), (-26, 6), (-18, 20), (0, 27), (18, 20), (26, 4), (23, -12)]),
        (1, AZU, [(23, -12), (14, -26), (4, -36), (-8, -44), (-22, -46)]),
        (0, AZU, [(-22, -46), (-36, -38), (-46, -18), (-50, 20), (-48, 66), (-36, 98), (0, 110)]),
    ]
    if etapa == 1:
        L.append((0, LAR, [(0, 110), (36, 98), (48, 66), (42, 50), (28, 44), (20, 38)]))
    else:
        L.append((0, LAR, [(0, 110), (36, 98), (48, 66), (40, 48), (22, 40), (15, 32)]))
        L.append((-1, LAR, [(15, 32), (15, 21), (15, 10)]))
        L.append((1, LAR, [(15, 10), (15, -10), (15, -24), (15, -40), (15, -62), (12, -76)]))
        L.append((-1, LAR, [(12, -76), (0, -86), (-12, -76)]))
        if etapa == 2:
            L.append((2, LAR, [(-12, -76), (-15, -62), (-16, -52)]))
        else:
            L.append((2, LAR, [(-12, -76), (-15, -62), (-15, -45), (-15, -22), (-15, 4)]))
            L.append((-1, LAR, [(-15, 4), (-15, 21), (-15, 36)]))
            L.append((1, LAR, [(-15, 36), (-16, 52), (-17, 64)]))
    L = [(z, cor, [(x * k, y * k) for x, y in pts]) for z, cor, pts in L]
    c.corda(L, w=11, ox=ox, oy=oy)
    return c.svg()

b = []
oy = 222
txt = [["Faça uma argola", "pequena (o \"buraco\")", "com a ponta POR CIMA."],
       ["A ponta sobe POR", "DENTRO do buraco e", "passa POR TRÁS."],
       ["Desce de volta pelo", "buraco. Aperte puxando", "a parte firme."]]
for i in range(3):
    b.append(painel(PX[i], 44, PW, 360, i + 1, txt[i], f"cl{i}"))
    b.append(f'<g clip-path="url(#cl{i})">' + lais(i + 1, PX[i] + 112, oy + 30) + '</g>')
b.append(lbl(PX[0] + 120, oy - 70, "parte firme", 11.5, "#1d4f80", True))
b.append(lbl(PX[0] + 152, oy + 30, "buraco", 11.5, "#222", True))
b.append(lbl(PX[0] + 160, oy + 84, "ponta", 11.5, "#a04d00", True))
b.append(lbl(PX[1] + 140, oy - 74, "\"em volta", 11, "#222", True))
b.append(lbl(PX[1] + 140, oy - 60, "da árvore\"", 11, "#222", True))
b.append(lbl(PX[2] + 112, oy + 104, "alça fixa:", 11.5, "#1e6b2e", True, "middle"))
b.append(lbl(PX[2] + 112, oy + 118, "não corre", 11.5, "#1e6b2e", True, "middle"))
b.append(box(8, 414, 664, 84, "#eef5ff", "#3f6d9e"))
b.append(text(20, 434, "\"O coelho sai da toca, dá a volta na árvore e volta para a toca.\"", 12.5, "#222", True))
b.append(text(20, 452, "(toca = buraco; árvore = parte firme; coelho = ponta)", 12.5))
b.append(text(20, 470, "Usos: alça que não aperta (laçar estaca, amarrar barco, resgate em volta do peito).", 12.5))
b.append(text(20, 488, "Deixe sobra de 10–12 cm na ponta. Pode se soltar sem carga: dê um cote extra na ponta.", 12.5, "#b3001b"))
open(D + "lais-de-guia.svg", "w").write(svg(680, 508, "Lais de guia (alça fixa que não corre)", "\n".join(b)))

# =====================================================================
# NO DIREITO (reef knot)
# =====================================================================
def torcao(Y0, H, A, voltas):
    """pontos de duas pernas torcidas (laranja comeca a esquerda); retorna ys e x(y) da laranja"""
    pts = []
    n = int(2 * voltas * 4)
    for k in range(n + 1):
        y = Y0 - k * (2 * H * voltas) / n
        pts.append((-A * math.cos(math.pi * (Y0 - y) / H), y))
    return pts

def direito(etapa, ox, oy):
    c = Cena(); w = 11
    if etapa in (1, 2):
        if etapa == 1:
            Y0, H, A, nv = 40, 40, 20, 1
            sobre = ["L", "A"]          # quem passa por cima em cada cruzamento
        else:
            Y0, H, A, nv = 62, 28, 18, 2
            sobre = ["L", "A", "A", "L"]
        tw = torcao(Y0, H, A, nv)     # pontos a cada H/4
        top = Y0 - 2 * H * nv
        for cor, sg in ((LAR, 1), (AZU, -1)):
            P = [(sg * x, y) for x, y in tw]
            legs = [(0, cor, [(sg * -150, Y0 + 34), (sg * -70, Y0 + 33), (sg * -A - 6, Y0 + 24), P[0], P[1]])]
            # cruzamentos ficam em P[2], P[6], P[10], P[14]
            for k in range(len(sobre)):
                me = "L" if sg == 1 else "A"
                z = 1 if sobre[k] == me else -1
                legs.append((z, cor, [P[4 * k + 1], P[4 * k + 2], P[4 * k + 3]]))
                legs.append((0, cor, [P[4 * k + 3], P[4 * k + 4]] + ([P[4 * k + 5]] if 4 * k + 5 < len(P) else [])))
            last = legs[-1][2][-1]
            legs[-1] = (0, cor, legs[-1][2] + [(sg * -A - 8, top - 18), (sg * -A - 22, top - 36)])
            c.corda(legs, w=w, ox=ox, oy=oy)
    else:
        def S(pts): return [(x * 0.92, y * 1.5) for x, y in pts]
        O = [(0, LAR, S([(-84, -9), (-70, -9)])), (-1, LAR, S([(-70, -9), (-53, -9), (-36, -10)])),
             (1, LAR, S([(-36, -10), (-18, -14), (0, -17.5), (18, -21)])), (0, LAR, S([(18, -21), (32, -24)])),
             (-1, LAR, S([(32, -24), (48, -18), (56, 0), (48, 18), (32, 24)])), (0, LAR, S([(32, 24), (18, 21)])),
             (1, LAR, S([(18, 21), (0, 17.5), (-18, 14), (-36, 10)])), (-1, LAR, S([(-36, 10), (-53, 9), (-70, 9)])),
             (0, LAR, S([(-70, 9), (-130, 9)]))]
        Bz = [(0, AZU, S([(84, -9), (70, -9)])), (1, AZU, S([(70, -9), (53, -9), (36, -10)])),
              (-1, AZU, S([(36, -10), (18, -14), (0, -17.5), (-18, -21)])), (0, AZU, S([(-18, -21), (-32, -24)])),
              (1, AZU, S([(-32, -24), (-48, -18), (-56, 0), (-48, 18), (-32, 24)])), (0, AZU, S([(-32, 24), (-18, 21)])),
              (-1, AZU, S([(-18, 21), (0, 17.5), (18, 14), (36, 10)])), (1, AZU, S([(36, 10), (53, 9), (70, 9)])),
              (0, AZU, S([(70, 9), (130, 9)]))]
        c.corda(O, w=w, ox=ox, oy=oy, inicio=True, fim=False)
        c.corda(Bz, w=w, ox=ox, oy=oy, inicio=True, fim=False)
    return c.svg()

b = []
oy = 214
txt = [["ESQUERDA por cima", "da direita, e por", "baixo (meio nó)."],
       ["Agora a DIREITA por", "cima da esquerda,", "e por baixo."],
       ["Puxe. Cada ponta sai", "AO LADO da sua", "parte firme."]]
for i in range(3):
    b.append(painel(PX[i], 44, PW, 300, i + 1, txt[i], f"cd{i}"))
    b.append(f'<g clip-path="url(#cd{i})">' + direito(i + 1, PX[i] + 108, oy + (20 if i < 2 else 16)) + '</g>')
b.append(lbl(PX[2] + 12, oy - 10, "ponta", 11.5, "#a04d00", True))
b.append(lbl(PX[2] + 204, oy - 10, "ponta", 11.5, "#1d4f80", True, "end"))
b.append(lbl(PX[2] + 12, oy + 54, "parte firme", 11.5, "#a04d00", True))
b.append(lbl(PX[2] + 204, oy + 54, "parte firme", 11.5, "#1d4f80", True, "end"))
b.append(lbl(PX[2] + 108, oy + 100, "duas alças abraçadas;", 11.5, "#1e6b2e", True, "middle"))
b.append(lbl(PX[2] + 108, oy + 114, "as 2 pontas do mesmo lado", 11.5, "#1e6b2e", True, "middle"))
b.append(box(8, 354, 664, 84, "#eef5ff", "#3f6d9e"))
b.append(text(20, 374, "Regra: \"esquerda sobre direita, depois direita sobre esquerda\".", 12.5, "#222", True))
b.append(text(20, 392, "ERRADO: repetir o mesmo lado dá o \"nó torto\" (de vovó): pontas atravessadas, escorrega.", 12.5, "#b3001b"))
b.append(text(20, 410, "Usos: emendar duas pontas de MESMA grossura, fechar atadura, amarrar feixe e saco.", 12.5))
b.append(text(20, 428, "NÃO use para emendar cordas que vão levar carga ou de grossuras diferentes: use o nó de escota.", 12.5, "#b3001b"))
open(D + "no-direito.svg", "w").write(svg(680, 448, "Nó direito (emendar duas pontas iguais)", "\n".join(b)))
print("ok")
