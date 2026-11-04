import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "02-saude", "img") + "/"
WOOD="#8b5a2b"
# ---------- TORNEIRA DE PE ----------
b=[]
b.append('<rect x="0" y="330" width="680" height="70" fill="#e8d3b0"/>')
b.append('<ellipse cx="250" cy="340" rx="110" ry="16" fill="#9a9a9a" stroke="#555"/>')
b.append(text(250,384,"buraco com pedras/brita (a água infiltra, não vira lama)",11.5,"#444",False,"middle"))
# postes e travessa
b.append(f'<rect x="90" y="80" width="16" height="262" fill="{WOOD}" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<rect x="394" y="80" width="16" height="262" fill="{WOOD}" stroke="#1e1e1e" stroke-width="2"/>')
b.append(f'<rect x="80" y="76" width="340" height="14" fill="{WOOD}" stroke="#1e1e1e" stroke-width="2"/>')
# galao inclinado pendurado
b.append('<g transform="rotate(-20 250 150)"><rect x="210" y="110" width="80" height="96" rx="10" fill="#e8f3fd" stroke="#1e1e1e" stroke-width="2.5"/><rect x="214" y="150" width="72" height="52" fill="#9fc5ec"/><rect x="236" y="96" width="24" height="16" fill="#3f6d9e" stroke="#1e1e1e" stroke-width="2"/><path d="M290 122 q24 6 0 40" fill="none" stroke="#1e1e1e" stroke-width="4"/></g>')
b.append('<line x1="250" y1="90" x2="262" y2="112" stroke="#555" stroke-width="2.5"/>')
b.append('<line x1="270" y1="90" x2="276" y2="118" stroke="#555" stroke-width="2.5"/>')
# furo e jato
b.append('<circle cx="212" cy="122" r="3" fill="#1e1e1e"/>')
b.append('<path d="M209 124 Q 196 160 200 210" fill="none" stroke="#4a90d9" stroke-width="3"/>')
# corda do pedal
b.append('<line x1="302" y1="190" x2="320" y2="318" stroke="#555" stroke-width="2.5"/>')
b.append(f'<rect x="300" y="314" width="120" height="10" rx="3" fill="{WOOD}" stroke="#1e1e1e" stroke-width="2" transform="rotate(-6 300 319)"/>')
b.append('<ellipse cx="440" cy="314" rx="22" ry="10" fill="#555"/>')
# sabao
b.append('<line x1="140" y1="90" x2="140" y2="150" stroke="#555" stroke-width="2"/><rect x="126" y="150" width="28" height="18" rx="5" fill="#f7e98a" stroke="#1e1e1e" stroke-width="2"/>')
# maos
b.append(hand(196,232,13)); b.append(hand(214,236,13))
b += [text(450,118,"1. Galão de 5 L com",12.5,"#222",True), text(450,134,"   furinho perto da tampa",12.5),
      text(450,168,"2. Pise no pedal: o galão",12.5,"#222",True), text(450,184,"   inclina e sai um fio de água",12.5),
      text(450,218,"3. Sabão pendurado",12.5,"#222",True), text(450,234,"   num barbante (não some,",12.5), text(450,250,"   não fica na lama)",12.5),
      text(450,284,"Sem tocar em nada com",12.5,"#2b6a1e",True), text(450,300,"a mão suja. Gasta ~0,5 L.",12.5,"#2b6a1e",True)]
b.append(text(300,350,"pedal amarrado na corda",11.5,"#222",True))
open(D+"torneira-pe.svg","w").write(svg(680,400,"Torneira de pé para lavar as mãos (sem tocar em nada)","\n".join(b)))

