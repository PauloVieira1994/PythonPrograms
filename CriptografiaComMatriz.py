import numpy as np

#Inserindo valores a serem transformados na tabela ASCII
frase = [str(input("Digite a frase desejada:\n"))]
print("\nFrase original : ", str(frase)) 
res = [] 
for i in frase: 
    res.extend(ord(num) for num in i) 
print("\nFrase em ASCII : ", str(res))

print("\n\n----------------------------")


#Verificando se a a quantidade de entrada é par ou impar para adicionar valor vazio
vazio = len(res)
resto = vazio % 2
if resto == 0:
  print("\nQuantidade de variáveis:",vazio)
else:
  res.append(0)
  print("\nQuantidade de variáveis",vazio)

print("\n----------------------------")

#Transformando variáveis em matriz nx2
divisor = len(res)/2
divisor = int(divisor)
n = divisor
splited = []
len_l = len(res)

for i in range(n):
    start = int(i*len_l/n)
    end = int((i+1)*len_l/n)
    splited.append(res[start:end])



matriz = np.array([splited])
print("\nCodigo transformado em matriz:\n",matriz)
print("\n\n----------------------------")


# matriz A codificadora
A = np.array([[3,1],[2,1]])
print("\nMatriz A para Codificar: ")
print(A)
# matriz B inversa de A
B = np.array([[1,-1],[-2,3]])
print("\nMatriz B inversa, para Decodificar: ")
print(B)
print("\n\n----------------------------")
# Multiplicando Matriz A no codigo
print("\nFrase Codificada: ")
cod=matriz.dot(A)
print(cod)

#Multiplicando Matriz B no codigo para decodificar
print("\n\n----------------------------")

print("\nFrase Decodificada: ")
decod = (cod.dot(B))
print(decod)

print("\n\n----------------------------")
if (decod==matriz).all:
  print("\nFrase em ASCII:\n",res)
  print("\nFrase Original:\n",frase)
else:
  print("Erro ao decodificar")
