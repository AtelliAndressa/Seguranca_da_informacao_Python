import ctypes

atributo_ocultar = 0x02

#criamos um arquivo no txt com o nome abaixo apenas para exemplo
retorno = ctypes.windll.kernel32.SetFileAttributesW('arquivo_para_ocultar.txt', atributo_ocultar)

if retorno:
    print("Arquivo ocultado")
else:
    print('Arquivo não foi ocultado')
