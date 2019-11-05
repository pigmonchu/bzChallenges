letras = 'abcdefghijklmnñopqrstuvwxyz'
letrasM = letras.upper()
numeros = '0123456789'
translateVocales = ''.maketrans('ÁÉÍÓÚÜáéíóúü', 'AEIOUUaeiouu')

def move(font, char, dist):
    try:
        i = font.index(char)
        return font[(font.index(char)+dist) % len(font)]
    except ValueError:
        return char

def moveAllList(char, dist, *fonts):
    for font in fonts:
        try:
            i = font.index(char)
            return font[(font.index(char)+dist) % len(font)]
        except ValueError:
            pass
    return char

def cifra1(cadena, distancia):
    result = ''
    cadena = cadena.translate(translateVocales)
    for char in cadena:
        if char in letras:
            result += move(letras, char, distancia)
        elif char in letrasM:
            result += move(letrasM, char, distancia)
        elif char in numeros:
            result += move(numeros, char, distancia)
        else:
            result += char
    
    return result

def cifra2(cadena, distancia):
    result = ''
    cadena = cadena.translate(translateVocales)
    for char in cadena:
        char = move(letras, char, distancia)
        char = move(letrasM, char, distancia)
        char = move(numeros, char, distancia)
        result += char
    return result

def cifra(cadena, distancia):
    result = ''
    cadena = cadena.translate(translateVocales)
    for char in cadena:
        char = moveAllList(char, distancia, letras, letrasM, numeros)
        result += char
    return result