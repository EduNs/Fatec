#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Exercícios extras para listas

# D. Dada uma lista de números retorna uma lista sem os elementos repetidos
def remove_iguais(nums):
  nums.sort()
  for k in nums:
      while nums.count(k) > 1: nums.remove(k)
  return nums

# E. Cripto desafio!!
# Dada uma frase, você deve retirar todas as letras repetidas das palavras
# e ordenar as letras que sobraram
# Exemplo: 'ana e mariana gostam de banana' vira 'an e aimnr agmost de abn'
# Dicas: tente transformar cada palavra em um conjunto,
# depois tente ordenar as letras e montar uma string com o resultado.
# Utilize listas auxiliares se facilitar
def cripto(frase):
  palavras = frase.split()
  letras_palavras = []
  for palavra in palavras:
    l = []
    for letra in palavra:
      l.append(letra)
    letras_palavras.append(l)
  ps = []
  s = ""
  for k in letras_palavras:
    p = []
    for y in k:
      if y not in p: p.append(y)
    p.sort()
    ps.append("".join(p))
  for w in ps:
    if w != ps[-1]: s += w + " "
    else: s += w
  return s

# F. Derivada de um polinômio
# Os coeficientes de um polinômio estão numa lista na ordem do seu grau.
# Você deverá devolver uma lista com os coeficientes da derivada.
# Exemplo: [3, 2, 5, 2] retorna [2, 10, 6]
# A derivada de 3 + 2x + 5x^2 + 2x^3 é 2 + 10x + 6x^2
def derivada(coef):
  coeficientes = []
  exp = 1
  for c in coef[1:]:
    n = exp * c
    coeficientes.append(n)
    exp += 1
  return coeficientes

# G. Soma em listas invertidas
# Colocamos os dígitos de dois números em listas ao contrário
# 513 vira [3, 1, 5] e 295 vira [5, 9, 2]
# [3, 1, 5] + [5, 9, 2] = [8, 0, 8]
# Não vale converter a lista em número para somar diretamente
def soma(n1, n2):
  soma = 0
  c = len(n1)-1
  dn1,dn2 = [],[]
  while c >= 0:
    dn1.append(n1[c])
    c -= 1
  c = len(n2)-1
  while c >= 0:
    dn2.append(n2[c])
    c -= 1
  sn1,sn2 = "",""
  for k in dn1: sn1 += str(k)
  for y in dn2: sn2 += str(y)
  soma = str(int(sn1)+int(sn2))
  l = []
  for w in soma:
    l.append(int(w))
  l.reverse()
  return l

# H. Anagrama
# Verifique se duas palavras são anagramas,
# isto é são uma é permutação das letras da outra
# anagrama('aberto', 'rebato') = True
# anagrama('amor', 'ramo') = True
# anagrama('aba', 'baba') = False
def anagrama(s1, s2):
  c = 0
  if len(s1) == len(s2):
    s1,s2 = list(s1),list(s2)
    s1.sort()
    s2.sort()
    for k in s1:
      if k == s2[c]: c += 1
      else: return False
    return True
  else:
    return False

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('remove_iguais')
  test(remove_iguais([2, 2, 1, 3]), [1, 2, 3])
  test(remove_iguais([2, 2, 3, 2, 3]), [2, 3])
  test(remove_iguais([]), [])

  print ()
  print ('cripto')
  test(cripto('ana e mariana gostam de banana'),
       'an e aimnr agmost de abn')
  test(cripto('Batatinha quando nasce esparrama pelo chão'),
       'Bahint adnoqu acens aemprs elop choã')

  print ()
  print ('derivada de polinômio')
  test(derivada([3, 0, 4, 3, 5]), [0, 8, 9, 20])
  test(derivada([4, 16, 1]), [16, 2])

  print ()
  print ('soma em listas invertidas')
  test(soma([5, 2, 3, 4], [9, 8, 7, 8]), [4, 1, 1, 3, 1])
  test(soma([3, 1, 5], [5, 9, 2]), [8, 0, 8])

  print ()
  print ('anagrama')
  test(anagrama('aberto', 'rebato'), True)
  test(anagrama('amor', 'roma'), True)
  test(anagrama('ramo', 'amor'), True)
  test(anagrama('baba', 'aba'), False)
  test(anagrama('casa', 'cassa'), False)

if __name__ == '__main__':
  main()
