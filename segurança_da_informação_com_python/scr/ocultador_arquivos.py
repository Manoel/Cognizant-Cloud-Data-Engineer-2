# Ocultador de arquivos
#

import ctypes

pasta = input("Digite o caminho da pasta a ser ocultada ex (C:/pasta): ")

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)

if retorno:
    print("Arquivo ocultado com sucesso!")
else:
    print("Erro ao ocultar arquivo!")