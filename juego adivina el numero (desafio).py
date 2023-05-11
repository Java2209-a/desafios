import random

intentos_realizados = 0

print('Hola ¿Cómo es tu nombre?')
nombre = input()

número = random.randint(1, 100)
print('Bueno, ' + nombre + ', te gustaria jugar un juego?.')
print("el juego es simple, adivina el numero q estoy pensando entre el 1 y el 100, tienes 8 intentos para adivinar")
print("te animas a jugar?")


while intentos_realizados < 8:
    print('Bueno ' + nombre + ' Intenta adivinar. Dime un numero')
    eleccion = int(input())
    eleccion = int(eleccion)

    intentos_realizados = intentos_realizados + 1

    if eleccion < número:
        intentos_realizados = str(intentos_realizados)
        print('No el numero que estoy pensando es mas alto.')
        print('te quedan ' + intentos_realizados + ' intentos, tu puedes.')

    if eleccion > número:
        intentos_realizados = str(intentos_realizados)
        print('No el numero que estoy pensando es mas bajo.')
        print('te quedan ' +  intentos_realizados + ' intentos, tu puedes.')

    if eleccion == número:
        break

if eleccion == número:
    intentos_realizados = str(intentos_realizados)
    print('¡Buen trabajo, ' + nombre + '! ¡Has adivinado mi número en ' + intentos_realizados + ' intentos!')

if eleccion != número:
    número = str(número)
    print('Pues no. El número que estaba pensando era ' + número + ' perdiste.')

