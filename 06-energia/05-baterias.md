# Baterias

**Resumo:** bateria guarda energia, mas se estraga fácil. Chumbo-ácido (carro, estacionária)
dura mais quanto **menos** você descarrega: use só até a **metade** (12,1–12,2 V em repouso) e
recarregue **cheia** sempre que puder. **LiFePO4** aguenta 80–90% de descarga por milhares de
ciclos. Bateria carregando solta **hidrogênio**, que explode: ventilação, nada de faísca, e
tire anéis e relógio antes de mexer.

---

## Tipos de bateria

| Tipo | Para que foi feita | Ciclos (descarga de 50%) | Observação |
|---|---|---|---|
| **Automotiva (de partida)** | Dar 300–800 A por segundos para o motor de arranque | 50–200 | Placas finas; morre rápido se descarregada fundo todo dia. Serve como "quebra-galho" |
| **Estacionária** (de no-break, solar) | Descargas moderadas e longas | 500–1.000 | A mais vendida para solar no Brasil (ex.: linhas "estacionárias" das marcas nacionais) |
| **Ciclo profundo / tracionária** (carrinho de golfe, empilhadeira, células de 2 V e 6 V) | Descarregar fundo todo dia | 1.000–2.000 | Placas grossas; pesadas; as melhores de chumbo |
| **AGM / Gel** (seladas, VRLA) | Sem manutenção, não derramam | 500–1.200 | Não abra; não aceitam água; não equalize |
| **LiFePO4** (lítio-ferro-fosfato) | Ciclos diários profundos | 3.000–6.000 (a 80%) | 1/3 do peso; precisa de **BMS** (placa de proteção); a mais segura das de lítio |
| **Lítio comum (Li-ion, NMC)** | Celular, notebook, patinete, power bank | 300–1.000 | Pega fogo se furada, esmagada, inchada ou sobrecarregada |

- **Chumbo-ácido líquida** (com tampinhas): aceita água destilada e equalização; dura mais se bem
  cuidada. **Selada:** não precisa de água, mas morre se esquentar ou sobrecarregar.
- **Tensão:** chumbo-ácido 12 V = 6 células de 2 V. LiFePO4 "12 V" = 4 células de 3,2 V = **12,8 V**.
- **Calor mata bateria de chumbo:** a cada ~10 °C acima de 25 °C, a vida cai pela **metade**.
  Guarde na sombra e com ventilação (nunca ao sol ou sob telha quente).

## Profundidade de descarga e vida útil

Quanto mais fundo você descarrega, menos ciclos a bateria aguenta:

| Descarga a cada ciclo | Chumbo-ácido estacionária/ciclo profundo | LiFePO4 |
|---|---|---|
| 20% | 1.500–2.500 ciclos | 6.000+ |
| 30% | 1.000–1.500 | 5.000+ |
| **50%** | **500–1.000** | 4.000–6.000 |
| 80% | 250–400 | **3.000–6.000** |
| 100% | 150–250 (e pode estragar na hora) | 2.000–3.000 |

Bateria automotiva usada em ciclo dura de 5 a 10 vezes menos que isso. Regra: **chumbo-ácido,
use até 50%; LiFePO4, até 80–90%**. Bateria de chumbo deixada descarregada **sulfata** (cristais
brancos nas placas) em poucas semanas e perde capacidade para sempre.

## Quanto de carga tem? (tensão em repouso)

Meça com multímetro **depois de 4 horas ou mais sem carregar e sem nada ligado** (de manhã
cedo, antes do sol, é o melhor horário). Tensão medida com carga ligada ou carregando engana.

| Carga | Chumbo-ácido 12 V (25 °C) | LiFePO4 12,8 V (aprox.) |
|---|---|---|
| 100% | 12,7 V ou mais | 13,4–13,6 V |
| 90% | 12,6 V | 13,3 V |
| 80% | 12,5 V | 13,3 V |
| 70% | 12,4 V | 13,2 V |
| 60% | 12,2 V | 13,2 V |
| **50%** | **12,1 V** — pare aqui (chumbo) | 13,1 V |
| 40% | 12,0 V | 13,0 V |
| 30% | 11,8 V | 13,0 V |
| 20% | 11,7 V | 12,9 V — pare aqui (LiFePO4) |
| 10% | 11,5 V | 12,5 V |

