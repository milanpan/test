pozicija_automobila = 0
pozicija_cilja = 10

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)


pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)


pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)


for ime in["marko","milos","marija","ana","sofija"]:
    print("Hello",ime)

print("Prva sledeca linija...")

for broj in [1,2,3,4,5]:
    print("Ovo je broj:", broj)


for broj in range(1, 10, 2):
    print("Stampanje broja:", broj)    

for broj in range(100, 0, -1):
    print("Prikaz",broj)

pozicija_automobila = 0
pozicija_cilja = 10 

for kretanje in range(5):
    pozicija_automobila += 2
    print(pozicija_automobila == pozicija_cilja)

for trenutna_pozicija in range(pozicija_cilja +1):
    pozicija_automobila = trenutna_pozicija
    print(pozicija_automobila == pozicija_cilja)  

pocetna_godina = 2010
zavrsna_godina = 2021
for godina in range(pocetna_godina,zavrsna_godina):
    print(godina)

for zvezda in range (100):
    print("*", end="") 

print()

print("1\t2\t3")
print("**************************")  

for brojac in range(1,5):
    print(brojac * 1, end="\t")
    print(brojac * 2, end="\t")
    print(brojac * 3, end="\n")

# brojac = 1
# print(1 * 1, end="\t")
# print(1 * 2, end="\t")
# print(1 * 3, end="\n")

# print(2 * 1, end="\t")
# print(2 * 2, end="\t")
# print(2 * 3, end="\n")

# print(3 * 1, end="\t")
# print(3 * 2, end="\t")
# print(3 * 3, end="\n")



# for x in range(5):
#     for y in range(3):
#         print("Ovo je x:", x, "Ovo je y:", y)


for x in range(10):
    for y in range(10):
        if x == y:
            print("*", end= " ")
        else:
            print("#", end = " ")    
    print()


# ili posle drugog koraka   print("*" if x == y else "# , end=" ")



# for x in range(10):
#     for y in range(10):
#         if x == 0 or x == 9 or y == 0 or y == 9:
#             print("#", end= " ")
#         else:
#             print(" ", end= " ")  



# sekunde = 10

# while sekunde > 0:
#     print(sekunde) 
#     sekunde -= 1             




baterija = 90

while baterija > 0:
    print("Mozes koristiti telefon:", baterija, "%")
    baterija -= random.randint(5,20)

print("Baterija je prazna")  

for broj in range(11):
    if broj == 5:
        break
    print(broj)

for broj in range(11):
    if broj == 2:
        continue
    print(broj)    




