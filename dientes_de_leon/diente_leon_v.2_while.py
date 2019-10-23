import turtle

miT = turtle.Turtle()
'''
Refactorizar para encontrar patrones repetidos y meterlos en un bucle
'''
#Limpiar pantalla
miT.reset()

#Posición vertical
miT.left(90)

#Diente de leon
miT.pd()
miT.forward(100)
miT.right(90)
miT.pu()
miT.fd(6)

contador = 0
while contador < 15:
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

    contador +=1 #Se pone esto para que la condición de mantenerse en el bucle cambie en cada ciclo


miT.backward(6)
miT.left(90)
miT.backward(100)


#Mantener abierto el lienzo
turtle.mainloop()