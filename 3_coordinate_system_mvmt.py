#Pocetna pozicija kursora u koordinatnom sustavu je na koordinamata 0,0. Trazite
#od korisnika unos jednog od slova: U(p), D(own), L(eft), R(ight), te sa svakim
#unosom pomaknite kursor za jedno mjesto u zeljenom smjeru. Unosom slova
#Q prekinite program i ispisite trenutnu poziciju kursora. Npr. za slijed unosa
#URRRUL, kursor treba zavrsiti na kordinatama 2,2.

#komande U D L R Q
# x = 0, y = 0, T(0,0)
# print ("T(",x,y")")

x = 0
y = 0

while True:
    pomak = input("Write U for up, D for down, R for right, L for left, Q for quit: ")

    if pomak == "U":
        y = y + 1
    elif pomak == "D":
        y = y - 1
    elif pomak == "R":
        x = x + 1
    elif pomak == "L":
        x = x -1
    elif pomak == "Q":
        print("T(" + str(x) + "," + str(y) + ")")
    else:
        print ("You entered wrong value!!")