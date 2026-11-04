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
        fant = {}
        for k, leg in enumerate(legs):
            z, cor, pts = leg[:3]
            fant[k] = leg[3] if len(leg) > 3 else self.fantasma
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
            if z < 0 and fant[k]:   # trecho escondido: desenha "fantasma" tracejado por cima do poste
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
b.append(lbl(PX[0] + 158, oy + 30, "buraco", 11.5, "#222", True))
b.append(lbl(PX[0] + 160, oy + 84, "ponta", 11.5, "#a04d00", True))
b.append(lbl(PX[1] + 140, oy - 74, "\"em volta", 11, "#222", True))
b.append(lbl(PX[1] + 140, oy - 60, "da árvore\"", 11, "#222", True))
b.append(lbl(PX[2] + 112, oy + 132, "alça fixa:", 11.5, "#1e6b2e", True, "middle"))
b.append(lbl(PX[2] + 112, oy + 146, "não corre", 11.5, "#1e6b2e", True, "middle"))
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
b.append(lbl(PX[2] + 12, oy + 64, "parte firme", 11.5, "#a04d00", True))
b.append(lbl(PX[2] + 204, oy + 64, "parte firme", 11.5, "#1d4f80", True, "end"))
b.append(lbl(PX[1] + 14, oy + 60, "1º meio nó", 11, "#555", True))
b.append(lbl(PX[1] + 14, oy + 6, "2º meio nó", 11, "#555", True))
b.append(lbl(PX[2] + 108, oy + 100, "duas alças abraçadas;", 11.5, "#1e6b2e", True, "middle"))
b.append(lbl(PX[2] + 108, oy + 114, "as 2 pontas do mesmo lado", 11.5, "#1e6b2e", True, "middle"))
b.append(box(8, 354, 664, 84, "#eef5ff", "#3f6d9e"))
b.append(text(20, 374, "Regra: \"esquerda sobre direita, depois direita sobre esquerda\".", 12.5, "#222", True))
b.append(text(20, 392, "ERRADO: repetir o mesmo lado dá o \"nó torto\" (de vovó): pontas atravessadas, escorrega.", 12.5, "#b3001b"))
b.append(text(20, 410, "Usos: emendar duas pontas de MESMA grossura, fechar atadura, amarrar feixe e saco.", 12.5))
b.append(text(20, 428, "NÃO use para emendar cordas que vão levar carga ou de grossuras diferentes: use o nó de escota.", 12.5, "#b3001b"))
open(D + "no-direito.svg", "w").write(svg(680, 448, "Nó direito (emendar duas pontas iguais)", "\n".join(b)))

