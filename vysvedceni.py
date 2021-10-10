schoolReport = {
  "Český jazyk": 1,
  "Anglický jazyk": 1, 
  "Matematika": 1, 
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělešná výchova": 3,
  "Chemie": 4,
}
total = 0
for key, value in schoolReport.items():
  total = total + value
  if value == 1:
    print(key)
print(total/len(schoolReport))

