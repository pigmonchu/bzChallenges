letras = 'abcdefghijklmnñopqrstuvwxyz'
letrasM = letras.upper()
numeros = '0123456789'
translateVocales = ''.maketrans('ÁÉÍÓÚÜáéíóúü', 'AEIOUUaeiouu')

def move(font, char, dist):
    return font[(font.index(char)+dist) % len(font)]

def cifra(cadena, distancia):
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
