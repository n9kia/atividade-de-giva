perguntinha1=["diga-me, cr7 ou messi?",
              "Você tem inimigos?",
              "Qual o time mais insignificante da história?",
              "Onde ocorreu a primeira copa das confederações?",
              "Onde surgiu o volei?",
              "QUAL O JOGADOR QUE MAIS PERDEU PENALTI NO SÉCULO XXI?",
              "quantas copas tem o mexico?",
              "qual o time nordestino com maior número de invencibilidade no brasileiro?"]

respostas2=["cr7",
            "nao",
            "sport",
            "arabia saudita",
            "estados unidos",
            "messi",
            "zero",
            "santa cruz"]

x=0
for i in range (8):
   a=input (perguntinha1[i]) 
   x = x + 1 
   if (a== respostas2[i]):
      print("sim, sim")
   else:
      print("não, não")

print(f"sua nota {x}")
