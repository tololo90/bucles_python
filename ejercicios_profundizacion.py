#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "tololo90"
__email__ = "tololo90@gmail.com"
__version__ = "1.1"

# Variable global utilizada para el ejercicio de nota
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# Variable global utilizada para el ejercicio de temperaturas
temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]


def ej1():
    print('Comenzamos a ponernos serios!')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuente cuantos números ingresados hay y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''
    print("ingrese dos numeros que representen "
          "el principio y fin de una secuencia numerica")

    inicio = int(input("ingrese el primer numero de la secuencia\n"))
    fin = int(input("ingrese el segundo numero de la secuencia\n"))

    cantidad_numeros = 0
    sumatoria = 0

    # bucle.....
    for numero in range(inicio, fin + 1):
        cantidad_numeros += 1
        sumatoria += numero

    # Al terminar el bucle calcular el promedio como:
    # promedio = sumatoria / cantidad_numeros
    promedio = sumatoria / cantidad_numeros
    # Imprimir resultado en pantalla
    print("el promedio de los numeros dentro de la"
          f"secuencia es {promedio}")


def ej2():
    print("Mi Calculadora (^_^)")

    '''
    Tome el ejercicio de clase:
    <condicionales_python /  ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
    indefinidamente hasta que como operador se ingrese la palabra "FIN",
    en ese momento debe terminar el programa

    Se debe debe imprimir un cartel de error si el operador ingresado no es
    alguno de lo soportados o no es la palabra "FIN"
    '''
    print('Ejercicios de práctica con números')

    while True:

            operacion = str(input("elija que operacion desea realizar entre "
                                  "dos numeros\n"
                                  "suma (+)\nresta (-)\nmultiplicacion (*)\n"
                                  "division (/)\npotencia "
                                  "(**)\nfinalizar (FIN)\n"))
            if(operacion == "+" or operacion == "-" or operacion == "*" or
               operacion == "/" or operacion == "**"):
                pass
            elif(operacion == "FIN"):
                break
            else:
                print("error")
                continue

            numero_1 = int(input("ingrese un numero \n"))
            numero_2 = int(input("ingrese otro numero \n"))

            suma = numero_1 + numero_2
            resta = numero_1 - numero_2
            multiplicacion = numero_1 * numero_2
            division = (numero_1 / numero_2)
            potencia = numero_1 ** numero_2

            if(operacion == "+"):
                print(f"{numero_1} + {numero_2} = {suma}")
                continue
            if(operacion == "-"):
                print(f"{numero_1} - {numero_2} = {resta}")
                continue
            if(operacion == "*"):
                print(f"{numero_1} * {numero_2} = {multiplicacion}")
                continue
            if(operacion == "/"):
                print(f"{numero_1} / {numero_2} = {division}")
                continue
            if(operacion == "**"):
                print(f"{numero_1} ** {numero_2} = {potencia}")
                continue


def ej3():
    print("Mi organizador académico (#_#)")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_clase / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Las notas del estudinte se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe caluclar el promedio de todas las notas y luego transformar
    la califiación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_clase / ej3>

    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente

    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''

    # Para calcular el promedio primero debe obtener la suma
    # de todas las notas, que irá almacenando en esta variable
    sumatoria = 0           # Ya le hemos inicializado en 0

    cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
    cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

    # Realice aquí el bucle para recorrer todas las notas
    # y cacular la sumatoria

    # Terminado el bucle calcule el promedio como
    # promedio = sumatoria / cantidad_notas

    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado

    # Imprima en pantalla al cantidad de ausentes
    for nota in notas:
        if nota < 0:
            cantidad_ausentes += 1
        if nota > 0:
            cantidad_notas += 1
            sumatoria += nota

    promedio = sumatoria / cantidad_notas

    puntaje = promedio

    if(puntaje >= 90):
        print("la calificacion promedio es A")
    elif(puntaje >= 80):
        print("la calificacion promedio es B")
    elif(puntaje >= 70):
        print("la calificacion promedio es C")
    elif(puntaje >= 60):
        print("la calificacion promedio es D")
    else:
        print("la calificacion promedio es F")
    print(f"cantidad de ausentes {cantidad_ausentes}")


