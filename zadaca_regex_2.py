# Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
# Nakon toga napisati regex za provjeru eduId koji mora biti formata iprezimeX@sum.ba gdje je i prvo slovo
# imena + prezime. X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti
# samo iprezime@sum.ba). Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.

import re
rezultat_email = None
rezultat_regex = None
while not rezultat_email:
    email = input("Unesite e-mail: ")
    regex = r'^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$'
    if re.match(regex, email):
        print("Uneseni e-mail je validan.")
        rezultat_email = True
        while not rezultat_regex:
            eduid = input("Unesite eduId: ")
            regex_eduid = r'^[a-z][a-zA-Z]+[0-9]*@sum\.ba$'
            if re.match(regex_eduid, eduid):
                print("Uneseni eduId je validan.")
                rezultat_regex = True
                print("Uneseni podaci su točni!")
            else:
                print("Uneseni eduId nije validan.")
    else:
        print("Uneseni e-mail nije validan.")
