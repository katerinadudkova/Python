class Package:
  def getInfo(self):
    print(f"Adresa je {self.address}, hmonost je {self.weightInKilos} kg.")
    print("Adresa je " + self.address + ", hmonost je " + str(self.weightInKilos) + " kg.")
    if self.delivered == True:
      print("Balík již byl doručen")
    else:
      print("Balík ještě nebyl doručen")
  def deliver(self):
    self.delivered = True
  def __init__(self, address, weightInKilos):
    self.address = address
    self.weightInKilos = weightInKilos
    self.delivered = False
balik1 = Package("Plzeň 123", 2.45)
balik2 = Package("Praha 234", 1.45)
balik1.getInfo()
balik2.getInfo()
balik1.deliver()
balik1.getInfo()

class ValuablePackage(Package):
  def __init__(self, address, weightInKilos, value):
    super().__init__(address, weightInKilos)
    self.value = value