# =====================================================================
# NO DE CAMINHONEIRO (trucker's hitch)
# =====================================================================
def caminhoneiro(etapa, ox, oy):
    c = Cena(); w = 10
    # ponto fixo (galho/barra) no alto e barra da carroceria embaixo
    c.add(-5, f'<rect x="{ox-70}" y="{oy-84}" width="140" height="14" rx="5" fill="{WOOD}" stroke="{OUT}" stroke-width="2.5"/>')
    c.add(3, f'<rect x="{ox-14}" y="{oy-86}" width="9" height="18" rx="3" fill="{AZU[0]}" stroke="{OUT}" stroke-width="2"/>'
             f'<rect x="{ox-4}" y="{oy-86}" width="9" height="18" rx="3" fill="{AZU[0]}" stroke="{OUT}" stroke-width="2"/>')
    c.add(0, f'<circle cx="{ox+20}" cy="{oy+170}" r="9" fill="#9a9a9a" stroke="{OUT}" stroke-width="2.5"/>'
             f'<rect x="{ox-90}" y="{oy+194}" width="180" height="40" fill="#6b7a86" stroke="{OUT}" stroke-width="2.5"/>')
    L = [
        (0, AZU, [(-8, -72), (-8, -50), (-8, -30), (-8, -12), (-11, 6), (-22, 26), (-24, 52), (-15, 74), (0, 80)]),
        (0, AZU, [(0, 80), (15, 74), (24, 52), (22, 26), (11, 6), (8, -12), (8, -30), (12, -40)]),
        (0, AZU, [(12, -40), (22, -40), (27, -31)]),
        (1, AZU, [(27, -31), (14, -27), (0, -25), (-14, -23), (-27, -19)]),
        (-1, AZU, [(-27, -19), (-20, -14), (-8, -13), (8, -12), (20, -9)]),
        (0, LAR, [(20, -9), (30, 4), (35, 24), (35, 60), (35, 100)]),
    ]
    dob = (3, 4, 5)
    if etapa == 1:
        L[-1] = (0, LAR, L[-1][2] + [(35, 112)])
    else:
        L += [(0, LAR, [(35, 100), (35.5, 130), (35.5, 170), (31, 181), (20, 185.5), (9, 181), (4.5, 170), (5, 140), (7, 100), (8, 90)]),
              (-1, LAR, [(8, 90), (8, 80), (8, 70)]),
              (0, LAR, [(8, 70), (8, 56), (4, 47), (-4, 47), (-9, 56), (-9, 66)]),
              (1, LAR, [(-9, 66), (-9, 78), (-9, 88)])]
        if etapa == 2:
            L.append((0, LAR, [(-9, 88), (-9, 120), (-10, 160), (-11, 200)]))
        else:
            yc, xl, xr = 120, -3, 46
            L += [(0, LAR, [(-9, 88), (-24, 96), (-46, 112), (-44, 128), (-26, yc + 12), (-12, yc + 12)]),
                  (1, LAR, [(-12, yc + 12), (xl + 4, yc + 12), (21, yc + 12), (xr - 4, yc + 12), (xr + 7, yc + 13)]),
                  (-1, LAR, [(xr + 7, yc + 13), (xr - 4, yc + 17), (21, yc + 20), (xl + 4, yc + 23), (xl - 7, yc + 26)], False),
                  (2, LAR, [(xl - 7, yc + 26), (xl + 4, yc + 27), (21, yc), (xr - 4, yc - 25), (xr + 7, yc - 27)]),
                  (-1, LAR, [(xr + 7, yc - 27), (xr - 4, yc - 24), (21, yc - 19), (xl + 4, yc - 15), (xl - 7, yc - 12)], False),
                  (1, LAR, [(xl - 7, yc - 12), (xl + 4, yc - 12), (21, yc - 12), (xr + 8, yc - 12), (68, yc - 13), (84, yc - 16)])]
            dob = (3, 4, 5, 10, 11, 12, 13)
    c.corda(L, w=w, ox=ox, oy=oy, dobras=dob)
    if etapa == 2:
        c.add(5, arrow(ox - 34, oy + 130, ox - 34, oy + 196, "#d62828", 5))
    return c.svg()

b = []
oy = 196
txt = [["Faça uma alça fixa", "no meio da corda", "(ver texto)."],
       ["Ponta pelo gancho e", "de volta PELA ALÇA.", "Puxe para baixo."],
       ["Segure e trave com", "2 cotes em volta das", "duas pernas."]]
for i in range(3):
    b.append(painel(PX[i], 44, PW, 368, i + 1, txt[i], f"cc{i}"))
    b.append(f'<g clip-path="url(#cc{i})">' + caminhoneiro(i + 1, PX[i] + 100, oy) + '</g>')
b.append(lbl(PX[0] + 128, oy - 60, "ponto fixo", 11, "#222", True))
b.append(lbl(PX[0] + 134, oy - 26, "nó", 11.5, "#222", True))
b.append(lbl(PX[0] + 12, oy + 50, "alça", 11.5, "#1d4f80", True))
b.append(lbl(PX[0] + 12, oy + 64, "fixa", 11.5, "#1d4f80", True))
b.append(lbl(PX[0] + 136, oy + 160, "gancho ou", 11, "#222", True))
b.append(lbl(PX[0] + 136, oy + 174, "barra", 11, "#222", True))
b.append(lbl(PX[0] + 100, oy + 214, "carroceria / estaca", 11, "#fff", True, "middle").replace('stroke="#fff"', 'stroke="#6b7a86"'))
b.append(lbl(PX[1] + 10, oy + 126, "PUXE", 13, "#b3001b", True))
b.append(lbl(PX[1] + 134, oy + 56, "a alça vira", 11, "#1e6b2e", True))
b.append(lbl(PX[1] + 134, oy + 70, "roldana:", 11, "#1e6b2e", True))
b.append(lbl(PX[1] + 134, oy + 84, "força x2", 11, "#1e6b2e", True))
b.append(lbl(PX[2] + 152, oy + 152, "2 cotes", 11.5, "#a04d00", True))
b.append(box(8, 420, 664, 84, "#eef5ff", "#3f6d9e"))
b.append(text(20, 440, "Usos: esticar lona, varal, corda de carga em caminhão ou carroça, cerca provisória.", 12.5))
b.append(text(20, 458, "Alça fixa: nó de borboleta (melhor) ou alça de nó simples. A \"alça de correr\" serve para carga leve.", 12.5))
b.append(text(20, 476, "Para soltar: desfaça os cotes e deixe a ponta correr. Use corda boa: a força dobra.", 12.5))
b.append(text(20, 494, "Cuidado: corda que arrebenta sob tensão chicoteia. Não fique na linha da corda.", 12.5, "#b3001b"))
open(D + "no-caminhoneiro.svg", "w").write(svg(680, 514, "Nó de caminhoneiro (esticar e prender carga)", "\n".join(b)))

