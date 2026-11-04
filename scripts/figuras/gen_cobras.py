import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "02-saude", "img") + "/"
b = []
# painel A: cabeca peconhenta
b.append(text(240,72,"Peçonhenta (jararaca, cascavel, surucucu)",14,"#b3001b",True,"middle"))
b.append('<path d="M60 178 C 64 148, 112 130, 180 130 C 250 130, 300 142, 345 160 L 470 168 L 470 220 L 345 222 C 280 228, 190 230, 116 214 C 82 207, 60 196, 60 178 Z" fill="#a98a5b" stroke="#1e1e1e" stroke-width="3"/>')
for x in (360,410,452):
    b.append(f'<path d="M{x} 168 l18 22 l18 -22" fill="none" stroke="#4a3a22" stroke-width="7" stroke-linejoin="round"/>')
b.append('<path d="M70 190 Q 190 206 320 200" fill="none" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append('<circle cx="186" cy="160" r="15" fill="#e8d36a" stroke="#1e1e1e" stroke-width="2.5"/><ellipse cx="186" cy="160" rx="3.5" ry="12" fill="#1e1e1e"/>')
b.append('<ellipse cx="86" cy="166" rx="6" ry="5" fill="#1e1e1e"/>')
b.append('<ellipse cx="134" cy="172" rx="9" ry="7.5" fill="#1e1e1e"/>')
b.append('<circle cx="134" cy="172" r="19" fill="none" stroke="#d62828" stroke-width="3.5"/>')
b.append('<line x1="128" y1="190" x2="110" y2="246" stroke="#d62828" stroke-width="2.5"/>')
b += [text(20,262,"FOSSETA LOREAL: um buraco ENTRE o olho e a narina",13.5,"#b3001b",True),
      text(20,280,"(órgão que sente calor). Tem fosseta = PEÇONHENTA.",13,"#b3001b")]
b += [text(196,124,"pupila em fenda",11.5,"#444"), text(40,140,"narina ↓",11.5,"#444")]
# cabeca nao peconhenta
b.append(text(586,92,"Em geral não",13,"#2b6a1e",True,"middle")); b.append(text(586,108,"peçonhenta",13,"#2b6a1e",True,"middle"))
b.append('<path d="M520 170 C 522 150, 548 138, 585 138 C 625 138, 650 150, 665 162 L 665 196 C 640 204, 600 206, 560 200 C 532 196, 520 186, 520 170 Z" fill="#7aa36a" stroke="#1e1e1e" stroke-width="3"/>')
b.append('<circle cx="580" cy="160" r="12" fill="#f0e6c0" stroke="#1e1e1e" stroke-width="2.5"/><circle cx="580" cy="160" r="6" fill="#1e1e1e"/>')
b.append('<ellipse cx="534" cy="162" rx="4.5" ry="4" fill="#1e1e1e"/>')
b += [text(512,226,"sem fosseta,",12,"#2b6a1e"), text(512,241,"pupila redonda",12,"#2b6a1e"), text(512,258,"(NÃO pegue: há",11.5,"#444"), text(512,272,"exceções, como a coral)",11.5,"#444")]
b.append('<line x1="20" y1="296" x2="660" y2="296" stroke="#ccc" stroke-width="2"/>')
b.append(text(340,322,"Reconheça pela cauda e pelas cores",15,"#222",True,"middle"))
def cauda(ox, oy, cor="#a98a5b"):
    return f'<path d="M{ox} {oy-16} C {ox+60} {oy-16}, {ox+110} {oy-8}, {ox+138} {oy} C {ox+110} {oy+6}, {ox+60} {oy+16}, {ox} {oy+16} Z" fill="{cor}" stroke="#1e1e1e" stroke-width="2.5"/>'
# jararaca
ox, oy = 20, 380
b.append(cauda(ox,oy))
for dx in (14,52,88):
    b.append(f'<path d="M{ox+dx} {oy-12} l10 12 l10 -12" fill="none" stroke="#4a3a22" stroke-width="5"/>')
b += [text(ox,420,"JARARACA",13,"#222",True), text(ox,436,"desenhos em \"V\" ou",11.5), text(ox,450,"\"gancho de telefone\";",11.5), text(ox,464,"cauda lisa e fina",11.5), text(ox,480,"~ 80% dos acidentes",11.5,"#b3001b",True)]
# cascavel
ox = 185
b.append(f'<path d="M{ox} {oy-16} C {ox+40} {oy-16}, {ox+70} {oy-10}, {ox+86} {oy-8} L {ox+86} {oy+8} C {ox+70} {oy+10}, {ox+40} {oy+16}, {ox} {oy+16} Z" fill="#b59a66" stroke="#1e1e1e" stroke-width="2.5"/>')
for i in range(5):
    x = ox+86+i*12
    b.append(f'<rect x="{x}" y="{oy-11+i}" width="13" height="{22-2*i}" rx="5" fill="#e9dcb8" stroke="#1e1e1e" stroke-width="2"/>')
b += [text(ox,420,"CASCAVEL",13,"#222",True), text(ox,436,"chocalho (guizo) na",11.5), text(ox,450,"ponta da cauda; faz",11.5), text(ox,464,"barulho de chiado",11.5), text(ox,480,"ataca nervos e rins",11.5,"#b3001b",True)]
# surucucu
ox = 350
b.append(cauda(ox,oy,"#c79a52"))
b.append(f'<path d="M{ox+92} {oy-8} l6 -10 l6 9 l6 -10 l6 9 l6 -9 l6 8 l4 -6 L {ox+138} {oy} L {ox+128} {oy+5} l-6 8 l-6 -7 l-6 8 l-6 -7 l-6 8 l-6 -8 Z" fill="#3a2a16" stroke="#1e1e1e" stroke-width="1.5"/>')
for dx in (10,46):
    b.append(f'<path d="M{ox+dx} {oy-14} l14 14 l14 -14 Z" fill="#3a2a16"/>')
b += [text(ox,420,"SURUCUCU",13,"#222",True), text(ox,436,"(pico-de-jaca): ponta da",11.5), text(ox,450,"cauda com escamas",11.5), text(ox,464,"arrepiadas e escuras",11.5), text(ox,480,"Amazônia e",11.5,"#444"), text(ox,494,"Mata Atlântica",11.5,"#444")]
# coral
ox = 515
cores = ["#d62828","#1e1e1e","#f4f1e6","#1e1e1e","#f4f1e6","#1e1e1e","#d62828","#1e1e1e","#f4f1e6","#1e1e1e"]
x = ox
b.append(f'<clipPath id="cc"><path d="M{ox} {oy-15} C {ox+60} {oy-15}, {ox+120} {oy-12}, {ox+145} {oy} C {ox+120} {oy+12}, {ox+60} {oy+15}, {ox} {oy+15} Z"/></clipPath>')
g = '<g clip-path="url(#cc)">'
w = [16,10,7,10,7,10,16,10,7,10,30]
for i,c in enumerate(cores+["#d62828"]):
    g += f'<rect x="{x}" y="{oy-20}" width="{w[i]}" height="40" fill="{c}"/>'; x += w[i]
g += '</g>'
b.append(g)
b.append(f'<path d="M{ox} {oy-15} C {ox+60} {oy-15}, {ox+120} {oy-12}, {ox+145} {oy} C {ox+120} {oy+12}, {ox+60} {oy+15}, {ox} {oy+15} Z" fill="none" stroke="#1e1e1e" stroke-width="2.5"/>')
b += [text(ox,420,"CORAL",13,"#222",True), text(ox,436,"anéis vermelhos, pretos",11.5), text(ox,450,"e brancos/amarelos que",11.5), text(ox,464,"dão a VOLTA no corpo",11.5), text(ox,480,"sem fosseta, mas",11.5,"#b3001b",True), text(ox,494,"MUITO perigosa",11.5,"#b3001b",True)]
b.append(box(20,506,640,46,"#fdecea","#d62828"))
b += [text(34,526,"Cabeça triangular NÃO é sinal confiável. Existem corais falsas iguais às verdadeiras.",12.5,"#222",True),
      text(34,543,"Na dúvida, trate TODA cobra como perigosa: não chegue perto, não pegue, não tente matar.",12.5)]
open(D+"cobras.svg","w").write(svg(680,562,"Como reconhecer cobras peçonhentas do Brasil","\n".join(b)))
