import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "02-saude", "img") + "/"
CLOTH = "#e9e1c8"; WOOD = "#8b5a2b"
# ---------- TORNIQUETE ----------
def braco(ox, oy):
    s = limb([(ox+20, oy), (ox+262, oy+4)], 42, SKIN)
    s += f'<ellipse cx="{ox+284}" cy="{oy+4}" rx="18" ry="22" fill="{SKIN}" stroke="{OUT}" stroke-width="2.5"/>'
    s += f'<ellipse cx="{ox+222}" cy="{oy+2}" rx="13" ry="8" fill="#b3001b" stroke="#600" stroke-width="1.5"/>'
    s += f'<path d="M{ox+222} {oy+16} q-4 9 0 13 q4 -4 0 -13z" fill="#b3001b"/>'
    return s
def faixa(ox, oy, tw=False):
    s = f'<rect x="{ox+128}" y="{oy-28}" width="26" height="60" rx="4" fill="{CLOTH}" stroke="{OUT}" stroke-width="2"/>'
    if tw:
        s += "".join(f'<line x1="{ox+130}" y1="{oy-24+k*11}" x2="{ox+152}" y2="{oy-18+k*11}" stroke="#8a7d5a" stroke-width="2"/>' for k in range(5))
    return s
def bastao(ox, oy):
    return f'<rect x="{ox+104}" y="{oy-38}" width="74" height="10" rx="4" fill="{WOOD}" stroke="{OUT}" stroke-width="2"/>'
b = []
P = [(10,70),(345,70),(10,262),(345,262)]
titles = ["1. Faixa LARGA (4 cm ou mais)", "2. Nó, bastão por cima, outro nó", "3. Gire o bastão até o sangue PARAR", "4. Prenda o bastão e anote a HORA"]
for k,(ox,oy) in enumerate(P):
    b.append(f'<rect x="{ox}" y="{oy-28}" width="325" height="186" rx="10" fill="#fafafa" stroke="#ccc"/>')
    b.append(text(ox+12, oy-8, titles[k], 13.5, "#222", True))
    y = oy+84
    b.append(braco(ox, y))
    b.append(faixa(ox, y, tw=(k>=2)))
    if k == 0:
        b.append(f'<line x1="{ox+154}" y1="{y+42}" x2="{ox+210}" y2="{y+42}" stroke="#d62828" stroke-width="2"/>')
        b.append(f'<line x1="{ox+154}" y1="{y+36}" x2="{ox+154}" y2="{y+48}" stroke="#d62828" stroke-width="2"/><line x1="{ox+210}" y1="{y+36}" x2="{ox+210}" y2="{y+48}" stroke="#d62828" stroke-width="2"/>')
        b.append(text(ox+182, y+62, "5 a 8 cm ACIMA da ferida", 12, "#b22", True, "middle"))
        b.append(text(ox+18, y-34, "nunca sobre cotovelo ou joelho", 11.5, "#444"))
        b.append(text(ox+18, y+62, "ombro →", 11, "#666"))
    if k >= 1:
        b.append(bastao(ox, y))
        b.append(f'<circle cx="{ox+141}" cy="{y-26}" r="7" fill="{CLOTH}" stroke="{OUT}" stroke-width="2"/>')
    if k == 1:
        b.append(text(ox+18, y-48, "bastão: galho firme, caneta grossa, colher", 11.5, "#444"))
        b.append(text(ox+18, y+62, "NUNCA use fio, arame ou corda fina", 12, "#b22", True))
    if k == 2:
        b.append(f'<path d="M{ox+100} {y-62} A 42 18 0 1 1 {ox+182} {y-62}" fill="none" stroke="#d62828" stroke-width="3.5"/>')
        b.append(f'<polygon points="{ox+182},{y-50} {ox+174},{y-64} {ox+190},{y-64}" fill="#d62828"/>')
        b.append(text(ox+196, y-68, "gire", 12.5, "#b22", True))
        b.append(text(ox+18, y+62, "Vai doer muito. É normal. NÃO afrouxe.", 12, "#b22", True))
    if k == 3:
        b.append(f'<rect x="{ox+170}" y="{y-44}" width="12" height="22" rx="3" fill="{CLOTH}" stroke="{OUT}" stroke-width="1.5"/>')
        b.append(f'<rect x="{ox+238}" y="{y-60}" width="72" height="30" rx="4" fill="#fff" stroke="#d62828" stroke-width="2"/>')
        b.append(text(ox+274, y-40, "T 14:35", 15, "#b22", True, "middle"))
        b.append(text(ox+18, y+62, "Escreva a hora no torniquete ou na testa.", 12, "#222"))
