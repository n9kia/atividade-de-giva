def empenho(nota): 
    if nota >= 5.0:
        return "Aprovado"
    else:
        return "Reprovado"

# Abre o arquivo "alunos.txt" para escrita
c = open("alunos.txt", "w")
c.write("Max : 7.0\n")
c.write("Borgia : 8.0\n")
c.write("Alexandre : 4.0\n")
c.write("Juliano : 3.0\n")
c.close()

# Abre o arquivo "alunos.txt" para leitura
lista = open("alunos.txt", "r")

# Abre os arquivos "Aprovados.txt" e "Reprovados.txt" para escrita
aprovados = open("Aprovados.txt", "w")
reprovados = open("Reprovados.txt", "w")

for linha in lista:
    nome, pontuacao = linha.strip().split(":")
    nota = float(pontuacao)
    resultado = empenho(nota)

    if resultado == "Aprovado":
        aprovados.write(f"{nome} : {nota}\n")
    else: 
        reprovados.write(f"{nome} : {nota}\n")

# Fecha os arquivos após escrever neles
lista.close()
aprovados.close()
reprovados.close()

print("Os arquivos 'Aprovados.txt' e 'Reprovados.txt' foram criados com sucesso.")

# CÉSAR
#         HENRIQUE
#                  2° B