# =====================================================================
# CORDA DE 2 PERNAS (torcer e cruzar)
# =====================================================================
FA = ("#e2bf7e", "#9c7432")   # fibra clara
FB = ("#c9955a", "#7a5226")   # fibra escura

def duas_pernas(c, x0, y0, n, H, A, w, rabo=None):
    """corda de 2 pernas horizontal, comecando na dobra em x0; n cruzamentos; rabo = (compA, compB) pernas soltas"""
    for sg, cor in ((1, FA), (-1, FB)):
        P = []
        for k in range(4 * n + 1):
            x = x0 + k * H / 4
            P.append((x, y0 + sg * -A * math.cos(math.pi * (x - x0) / H)))
        legs = []
        # dobra (inicio): meia volta ligando as duas pernas
        if sg == 1:
            arc = [(x0 + 2, y0 - A), (x0 - A * 0.9, y0 - A * 0.55), (x0 - A * 1.15, y0), (x0 - A * 0.9, y0 + A * 0.55), (x0 + 2, y0 + A)]
        for k in range(n):
            # cruzamento k em P[4k+2]; a perna que desce (vai de cima para baixo) passa na frente
            desce = (sg == 1) == (k % 2 == 0)
            legs.append((0, cor, [P[4 * k], P[4 * k + 1]]))
            legs.append((1 if desce else -1, cor, [P[4 * k + 1], P[4 * k + 2], P[4 * k + 3]]))
            legs.append((0, cor, [P[4 * k + 3], P[4 * k + 4]]))
        if rabo:
            L = rabo[0] if sg == 1 else rabo[1]
            yl = P[-1][1]
            legs.append((0, cor, [P[-1], (P[-1][0] + 12, yl + sg * -4), (P[-1][0] + L * 0.5, yl + sg * -10), (P[-1][0] + L, yl + sg * -12)]))
        # junta trechos para o contorno
        c.corda(legs, w=w, fim=bool(rabo))
    # dobra desenhada por cima do inicio
    d = f"M{x0+1} {y0-A} C {x0-A*1.3} {y0-A}, {x0-A*1.3} {y0+A}, {x0+1} {y0+A}"
    c.add(2, f'<path d="{d}" fill="none" stroke="{OUT}" stroke-width="{w+4.5}"/><path d="{d}" fill="none" stroke="{FA[0]}" stroke-width="{w}"/>'
             f'<path d="{d}" fill="none" stroke="{FA[1]}" stroke-width="{w-3}" stroke-dasharray="1.6 5" stroke-opacity="0.55"/>')

def feixe(x0, y0, comp1, comp2, gap, w):
    """feixe de fibras dobrado (U deitado), dobra a esquerda"""
    d = f"M{x0+comp1} {y0-gap} L {x0} {y0-gap} C {x0-gap*1.35} {y0-gap}, {x0-gap*1.35} {y0+gap}, {x0} {y0+gap} L {x0+comp2} {y0+gap}"
    s = f'<path d="{d}" fill="none" stroke="{OUT}" stroke-width="{w+4.5}" stroke-linecap="round"/>'
    s += f'<path d="{d}" fill="none" stroke="{FA[0]}" stroke-width="{w}" stroke-linecap="round"/>'
    for off in (-w * 0.3, 0, w * 0.3):
        dd = f"M{x0+comp1} {y0-gap+off} L {x0} {y0-gap+off} C {x0-(gap-off)*1.35} {y0-gap+off}, {x0-(gap-off)*1.35} {y0+gap-off}, {x0} {y0+gap-off} L {x0+comp2} {y0+gap-off}"
        s += f'<path d="{dd}" fill="none" stroke="{FA[1]}" stroke-width="0.9" stroke-opacity="0.7"/>'
    return s

