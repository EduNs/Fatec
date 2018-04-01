#-------------------------------------------------------
# Exercício 1
print("============== Exercício 1 ==============")
nota = float(input("nota: "))
while nota < 0 or nota > 10:
    print("nota inválida!")
    nota = float(input("nota: "))
#-------------------------------------------------------
#-------------------------------------------------------
# Exercício 2
print("============== Exercício 2 ==============")
usuario = input("usuário: ")
senha = input("senha: ")
while usuario == senha:
    print("o usuário não pode ser igual à senha!")
    usuario = input("usuário: ")
    senha = input("senha: ")
#-------------------------------------------------------
#-------------------------------------------------------
# Exercício 3
print("============== Exercício 3 ==============")
populacao_A = 80000
populacao_B = 200000
anos = 0
while populacao_A <= populacao_B:
    populacao_A += populacao_A * 0.03
    populacao_B += populacao_B * 0.015
    anos += 1
print(f"anos necessários: {anos}")
#-------------------------------------------------------
#-------------------------------------------------------
# Exercício 4
print("============== Exercício 4 ==============")
a,b = 1,1
x = 1
soma_anterior = 0
n = int(input("n: "))
print("F1:1\nF2:1")
while x <= n-2:
    a,b = b,a+b
    x += 1
    print(f"F{x}:{b}")
#-------------------------------------------------------
#-------------------------------------------------------
# Exercício 5
print("============== Exercício 5 ==============")
a = int(input('a: '))
b = int(input('b: '))
while a % b != 0:
	a,b = b, a%b
print(f"mdc: {b}")
#-------------------------------------------------------
