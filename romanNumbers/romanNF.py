'''
Estructuras de datos
    units: digitos necesarios para las unidades, se incluye 'X' para el 9
    tens: digitos necesarios para las decenas, se incluye 'C' para el 90
    hundreds: digitos necesarios para las centenas, se incluye 'X' para el 900
    thousands: digitos necesarios para los millares
'''
units = {1: 'I', 5: 'V', 'next': 'X'} 
tens = {1: 'X', 5: 'L', 'next': 'C'}
hundreds = {1: 'C', 5: 'D', 'next': 'M'}
thousands = {1: 'M', 'gt3': units, 'next': ''}

'''
Diccionario con los dígitos por rango.
   10^0 -> Unidades -> se usa el 1, el 5 y el 10
   10^1 -> Unidades -> se usa el 10, el 50 y el 100
   10^2 -> Unidades -> se usa el 100, el 500 y el 1000
   10^3 -> Unidades -> se usa el 1000
'''
romanDigits = {
    0: units,
    1: tens,
    2: hundreds,
    3: thousands,
}

'''
Diccionario inverso para pasar de romano a arábigo
'''
romanSymbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}

'''
Reglas de codificación romana
    - Hasta el 4 (0,1,2,3): Repetimos unidades del rango elegido
    - El 4 (4): IV, XL, CD
    - Hasta el 9 (5,6,7,8): El cinco y repetimos la unidad hasta 3 veces
    - El 9 (9): IX, XC, CM
    - Si el número es mayor de 3999, se codifica como unidades del grupo millar siguiente
'''

def untilFour(val, symbols):
    res = ''
    for i in range(0, val):
        res += symbols[1]
    return res

def isFour(val, symbols, rng):
    if rng < 3:
        res = (symbols[1]+symbols[5])
    else: 
        res = thousands['gt3'][1] + thousands['gt3'][5]
        res = '({})'.format(res)    
    return res

def untilNine(val, symbols, rng):
    if rng < 3:
        res = symbols[5]
        res += untilFour(val-5, symbols)
    else:
        res = romanDigits[0][5]
        res += untilFour(val-5, thousands['gt3'])
        res = '({})'.format(res)    
    return res

def isNine(val, symbols, rng):
    if rng < 3:
        res = symbols[1]+symbols['next']
    else:
        res = thousands['gt3'][1]+symbols['next']
        res = '({})'.format(res)    
    return res

def setParameters(val, rng):
    try:
        val = int(val)
    except ValueError:
        raise ValueError('Valor ({}) ha de ser entero'.format(val))

    if val <0 or val > 9:
        raise ValueError('Valor ({}) ha de estar entre cero y nueve (0-9)'.format(val))
    
    try:
        rng = int(rng)
    except ValueError:
        raise ValueError('Rango ({}) ha de ser entero'.format(rng))
    
    if rng <0 or rng > 3:
        raise ValueError('Rango ({}) ha de estar entre cero y tres (0-3)'.format(rng))

    return val, rng
    
def tradFigure(valor, rango):
    '''
    traduce un dígito arábigo en dígito/s romano/s
    '''
    valor, rango = setParameters(valor, rango)

    symbols = romanDigits[rango]

    res = ''
    if valor < 4:
        res += untilFour(valor, symbols)
    elif valor == 4:
        res += isFour(valor, symbols, rango)
    elif valor < 9:
        res += untilNine(valor, symbols, rango)
    else:
        res += isNine(valor, symbols, rango)
    return res

def extractFigures(valor):
    '''
    Separa un número entero en una lista de sus cifras ordenadas por exponente (inverso)
        Ej. extractFigures(1970) -> [0, 7, 9, 1]

                                     |  |  |  +-> 1 · 10 ^ 3 
                                     |  |  +----> 9 · 10 ^ 2
                                     |  +-------> 7 · 10 ^ 1
                                     +----------> 0 · 10 ^ 0
    '''
    cad = str(valor)

    cifras = []
    for u in range(1,len(cad)+1):
        valSep = valor % 10 ** u
        cifras.append(int(valSep/10**(u-1)))
        valor -= valSep
    return cifras

def rompeMiles(valor):
    '''
    Rompe un número en grupos de miles. Tiene en cuenta que si en el grupo siguiente las unidades de mil son menores de 4 se incluyen en el grupo actual.
    Ej.
        1970 -> [1970] 
        8970 -> [8, 970]
    '''
    miles = []
    while valor > 0:
        candidate = valor % 10000
        if candidate > 3999:
            candidate = candidate % 1000
        miles.append(candidate)
        valor -= candidate
        valor = valor // 1000

    return miles

