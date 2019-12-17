#U cijenu zrakoplovne karte je ukljuˇcen jedan komad prtljage po osobi teˇzine do
#15 kg. Za svaki kg preko kompanija napla´cuje 50 kn. Napisati program koji
#simulira kontrolu teˇzine prtljage u zraˇcnoj luci na naˇcin da program uˇcitava
#teˇzinu (kao decimalni broj) te ispisuje neˇsto od slijede´ceg ovisno o tome koji je
#uvjet ispunjen:
#• Ukoliko je uneseno vrijednost manja od 0 ispisati { Nedopuˇsten unos\
#• Ukoliko se unese vrijednost ve´ca od 50 ispisati { Nedopuˇsten unos\
#• Ukoliko prtljaga teˇzi do 15 kg ispisati { Nema nadoplate\
#* Ukoliko prtljaga teˇzi viˇse od 15 kg potrebno je ispisati iznos nadoplate.
#Npr. za prtljagu teˇzine 18.8 kg potrebno je ispisati Nadoplata iznosi 190 kn\

luggage_weight = int(input("Enter luggage weight: "))
charge = 50 * luggage_weight

if luggage_weight <= 0 or luggage_weight > 50:
    print ("Error, not valid input")
elif luggage_weight < 15:
    print ("No additional charges")
elif luggage_weight > 15:
    print ("Additional charge for you luggage is: " + str(charge))


