letras = 'abcdefghijklmnñopqrstuvwxyz'
letrasM = letras.upper()
numeros = '0123456789'
translateVocales = ''.maketrans('ÁÉÍÓÚÜáéíóúü', 'AEIOUUaeiouu')

def move1(font, char, dist):
    return font[(font.index(char)+dist) % len(font)]

def cifra1(cadena, distancia):
    result = ''
    cadena = cadena.translate(translateVocales)
    for char in cadena:
        if char in letras:
            result += move1(letras, char, distancia)
        elif char in letrasM:
            result += move1(letrasM, char, distancia)
        elif char in numeros:
            result += move1(numeros, char, distancia)
        else:
            result += char
    
    return result

def move2(font, char, dist):
    try:
        i = font.index(char)
        return font[(font.index(char)+dist) % len(font)]
    except ValueError:
        return char

def cifra2(cadena, distancia):
    result = ''
    cadena = cadena.translate(translateVocales)
    for char in cadena:
        char = move2(letras, char, distancia)
        char = move2(letrasM, char, distancia)
        char = move2(numeros, char, distancia)
        result += char
    return result

def moveAllList(char, dist, *fonts):
    for font in fonts:
        try:
            i = font.index(char)
            return font[(font.index(char)+dist) % len(font)]
        except ValueError:
            pass
    return char


def cifra(cadena, distancia):
    result = ''
    cadena = cadena.translate(translateVocales)
    for char in cadena:
        char = moveAllList(char, distancia, letras, letrasM, numeros)
        result += char
    return result