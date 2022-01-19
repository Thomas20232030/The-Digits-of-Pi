########################################################
#                                                      #
#  The Digits of Pi                                    #
#  Thomas Hoppe January 2022                           #
#  https://github.com/Thomas20232030/The-Digits-of-Pi  #
#                                                      #
########################################################

import time
import textwrap
import matplotlib.pyplot as plt


def messen(sta, anz):
    delta = (time.time() - sta)
    m, s = divmod(int(delta), 60)
    h, m = divmod(m, 60)
    print(f"=>{anz:6.0f} Stellen in {h:02}:{m:02}:{s:02} h  / {(delta / anz * 1000):5.2f} Millisekunde pro Stelle")
    return delta


def ausgabe(liste, stellen):
    showlist = "".join(liste)
    wrapper = textwrap.TextWrapper(width=stellen)
    showpi = wrapper.wrap(text=showlist)
    print()
    for element in showpi:
        print(element)
    return


def pistellen(x):
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while x > 0:
        p, q, k = k * k, 2 * k + 1, k + 1
        a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
        d, d1 = a / b, a1 / b1
        while d == d1 and x > 0:
            yield int(d)
            x -= 1
            a, a1 = 10 * (a % b), 10 * (a1 % b1)
            d, d1 = a / b, a1 / b1


def piextern():
    with open("1 million digits of pi.txt", "r") as f:
        pl = f.read()
    plr = list(pl)
    plr.insert(1, ',')
    return plr


def pistellenout(anzahl):
    pilistcalc = [str(n) for n in list(pistellen(anzahl))]
    pilistcalc.insert(1, ',')
    ausgabe(pilistcalc, 150)
    pilistready = piextern()
    if pilistready[0:anzahl + 1] == pilistcalc:
        print(f"\nDie Berechnung und die Liste sind auf {anzahl} Stellen korrekt")
    else:
        print(f"\nDie Berechnung und die Liste sind auf {anzahl} Stellen nicht korrekt")


def eingabeendwert(text, minimum):
    while True:
        try:
            end = int(input(text))
            if end < minimum:
                print("\nBitte einen größeren Wert eingeben...\n")
                continue
            break
        except ValueError:
            print("\nBitte die Zahl im richtigen Format als ganze Zahl eingeben...\n")
    return end


def main():
    while True:

        print("\nBerechnungen zu Pi:")
        print("-------------------")
        print("(1) Die Stellen von Pi")
        print("(2) Laufzeitverhalten des Algorithmus")
        print("(0) Ende\n")
        auswahl = input("Deine Wahl: ")

        if auswahl == "1":
            print("\nPi mit beliebigen Nachkommastellen")
            print("----------------------------------")
            start = time.time()
            anzahl = eingabeendwert("Auf wie viele Stellen soll Pi berechnet werden? ", 1)
            pistellenout(anzahl)
            messen(start, anzahl)

        elif auswahl == "2":
            print("\nLaufzeitverhalten des Algorithmus")
            print("---------------------------------")
            ergebnislistex = []
            ergebnislistey = []
            grenze = eingabeendwert("Erhöhung in 1000er-Schritten. Bis zu welcher Grenze >=2000? ", 2000) + 1
            print()
            for anzahl in range(1000, grenze, 1000):
                start = time.time()
                pilistcalc = [str(n) for n in list(pistellen(anzahl))]
                pilistcalc.insert(1, ',')
                ergebnislistex.append([anzahl])
                ergebnislistey.append([messen(start, anzahl)])
            print()

            plt.title("Laufzeit des Algorithmus von 1000 bis " + str(grenze - 1))
            plt.plot(ergebnislistex, ergebnislistey)
            plt.grid(True)
            plt.axis()
            plt.ylabel("Dauer")
            plt.xlabel("Durchläufe")
            plt.show()

        elif auswahl == "0":

            print("\nDas Programm wird beendet...")
            break

        else:

            print("\nFalsche Eingabe. Bitte wiederholen...")


if __name__ == "__main__":
    main()
