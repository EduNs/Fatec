#-------------------------------------------------------
# Exercício 1
print("============= Exercício 1 ==============")
n1 = int(input("n1: "))
n2 = int(input("n2: "))

print(f'soma: {n1+n2}')
#-------------------------------------------------------
#-------------------------------------------------------
# Exercício 2
print("\n\n============= Exercício 2 ==============")
valor_metros = int(input("valor em metros: "))
valor_milimetros = valor_metros * 1000

print(f'valor em milímetros: {valor_milimetros}mm')
#-------------------------------------------------------

#-------------------------------------------------------
# Exercício 3
print("\n\n============= Exercício 3 ==============")
dias = int(input("dias: "))
horas = int(input("horas: "))
minutos = int(input("minutos: "))
segundos = int(input("segundos: "))
total_segundos = (minutos * 60) + (horas * 60 * 60) + (dias * 365 * 24 * 60) + segundos

print(f'total de segundos: {total_segundos:.0f}s')
#-------------------------------------------------------

#-------------------------------------------------------
# Exercício 4
print("\n\n============= Exercício 4 ==============")
salario = float(input("salário: "))
porcentagem_aumento = int(input("porcentagem de aumento: ")) / 100
aumento_salario = salario * porcentagem_aumento
novo_salario = salario + aumento_salario

print(f'aumento: R${aumento_salario}\nnovo salário: R${novo_salario}')
#------------------------------------------------------

#------------------------------------------------------
# Exercício 5
print("\n\n============= Exercício 5 ==============")
preco_mercadoria = float(input("preço: "))
porcentagem_desconto = float(input("porcentagem de desconto: ")) / 100
valor_desconto = preco_mercadoria * porcentagem_desconto

print(f'desconto: R${valor_desconto}\npreço a pagar: R${preco_mercadoria - valor_desconto}')
#------------------------------------------------------

#------------------------------------------------------
# Exercício 6
print("\n\n============= Exercício 6 ==============")
distancia = int(input("distância a percorrer: "))
velocidade_media = float(input("velocidade média: "))

print(f'tempo de viagem: {distancia / velocidade_media}h')
#------------------------------------------------------

#------------------------------------------------------
# Exercício 7
print("\n\n============= Exercício 7 ==============")
temperatura_celsius = float(input("Temperatura em Celsius: "))
temperatura_fahrenheit = 9 * temperatura_celsius / 5 + 32

print(f'Temperatura em Fahrenheit: {temperatura_fahrenheit}ºF')
#------------------------------------------------------

#------------------------------------------------------
# Exercício 8
print("\n\n============= Exercício 8 ==============")
temperatura_fahrenheit = float(input("Temperatura em Fahrenheit: "))
temperatura_celsius = (temperatura_fahrenheit - 32) / 9

print(f'Temperatura em Celsius: {temperatura_celsius:.0f}ºC')
#------------------------------------------------------

#------------------------------------------------------
# Exercício 9
print("\n\n============= Exercício 9 ==============")
qtde_km = int(input("Kilômetros percorridos: "))
dias = int(input("Dias: "))
preco = 60 * dias + qtde_km * 0.15

print(f'Preço a pagar: R${preco}')
#------------------------------------------------------

#------------------------------------------------------
# Exercício 10
print("\n\n============= Exercício 10 ==============")
qtde_cigarros = int(input("Quantidade de cigarros: "))
anos_fumados = int(input("Anos fumados: "))
total_cigarros_fumados = anos_fumados * 365 * qtde_cigarros
dias_perdidos = total_cigarros_fumados / 144

print(f'Dias perdidos: {dias_perdidos:.0f} dias')
#------------------------------------------------------

#------------------------------------------------------
# Exercício 11
print("\n\n============= Exercício 11 ==============")
tamanho = len(str(2 ** 1000000))
print(f'Tamanho: {tamanho} caracteres')
#------------------------------------------------------
