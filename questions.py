import random
# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?", "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden
# que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el 
# mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

#importo la funcion para poder hacer el exit status
import sys
#if ((user_answer.isdigit()) and (user_answer >= 0 and user_answer <3)):

#Inicializo la variable para ir contando el puntaje
score = 0.0

#inicializo la varable questions_to_ask para convertirla en una tupla de listas
#cambiamos el random.choice por el random.sample para que no se repita ninguna pregunta
questions_to_ask = random.sample(list(zip(questions,answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas. Hago un for en el que se desempaqueten en las siguientes 3 variables la informacion
#que se necesita por medio de la tupla de listas

for question,answer_options,correct_answers in questions_to_ask:
# Se muestra la pregunta y las respuestas posibles
    print (question) 
    for i, options in enumerate(answer_options):
      print(f"{i + 1}. {options}")
# El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
     user_answer = input("Respuesta: ")
     if (not user_answer.isdigit()) or (not (0 <= int(user_answer) - 1 <= 3)):
         print ('Respuesta no valida ')
         sys.exit(1)
     else:
         user_answer = int(user_answer) - 1 
# Aqui uso directamente la variable correct_answers ya que tiene el valor correcto, porque fue desempaquetado previamente en la condicion del for         
         if user_answer == correct_answers:
# Se verifica si la respuesta es correcta 
             print("¡Correcto!")
             score = score + 1.0
             break
         elif (score != 0):
             score = score - 0.5
    else:
# Si el usuario no responde correctamente después de 2 intentos,
# se muestra la respuesta correcta
     print("Incorrecto. La respuesta correcta es:")
     print(answer_options[correct_answers])
# Se imprime un blanco al final de la pregunta
print()

# Se imprime el puntaje del jugador
print (f'El puntaje del jugador es: {score}')

# Modifique el juego para que no muestre preguntas repetidas


