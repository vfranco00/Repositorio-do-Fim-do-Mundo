import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "02-saude", "img") + "/"
# ---------- RCP ----------
b = []
b.append('<line x1="20" y1="342" x2="440" y2="342" stroke="#6b4f2a" stroke-width="3"/>')
b.append(limb([(300,300),(424,302)], 30, VIT)); b.append(limb([(432,300),(438,276)], 12, VIT))
b.append(limb([(130,296),(300,298)], 46, VIT)); b.append(head(96, 294, 25, VIT, 0, -1))
b.append(limb([(258,330),(362,332)], 20, SOC)); b.append(limb([(272,238),(258,330)], 27, SOC))
b.append(limb([(272,238),(206,154)], 42, SOC)); b.append(head(182, 122, 23, SOC, -0.55, 0.83))
b.append(limb([(206,158),(206,262)], 14, SOC)); b.append('<ellipse cx="206" cy="268" rx="17" ry="8" fill="%s" stroke="%s" stroke-width="2"/>' % (SKIN, OUT))
b.append('<line x1="206" y1="62" x2="206" y2="282" stroke="#d62828" stroke-dasharray="7 5" stroke-width="2"/>')
b.append(arrow(150, 196, 150, 270)); b.append(arrow(124, 270, 124, 204, "#2b8a3e", 3))
b += [text(20,188,"afunde",13,"#b22",True), text(20,205,"5–6 cm",13,"#b22",True), text(20,236,"deixe o peito",12,"#2b6a1e"), text(20,251,"voltar todo",12,"#2b6a1e"),
      text(216,74,"ombros em cima das mãos,",12.5,"#b22"), text(216,91,"braços RETOS, use o peso do corpo",12.5,"#b22")]
b.append('<rect x="460" y="56" width="206" height="252" rx="8" fill="#f7f7f7" stroke="#999"/>')
b.append(text(563,80,"Onde pôr as mãos",13.5,"#222",True,"middle"))
b.append('<path d="M500 100 Q563 86 626 100 L636 282 Q563 298 490 282 Z" fill="#f2d7c2" stroke="#8a6a50" stroke-width="2"/>')
b.append('<rect x="556" y="110" width="14" height="122" rx="5" fill="#fff" stroke="#8a6a50"/>')
b.append('<circle cx="523" cy="170" r="4" fill="#a0705a"/><circle cx="603" cy="170" r="4" fill="#a0705a"/><line x1="510" y1="170" x2="616" y2="170" stroke="#999" stroke-dasharray="3 3"/>')
b.append('<ellipse cx="563" cy="184" rx="23" ry="17" fill="#d62828" fill-opacity="0.8" stroke="#7a1010" stroke-width="2"/>')
b.append(text(563,189,"AQUI",11,"#fff",True,"middle"))
b += [text(470,326,"Centro do peito, metade de",11.5), text(470,341,"baixo do esterno (osso do meio),",11.5), text(470,356,"na linha dos mamilos.",11.5)]
b.append(box(20,368,640,64))
b += [text(34,390,'<tspan font-weight="bold">Ritmo:</tspan> 100–120/min · <tspan font-weight="bold">Profundidade:</tspan> 5–6 cm · <tspan font-weight="bold">30 compressões : 2 ventilações</tspan>',13.5),
      text(34,409,"Sem treino para ventilar? Só compressões, sem parar. Troque de pessoa a cada 2 minutos.",13),
      text(34,426,"Criança: 1–2 mãos, ~5 cm · Bebê: 2 dedos, ~4 cm · Afogado: 5 ventilações primeiro.",12.5)]
open(D+"rcp.svg","w").write(svg(680,444,"RCP em adulto — compressões no peito","\n".join(b)))

