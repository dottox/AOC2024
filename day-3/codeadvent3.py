def readInput():

  with open("input.txt") as inp:
    memory = inp.read()

  return memory


def mul(x, y):
  return x * y

import re   # Libreria que nos permite hacer regex
def first(memory):
  sumOfMuls = 0
  
  while True:
    match = re.search(r"mul\([0-9]{1,3},[0-9]{1,3}\)", memory) # Buscar la expresión regular en la memoria
    if match is None:
      break
    
    limits = (match.span()[0], match.span()[1]) # Obtener los límites de indices del match
    memory = memory[limits[1]:] # Borrar desde el inicio hasta la expresión, para no encontrar la misma nuevamente.

    sumOfMuls += eval(match.string[limits[0]:limits[1]]) # Evaluar la expresión y sumar al total

  return sumOfMuls  # Retornar el total de multiplicaciones


def second(memory):
  sumOfMuls = 0
  enabled = True

  while True:
    match = re.search(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do(n't)?\(\)", memory) # El otro regex, ahora incluye la parte de do() y don't()
    if match is None:
      break
    
    limits = (match.span()[0], match.span()[1])
    memory = memory[limits[1]:]

    match = match.string[limits[0]:limits[1]]

    # 3 caminos diferentes dependiendo con lo que hagamos match:
    #   - Si es "don't()", deshabilitamos las multiplicaciones
    #   - Si es "do()", habilitamos las multiplicaciones
    #   - Si es una multiplicación, la evaluamos y sumamos al total si están habilitadas
    if match == "don't()":
      enabled = False
    elif match == "do()":
      enabled = True
    else:
      sumOfMuls += eval(match) if enabled else 0
  
  return sumOfMuls

    
if __name__ == "__main__":
  memory = readInput()

  print("First result: ", first(memory))
  print("Second result: ", second(memory))