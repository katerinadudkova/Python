class Employee:
  def takeHolidays(self, days):
    if self.holidays >= days:
      self.holidays = self.holidays - days
      return f"Užij si to. Zbývá ti {self.holidays}."
    else:
      return f"Na tolik nemáš nárok. Zbývá ti jenom {self.holidays}."
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}"
  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.holidays = 25

class Manager(Employee):
  def addSub(self, newSub):
    self.sub.append(newSub)
  def getInfo(self):
    text = super().getInfo()
    text = text + self.getSub()
    return text
  def getSub(self):
    text = "\n" + "Podřízení:"
    for item in self.sub:
      text = text + item.name + ", "
      # text += item.name + " "
    return text
  def __init__(self, name, position):
    super().__init__(name, position)
    self.sub = []
    self.holidays = 30
boss = Manager("Marian Přísný", "vedoucí konstrukčního oddělení")
frantisek = Employee("František Novák", "konstruktér")
klara = Employee("Klára Nová", "konstruktérka")
boss.addSub(frantisek)
boss.addSub(klara)
print(boss.getInfo())


