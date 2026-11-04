import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from fig import *
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "02-saude", "img") + "/"
# ---------- CORDAO ----------
b = []
# barriga do bebe
b.append('<path d="M20 90 Q 150 70 210 110 Q 240 150 210 200 Q 150 240 20 220 Z" fill="#f6d3b7" stroke="#1e1e1e" stroke-width="3"/>')
b.append(text(70,160,"barriga",14,"#7a5a40",True))
b.append(text(70,178,"do bebê",14,"#7a5a40",True))
# cordao
b.append('<path d="M214 150 C 300 120, 360 190, 450 150 S 600 120, 660 160" fill="none" stroke="#1e1e1e" stroke-width="20" stroke-linecap="round"/>')
b.append('<path d="M214 150 C 300 120, 360 190, 450 150 S 600 120, 660 160" fill="none" stroke="#c9d6e8" stroke-width="15" stroke-linecap="round"/>')
b.append('<path d="M214 150 C 300 120, 360 190, 450 150 S 600 120, 660 160" fill="none" stroke="#b9506a" stroke-width="3" stroke-dasharray="10 8"/>')
b.append(text(600,120,"→ placenta",13,"#444"))
# amarras
for x,y in ((262,138),(340,158)):
    b.append(f'<rect x="{x-5}" y="{y-20}" width="10" height="40" rx="3" fill="#f7f0d0" stroke="#1e1e1e" stroke-width="2.5"/>')
# medidas
b.append('<line x1="214" y1="214" x2="262" y2="214" stroke="#d62828" stroke-width="2"/><line x1="214" y1="207" x2="214" y2="221" stroke="#d62828" stroke-width="2"/><line x1="262" y1="207" x2="262" y2="221" stroke="#d62828" stroke-width="2"/>')
b.append(text(238,240,"2 cm",13,"#b3001b",True,"middle"))
b.append('<line x1="214" y1="262" x2="340" y2="262" stroke="#d62828" stroke-width="2"/><line x1="214" y1="255" x2="214" y2="269" stroke="#d62828" stroke-width="2"/><line x1="340" y1="255" x2="340" y2="269" stroke="#d62828" stroke-width="2"/>')
b.append(text(277,288,"5 cm",13,"#b3001b",True,"middle"))
# tesoura / corte
b.append('<line x1="301" y1="96" x2="301" y2="206" stroke="#1d4ed8" stroke-width="2.5" stroke-dasharray="6 4"/>')
b.append(text(301,88,"CORTE AQUI",13,"#1d4ed8",True,"middle"))
b += [text(262,112,"1º nó",12,"#222",True,"middle"), text(352,206,"2º nó",12,"#222",True,"middle")]
b.append(box(20,302,640,96,"#f6f9ff","#3f6d9e"))
b += [text(34,324,"1. Espere 1 a 3 minutos (ou até o cordão parar de pulsar), com o bebê seco e no colo da mãe.",12.5),
      text(34,344,"2. Amarre bem apertado com barbante/cadarço FERVIDO: um nó a 2 cm e outro a 5 cm da barriga.",12.5),
      text(34,364,"3. Corte ENTRE os dois nós com lâmina ou tesoura nova/fervida.",12.5),
      text(34,384,"4. Mantenha o coto limpo e SECO, sem pó, pomada caseira ou faixa. Cai sozinho em 5–15 dias.",12.5)]
open(D+"cordao-umbilical.svg","w").write(svg(680,408,"Como amarrar e cortar o cordão umbilical","\n".join(b)))

# ---------- MUAC ----------
b = []
# braco
b.append(limb([(60,120),(330,128)],70,"#f6d3b7"))
b.append(f'<ellipse cx="350" cy="128" rx="26" ry="40" fill="#f6d3b7" stroke="{OUT}" stroke-width="2.5"/>')
b.append(text(40,82,"ombro",12,"#444")); b.append(text(330,82,"cotovelo",12,"#444"))
b.append('<rect x="186" y="86" width="22" height="86" rx="4" fill="#fff" stroke="#1e1e1e" stroke-width="2"/>')
b.append('<line x1="208" y1="92" x2="400" y2="92" stroke="#555"/>'); b.append(text(404,90,"fita ou barbante em volta,",12,"#222")); b.append(text(404,106,"justa, sem apertar",12,"#222"))
b.append(text(196,200,"no meio do braço esquerdo, braço solto",12,"#222",False,"middle"))
# fita
y = 240; x0 = 40
cols = [("#d62828","menos de 11,5 cm","DESNUTRIÇÃO GRAVE","Risco de morte: alimentação terapêutica, tratar infecções"),
        ("#f2c94c","11,5 a 12,5 cm","DESNUTRIÇÃO MODERADA","Reforçar alimentação: + 1–2 refeições/dia, gordura, proteína"),
        ("#2b8a3e","12,5 cm ou mais","NORMAL","Manter alimentação e acompanhar todo mês")]
for i,(c,a,t1,t2) in enumerate(cols):
    yy = y + i*52
    b.append(f'<rect x="{x0}" y="{yy}" width="160" height="44" rx="6" fill="{c}" stroke="#1e1e1e" stroke-width="1.5"/>')
    b.append(text(x0+80, yy+28, a, 13, "#fff" if c!="#f2c94c" else "#222", True, "middle"))
    b.append(text(x0+176, yy+19, t1, 13.5, "#222", True))
    b.append(text(x0+176, yy+37, t2, 12, "#333"))
b.append(text(40,404,"Também é GRAVE, em qualquer medida: inchaço nos dois pés",12.5,"#b3001b",True)); b.append(text(40,420,"(aperte o peito do pé por 3 segundos: se fica a marca do dedo).",12,"#b3001b"))
b.append(text(40,440,"Improvise a fita: barbante marcado a 11,5 e 12,5 cm com régua. Vale para crianças de 6 meses a 5 anos.",12))
open(D+"muac.svg","w").write(svg(680,452,"Medida do braço da criança (6 meses a 5 anos)","\n".join(b)))
