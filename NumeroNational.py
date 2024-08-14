#670113-456-56
#670!13-456-56
#

list_n_n = ["17 07 3èè 00 33 84", "85 07 30 033 28", "910130blabladd"]

import datetime
import re

def remplacer_caracteres_speciaux(texte):
    return re.sub(r'[^a-zA-Z0-9\s]','', texte)


for i in range(len(list_n_n)):
   print(i)
   list_n_n[i] = remplacer_caracteres_speciaux(list_n_n[i])
   list_n_n[i] = list_n_n[i].replace(" ","")
   print(int(list_n_n[i]))

for element in list_n_n:
    print (len(element))
    birthday_date = element[:6]
    AA = int(birthday_date[0:2])
    MM = int(birthday_date[2:4])
    JJ = int(birthday_date[4:6])
    print(AA,MM,JJ)
    if (1<=JJ<=31) and (1<=MM<=12) and not (24>=AA>=40) == True:
        ma_date = datetime.date(AA, MM, JJ)
        print(ma_date)
    else :
        print("La date n'est pas valide !")
    # verifier si la date est une date valide
    # 1 - verifier si JJ entre 1 et 31
    # 2 - verifier si MM entre 1 et 12
    # 3 - verifier si AA entre 40 et 24  1940-2024
    #
    # Si la date n'est pas valide, afficher une erreur/un message
    # 300156 ---> 30 Janvier 1956
    #sinon, afficher la date sous le format : 30 Janvier 1956