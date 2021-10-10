uzivatelskeJmeno=input("Zadej své uživatelské jméno: ")
print(uzivatelskeJmeno)
email=input("Zadej svůj email: ")
print(email)
if not"@" in email:
  print("Neplatný email")
if not "." in email:
  print("neplatný email")
if len(email) <5:
  print("neplatny email")
