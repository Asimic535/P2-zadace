import csv
from csv import reader

# Otvaranje datoteke i trazenje imena, prezimena i bodova u listama csv datoteke:
rezultati = []
with open('C:\\Users\\antes\\Desktop\\Ostalo\\rezultati.csv', 'r', encoding="UTF-8") as file:
    csv_reader = csv.reader(file)
    rows = list(csv_reader)

    for row in rows[4:-2]:
        if len(row) >= 3:
            ime = row[0]
            prezime = row[1]
            bodovi = int(row[2])
            rezultati.append((ime, prezime, bodovi))

# Sortiranje po prezimenima (chatGPT kod):
rezultati.sort(key=lambda x: x[1])

# Kreiranje rijecnika i unosenje broja pojedinih ocjena:
ocjene = {'Nedovoljan': 0, 'Dovoljan': 0, 'Dobar': 0, 'Vrlodobar': 0, 'Izvrstan': 0}
for ime, prezime, bodovi in rezultati:
    if bodovi >= 0 and bodovi < 50:
        ocjene['Nedovoljan'] += 1
    elif bodovi >= 50 and bodovi < 66:
        ocjene['Dovoljan'] += 1
    elif bodovi >= 66 and bodovi < 81:
        ocjene['Dobar'] += 1
    elif bodovi >= 81 and bodovi < 91:
        ocjene['Vrlodobar'] += 1
    elif bodovi >= 91 and bodovi <= 100:
        ocjene['Izvrstan'] += 1

# Ispisivamo konačni rezultat (koliko kojih ocjena ima):
print("Ocjene:")
for ocjena, broj_ocjena in ocjene.items():
    print(f'{ocjena}: {broj_ocjena}')
