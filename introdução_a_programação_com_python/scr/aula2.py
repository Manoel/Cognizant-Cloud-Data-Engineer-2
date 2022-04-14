a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('soma: {soma}. \nSub: {subtracao}. \nMulti: {multiplicacao}. '
      '\ndiv: {divisao}. \nresto: {resto}'.format(soma=soma, subtracao=subtracao,
                                                   multiplicacao=multiplicacao, divisao=divisao,
                                                   resto=resto))
print(resultado)
#print('soma: ' + str(soma))
# print(subtracao)
# print(multiplicacao)s
# print(divisao)
# print(int(divisao))
# print(resto)