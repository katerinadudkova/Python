znamky = [
  ['Petr', 2],
  ['Roman', 1],
  ['Jitka', 3],
  ['Zuzana', 5],
  ['Ondřej', 2],
  ['Julie', 2],
  ['Karel', 4],
  ['Anna', 1],
  ['Eva', 1]
]
soucet = 0
for radek in znamky:
  soucet = soucet + radek[-1]
  # soucet += radek[-1]
prumer = soucet / len(znamky)
prumer = round(prumer, 2)
print("Průměr známek je", prumer,".")
print(f"Průměr známek je {prumer}.")

