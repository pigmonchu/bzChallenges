from .silabeador import *

_INTERSILABA = 'pi'

def pipalabra(word):
    silabas = silabea(word)
    newword = _INTERSILABA+ _INTERSILABA.join(silabas)
    
    return newword

def pilengua(word):
    if ' ' in word:
        newphrase = []
        palabras = word.split()
        for palabra in palabras:
            newword = silabea(palabra)
            if newword and newword[0][0].lower() == 'r':
                newword[0] = newword[0][0] + newword[0]

            newword = _INTERSILABA + _INTERSILABA.join(newword) 
            newphrase.append(newword)
        return ' '.join(newphrase).lower()
    else:
        return pipalabra(word)

def busca(word, cadena):
    try:
        return word.index(cadena)
    except ValueError:
        return -1

def inversa(word):
    original = ''
    contJumps = 1
    p1 = word[2*contJumps+len(original):]
    while len(p1) > 2:
        froc = silabea(p1)
        original += froc[0]
        contJumps += 1
        p1 = word[2*contJumps+len(original):]

    #procesa doble R
    original = original.lower()
    
    if original[0:2] == 'rr':
        original = original[1:]
        
    pos = busca(original, (' rr'))
    while pos != -1:
        original = original[:pos+1]+original[pos+2:]
        pos = busca(original, (' rr'))

    return original
    
