import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('arquivo_para_ocultar.txt', atributo_ocultar)

if retorno:
    print("Arquivo ocultado")
else:
    print('Arquivo não foi ocultado')
