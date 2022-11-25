osoba = ["Sofija",25,"plava", False]
for x in range(len(osoba)):
    print(osoba[x])



for osobina in osoba:
    print(osobina)

voce_i_povrce = ["jabuka", "beli luk", "crni luk","banana","mandarina", "lubenica", "krastavac"]

for stavka in voce_i_povrce:
    print(stavka)

for i in range(len(voce_i_povrce)):
    print(voce_i_povrce[i])

for indeks, vrednost in enumerate(voce_i_povrce):
    print("Indeks:", indeks, "Stavka:", vrednost)     


automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo"]
# Pozicija:0 Auto:Citroen

for pozicija,auto in enumerate(automobili):
    print("Pozicija:", pozicija, "Auto", auto)

#prosirenje ponude
automobili.append("Mercedes")
print(automobili) 
automobili[2] = "Opel Corsa"
print(automobili)
automobili[3] = "Kia Sportage"

del automobili[3]
print(automobili)
automobili.remove("BMW")
print(automobili)
automobili.pop(0)
print(automobili)

broj_opela = 0
for indeks in range(len(automobili)):
    if automobili[indeks]


utomobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo","Peugeot","Audi"]

automobili_akcija = []
for i in range(len(automobili)):
    if i == 1 or i == 2 or i == 3:
        automobili_akcija.append(automobili[i])
print(automobili_akcija)

automobili_akcija = automobili[1:4]
print


# lista
# prazne liste,parni neparni
# for
# %
# if else

a = [3,7,1,9,2,4,5,12]
odd = []
even = []

for 
