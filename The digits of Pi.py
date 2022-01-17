########################################################
#                                                      #
#  The Digits of Pi                                    #
#  Thomas Hoppe January 2022                            #
#  https://github.com/Thomas20232030/The-Digits-of-Pi  #
#                                                      #
########################################################

import time
import textwrap


def messen(sta, anz):
    delta = (time.time() - sta)
    m, s = divmod(int(delta), 60)
    h, m = divmod(m, 60)
    print(f"\nDauer bei {anz} Stellen von Pi in Stunden, Minuten und Sekunden: {h:02}:{m:02}:{s:02}")
    print(f"Pro einzelner Berechnung sind das {round((delta / anz * 1000), 2)} Millisekunden")
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


def main():
    while True:

        print("\nBerechnungen zu Pi:")
        print("-------------------")
        print("(1) Die Stellen von Pi")
        print("(0) Ende\n")
        auswahl = input("Deine Wahl: ")

        if auswahl == "1":
            print("\nPi mit beliebigen Nachkommastellen")
            print("----------------------------------")
            start = time.time()
            anzahl = 100
            pistellenout(anzahl)
            messen(start,anzahl)

        elif auswahl == "0":

            print("\nDas Programm wird beendet...")
            break

        else:

            print("\nFalsche Eingabe. Bitte wiederholen...")


if __name__ == "__main__":
    main()
