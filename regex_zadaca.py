import re
txt = str(input("Unesite vaš `string`: "))
rezultat = re.findall("^[A|a].*[0-5].*\s.*[S|s]$", txt)
print(rezultat)