open(D+"torniquete.svg","w").write(svg(680,466,"Torniquete improvisado (braço ou perna)","\n".join(b)))

# ---------- IMOBILIZACAO ----------
b = []
b.append(text(170,64,"A) Tala na perna",15,"#222",True,"middle"))
y=150
b.append(limb([(40,y),(290,y+4)],40,SKIN))
b.append(f'<path d="M290 {y-16} L316 {y-38} L326 {y-28} L304 {y+22} Z" fill="{SKIN}" stroke="{OUT}" stroke-width="2.5"/>')
b.append(f'<rect x="30" y="{y-34}" width="270" height="11" rx="3" fill="{WOOD}" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<rect x="30" y="{y+27}" width="270" height="11" rx="3" fill="{WOOD}" stroke="{OUT}" stroke-width="2"/>')
for x in (52,120,214,272):
    b.append(f'<rect x="{x}" y="{y-38}" width="12" height="80" rx="3" fill="{CLOTH}" stroke="{OUT}" stroke-width="1.5"/>')
b.append(f'<path d="M160 {y-18} l8 10 l-8 10 l8 10 l-8 10" fill="none" stroke="#d62828" stroke-width="3"/>')
b.append(text(164,y+64,"fratura",12.5,"#b22",True,"middle"))
b.append(text(98,y-48,"joelho",11.5,"#444","","middle") if False else text(84,y-46,"↓ joelho",11.5,"#444"))
b.append(text(250,y-46,"tornozelo ↓",11.5,"#444"))
b += [text(20,250,"• Tala dos dois lados, acolchoada com pano.",12.5), text(20,268,"• Pegue a articulação ACIMA e a ABAIXO.",12.5),
      text(20,286,"• Amarre acima e abaixo da fratura,",12.5), text(20,302,"  nunca em cima dela.",12.5),
      text(20,320,"• Confira depois: dedos rosados, quentes",12.5), text(20,336,"  e com sensibilidade. Roxo/frio = afrouxe.",12.5)]
b.append('<line x1="345" y1="48" x2="345" y2="350" stroke="#ccc" stroke-width="2"/>')
b.append(text(512,64,"B) Tipoia (braço, punho, clavícula)",15,"#222",True,"middle"))
# pessoa de frente (busto)
b.append(limb([(500,150),(500,262)],80,VIT))
b.append(head(500,102,26,VIT))
b.append(limb([(452,150),(438,226),(434,272)],18,VIT))
b.append(limb([(548,150),(562,226),(468,208)],18,VIT)); b.append(hand(460,206,11))
# tipoia: berco sob o antebraco + duas tiras ate o pescoco
b.append(f'<path d="M478 132 L452 204" stroke="{OUT}" stroke-width="13" stroke-linecap="round"/><path d="M478 132 L452 204" stroke="{CLOTH}" stroke-width="9" stroke-linecap="round"/>')
b.append(f'<path d="M522 132 L566 214" stroke="{OUT}" stroke-width="13" stroke-linecap="round"/><path d="M522 132 L566 214" stroke="{CLOTH}" stroke-width="9" stroke-linecap="round"/>')
b.append(f'<path d="M444 206 Q505 248 576 216 L572 238 Q505 270 446 228 Z" fill="{CLOTH}" stroke="{OUT}" stroke-width="2"/>')
b.append(f'<circle cx="524" cy="132" r="8" fill="{CLOTH}" stroke="{OUT}" stroke-width="2"/>')
b.append('<line x1="532" y1="130" x2="590" y2="112" stroke="#555"/>'); b += [text(592,108,"nó do lado",12), text(592,123,"do pescoço",12)]
b.append('<line x1="452" y1="200" x2="410" y2="168" stroke="#555"/>'); b += [text(352,150,"mão acima",12), text(352,165,"do cotovelo",12)]
b.append('<line x1="572" y1="236" x2="600" y2="250" stroke="#555"/>'); b += [text(586,266,"pano apoia",12), text(586,281,"o antebraço",12)]
b += [text(362,300,"Faça com pano triangular (quadrado de ~1 m",12.5), text(362,316,"dobrado na diagonal), camisa ou cachecol.",12.5), text(362,334,"Deixe os dedos de fora para ver a cor.",12.5)]
open(D+"imobilizacao.svg","w").write(svg(680,356,"Imobilização de fraturas","\n".join(b)))

