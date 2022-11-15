#while esim 1 "iteroiva"
"""
hinta = int(input("paljon maksaa?"))
maksettu = 0
while maksettu < hinta:
    maksettu = maksettu + 1
    print("maksetaan 1 euroa")
    print(f"maksettavaa jäljellä {hinta - maksettu}")
print("kahvi maksettu kokonaan")
"""
# ehile esim 2 "ohjelmavalikko"

command = ""
while command != "lopeta":
    command = input("anna komento: ").lower()
    if command == "tulosta":
        print("tulostetaan")
    elif command == "lopeta":
        print("ohjelma sammutetaan")
        #break
    else:
        print("en ymmärtänyt, anna toimiva komento")
print("ohjelma lopetettu")