# Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu ocjenu od 1 do 5.
# Prebrojati u rječnik koliko ima kojih ocjena.
# Izračunati postotak prolaznosti. (sve ocjene veće od 1)
import random

# Lista učenika kopirana iz zadatka
imena = ['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko',
         'Dario', 'Mihael', 'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela',
         'Leon', 'Ivan', 'Ante', 'Ivan', 'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin',
         'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan', 'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni',
         'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel', 'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka',
         'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario', 'Antonio', 'Stipe', 'Filip', 'Ivan',
         'Ivan', 'Luka', 'Ante', 'Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina', 'Josip',
         'Lucija']

# Dodjela nasumicnih ocijena svakom uceniku
# (prvo napravljen je filtar duplih imena, nije mi bilo jasno trazi
# li se pa sam ipak stavio da izbaci duple jer je to teže :)
imena2 = []
for i in imena:
    if i not in imena2:
        imena2.append(i)
rjecnik = {imena2[i]: random.randint(1, 5) for i in range(0, len(imena2))}

# Izračunavanje postotka prolaznosti
broj_prolaznih = 0
broj_neprolaznih = 0
ocjene = []
for i in rjecnik.values():
    ocjene.append(i)
for i in ocjene:
    if i > 1:
        broj_prolaznih += 1
    else:
        broj_neprolaznih += 1
# Formula za postotak
prolaznost = broj_prolaznih / len(imena2) * 100
# Zaokruzivanje prolaznosti na 2 decimale
prolaznost = round(prolaznost, 2)

# Prebrojavanje kolicine ocijena 1-5
dvice = 0
trice = 0
cetvrtice = 0
petice = 0
for i in ocjene:
    if i == 2:
        dvice += 1
    if i == 3:
        trice += 1
    if i == 4:
        cetvrtice += 1
    if i == 5:
        petice += 1
# Kreiranje rijecnika
rijecnik_s_ocjenama = {1: broj_neprolaznih, 2: dvice, 3: trice, 4: cetvrtice, 5: petice}

# Linija 59 (ispod) je u komentaru jer nije od vitalnog znacenja da se vidi, ali ako se
# izbaci iz komentara moze se vidjeti koju je ocijenu koji ucenik dobio.
# print(rjecnik)
print("Prolaznost ucenika je:", prolaznost, "%")
print("Ovdje vidimo koliko kojih ocijena ima: \n", rijecnik_s_ocjenama)
