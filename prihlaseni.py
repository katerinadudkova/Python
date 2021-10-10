uzivatelskeJmeno=input("Zadej své uživatelské jméno: ")
print(uzivatelskeJmeno)
heslo=input("Zadej heslo: ")
print(heslo)
if heslo =="simsalabim":
  vek=int(input("Jaký je tvůj věk? "))
  if vek >=18:
    print("Můžeš vstoupit")
  if vek <18:
    print("Vstup nepovolen")
else:
  print("Vstup nepovolen")
exit()

