# Comando FOR
# Numeros primos
# Números primos são aqueles divisíveis apenas por 1 e por eles mesmos.

# a = int(input("Digite um numero: "))
# div = 0

# for x in range(1, a + 1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1

# if div == 2:
#     print('O numero {} é primo'.format(a))
# else:
#     print('O numero {} não é primo'.format(a))

# # Verificando os numeros primos de 0 a 100.
a = int(input("Digite um numero: "))

# for num in range(a):
#     div = 0
#     for x in range(1, num + 1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print('O numero {} é primo'.format(num))
#     else:
#         print('O numero {} não é primo'.format(num))

# Comando WHILE

a = int(input('Primeiro bimestre: '))

while a > 10:
    a = int(input('O valor deve ser menor ou igual a 10! Digite novamente: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('O valor deve ser menor ou igual a 10! Digite novamente: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('O valor deve ser menor ou igual a 10! Digite novamente: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('O valor deve ser menor ou igual a 10! Digite novamente: '))

media = (a + b + c + d) / 4

print('A média do aluno é {}'.format(media))
