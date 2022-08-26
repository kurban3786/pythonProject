# Moduuli2, syöte- ja muutujaesimerkkejä
import math
import random

username = "kalle"
# int
age = 6
age = age+1
# float value
wallet_balance = 15.40
fullname = "kalle kontio"
# merkkijonojen liitäminen
user = username + " (" + fullname + ")"
print("käyttäjä", user, "on "+str(age)+" vuotta")
print(wallet_balance)
price = input(username+" mitä maksaa lippu on ?")
wallet_balance = wallet_balance - float(price)
print(f"last balance {wallet_balance:.2f} euroa")

# ympyrän pinta-alan laskeminen
# kaava: pii (3.14) * r*r
# säde r
r = float(input("anna ympyrän säde: "))
area = math.pi * r * r
print(f"{r}(m) säteisin ympyrän pintaála on {area:.3f} neliömetriä.")

# "satunnaisluvun" tuottaminen

some_random_number = random.randint(1, 9)
print(f"Arvottu numero väliltä 1-9: {some_random_number}")
some_random_number = random.randint(1, 9)
print(f"Arvottu numero väliltä 1-9: {some_random_number}")
some_random_number = random.randint(1, 9)
print(f"Arvottu numero väliltä 1-9: {some_random_number}")
some_random_number = random.randint(1, 9)
print(f"Arvottu numero väliltä 1-9: {some_random_number}")
some_random_number = random.randint(1, 9)
print(f"Arvottu numero väliltä 1-9: {some_random_number}")
some_random_number = random.randint(1, 9)
print(f"Arvottu numero väliltä 1-9: {some_random_number}")
