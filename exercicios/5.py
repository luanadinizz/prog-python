num=[[],[]]
valor=0
tamanho=int(input('digite o tamanho do seu vetor:'))
for c in range (1,tamanho+1):
    valor=int(input('digite um valor:'))
    if valor%2==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('os valores pares digitados foram', num[0])
