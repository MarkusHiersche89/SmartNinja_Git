#
# zum temporären testen...
#

import random

secret = random.randint(0, 100)
zaehler = 0

while True:
    zaehler += 1
    eingabe = int(input("Deine Zahl: "))
    if eingabe < secret :
        print("Deine Zahl war zu klein")
    elif eingabe == secret :
        print("Perfekt! Du hast " + str(zaehler) + " Versuche gebraucht.")
    else:
        print("Deine Zahl war zu groß")