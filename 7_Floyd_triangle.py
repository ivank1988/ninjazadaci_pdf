broj_redaka = int(input("Enter the range: "))
brojac = 1

for i in range(1, broj_redaka + 1):
#ako stavimo brojac = 1 ovdje, onda ce svaki red poceti s 1

    for broj_stupaca in range(1, i + 1):
        print(brojac, end=" ")
        #ako ovdje stavimo ("*", end=" "), onda će umjesto brojeva ispisivati *
        brojac = 1 + brojac
    print()
