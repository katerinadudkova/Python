sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
total=0
for key, value in sales.items():
  print("Knihy " + key + " jsme prodali " + str(value) + " kusů.")
  print(f"Knihy {key} jsme prodali {value} kusů.")
  total=total+value
print("celkem jsme prodali "+str(total)+"kusů.")