import json

# Opening JSON file
f = open("body.json", mode="r", encoding="utf-8")
 
# returns JSON object as a dictionary
data = json.load(f)

prospech = []
for k, v in data.items():
    vysledek = "fail"
    if v > 59:
        vysledek = "pass"
    prospech.append((k,vysledek))

# Serializing json
json_object = json.dumps(prospech, indent=4, ensure_ascii=False)
 
# Writing to sample.json
with open("sample.json", "w", encoding="utf-8") as outfile:
    outfile.write(json_object)

##komentar M.Jurosz
##ukol ti nevraci slovnik ale pole, coz je vlastne slozitejsi a pro nase ucely na dalsi zpracovani neni pole moc idealni
##nize je nahrada kodu mezi radky 9 - 21 a je tam pozadovany vystup. Kdyz tak vyzkousej a dej vedet zda je to pochopitelne nebo to muzem probrat

# hodnoceni = {}
# for student in f:
    # if f[student] >= 60:
        # hodnoceni[student] = "Pass"
    # else:
        # hodnoceni[student] = "Fail"
# with open('prospech.json', mode='w', encoding='utf-8') as out_file:
    # json.dump(hodnoceni, out_file, indent=4, ensure_ascii=False)
