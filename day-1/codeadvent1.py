from collections import Counter

def readInput():
  list1 = []
  list2 = []

  with open("input.txt") as inp:
    for row in inp:
      row = row.split("   ")
      list1.append(int(row[0]))
      list2.append(int(row[1]))

  list1.sort()
  list2.sort()

  return list1, list2


def first(list1, list2):
  distance = 0

  for i in range(len(list1)):
    distance += abs(list1[i] - list2[i])

  return distance


def second(list1, list2):
  similarity = 0

  count = Counter(list2)

  for value in list1:
    similarity += value * count[value]

  return similarity


if __name__ == "__main__":
  list1, list2 = readInput()
  print("First result: ", first(list1, list2))
  print("Second result: ", second(list1, list2))