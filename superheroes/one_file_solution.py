import datetime
'''
    Datos y variables
'''
_FORMATO_FECHA = "%d-%m-%Y"

caracteresPermitidos = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÀÉÈÍÌÏÓÒÜÚÙ"

nombreSuperHeroes = {'A': 'Sobaco', 'B': 'Asesino', 'C': 'Capitan', 'D': 'Pezon', 'E': 'Trueno', 'F': 'Lobo', 'G': 'Conejo', 'H': 'Halcon',
                     'I': 'Sargento', 'J': 'Principe', 'K': 'El Milagro', 'L': 'El Rey', 'M': 'Maestro', 'N': 'Robot', 'Ñ': 'Robot', 'O': 'Vigilante',
                     'P': 'Avispa', 'Q': 'Doctor', 'R': 'Orificio', 'S': 'Fantasma', 'T': 'Prepucio', 'U': 'Tiburon', 'V': 'Aguijon', 'W': 'Pepino',
                     'X': 'Agente', 'Y': 'Tornado', 'Z': 'Brujo'}

apellidoSuperHeroes = {'A': 'Elastico', 'B': 'Carmesi', 'C': 'Radiactivo', 'D': 'Volador', 'E': 'Espacial',
                      'F': 'Letal', 'G': 'Flacido', 'H': 'Marciano', 'I': 'Venenoso', 'J': 'Invisilbe',
                      'K': 'Mutante', 'L': 'Vengador', 'M': 'Amoroso', 'N': 'Apestoso', 'Ñ': 'Apestoso', 'O': 'Magico',
                      'P': 'Gigante', 'Q': 'Nazi', 'R': 'Bionico', 'S': 'Celestial', 'T': 'Sangriento',
                      'U': 'Rocoso', 'V': 'De Hierro', 'W': 'Psiquico', 'X': 'Maravilla', 'Y': 'Hipster',
                      'Z': 'Invencible'}

colorTraje = ['Escarlata', 'Dorado', 'Amarillo', 'Oscuro', 'Verde', 'Blanco', 'Azul', 'Gris', 'Plateado', 'Rojo']
superPoderes = ['Convertir todo en Algodon', 'Velocidad de la luz', 'Hablar con los animales', 'Super Fuerza', 'Control Mental', 'Invisibilidad', 
                'Control del Fuego', 'Crear Tormentas', 'Convertir el agua en Cerveza', 'Destruir Planetas', 'Saltar 20 Metros', 'Volar']
armas = ['Bastón', 'Espada', 'Hacha', 'Sombrilla', 'Escudo', 'Varita Mágica', 'Rifle', 'Cuchillo', 'Bate de Baseball', 'Cuerda',
         'Arco y Flecha', 'Guantes de Box', 'Sarten', 'Pistola', 'Manopla', 'Chacos Ninja', 'Martillo', 'Motosierra',
         'Cadenas', 'Destornillador', 'Escoba', 'Daga', 'Bumerangs', 'Estrellas Ninja', 'Extintor', 'Tijeras', 'Destapacaños', 
         'Lanza misiles', 'Bastón de Jokey', 'Cepillo de dientes', 'Espada Mágica']

'''
Funciones
'''

def validarPermitidos(cadena):
    for char in cadena:
        if char.upper() not in caracteresPermitidos:
            return False
    return True

def esFechaYEsMenorQueHoy(cadena):
    try:
        datetimeObject = datetime.datetime.strptime(cadena, _FORMATO_FECHA)
        now = datetime.datetime.now()
        return now >= datetimeObject
    except ValueError:
        return False

'''
Proceso principal
'''
nombre = input('Introduce tu nombre, por favor: ')

while not validarPermitidos(nombre):
    print("Tu nombre contiene caracteres no permitidos, introducelo de nuevo, por favor: ")
    nombre = input('Introduce tu nombre, por favor: ')

apellido = input('Introduce tu primer apellido, por favor: ')
while not validarPermitidos(apellido):
    print("Tu apellido contiene caracteres no permitidos, introducelo de nuevo, por favor: ")
    apellido = input('Introduce tu primer apellido, por favor: ')

fechaNac = input('Introduce tu fecha de nacimiento (DD-MM-YYYY): ')
while not esFechaYEsMenorQueHoy(fechaNac):
    print("Fecha incorrecta o superior a hoy")
    fechaNac = input('Introduce tu fecha de nacimiento (DD-MM-YYYY): ')

'''
Asigna nombre superheroe
'''
nombre =  nombre.strip().upper()  #Transformo el nombre en mayúsculas y le quito los espacios delante y detrás si los hubiera (no debería por validaPermitidos)
if nombre[0] in nombreSuperHeroes:
    superH = nombreSuperHeroes.get(nombre[0])
else: 
    superH = 'no asignado'

'''
Asigna apellido superheroe
'''
apellido =  apellido.strip().upper()  #Transformo el nombre en mayúsculas y le quito los espacios delante y detrás si los hubiera (no debería por validaPermitidos)
if apellido[0] in apellidoSuperHeroes:
    superA = apellidoSuperHeroes.get(apellido[0])
else: 
    superA = 'no asignado'

'''
Asigna parametros de fecha
'''
fecha = fechaNac.split('-') # divido la fecha en [dia, mes, año] independientemente de cero a la izquierda o no "8/4/1970" = "08/04/1970"

color =  int(fecha[2][0])   # cojo el primer dígito del año y lo transformo en entero
superColor = colorTraje[color]

poder = int(fecha[1][0])
superPoder = superPoderes[poder]

arma = int(fecha[0][0])
superArma = armas[arma]

'''
Imprime frase
'''


print(f"Soy {superH} {superA} {superColor}, mi poder es {superPoder} y voy a luchar contra la injusticia con mi {superArma}!!")