# ---------- QUEIMADURA: area ----------
b = []
b.append(text(180,64,"Regra dos 9 (adulto)",15,"#222",True,"middle"))
def corpo(cx, top, col):
    s = limb([(cx-16,top+190),(cx-20,top+300)],26,col) + limb([(cx+16,top+190),(cx+20,top+300)],26,col)
    s += limb([(cx,top+70),(cx,top+180)],78,col)
    s += limb([(cx-46,top+66),(cx-62,top+170)],20,col) + limb([(cx+46,top+66),(cx+62,top+170)],20,col)
    s += head(cx, top+28, 26, col)
    return s
b.append(corpo(95,80,"#f6d3b7")); b.append(text(95,414,"FRENTE",12,"#444",True,"middle"))
b.append(corpo(268,80,"#e9c2a2")); b.append(text(268,414,"COSTAS",12,"#444",True,"middle"))
def lab(x,y,t,c="#b3001b"): return text(x,y,t,13,c,True,"middle")
b += [lab(95,113,"4,5"), lab(268,113,"4,5"), lab(95,212,"18"), lab(268,212,"18"),
      lab(41,206,"4,5"), lab(149,206,"4,5"), lab(214,206,"4,5"), lab(322,206,"4,5"),
      lab(77,330,"9"), lab(113,330,"9"), lab(250,330,"9"), lab(286,330,"9"), lab(95,262,"1")]
b += [text(20,440,"Cabeça 9 · cada braço 9 · tronco frente 18 · costas 18",12), text(20,456,"cada perna 18 · genitais 1  (total 100%)",12)]
b.append('<line x1="360" y1="48" x2="360" y2="462" stroke="#ccc" stroke-width="2"/>')
b.append(text(520,64,"Regra da palma",15,"#222",True,"middle"))
# mao
hx, hy = 520, 210
b.append(f'<rect x="{hx-48}" y="{hy-30}" width="96" height="104" rx="22" fill="#f6d3b7" stroke="{OUT}" stroke-width="2.5"/>')
for i,(dx,L) in enumerate([(-36,64),(-12,78),(12,74),(36,58)]):
    b.append(f'<rect x="{hx+dx-11}" y="{hy-30-L}" width="22" height="{L+14}" rx="11" fill="#f6d3b7" stroke="{OUT}" stroke-width="2.5"/>')
b.append(f'<rect x="{hx-90}" y="{hy+4}" width="56" height="22" rx="11" fill="#f6d3b7" stroke="{OUT}" stroke-width="2.5" transform="rotate(-30 {hx-40} {hy+15})"/>')
b.append(f'<rect x="{hx-46}" y="{hy-26}" width="92" height="98" rx="20" fill="#f6d3b7"/>')
b.append(text(hx,hy+30,"≈ 1%",22,"#b3001b",True,"middle"))
b += [text(380,330,"A palma da mão DA VÍTIMA,",13,"#222",True), text(380,348,"com os dedos juntos, cobre",13), text(380,366,"cerca de 1% do corpo dela.",13),
      text(380,396,"É GRAVE se passar de:",13,"#b22",True), text(380,414,"• 10% em criança ou idoso",12.5), text(380,430,"• 15–20% em adulto",12.5),
      text(380,446,"• rosto, mãos, pés, genitais, juntas",12.5)]