# ---------- ENGASGO ----------
b = []
b.append(text(170,62,"Adulto e criança acima de 1 ano",14.5,"#222",True,"middle"))
b.append('<line x1="40" y1="352" x2="310" y2="352" stroke="#6b4f2a" stroke-width="3"/>')
# socorrista atras
b.append(limb([(132,238),(122,346)],18,SOC)); b.append(limb([(142,238),(156,346)],18,SOC))
b.append(limb([(138,128),(136,238)],42,SOC)); b.append(head(142,94,23,SOC,1,0))
# vitima na frente
b.append(limb([(184,242),(176,346)],18,VIT)); b.append(limb([(194,242),(208,346)],18,VIT))
b.append(limb([(200,132),(188,242)],42,VIT)); b.append(head(210,98,23,VIT,1,0.15))
b.append(limb([(210,142),(236,150),(222,124)],11,VIT)); b.append(hand(220,122,7))
b.append(limb([(148,138),(170,194),(208,200)],13,SOC)); b.append(hand(216,200,11))
b.append('<path d="M262 226 Q236 226 232 202 L232 172" stroke="#d62828" stroke-width="4" fill="none"/><polygon points="224,176 240,176 232,158" fill="#d62828"/>')
b += [text(244,170,"para dentro",11.5,"#b22",True), text(244,186,"e para cima",11.5,"#b22",True)]
b += [text(242,248,"punho entre o",12), text(242,263,"umbigo e o fim",12), text(242,278,"do esterno",12)]
b += [text(240,96,"vítima com a",11,"#444"), text(240,109,"mão na garganta",11,"#444")]
b += [text(30,374,"Repita até o objeto sair. Grávida ou obeso: mãos",12), text(30,390,"no centro do peito. Desmaiou: deite e faça RCP.",12)]
b.append('<line x1="340" y1="48" x2="340" y2="392" stroke="#ccc" stroke-width="2"/>')
b.append(text(512,62,"Bebê (menos de 1 ano)",14.5,"#222",True,"middle"))
# painel 1
b.append(text(356,90,"1. Cinco tapas nas costas",13,"#222",True))
b.append(limb([(650,150),(436,178)],24,SOC)); b.append(hand(424,180,12))
b.append(limb([(576,128),(608,124),(622,146)],10,VIT)); b.append(limb([(574,138),(600,150),(596,170)],10,VIT))
b.append(limb([(570,134),(476,148)],32,VIT)); b.append(head(452,156,19,VIT,-0.35,0.9))
b.append(limb([(490,156),(470,182)],8,VIT))
b.append('<rect x="490" y="96" width="34" height="14" rx="6" fill="%s" stroke="%s" stroke-width="2"/>' % (SKIN,OUT))
b.append(arrow(507,104,507,124))
b += [text(536,104,"entre as escápulas,",11.5), text(536,118,"com a base da mão",11.5)]
b += [text(356,206,"cabeça MAIS BAIXA que o corpo;",11.5,"#444"), text(356,220,"segure pelo queixo, não pela garganta",11.5,"#444")]
# painel 2
b.append(text(356,250,"2. Vire: cinco compressões no peito",13,"#222",True))
b.append(limb([(650,316),(436,344)],24,SOC)); b.append(hand(424,346,12))
b.append(limb([(576,296),(608,290),(622,312)],10,VIT))
b.append(limb([(570,300),(476,314)],32,VIT)); b.append(head(452,322,19,VIT,-0.3,-0.9))
b.append(limb([(500,268),(500,292)],6,SKIN)); b.append(limb([(512,268),(512,290)],6,SKIN))
b += [text(522,264,"2 dedos, centro do peito,",11.5), text(522,278,"abaixo dos mamilos",11.5)]
b += [text(356,374,"3. Repita 5 tapas + 5 compressões até sair.",12.5,"#222",True), text(356,391,"Desmaiou: RCP de bebê. Tire o objeto só se visível.",11.5)]
open(D+"engasgo.svg","w").write(svg(680,400,"Engasgo grave — adulto e bebê","\n".join(b)))

# ---------- POSICAO LATERAL ----------
b = []
b.append('<rect x="30" y="52" width="620" height="292" rx="10" fill="#f4efe6" stroke="#c9bba0"/>')
b.append(text(340,74,"vista de cima (pessoa deitada de lado no chão)",12.5,"#6b4f2a",False,"middle"))
# perna de baixo esticada
b.append(limb([(350,172),(578,180)],24,VIT)); b.append(limb([(586,180),(590,200)],11,VIT))
# tronco (costas para cima na imagem, frente para baixo)
b.append(limb([(170,170),(350,174)],58,VIT))
# perna de cima: coxa para a frente (90 graus), canela paralela ao corpo
b.append(limb([(346,186),(372,282),(486,288)],26,VIT)); b.append(limb([(494,288),(498,308)],11,VIT))
# braco de cima: para a frente, mao sob a bochecha
b.append(limb([(196,190),(214,280),(132,240)],15,VIT))
b.append(head(118,182,32,VIT,-0.45,0.89)); b.append(hand(128,236,11))
b.append('<line x1="100" y1="152" x2="84" y2="122" stroke="#555"/>'); b += [text(44,102,"cabeça para trás, boca",12.5), text(44,117,"virada para o chão",12.5)]
b.append('<line x1="140" y1="246" x2="180" y2="304" stroke="#555"/>'); b += [text(170,318,"mão de cima sob a bochecha",12.5)]
b.append('<line x1="372" y1="282" x2="392" y2="302" stroke="#555"/>'); b += [text(376,318,"perna de cima dobrada em ângulo reto,",12.5), text(376,333,"joelho no chão: trava o corpo",12.5)]
b += [text(470,154,"perna de baixo esticada",12.5)]
b += [text(240,132,"costas",12,"#555")]
b.append(box(30,356,620,56,"#eef5ff","#3f6d9e"))
b += [text(44,379,"Verifique a respiração a cada minuto. Parou? Vire de costas e comece a RCP.",13), text(44,399,"Suspeita de lesão na coluna: só vire se necessário, em bloco, com 2 a 4 pessoas.",13)]
open(D+"posicao-lateral.svg","w").write(svg(680,422,"Posição lateral de segurança","\n".join(b)))
