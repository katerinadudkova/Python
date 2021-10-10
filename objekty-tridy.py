class Employee:
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}"
    # return self.name + " pracuje na pozici " + self.position
frantisek = Employee()
frantisek.name = "František Novák"
frantisek.position = "konstruktér"
klara = Employee()
klara.name = "Klára Nová"
klara.position = "konstruktérka"
print(frantisek.getInfo())
print(klara.getInfo())
#
# funkce __init__
class Employee:
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}"
    # return self.name + " pracuje na pozici " + self.position
  def __init__(self, name, position):
    self.name = name
    self.position = position
frantisek = Employee("František Novák", "konstruktér")
klara = Employee("Klára Nová", "konstruktérka")
print(frantisek.getInfo())
print(klara.getInfo())
#
# přidání čerpání dovolené
class Employee:
  def takeHolidays(self, days):
    if self.holidays >= days:
      self.holidays = self.holidays - days
      # self.holidays -= days
      return f"Užij si to. Zbývá ti {self.holidays}."
      # return "Užij si to. Zbývá ti " + str(self.holidays) + "."
    else:
      return f"Na tolik nemáš nárok. Zbývá ti jenom {self.holidays}."
      # return "Na tolik nemáš nárok. Zbývá ti jenom " + str(self.holidays) + "."
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}"
  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.holidays = 25
frantisek = Employee("František Novák", "konstruktér")
print(frantisek.takeHolidays(10))
print(frantisek.takeHolidays(15))
print(frantisek.takeHolidays(10))
