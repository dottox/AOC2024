def readInput():

  with open("input.txt") as inp:
    reports = inp.read().splitlines()

  return reports


def isSafe(report):
  ascend, badReport = None, False

  # Por cada valor en el reporte
  for i in range(1, len(report)):
    report[i] = int(report[i])  # Convertir a entero
    report[i-1] = int(report[i-1])

    # Determinar si el reporte es ascendente o descendente
    if ascend is None:
      ascend = (True if (report[i] - report[i-1] > 0) else False)

    # Comprobar si los valores adyacentes se diferencian cada 3 y si siempre suben o bajan
    diff = report[i] - report[i-1]
    if abs(diff) not in range(1, 4) or (True if ascend != (diff > 0) else False):
      badReport = True  # Lo marcamos como un reporte malo
      break
  
  return not badReport


def first(reports):
  safeReports = 0

  for report in reports:  # Por cada reporte
    report = report.split(" ")  # Separar los valores

    if isSafe(report):  # Si el reporte es seguro, sumar al conteo
      safeReports += 1

  return safeReports


def second(reports):
  safeReports = 0

  for report in reports:  # Por cada reporte
    report = report.split(" ")  # Separar los valores

    # Si el reporte no es seguro, intentar encontrar un reporte seguro eliminando un elemento
    if not isSafe(report):  
      for i in range(len(report)):  # Por cada valor en el reporte
        cuttedReport = report[:i] + report[i+1:] # Eliminar el valor en la posición i
        if isSafe(cuttedReport): # Comprobar si ahora es seguro
          safeReports += 1
          break
    else: # Si el reporte es seguro desde el inicio, sumar al conteo
      safeReports += 1
    
  return safeReports
      
    
if __name__ == "__main__":
  reports = readInput()

  print("First result: ", first(reports))
  print("Second result: ", second(reports))