def ej4():
    print("Mi primer pasito en data analytics")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica /ej5>,
    copielo a este ejercicio y modifíquelo para cumplir el
    siguiente requerimiento

    En este ejercicio se lo provee de una lista de temperatuas,
    esa lista de temperatuas corresponde a los valores de temperaturas
    tomados durante una temperorada del año en Buenos Aires.
    Ustede deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo

    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados

    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperatuas

    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted.

    NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
    el máximo y el mínimo utilizando los mismos métodos vistos
    durante la clase (ejemplos_clase)
    '''

    temperatura_max = None      # Aquí debe ir almacenando la temp máxima
    temperatura_min = None      # Aquí debe ir almacenando la temp mínima
    temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las
    temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el
    temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay

    # Colocar el bucle aqui......
    for temperatura in temp_dataloger:
        if(temperatura_max is None) or (temperatura > temperatura_max):
            temperatura_max = temperatura
        if(temperatura_min is None) or (temperatura < temperatura_min):
            temperatura_min = temperatura
        temperatura_sumatoria += temperatura
        temperatura_len += 1

    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp
    funcion_max = max(temp_dataloger)
    funcion_min = min(temp_dataloger)

    if(funcion_max == temperatura_max and funcion_min == temperatura_min):
        print(f"variable temperatura_max ={temperatura_max}\n"
              f"variable funcion_max ={funcion_max}\n"
               "ambas variables son iguales")
    else:
        print(f"variable temperatura_max ={temperatura_max}\n"
              f"variable funcion_max ={funcion_max}\n"
               "las variables no son iguales")

    print(f"suma de todas las temperaturas ={temperatura_sumatoria}\n"
          f"cantidad de temperaturas ={temperatura_len}")
    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas
    temperatura_promedio = temperatura_sumatoria / temperatura_len
    print("temperatura promedio", temperatura_promedio)
    # Corroboren los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp
    funcion_sum = sum(temp_dataloger)
    if(temperatura_sumatoria == funcion_sum):
        print(f"variable temperatura_sumatoria ={temperatura_max}\n"
              f"variable funcion_sum ={funcion_max}\n"
               "las variables son iguales")
    else:
        print("variable temperatura_sumatoria ={temperatura_max}\n"
              f"variable funcion_sum ={funcion_max}\n"
              "las variables no son iguales")

    '''
    Una vez que tengamos nuestros valores correctamente calculados debemos
    determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    la estadística de años anteriores. Basados en el siguiente link realizamos
    las siguientes aproximaciones:

    verano -->      min = 19, max = 28
    otoño -->       min = 11, max = 24
    invierno -->    min = 8, max = 14
    primavera -->   min = 10, max = 24

    Referencia:
    https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
    '''
    verano = (19, 28)
    otoño = (11, 24)
    invierno = (8, 14)
    primavera = (10, 24)

    temperatura_min = int(temperatura_min)
    temperatura_max = int(temperatura_max)
    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo
    if temperatura_min and temperatura_max in verano:
        print("nos encontramos en verano")
    if temperatura_min and temperatura_max in otoño:
        print("nos encontramos en otoño")
    if temperatura_min and temperatura_max in invierno:
        print("nos encontramos en invierno")
    if temperatura_min and temperatura_max in primavera:
        print("nos encontramos en primavera")
    else:
        print("los datos no coinciden con una estacion")


def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica / ej4>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Realize un programa que corra indefinidamente en un bucle,al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú
    1 - Obtenerlapalabramásgrande por orden alfabético (usando el operador ">")
    2 - Obtenerlapalabramásgrandeporcantidad de letras (longitud de la palabra)
    3 - Salir del programa

    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    encasocontrariosisepresionar"1"o"2" debe continuar con la siguiente tarea

    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)

    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar)lodejamosagustodelalumno,intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando ennalista de palabras, dicha
    lista la debe inicializar vaciayagregarcadanuevovalorconelmétodo"append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:

    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    NOTA: No se debe ordenar la lista de palabras, se debe obtener
    el máximo utilizando el mismos métodos vistos durante la clase
    (ejemplos_clase), tal como el ejercicio anterior. Ordenar una
    lista representa un problema mucho más complejo que solo
    buscar el máximo.

    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorrelalistadepalabrasybuscalaayorsegúnelmotivoingresado("1" o "2")

  '''

    while True:
            total = 0
            lista = []
            orden = str(input("elija una opcion\n1 - Obtener la palabra más"
                              " grande por orden alfabético\n2 - Obtener la"
                              " palabra más grande por cantidad de letras\n"
                              "3 - Salir del programa\n"))
            if(orden == "3"):
                print("programa finalizado")
                break
            elif(orden == "1"):
                while total < 4:
                    palabra = str(input("ingrese 4 palabras\n"))

                    lista.append(palabra)

                    total += 1
                for i in range(len(lista)):
                    if lista[i] > palabra:
                        palabra = lista[i]
                print(f"la palabra mas grande es por orden"
                       "alfabetico es {palabra}")
                continue

            elif(orden == "2"):
                palabra_mas_larga = " "
                while total < 4:
                    palabra = str(input("ingrese 4 palabras\n"))

                    lista.append(palabra)

                    total += 1

                for i in lista:
                    if len(i) > len(palabra_mas_larga):
                        palabra_mas_larga = i
                print(f"la palabra con mas caracteres es {palabra_mas_larga}")
                continue
            else:
                print("error")
                continue


if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
