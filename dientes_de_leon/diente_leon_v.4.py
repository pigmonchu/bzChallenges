import turtle

miT = turtle.Turtle()
'''
Ahora vamos a dibujar dos pero uno la mitad de tamaño que el otro.
Lo normal es hacer calculos y ya no podemos hacerlo directamente con bucles, necesitaremos variables.

Una solución son las funciones
Crear una función diente_de_leon(longitud_tallo)

Si os fijáis se fijan todas las distancias y el radio de los pétalos como relaciones del parámetro de entrada.
Es decir, una función permite realizar procedimientos y según sus parámetros de entrada se puede adaptar a lo
que se necesite (como cambio de tamaño en este caso)
'''
#Limpiar pantalla
miT.reset()

#Posición vertical
miT.left(90)

def diente_de_leon(longitud_tallo):
    #Diente de leon, el tallo
    miT.pd()
    miT.forward(longitud_tallo)
    miT.right(90)
    miT.pu()
    miT.fd(0.06*longitud_tallo)
    for repes in range (15): #Hacemos 15 repeticiones con un for
        miT.pd()  #Cada uno de estos bloques es un petalo, hay 15 podemos repetirlos
        miT.left(24)
        miT.fd(0.12*longitud_tallo)
        miT.pd()
        miT.right(90)
        miT.fd(0.25*longitud_tallo)
        miT.right(90)
        miT.circle(6.25*longitud_tallo/100)
        miT.right(90)
        miT.fd(0.25*longitud_tallo)
        miT.right(90)

    miT.backward(0.06*longitud_tallo)
    miT.left(90)
    miT.backward(longitud_tallo)


diente_de_leon(100)
# ponemos la posición relativa del siguiente diente de leon
miT.pu()
miT.right(90)
miT.fd(200)
miT.left(90)

diente_de_leon(50)


#Mantener abierto el lienzo
turtle.mainloop()