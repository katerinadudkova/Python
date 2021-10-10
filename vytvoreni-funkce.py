def greetUser(name):
  print(f"Hello {name}!")
  print("Hello "+ name + "!")
greetUser("Jiří")


def sumTwoNumbers(a, b):
  return a + b
result = sumTwoNumbers(10, 5)
print(result)


def getMark(points, bonus=0):
  if points + bonus <= 60:
    mark = 5
  elif points + bonus <= 70:
    mark = 4
  elif points + bonus <= 80:
    mark = 3
  elif points + bonus <= 90:
    mark = 2
  else:
    mark = 1
  return mark
points = input("Zadej počet bodů: ")
points = int(points)
bonus = input("Zadej počet bonusových bodů: ")
bonus = int(bonus)
mark = getMark(points, bonus)
if mark == 5:
  points = input("Zadej počet bodů z opravného testu: ")
  points = int(points)
  mark = getMark(points, bonus)
print("Výsledná známka je " + str(mark))
print(f"Výsledná známka je {mark}")