# ---------- FOSSA VENTILADA ----------
b=[]
b.append('<rect x="0" y="250" width="680" height="218" fill="#e8d3b0"/>')
b.append('<line x1="0" y1="250" x2="680" y2="250" stroke="#6b4f2a" stroke-width="3"/>')
# fossa
b.append('<rect x="150" y="262" width="200" height="160" fill="#8a7458" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append('<rect x="152" y="380" width="196" height="40" fill="#5a4630"/>')
b.append('<rect x="140" y="252" width="220" height="12" fill="#9a9a9a" stroke="#1e1e1e" stroke-width="2"/>')
# casinha
b.append('<rect x="140" y="110" width="220" height="142" fill="#d9cbb0" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append('<polygon points="128,112 250,80 372,112" fill="#a0522d" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append('<rect x="160" y="150" width="54" height="100" fill="#4b3a2a" stroke="#1e1e1e" stroke-width="2"/>')
b.append(text(187,204,"porta",11,"#fff",False,"middle"))
b.append('<rect x="250" y="226" width="60" height="26" rx="6" fill="#bfbfbf" stroke="#1e1e1e" stroke-width="2"/>')
b.append('<ellipse cx="280" cy="252" rx="18" ry="4" fill="#1e1e1e"/>')
b.append(text(272,220,"assento",11,"#222",False,"middle"))
# tubo de ventilacao
b.append('<rect x="318" y="66" width="20" height="196" fill="#1e1e1e"/>')
b.append('<rect x="314" y="56" width="28" height="14" fill="#c0c0c0" stroke="#1e1e1e" stroke-width="1.5"/>')

for y in (236,186,136,106):
    b.append(arrow(328,y,328,y-30,"#f08c00",3))
b.append(arrow(240,300,320,270,"#f08c00",3))
b += [text(352,66,"tela contra moscas",12,"#222",True), text(352,82,"(as moscas vão para a luz",11.5), text(352,96,"no topo e ficam presas)",11.5),
      text(352,136,"tubo PRETO, do lado do sol,",12,"#222",True), text(352,152,"50 cm acima do telhado:",11.5), text(352,166,"esquenta e puxa o cheiro",11.5), text(352,180,"para cima",11.5)]
b += [text(380,300,"buraco: 2–3 m de fundo,",12,"#222",True), text(380,316,"~1 m de largura",11.5),
      text(380,340,"fundo pelo menos 2 m acima",11.5,"#b3001b",True), text(380,356,"do lençol de água",11.5,"#b3001b",True),
      text(380,380,"cheio até 50 cm do topo: cubra",11.5), text(380,396,"com terra, plante uma árvore e",11.5), text(380,412,"faça outra fossa ao lado",11.5)]
b.append(text(20,440,"Interior escuro (as moscas preferem a luz do tubo).",11.5,"#222",True)); b.append(text(20,458,"Pelo menos 30 m de poços, nascentes e rios, e ABAIXO deles no terreno.",11.5,"#b3001b",True))
open(D+"fossa-ventilada.svg","w").write(svg(680,468,"Fossa seca ventilada (latrina sem cheiro e sem moscas)","\n".join(b)))

# ---------- BANHEIRO SECO ----------
b=[]
# caixa
b.append('<rect x="40" y="150" width="200" height="130" fill="#c9a26b" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append('<ellipse cx="140" cy="150" rx="70" ry="12" fill="#e6e6e6" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append('<ellipse cx="140" cy="150" rx="40" ry="7" fill="#555"/>')
b.append('<path d="M80 172 L80 270 L200 270 L200 172" fill="#7aa36a" fill-opacity="0.5" stroke="#1e1e1e" stroke-width="2" stroke-dasharray="6 4"/>')
b.append(text(140,230,"balde de 20 L",12,"#1e1e1e",True,"middle"))
b.append(text(140,300,"1. Assento sobre um balde",12.5,"#222",True,"middle"))
# serragem
b.append('<path d="M290 190 L300 270 L370 270 L380 190 Z" fill="#f1dfa6" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append('<path d="M296 196 Q 335 180 374 196" fill="#e3c98a" stroke="#1e1e1e" stroke-width="1.5"/>')
b.append('<path d="M340 160 l26 -4 l-2 30 l-26 2 Z" fill="#9a9a9a" stroke="#1e1e1e" stroke-width="2"/>')
b.append(text(335,300,"2. Após cada uso, cubra",12.5,"#222",True,"middle"))
b.append(text(335,316,"com 1 caneca de serragem,",12,"#222",False,"middle"))
b.append(text(335,332,"cinza, cal ou terra seca",12,"#222",False,"middle"))
# composteira
b.append('<rect x="430" y="170" width="100" height="100" fill="#8a7458" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append('<rect x="540" y="170" width="100" height="100" fill="#6b5a40" stroke="#1e1e1e" stroke-width="2.5"/>')
b.append('<rect x="430" y="150" width="210" height="20" fill="#a0522d" stroke="#1e1e1e" stroke-width="2"/>')
b.append(text(480,226,"em uso",12,"#fff",True,"middle")); b.append(text(590,218,"descansando",12,"#fff",True,"middle")); b.append(text(590,234,"1 ano",12,"#fff",True,"middle"))
b.append(text(535,300,"3. Balde cheio: esvazie numa",12.5,"#222",True,"middle"))
b.append(text(535,316,"composteira de 2 baias; cubra",12,"#222",False,"middle"))
b.append(text(535,332,"com palha. Depois de 1 ano em",12,"#222",False,"middle"))
b.append(text(535,348,"repouso, use em ÁRVORES",12,"#222",False,"middle"))
b.append(arrow(240,215,282,215,"#555",3)); b.append(arrow(388,215,424,215,"#555",3))
b.append(box(30,368,620,58,"#eef5ff","#3f6d9e"))
b += [text(44,390,"Separar a urina (balde ou garrafa à parte) reduz muito o cheiro. Dilua 1 parte em 5–10 de",12.5),
      text(44,408,"água e use em árvores e capim. Fezes NUNCA em horta de folhas comidas cruas.",12.5)]
b.append(text(340,72,"Não precisa de água nem de buraco. Funciona dentro de casa.",13,"#2b6a1e",True,"middle"))
open(D+"banheiro-seco.svg","w").write(svg(680,436,"Banheiro seco de balde (sem água)","\n".join(b)))
