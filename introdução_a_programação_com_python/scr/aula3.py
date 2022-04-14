# Verificando o maior valor.

# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))

# if a > b and a > c:
#     print('O maior valor é {}'.format(a))
# elif b > a and b > c:
#     print('O maior valor é {}'.format(b))
# else:
#     print('O maior valor é {}'.format(c))
# print('Fim')
#---------------------------------------------

# Verificando se um número é par foi digitado.

# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))

# resto_a = a % 2
# resto_b = b % 2

# if resto_a == 0 or resto_b == 0:
# #if resto_a == 0 or not resto_b > 0: --Outra forma de escrever
#     print('Foi digitado um número par')
# else:
#     print('Nenhum número par foi digitado')
# print('Fim')
#---------------------------------------------

# Validando a media de um aluno.

# a = int(input('Primeiro bimestre: '))
# b = int(input('Segundo bimestre: '))
# c = int(input('Terceiro bimestre: '))
# d = int(input('Quarto bimestre: '))

# media = (a + b + c + d) / 4

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('A média do aluno é {}'.format(media))
# else:
#     print('Foi digitado um valor inválido')
# print('Fim')

# Validando a media de um aluno. --Outra forma de escrever

# a = int(input('Primeiro bimestre: '))
# if a > 10:
#     a = int(input('O valor deve ser menor ou igual a 10! Digite novamente: '))
# b = int(input('Segundo bimestre: '))
# if b > 10:
#     b = int(input('O valor deve ser menor ou igual a 10! Digite novamente: '))
# c = int(input('Terceiro bimestre: '))
# if c > 10:
#     c = int(input('O valor deve ser menor ou igual a 10! Digite novamente: '))
# d = int(input('Quarto bimestre: '))
# if d > 10:
#     d = int(input('O valor deve ser menor ou igual a 10! Digite novamente: '))
# media = (a + b + c + d) / 4

# print('A média do aluno é {}'.format(media))

# Validando a media de um aluno. --Outra forma de escrever

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