- Bateria de **24 V**: multiplique por 2. De **48 V**: por 4.
- AGM e gel ficam cerca de 0,1 V acima da tabela.
- **LiFePO4 mantém quase a mesma tensão de 90% a 20%**: só um **monitor com shunt** (contador de
  Ah) ou o aplicativo do BMS mostra a carga real.
- **Densímetro** (chumbo líquida): 1,265–1,280 = cheia; 1,225 = 75%; 1,190 = 50%; 1,155 = 25%;
  1,120 = vazia. Uma célula com 0,050 a menos que as outras está estragando.

## Carregamento

Carregadores e controladores bons fazem 3 etapas: **carga forte** (corrente máxima), **absorção**
(tensão alta fixa até a corrente cair) e **flutuação** (tensão menor para manter cheia).

| Tipo (12 V, a 25 °C) | Absorção | Flutuação | Equalização |
|---|---|---|---|
| Chumbo líquida (aberta) | 14,4–14,8 V | 13,5–13,8 V | 15,0–15,5 V por 1–3 h, a cada 1–3 meses |
| Chumbo selada "livre de manutenção" | 14,2–14,4 V | 13,3–13,8 V | não |
| AGM | 14,4–14,7 V | 13,5–13,8 V | não |
| Gel | 14,1–14,4 V | 13,5–13,8 V | não |
| LiFePO4 | 14,2–14,6 V | 13,4–13,6 V ou nenhuma | **nunca** |

- **Siga o que está escrito na bateria** quando houver.
- **Calor:** em chumbo-ácido, tire **0,03 V para cada °C acima de 25 °C** (a 35 °C, absorção de
  ~14,1 V em vez de 14,4 V). Bons controladores têm sensor de temperatura.
- **Corrente de carga:** chumbo, **10–20% da capacidade** (bateria de 100 Ah: 10–20 A). LiFePO4
  aceita até 50% (50 A).
- Chumbo-ácido precisa chegar a **100% com frequência** (pelo menos 1 vez por semana). Ficar dias
  em 60–80% também sulfata.
- **LiFePO4 não carrega abaixo de 0 °C** (o BMS bom bloqueia). Raro no Brasil, mas acontece em
  manhãs de geada no Sul.
- **Bateria quente** demais para pôr a mão, inchada, fervendo ou com cheiro de ovo podre: **pare a
  carga**. Está estragada ou sobrecarregada.

## Gases e ácido

> **ATENÇÃO:** bateria de chumbo carregando solta **hidrogênio**, gás sem cheiro que **explode**
> com qualquer faísca (de 4% a 75% no ar). A explosão joga pedaços de plástico e **ácido
> sulfúrico** no rosto.
> - Baterias em lugar **ventilado**, nunca em quarto, armário fechado ou junto de fogão; caixa de
>   bateria com saída de ar no **alto** (o hidrogênio sobe).
> - **Nada de cigarro, chama ou faísca** perto. Ligue e desligue o carregador **na tomada**, com as
>   garras já presas (a faísca acontece longe da bateria).
> - Na chupeta de carro, a **última garra** (preta) vai num **metal do motor, longe da bateria**.
> - Use **óculos** e luvas. Tire anel, relógio e correntes (curto de bateria derrete metal).

**Ácido nos olhos:** lave com água corrente **por 15–20 minutos**, pálpebras abertas, e procure
socorro. **Na pele:** muita água. **Derramou:** jogue **bicarbonato de sódio** ou cal até parar de
borbulhar, depois lave.

## Manutenção (chumbo-ácido líquida)