def toRoman(valor):
    '''
        1. Rompera valor en miles teniendo en cuenta la limitación hasta 3999
        2. Codificará en romano cada grupo de mil
        3. Rodeará por paréntesis el número romano para multiplicarlo por mil
            Ej. IV = 4
                (IV) = 4000
                ((IV)) = 4000000
            Ej. III = 3
                MMM = 3000
                (MMM) = 3000000

    '''
    try: 
        valor = int(valor)
    except ValueError:
        raise ValueError('Valor ({}) ha de ser entero'.format(valor))

    sgnValor = ''
    if valor < 0:
        valor = valor * -1
        sgnValor = '-'

    g1000 = rompeMiles(valor)
    res = ''
    for i1000 in range(len(g1000)-1, -1, -1):
        cifras = extractFigures(g1000[i1000])
        res += '(' * i1000
        for ix in range(len(cifras)-1, -1, -1):
            res += tradFigure(cifras[ix], ix)
        res += ')' * i1000
    
    return sgnValor + res

def digitRoman(symbol):
    try:
        return romanSymbols[symbol]
    except KeyError:
        raise ValueError('{} no es un dígito romano'.format(symbol))

def procesaParentesis(symbol)
    if symbol == ')'
        return +1
    elif symbol == '(':
        return -1
    return 0

def toArabic(cad):
    '''
    Lee la cifra de derecha a izquierda sumando o restando valores según proceda
    Realiza las principales validaciones
    '''
    cad = cad.strip()
    if len(cad) == 0:
        return 0

    sgnValor = 1
    if cad[0] == '-': #Procesa negativos. Elimina signo inicial y guarda para después
        sgnValor = -1
        cad = cad[1:]

    posDigit = len(cad)-1 #Empieza por el final. De derecha a izquierda
    valor = 0             #valor del número romano
    antVal = 0            #cifra anterior
    factor = 1            #contador de parentesis en forma de 1000
    maxFactor = 1         #control de cierre de paréntesis
    swResta = False       #La anterior cifra restaba (no se admite más de una resta)
    numReps = 0           #contador de repeticiones (nunca más de tres)

    while posDigit >=0:
        # caD = ' ' * (posDigit) + 'v'         # para debug
        symbol = cad[posDigit]

        esParentesis = procesaParentesis(symbol)

        if esParentesis:
            factor *= (1000 ** esParentesis) # multiplica por 1000 si esParentesis = 1, divide por 1000 si esParentesis = -1
            posDigit -= 1                    # Prepara procesamiento de siguiente dígito
            numReps = 0
            swResta = False
            antVal = 0
            continue                         # Vuelve al while

        # Validar orden de parentesis
        maxFactor = max(factor, maxFactor)
        if factor < maxFactor:
            raise ValueError('{} formato incorrecto. Paréntesis incorrectos\n'.format(cad)+' '*(posDigit+12)+'^')

        # Obtiene valor del digito romano. Si no es correcto digitRoman lanza excepcion
        actVal = digitRoman(symbol)
        es5 = str(actVal)[0] == '5' #Comprueba si es V, L o D
        
        if actVal > antVal:         #Se suman valores
            signo = 1
            numReps = 0
            swResta = False
        elif actVal == antVal:      #Se suman valores pero se comprueba número de repeticiones 3 para I, X, C, M. 1 para V, L, D
            swResta = False
            signo = 1
            numReps += 1
            if es5:
                raise ValueError('{} formato incorrecto. Repeticiones prohibidas\n'.format(cad)+' '*(posDigit+12)+'^')
            if numReps > 2:
                raise ValueError('{} formato incorrecto. Más de 3 repeticiones\n'.format(cad)+' '*(posDigit+12)+'^')
        elif swResta:              #Se restan valores. Pero se comprueba que no haya restas encadenadas. Por ejemplo IXC = 89
            raise ValueError('{} formato incorrecto. Solo una resta\n'.format(cad)+' '*(posDigit+12)+'^')
        elif es5:                  #Se restan valores. Pero se comprueba que no haya restas con V, L o D
            raise ValueError('{} formato incorrecto. No se pueden restar multiplos de 5\n'.format(cad)+' '*(posDigit+12)+'^')
        elif antVal != actVal * 10 and antVal != actVal * 5: #Se restan valores pero se comprueba que sean de un orden menor: Por ejemplo IC = 99
            raise ValueError('{} formato incorrecto. Restas sólo un orden menor\n'.format(cad)+' '*(posDigit+12)+'^')
        elif (valor/factor) // actVal > 10: #Se restan valores. Pero se comprueba que se pueda restar: Por ejemplo CMM = 1900
            raise ValueError('{} formato incorrecto. Valor incompatible con resta\n'.format(cad)+' '*(posDigit+12)+'^')
        else: #Se restan valores... por fin
            signo = -1
            swResta = True
            numReps = 0

        valor += actVal * factor * signo #Se ejecuta la operación

        antVal = actVal #Se recordarán valores para el siguiente dígito
        posDigit -= 1

    if factor != 1: #Se comprueba que los paréntesis se hayan cerrado de forma adecuada
        raise ValueError('{} formato incorrecto. Paréntesis incorrectos\n'.format(cad)+' '*11+'^')
    
    return valor*sgnValor #Se recuerda si el número era negativo