open(D+"queimadura-area.svg","w").write(svg(680,470,"Como medir o tamanho de uma queimadura","\n".join(b)))

# ---------- SUTURA ----------
b = []
b.append(text(170,62,"A) Corte lateral de um ponto",14.5,"#222",True,"middle"))
# camadas da pele
b.append('<path d="M20 90 L148 90 L170 200 L190 90 L320 90 L320 112 L20 112 Z" fill="#e8b49a" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append('<path d="M20 112 L152 112 L170 200 L188 112 L320 112 L320 170 L20 170 Z" fill="#f2cdb6" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append('<path d="M20 170 L164 170 L170 200 L176 170 L320 170 L320 230 L20 230 Z" fill="#fbe7a6" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append('<path d="M128 90 C 128 236, 212 236, 212 90" fill="none" stroke="#1d4ed8" stroke-width="3.5"/>')
b.append('<path d="M128 90 C 140 70, 200 70, 212 90" fill="none" stroke="#1d4ed8" stroke-width="3.5"/>')
b.append('<circle cx="170" cy="76" r="6" fill="#1d4ed8"/>')
b.append('<line x1="128" y1="250" x2="148" y2="250" stroke="#d62828" stroke-width="2"/><line x1="128" y1="244" x2="128" y2="256" stroke="#d62828" stroke-width="2"/><line x1="148" y1="244" x2="148" y2="256" stroke="#d62828" stroke-width="2"/>')
b += [text(152,262,"~5 mm da borda",12,"#b22",True)]
b += [text(24,104,"pele",11,"#5a2d1a"), text(24,145,"derme",11,"#5a2d1a"), text(24,205,"gordura",11,"#5a2d1a")]
b += [text(222,84,"← nó (3 voltas)",11.5,"#1d4ed8",True)]
b += [text(20,284,"Agulha entra em ângulo reto, desce até o",12.5), text(20,300,"fundo do corte e sai do outro lado na mesma",12.5), text(20,316,"distância. Sem espaço vazio embaixo.",12.5)]
b.append('<line x1="340" y1="44" x2="340" y2="330" stroke="#ccc" stroke-width="2"/>')
b.append(text(510,62,"B) Visto de cima",14.5,"#222",True,"middle"))
b.append('<rect x="360" y="100" width="300" height="110" rx="12" fill="#f2cdb6" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append('<path d="M380 156 Q510 150 640 156" stroke="#9b1c1c" stroke-width="3" fill="none"/>')
for x in (400,450,500,550,600):
    b.append(f'<line x1="{x}" y1="134" x2="{x}" y2="176" stroke="#1d4ed8" stroke-width="3"/>')
    b.append(f'<circle cx="{x+6}" cy="134" r="4" fill="#1d4ed8"/><path d="M{x+6} 134 l10 -10 M{x+6} 134 l12 -4" stroke="#1d4ed8" stroke-width="2"/>')
b.append('<line x1="400" y1="196" x2="450" y2="196" stroke="#d62828" stroke-width="2"/>')
b += [text(426,232,"5–10 mm entre pontos",12,"#b22",True,"middle")]
b += [text(360,262,"Cada ponto é separado e com nó próprio.",12.5), text(360,280,"Nó para o lado, não em cima do corte.",12.5),
      text(360,298,"Bordas só se encostam: não aperte até",12.5), text(360,314,"a pele ficar branca ou enrugada.",12.5)]
open(D+"sutura.svg","w").write(svg(680,330,"Sutura com ponto simples","\n".join(b)))
