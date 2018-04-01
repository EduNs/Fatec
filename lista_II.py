#-------------------------------------------------------
# Exercício 1
print("============== Exercício 1 ==============")
ladoA = int(input("Lado A: "))
ladoB = int(input("Lado B: "))
ladoC = int(input("Lado C: "))

if ladoA < ladoB + ladoC or ladoB < ladoA + ladoC or ladoC < ladoA + ladoB:
    if ladoA == ladoB == ladoC:
        print("Equilátero")
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print("Isósceles")
    elif ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
        print("Escaleno")
else: print("Não é um triângulo")
#-------------------------------------------------------

#-------------------------------------------------------
# Exercício 2
print("\n\n============== Exercício 2 ==============")
ano = int(input("ano: "))
if ano % 4 == 0:
    if ano % 100 != 0:
        print(f"{ano} é bissexto")
    else:
        print(f"{ano} não é bissexto")
elif ano % 400 == 0:
    print(f"{ano} é bissexto!")
else: print(f"{ano} não é bissexto")
#-------------------------------------------------------

#-------------------------------------------------------
# Exercício 3
print("\n\n============== Exercício 3 ==============")
peso = int(input("peso: "))
excesso = multa = 0
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
print(f"Excesso de peso: {excesso}kg\nMulta: R${multa}")
#-------------------------------------------------------

#-------------------------------------------------------
# Exercício 4
print("\n\n============== Exercício 4 ==============")
num1 = int(input("número 1: "))
num2 = int(input("número 2: "))
num3 = int(input("número 3: "))
if num1 > num2 and num1 > num3:
    print(f"{num1} é o maior")
elif num2 > num1 and num2 > num3:
    print(f"{num2} é o maior")
elif num3 > num1 and num3 > num2:
    print(f"{num3} é o maior")
#-------------------------------------------------------

#-------------------------------------------------------
# Exercício 5
print("\n\n============== Exercício 5 ==============")
num1 = int(input("número 1: "))
num2 = int(input("número 2: "))
num3 = int(input("número 3: "))
if num1 > num2 and num1 > num3:
    print(f"{num1} é o maior")
elif num2 > num3:
    print(f"{num2} é o maior")
else: print(f"{num3} é o maior")

if num1 < num2 and num1 < num3:
    print(f"{num1} é o menor")
elif num2 < num3:
    print(f"{num2} é o menor")
else: print(f"{num3} é o menor")
#-------------------------------------------------------

#-------------------------------------------------------
# Exercício 6
print("\n\n============== Exercício 6 ==============")
valor_hora = int(input("valor por hora: "))
horas_trabalhadas = int(input("horas trabalhadas: "))
salario = valor_hora * horas_trabalhadas
imposto_renda = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
salario = salario - sindicato - inss - imposto_renda
print(f"salário bruto: R${valor_hora * horas_trabalhadas}")
print(f"INSS: R${inss:.2f}")
print(f"sindicato: R${sindicato:.2f}")
print(f"imposto de renda: R${imposto_renda:.2f}")
print(f"salário líquido: R${salario:.2f}")
#-------------------------------------------------------

#-------------------------------------------------------
# Exercício 7
print("\n\n============== Exercício 7 ==============")
area = int(input("área: "))
if area % 54 == 0:
    latas = area / 54
else:
    latas = int(area / 54) + 1
print(f"preço total: R${latas * 80}\nlatas: {latas}")
#-------------------------------------------------------
