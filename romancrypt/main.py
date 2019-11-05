import traslation

def esEntero(x):
    try:
        int(x)
        return True
    except:
        return False


def InputUntil(ask, validation=None, error_msg = 'Se ha producido un error', transformation = None):
    _input_value = input(ask)
    while validation and not validation(_input_value):
        print(error_msg)
        _input_value = input(ask)

    if transformation:
        return transformation(_input_value)
    return _input_value

texto = InputUntil("Texto a traducir: ", lambda x: len(x) > 0)

despl = InputUntil("Valor de desplazamiento: ", esEntero, 'Ha de ser un entero', lambda x: int(x) )

cifrado = traslation.cifra(texto, despl)

print('Texto original: {}'.format(texto))
print('Desplazamiento: {}'.format(despl))
print('Cifrado.......: {}'.format(cifrado))
print('Descifrado....: {}'.format(traslation.cifra(cifrado, -despl)))
