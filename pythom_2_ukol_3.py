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