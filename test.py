# 1
import math
import random

print("Hei mitä sun nimi on ?")
user = input()
print(f"terve , {user}")

# 2

r = float(input("anna ympyrän säde: "))
area = math.pi * r * r
print(f"{r}(m) säteisin ympyrän pintaála on {area:.3f} neliömetriä.")

# 3

x = float(input("anna suorakulmion kannan : "))
y = float(input("anna suorakulmion korkeuden : "))
piirin = (x+y)*2
ala = x*y
print(f"suorakulmion piirin on : {piirin}")
print(f"suorakulmion pinta-ala on : {ala}")

# 4

a = float(input("syötä ensimmäinen numero : "))
b = float(input("syötä ensimmäinen numero : "))
c = float(input("syötä ensimmäinen numero : "))
summa = a+b+c
tulo = a*b*c
keskiarvo = summa // 3
print(f"summa on: {summa} , tulos on:{tulo} , keskiarvo on:{keskiarvo}")

# 5

a = float(input("syötä leiviskät : "))
b = float(input("syötä naulat : "))
c = float(input("syötä luodit : "))
total = (a*20*32+b*32+c)*13.3//1000
print(f"Massa nykymittojen mukaan:{total} kg")

# 6
some_random_number = random.randint(0, 9)
some_random_number2 = random.randint(0, 9)
some_random_number3 = random.randint(0, 9)

print(f"Arvottu numero väliltä 0-9: {some_random_number}{some_random_number2}{some_random_number3}")

some_random_number = random.randint(1, 6)
some_random_number2 = random.randint(1, 6)
some_random_number3 = random.randint(1, 6)
some_number4 = random.randint(1, 6)
print(f"Arvottu numero väliltä 1-6: {some_random_number}{some_random_number2}{some_random_number3}{some_number4}")
