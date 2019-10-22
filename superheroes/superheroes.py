import datetime
_FORMATO_FECHA = "%d-%m-%Y"

nombreSuperHeroes = {'A': 'Sobaco', 'B': 'Asesino', 'C': 'Capitan', 'D': 'Pezon', 'E': 'Trueno', 'F': 'Lobo', 'G': 'Conejo', 'H': 'Halcon',
                     'I': 'Sargento', 'J': 'Principe', 'K': 'El Milagro', 'L': 'El Rey', 'M': 'Maestro', 'N': 'Robot', 'O': 'Vigilante',
                     'P': 'Avispa', 'Q': 'Doctor', 'R': 'Orificio', 'S': 'Fantasma', 'T': 'Prepucio', 'U': 'Tiburon', 'V': 'Aguijon', 'W': 'Pepino',
                     'X': 'Agente', 'Y': 'Tornado', 'Z': 'Brujo'}

apellidoSuperHeroe = {'A': 'Elastico', 'B': 'Carmesi', 'C': 'Radiactivo', 'D': 'Volador', 'E': 'Espacial',
                      'F': 'Letal', 'G': 'Flacido', 'H': 'Marciano', 'I': 'Venenoso', 'J': 'Invisilbe',
                      'K': 'Mutante', 'L': 'Vengador', 'M': 'Amoroso', 'N': 'Apestoso', 'O': 'Magico',
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


def InputUntil(ask, validation=None, error_msg = 'Se ha producido un error', transformation = None):
    _input_value = input(ask)
    while validation and not validation(_input_value):
        print(error_msg)
        _input_value = input(ask)

    if transformation:
        return transformation(_input_value)
    return _input_value

def esFecha(cadena):
    try:
        datetimeObject = datetime.datetime.strptime(cadena, _FORMATO_FECHA)
        now = datetime.datetime.now()
        return now >= datetimeObject
    except ValueError:
        return False

def asignaNombre(cadena):
    cadena = cadena.strip().upper()
    if cadena[0] in nombreSuperHeroes:
        return nombreSuperHeroes[cadena[0]]
    return 'no asignado'

def asignaApellido(cadena):
    cadena = cadena.strip().upper()
    if cadena[0] in apellidoSuperHeroe:
        return apellidoSuperHeroe[cadena[0]]
    return 'no asignado'

def asigna_super_poder(nac):
    if isinstance(nac, datetime.datetime) and nac.month:
        return superPoderes[nac.month-1]
    else:
        return 'no asignado'

def asigna_color(nac):
    if isinstance(nac, datetime.datetime) and nac.year:
        return colorTraje[nac.year % 10]
    else:
        return 'no asignado'

def asigna_arma(nac):
    if isinstance(nac, datetime.datetime) and nac.day:
        return armas[nac.day-1]
    else:
        return 'no asignado'