def seta_curva(cx, cy, rx, ry, cor="#d62828"):
    # seta em arco (torcao) em volta de uma perna
    return (f'<path d="M{cx-rx} {cy+2} A {rx} {ry} 0 1 1 {cx+rx*0.2} {cy+ry*0.98}" fill="none" stroke="{cor}" stroke-width="3"/>'
            f'<polygon points="{cx+rx*0.2-8},{cy+ry*0.98-6} {cx+rx*0.2+2},{cy+ry*0.98} {cx+rx*0.2-8},{cy+ry*0.98+6}" fill="{cor}"/>')

b = []
# painel 1
b.append(painel(8, 44, 216, 190, 1, ["Dobre o feixe de", "fibras FORA do meio", "(2/3 de um lado, 1/3 do outro)."], "cp0"))
b.append(feixe(60, 170, 150, 100, 13, 13))
b.append(hand(54, 152, 10) + hand(54, 188, 10))
b.append(lbl(110, 146, "perna longa", 11, "#222", True)); b.append(lbl(84, 210, "perna curta", 11, "#222", True))
b.append(text(30, 226, "(as emendas não caem juntas)", 11, "#555"))
# painel 2
b.append(painel(232, 44, 216, 190, 2, ["Torça a perna de", "CIMA para longe de", "você; cruze-a POR CIMA."], "cp1"))
b.append(feixe(270, 170, 165, 165, 14, 13))
b.append(hand(264, 152, 10) + hand(264, 190, 10))
b.append(seta_curva(352, 156, 9, 16))
b.append(lbl(366, 140, "1. torça", 11.5, "#b3001b", True))
b.append('<path d="M392 150 C 404 162, 404 176, 392 190" fill="none" stroke="#1e6b2e" stroke-width="3.5"/><polygon points="384,184 392,196 398,183" fill="#1e6b2e"/>')
b.append(lbl(372, 222, "2. cruze por cima", 11.5, "#1e6b2e", True, "middle"))
# painel 3
b.append(painel(456, 44, 216, 190, 3, ["Repita: torce, cruza,", "torce, cruza... sempre", "nos mesmos sentidos."], "cp2"))
c = Cena()
duas_pernas(c, 498, 170, 4, 22, 7, 11, rabo=(70, 40))
b.append(c.svg())
b.append(hand(492, 152, 10) + hand(492, 188, 10))
# detalhe grande
b.append(text(340, 262, "Como fica a corda (detalhe)", 14, "#222", True, "middle"))
c = Cena()
duas_pernas(c, 80, 320, 10, 44, 13, 21, rabo=(90, 30))
b.append(c.svg())
b.append(lbl(40, 296, "dobra", 11.5, "#222", True))
b.append(lbl(150, 362, "cada perna fica torcida para um lado...", 12, "#222", True))
b.append(lbl(150, 378, "...e as pernas se enrolam para o outro: é isso que trava.", 12, "#222", True))
b.append(lbl(600, 296, "pernas soltas", 11.5, "#222", True, "middle"))
b.append(box(8, 392, 664, 84, "#eef5ff", "#3f6d9e"))
b.append(text(20, 412, "Emenda: quando uma perna estiver a ~5 cm do fim, junte fibras novas (afinadas na ponta)", 12.5))
b.append(text(20, 430, "sobrepondo 5–10 cm e continue torcendo. Nunca emende as duas pernas no mesmo ponto.", 12.5))
b.append(text(20, 448, "Fibra úmida torce melhor (sisal, caroá, embira, bananeira, taboa, palha, tiras de PET).", 12.5))
b.append(text(20, 466, "Corda caseira é fraca e irregular: nunca use para escalar ou levantar pessoas.", 12.5, "#b3001b", True))
open(D + "corda-duas-pernas.svg", "w").write(svg(680, 486, "Fazer corda de 2 pernas com as mãos", "\n".join(b)))
print("ok")