**Mensal (mais vezes no calor):**
1. **Nível do líquido:** abra as tampinhas. O líquido deve cobrir as placas com **~1 cm** (ou ir
   até a marca/anel indicador). Complete **só com água destilada ou deionizada**, **depois** de
   carregar (se as placas estiverem descobertas, ponha só o suficiente para cobrir, carregue, e
   então complete). **Nunca encha até a boca** (transborda ácido ao carregar).
   - Sem água destilada: use água de um [destilador](../01-agua/02-tratamento-e-purificacao.md), ou
     água de chuva colhida **direto do céu** numa vasilha plástica limpa (não do telhado).
     **Nunca** água de torneira, poço ou mineral (os minerais estragam as placas). **Nunca** ponha
     ácido.
2. **Bornes e terminais:** o pó branco ou azul-esverdeado (zinabre) causa mau contato. Desligue,
   escove com **1 colher de sopa de bicarbonato em 1 copo de água** e escova de aço, enxágue, seque
   e passe **vaselina ou graxa** fina. Aperte bem.
3. **Tampa limpa e seca:** sujeira úmida com ácido descarrega a bateria aos poucos.
4. **Anote a tensão em repouso** de cada bateria do banco. Uma que fica sempre mais baixa está
   ruim e vai derrubar as outras.
5. **Equalização** (só líquida), a cada 1–3 meses: carga a 15,0–15,5 V por 1–3 horas, com
   ventilação. Iguala as células e solta a sulfatação. Desligue aparelhos 12 V antes (tensão alta).

## Pilhas recarregáveis (NiMH) e baterias de lítio pequenas

- **NiMH (AA, AAA):** 1,2 V (as alcalinas têm 1,5 V, mas quase todo aparelho funciona com 1,2 V).
  AA 1.900–2.500 mAh; AAA 800–1.000 mAh. **500–2.000 recargas**.
- Prefira as **"pré-carregadas" / baixa autodescarga (LSD)**: guardam 70–85% da carga após 1 ano.
- **Carregador inteligente** (desliga sozinho). Com carregador simples, carga lenta: **10% da
  capacidade por 14–16 horas** (pilha de 2.000 mAh: 200 mA por 14–16 h) e não passe disso.
- Carregadores USB funcionam com **painel solar pequeno** ou power bank.
- Não misture pilhas velhas e novas, nem marcas diferentes, no mesmo aparelho.
- **Nunca recarregue pilha alcalina ou de zinco comum:** vaza, esquenta, pode estourar.
- **Lítio 18650 e similares (3,7 V):** muita energia em pouco espaço; use carregador próprio,
  nunca descarregue abaixo de ~3,0 V por célula, carregue sobre superfície que não queima.

> **ATENÇÃO:** bateria de lítio **inchada, amassada, furada ou quente sem motivo** pode pegar fogo
> sozinha, com chama violenta que a água não apaga bem. Leve para fora, sobre terra ou areia, longe
> de coisas que queimam, e cubra com areia. Nunca jogue no lixo comum nem no fogo.

## Power banks (carregador portátil)

- A capacidade escrita (mAh) é a **3,7 V**. O celular recebe só **60–70%** dela (perdas na
  conversão para 5 V).
- **10.000 mAh** ≈ 37 Wh → ~24 Wh úteis → **1,5–2 cargas** de um celular comum. **20.000 mAh** →
  3–4 cargas.
- Power bank "solar" de bolso: o painelzinho de 1–3 W leva **dias** para encher. Melhor um painel
  dobrável USB de **10–20 W** separado.
- Guarde com **40–60% de carga**, em lugar fresco (carro ao sol estraga), e recarregue a cada
  3–6 meses.

## Armazenamento de longo prazo

