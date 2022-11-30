

# brojevi.sort()
# brojevi.reverse

# print(brojevi)

# brojevi = [9,1,3,2,5,8,7]

# while True:
#     for i in range(1,len(brojevi)):
#         if brojevi[i] < brojevi[i-1]:
#             privremena = brojevi[i]  #1
#             brojevi[i] = brojevi[i-1] #9
#             brojevi[i-1] = privremena #1
#             izvrsena_zamena = True
#     if izvrsena_zamena == False:
#         break        

# print(brojevi)

# proizvodi = ["Telefon", "TV" ,"Laptop"]
# cene      = [100,       200,    300]

# proizvodi[0] cene[0]
# proizvodi[1] cene[1]
# proizvodi[2] cene[2]

# for i in range(len(proizvodi)):
#     print(proizvodi[i], cene[i])

# automobili = ["Audi", "BMW", "Yugo", "Citroen","Peugeot"]

# for i in range(len(automobili)):
#     print(automobili[i])
#     if i == 3:
#         print(automobili[i])

# proizvodi = [
#                 ["iphone 11", "samsung s22", "xiaomi x3"],
#                 ["acer", "macbook", "dell"],
#                 ["ipad", "samsung galaxy tab","xiaomi tablet"]
#             ]

# telefoni = ["iphone 11", "samsung s22", "xiaomi x3"]
# laptopovi = ["acer", "macbook", "dell"]
# tableti = ["ipad", "samsung galaxy tab","xiaomi tablet"]

# print(proizvodi[0][0])
# print(proizvodi[0][1])

# for i in range(len(proizvodi)):
#     print(proizvodi[i])
#     for j in range(len(proizvodi[i])):
#         print(proizvodi[i][j])


# hrana = [
#          ["cokolada","bombone","palacinke"]
#          ["sarma","musaka","kiseli kupus"]
#          ["pecena paprika","ajvar","sopska"]
# ]
# for kategorija in hrana:
#     for jelo in kategorija:
#         print("naziv:", jelo)




biblioteka = []

print("Odaberi komandu: 1-unos, 2-prikaz, 3-brisanje, > 3 izlaz")
komanda = int(input("Unesite komandu: "))

if komanda == 1:
    naslov = input("Unesite naslov: ")
    autor = input("Unesite autora: ")
    isbn = int(input("Unesite isbn: "))
    biblioteka.append([naslov,autor,isbn])
    print("Dodata knjiga")
if komanda == 2:
    for knjiga in biblioteka:
        for detalj in knjiga:
            print(detalj)
if komanda == 3:
    kljucna_rec = input("Unesite naziv knjige koju zelite da obrisem. ")  
    for knjiga in biblioteka:
        for detalj in knjiga:
            if detalj == kljucna_rec:
                biblioteka.remove(knjiga)
                print("Knjiga je obrisana")              



biblioteka = [

]

while True:
    print("Odaberi komandu: 1-unos, 2-prikaz, 3-brisanje, > 3 izlaz")
    komanda = int(input("Unesite komandu: "))

    if komanda == 1:
        # unos knjige, preuzmi podatke
        naslov = input("Unesite naslov: ")
        autor = input("Unesite autora: ")
        isbn = int(input("Unesite isbn: "))
        biblioteka.append([naslov, autor, isbn])
        print("Dodata knjiga")
    if komanda == 2:
        for knjiga in biblioteka:
            for detalj in knjiga:
                print(detalj)
    if komanda == 3:
        #ovde vrsim brisanje
        kljucna_rec = input("Unesite naziv knjige koju zelite da obrisem. ")
        for knjiga in biblioteka:
            #proveravam detalje KNJIGE
            for detalj in knjiga:
                if detalj == kljucna_rec:
                    biblioteka.remove(knjiga)
                    print("Knjiga je obrisana")
    




