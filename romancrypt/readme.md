# Criptografía sencilla

## Enunciado
Una de las técnicas de criptografía más rudimentarias consiste en sustituir cada uno de los caracteres por otro situado n posiciones más a la derecha. Si n = 2, por ejemplo, sustituiremos la `a` por la `c`, la `b` por la `e`, y así sucesivamente. El problema que aparece en las últimas n letras del alfabeto tiene fácil solución: en el ejemplo, la letra `y` se sustituirá por la `a` y la letra `z` por la `b`. La sustitución debe aplicarse a las letras minúsculas y mayúsculas y a los dígitos (el `0` se sustituye por el `2`, el `1` por el `3` y así hasta llegar al `9`, que se sustituye por el `1`).
Diseña un programa que lea un texto y el valor de n y muestre su versión criptografiada y la versión inversa, que dado un texto y la distancia lo descodifique.

Ten en cuenta los acentos y mayúsculas.

## Apuntes a las soluciones propuestas

### Cifra 1

La primera versión realizada es la función `cifra1(cadena, distancia)` con las tres listas de caracteres para hacer la traslacion. Se elige en función del tipo de carácter a traducir con una selección `if - elif - else`

### Cifra 2

La segunda versión intenta evitar la estructura `if else` y la sustituye por una más común `try-except` trasladada a move2. Ahora bien es menos eficiente puesto que para cada caracter se hacen tres try-except mientras que en la selección se hacen uno, dos o tres ifs en función del carácter. Habría que medir tiempos de ejecución para ver cual de los dos métodos es más rápido.

### Cifra definitivo

Al convertir move2 en un move con todas las listas donde realizar la traslación como parámetro de la función se mezclan ambas soluciones y así sólo se llevarán a cabo tantos `try-except` como sean necesarios para encontrar el caracter en la lista adecuada y la legibilidad del código está más clara.