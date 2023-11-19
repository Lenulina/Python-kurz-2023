class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return "Potvrzuji zapůjčení vozidla"
        else:
            return "Vozidlo není k dispozici"

    def get_info(self):
        return f"Auto: {self.registracni_znacka}, {self.typ_vozidla}, Dostupné: {self.dostupne}"

def pujceni_auta(auto1, auto2):
    vybrana_znacka = input("Zadej značku vozidla (Peugeot nebo Škoda): ")
    
    if vybrana_znacka.lower() == "peugeot":
        auto = auto1
    elif vybrana_znacka.lower() == "škoda":
        auto = auto2
    else:
        print("Neplatná volba značky.")
        exit()

    print(auto.get_info())
    
    vysledek_pujceni = auto.pujc_auto()
    print(vysledek_pujceni)

    # Znovu získání informací o vozidle a pokus o půjčení znovu
    print(auto.get_info())
    vysledek_opakovaneho_pujceni = auto.pujc_auto()
    print(vysledek_opakovaneho_pujceni)

# Vytvoření objektů reprezentujících automobily
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

# Zavolání funkce pro půjčení auta
pujceni_auta(auto1, auto2)

### jedna z monznych uprav na pujceni auta od radku 18

def pujceni_auta(auto):
    #vybrana_znacka = input("Zadej značku vozidla (Peugeot nebo Škoda): ")
    ##auto jiz vybrane takze ve funkci jen resime zda je auto k dispozici  jeho pujceni
    # if vybrana_znacka.lower() == "peugeot":
        # auto = auto1
        # #ulozeni pujceni auta
    # elif vybrana_znacka.lower() == "škoda":
        # auto = auto2
    # else:
        # print("Neplatná volba značky.")
        # exit()
    if auto.dostupne:
        print(auto.get_info()) 
        potvrzeni = auto.pujc_auto()
        print(potvrzeni)
    else:
        print("Automobil není k dispozici.")



    # print(auto.get_info())
    
    # vysledek_pujceni = auto.pujc_auto()
    # print(vysledek_pujceni)

    # # Znovu získání informací o vozidle a pokus o půjčení znovu
    # print(auto.get_info())
    # vysledek_opakovaneho_pujceni = auto.pujc_auto()
    # print(vysledek_opakovaneho_pujceni)

# Vytvoření objektů reprezentujících automobily
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

# Zavolání funkce pro půjčení auta
##pujceni_auta(auto1, auto2)
## rozhodnuti ktere auto se pujci dat mimo funkci
volba = input("Zadej značku vozidla (Peugeot nebo Škoda): ")
 
if volba.lower() == "peugeot":
     #auto = auto1
    pujceni_auta(auto1) 
elif volba.lower() == "škoda":
    #auto = auto2
    pujceni_auta(auto2) 
else:
    print("Neplatná volba značky.")
    exit()
