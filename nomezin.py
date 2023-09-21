# names = ['pedro','eric',"kaio"]
# filename = "meuArquivo.txt"
# file = open(filename, "w")
# for name in names:
#  file.write ("%s\n" % name)
# file.close()

# # fazendo algo legal que giva pediu. listas de um estoque e como relacionar essas coisas...deve ser isso. ANAUÊ

# produtos= ["macaxeira","charque","cuzcuz", "leite","cafezin",]
# estoque_quant= ["10", "15","11","8","20"]
# preço_produto= ["12","26","3","7","6"]
 
# # atividade muito braba que eu fiz 7
estoque=[]
produto=[]
preço=[]

concluir=False

while (not concluir):
    print("Digite o nome do produto:")
    produtos = input()
    print("Digite a quantidade produtos no estoque")
    estoque_quant= input()
    print("digite o preço do produto")
    preço_produto= input()
    produto.append(produtos)
    estoque.append(estoque_quant)
    preço.append (preço_produto)
    print("Deseja inserir outro produto?(s/n)")
    concluir = input() == "n"

input("Pressione Enter pra terminar...")

import os 
filename= "meuArquivozinho.txt"
file= open(filename, "w")

for name in range(len(produto)):
        linha= f"produto: {produto[name]}\nestoque do produto:{estoque[name]}\npreços {preço[name]}\n\n"
        file.write (linha)
file.close() 
os.system(f"notepad {filename}")