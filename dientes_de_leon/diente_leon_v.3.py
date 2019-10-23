import turtle

miT = turtle.Turtle()
'''
Ahora vamos a dibujar dos y para ello vamos a utilizar bucles anidados
'''
#Limpiar pantalla
miT.reset()

#Posición vertical
miT.left(90)


for numflor in range(2):
    #Diente de leon, el tallo
    miT.pd()
    miT.forward(100)
    miT.right(90)
    miT.pu()
    miT.fd(6)
    for repes in range (15): #Hacemos 15 repeticiones con un for
        miT.pd()  #Cada uno de estos bloques es un petalo, hay 15 podemos repetirlos
        miT.left(24)
        miT.fd(12)
        miT.pd()
        miT.right(90)
        miT.fd(25)
        miT.right(90)
        miT.circle(6.25)
        miT.right(90)
        miT.fd(25)
        miT.right(90)

    miT.backward(6)
    miT.left(90)
    miT.backward(100)

    # ponemos la posición relativa del siguiente diente de leon
    miT.pu()
    miT.right(90)
    miT.fd(200)
    miT.left(90)


#Mantener abierto el lienzo
turtle.mainloop()