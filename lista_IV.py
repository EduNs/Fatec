import random
#-------------------------------------------------------
# Exercício 1
print("============= Exercício 1 ==============")
l = []
for x in range(10):
    l.append(random.randint(1,100))
print(l)
menor = maior = l[0]
for i in range(10):
    if l[i] < menor:
        menor = l[i]
    if l[i] > maior:
        maior = l[i]
print(f"maior: {maior} - menor: {menor}")
#-------------------------------------------------------
#-------------------------------------------------------
# Exercício 2
print("============= Exercício 2 ==============")
l,pares,impares = [],[],[]
for x in range(20):
    l.append(random.randint(1,100))
    
for i in range(20):
    if l[i] % 2 == 0: pares.append(l[i])
    else: impares.append(l[i])
print(f"lista: {l}\npares: {pares}\nímpares: {impares}")
#-------------------------------------------------------
#-------------------------------------------------------
# Exercício 3
print("============= Exercício 3 ==============")
v1,v2,v3 = [],[],[]
for x in range(10):
    v1.append(random.randint(1,100))
    v2.append(random.randint(1,100))
x = 0
while x < 20:
    if x < 10:
        if x % 2 == 0: v3.append(v2[x])
        else: v3.append(v1[x])
    else:
        if x % 2 == 0: v3.append(v1[x-10])
        else: v3.append(v2[x-10])
    x += 1
print(f"v1:{v1}\nv2:{v2}\nv3:{v3}")
#-------------------------------------------------------
#-------------------------------------------------------
# Exercício 4
print("============= Exercício 4 ==============")
s = '''
The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''
s = s.replace(',','').replace('.','').replace(':','')
palavras = s.split()
lista = []
for x in range(len(palavras)):
    if palavras[x][0].lower() in "python" or palavras[x][-1].lower() in "python":
        lista.append(palavras[x])
print(f"lista: {lista}")
#-------------------------------------------------------
#-------------------------------------------------------
# Exercício 5
print("============= Exercício 5 ==============")
s = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''
s = s.replace(',','').replace('.','').replace(':','')
splitado = s.split()
c = 0
for x in range(len(splitado)):
    for i in range(len(splitado[x])):
        if splitado[x][i].lower() in "python" and len(splitado[x]) > 4:
            c += 1
            break
print(f"palavras: {c}")
#-------------------------------------------------------
