import random, string

# rnd.choice retorna um item aleatório de uma lista


tamanho = int(input("Digite o tamanho da senha: "))

chars = string.ascii_letters + string.digits + '!@#$%^&*()-=_+,./;:[]{}|?'

rnd = random.SystemRandom() # os.urandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))
