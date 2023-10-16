sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10,
  "A": 10
}

print(sklad)

def deleteFomList():
    #print(sklad[kod])
    if sklad[kod] <= cislo:
        print("Je tam toho málo")
        sklad.pop(kod)    
    else:
        print("Bylo toho dost") 
        sklad[kod] = sklad[kod] - cislo


kod = str(input("Zadej kod: "))
cislo = int(input("Zadej cislo: "))


#if sklad.has_key(kod):
if kod in sklad:
    deleteFomList()
else:
    print(kod, "Není na skladě")

print(sklad)