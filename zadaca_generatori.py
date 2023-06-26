def generiraj_brojeve(n):
    for broj in range(n):
        if broj % 2 == 0:
            yield f"Parni: {broj}"
        else:
            yield f"Neparni: {broj}"

parametar = 10

generator = generiraj_brojeve(parametar)

for broj in generator:
    print(broj)
