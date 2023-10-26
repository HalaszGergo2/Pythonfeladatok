import math


def elsofeladat():
    szam = 0
    while szam < 148:
        if szam % 2 == 0:
            szam += 2
            print(szam, end=", ")
    print("150")


def masodikfeladat():
    osszszam = 0
    bekeres = 0
    while bekeres < 10:
        szam = int(input("Kérem adj meg egy számot: "))
        if szam % 3 == 0:
            osszszam += 1
        bekeres += 1
    print("A 3-al osztható számok összege: ", osszszam)


def harmadikfeladat():
    szam = int(input("Kérlek adj meg egy számot: "))
    while not szam % 10 == 0:
        szam = int(input("Kérlek adj meg egy számot"))
    if szam % 10 == 0:
        print("A", szam, "szám 10-el osztható")


def negyedikfeladat():
    szam = int(input("Kérlek adj meg egy számot: "))
    while not szam > 9:
        szam = int(input("Kérlek adj meg egy számot: "))
    if (szam % 2 == 0) and (szam >= 10) and (szam < 100):
        print("A szám páros és kétjegyű!")


def otodikfeladat():
    szam = int(input("Kérlek adj meg egy számot: "))
    while szam < 1 or szam % 2 == 0:
        szam = int(input("Kérlek adj meg egy számot: "))
    if(szam % 2 == 1) or (szam < 0):
        print("A szám páratlan és pozitív.")


def hatodikfeladat():
    szam = int(input("Kérlek adj meg egy számot: "))
    while not((szam % 3 == 0) or (math.sqrt(szam) == int(math.sqrt(szam)))):
        szam = int(input("Kérlek adj meg egy számot: "))
    print("A szám osztható 3-al vagy négyzetszám")


def hetedikfeladat():
    a = float(input("Kérlek adj meg egy számot: "))
    b = float(input("Kérlek adj meg egy számot: "))
    c = float(input("Kérlek adj meg egy számot: "))
    while not ((a + b > c) and (a + c > b) and (b + c > a)):
        print("Ez egy nem szerkeszthető háromszög: ")
        a = float(input("Kérlek adj meg egy számot: "))
        b = float(input("Kérlek adj meg egy számot: "))
        c = float(input("Kérlek adj meg egy számot: "))
    print("Ez egy szerkeszthető háromszög.")


def nyolcadikfeladat():
    szoveg = input("Kérlek adj meg egy szöveget: ")
    while not len(szoveg) >= 3:
        szoveg = input("Kérlek adj meg egy szöveget ami minimum 3 karakterből áll: ")
    print(szoveg.upper())


def kilences():
    szoveg = input("Kérlek adj meg egy szöveget: ")
    while not((len(szoveg) >= 4) and (szoveg.islower())):
        szoveg = input("Kérlek adj meg egy szöveget ami minimum 4 karakterből áll és csupa kisbetűs: ")
    print(szoveg)