| Tipo | Como guardar | Cuidado |
|---|---|---|
| Chumbo-ácido | **100% carregada**, lugar fresco e seco | Perde 2–5% por mês (mais no calor). Recarregue quando cair a **12,4 V** (a cada 1–3 meses) ou deixe num painel pequeno (5–10 W) com controlador. **Nunca guarde descarregada** |
| LiFePO4 | **50–60%**, BMS desligado (se tiver chave) | Confira a cada 6 meses |
| Lítio comum, power bank | 40–60% | Confira a cada 3–6 meses; descarte se inchar |
| NiMH baixa autodescarga | Carregadas | Recarregue a cada 6–12 meses |
| Alcalinas | Fora dos aparelhos, na embalagem, lugar fresco | 5–10 anos; vazam e corroem os contatos |
| Pilhas de lítio AA/AAA (não recarregáveis) | Lugar fresco | 15–20 anos: as melhores para estoque e lanternas de emergência |

## Descarte

- **Chumbo-ácido:** devolva na loja que vende baterias (no Brasil a loja é **obrigada** a receber a
  usada). O chumbo é reciclado quase 100%.
- **Lítio e pilhas:** pontos de coleta (supermercados, lojas de eletrônicos).
- **Sem coleta (colapso):** guarde as baterias velhas em lugar coberto, sobre piso de concreto ou
  dentro de bacia plástica, **longe de poços, hortas e crianças**.

> **ATENÇÃO:** não abra bateria de chumbo nem **derreta o chumbo** em casa: vapor e pó de chumbo
> envenenam (principalmente crianças: atraso no desenvolvimento, anemia, dano nos rins).

## Bateria de carro para luz e celular

Uma bateria de carro comum (45–70 Ah) usada até a metade dá **~300–400 Wh**: uma lâmpada LED de
5 W por **60–80 horas**, ou **12–15 cargas** de celular.

**Como ligar:**
1. **Tomada de acendedor com garras jacaré** (vende em loja de autopeças) + **fusível de 10 A** no
   fio positivo (vermelho no +, preto no −).
2. Nela, ligue um **carregador USB de carro** (celular, rádio USB, lanterna) ou **lâmpadas LED
   12 V** (de carro, caminhão, barco, fita de LED 12 V).
3. Para aparelhos de 127/220 V pequenos (até ~150 W), um **inversor pequeno** de tomada de
   acendedor. Acima disso, inversor ligado direto nos bornes com cabo grosso e fusível.
4. Se o carro ainda vai precisar dar partida, **não deixe a bateria baixar de 12,4 V**. Só para
   luz, pare em **12,2 V**.

**Recarregar:**
- **Painel solar de 20–50 W com controlador** (o melhor; um de 50 W repõe ~150–200 Wh num dia de sol).
- Motor do carro: em marcha lenta carrega pouco e gasta **0,6–1 L de combustível por hora**. Se
  for usar o motor, deixe a **1.500–2.000 rpm** por ~1 hora, **ao ar livre**.

> **ATENÇÃO:** nunca ligue o motor em garagem ou lugar fechado (monóxido de carbono mata em
> minutos). Não deixe a bateria do carro em cima de banco, no quarto ou em lugar fechado enquanto
> carrega.

**Chupeta (dar partida com outro carro):** ambos desligados → garra **vermelha** no + da bateria
fraca → **vermelha** no + da boa → **preta** no − da boa → **preta** num **metal sem pintura do
motor** do carro parado, longe da bateria. Ligue o carro bom, espere 2–3 min, dê a partida. Tire
as garras na **ordem inversa**. Mais em [Mecânica automotiva](../08-ferramentas-e-mecanica/02-mecanica-automotiva.md).

**Baterias de no-break (12 V 7–9 Ah):** dão ~40 Wh úteis — uma lâmpada LED de 3 W por ~12 horas.
Ótimas para luz de emergência com um painel de 10 W.

---

Ver também: [Energia solar](04-energia-solar.md) · [Eletricidade básica](03-eletricidade-basica.md) · [Iluminação](08-iluminacao.md) · [Motores e geradores](../08-ferramentas-e-mecanica/03-motores-pequenos-e-geradores.md) · [Rotinas de manutenção](../anexos/03-rotinas-de-manutencao.md)
