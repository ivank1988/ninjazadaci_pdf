#Alfonaca je bilo svega 5 milijuna, dok je Velonaca bilo cak 9 milijuna.
# broj Alfonaca se povecavao 6% godisnje, dok je broj Velonaca u istom periodu rastao tek 2%.
#  u Velonskim ratovima, koji su izbijali redovno svake cetiri godine,stradavalo je pola milijuna Velonaca,
#  no u tim je godinama, neposredno pred rat, i natalitet rastao sa uobicajenih 2% na 5%
#Izracunajte za koliko ce godina broj Alfonaca premasiti broj Velonaca,
# te kolika ce njihova ukupna brojnost biti te godine.

alfonci = 5000000
velonci = 9000000
godina = 0

while True:

    if godina + 1:
    alfonci = alfonci * 1.06
    velonci = velonci * 1.02

    if alfonci > velonci:
        print (str(alfonci))
        break

    if godina == 4:
        velonci = velonci - 500000
        velonci = velonci + 1.5%

#kao fizbuz