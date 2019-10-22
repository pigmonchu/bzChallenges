from superheroes import *
from superheroes import _FORMATO_FECHA

nombre = InputUntil('Introduce tu nombre, por favor: ', lambda s: s.isalnum())
apellido = InputUntil('Introduce tu primer apellido, por favor: ', lambda s: s.isalnum())
fecha_nacimiento = InputUntil('Introduce tu fecha de nacimiento (DD-MM-YYYY): ', esFecha, 'Formato incorrecto', lambda s: datetime.datetime.strptime(s, _FORMATO_FECHA))

frase = "Soy {} {} {}, mi poder es {} y voy a luchar contra la injusticia con mi {}!!"
print(frase.format(asignaNombre(nombre).upper(), asignaApellido(apellido).upper(), asigna_color(fecha_nacimiento).upper(), asigna_super_poder(fecha_nacimiento).upper(), asigna_arma(fecha_nacimiento).upper()))
