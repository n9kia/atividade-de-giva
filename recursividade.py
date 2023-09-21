#César henrique

# contagem regressiva 
import time
def contagem_morrida(numero_mortal):
    print(numero_mortal)
    time.sleep(1)
    if numero_mortal == 0:
        return 0
    else: return contagem_morrida(numero_mortal - 1)

numero_mortO= int(input("diga-me um número: "))

contagem_morrida(numero_mortO)

print("NÃO OLHE PARA TRÁS!!")

#contagem recursiva
# def soma_estranha (numerozin):
#     if numerozin == 1: 
#         return 1
#     else: return numerozin + soma_estranha(numerozin - 1)
    
    
# numerozin= int(input("Diga-me um número legal: "))

# x=soma_estranha(numerozin)
# print(f"a soma do teu número até 1 é {x}")

# ##inversão de string
def inversão_string(s):
    if len(s) == 0: return ""
    else: return s[-1] + inversão_string(s[:-1])

print("inverter string")
print(f"recursividade: {inversão_string('recursividade')}")

#potencia
def potencia_recursiva(base,expoente):
    if expoente== 0: return 1
    else: return base * potencia_recursiva(base,expoente - 1)

print(f"2 elevado a 3: {potencia_recursiva(2,3)}")
