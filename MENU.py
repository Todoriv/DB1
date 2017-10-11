from Country import Country
from City import City
from Countries import Countries
from Cities import Cities
from Relation import Relation


cntr1 = Country("Ukraine", 48 * 10^6)
cntr2 = Country("Mongolia", 3*10^6)
cntr3 = Country("Romania", 3*10^7)

ct1 = City("Kyiv", 100000)
ct2 = City("Chernihiv", 1000000)
ct3 = City("Zhashkiv", 10)
ct4 = City("Ulan-Bator", 100)
ct5 = City("Gurguleshti", 1000)
ct6 = City("Bucharest", 10000)

Cntrs = Countries()

Cntrs.add(cntr1)
Cntrs.add(cntr2)
Cntrs.add(cntr3)

Cts = Cities()

Cts.add(ct1)
Cts.add(ct2)
Cts.add(ct3)
Cts.add(ct4)
Cts.add(ct5)


ER = Relation()

ER.add(0,0,Cntrs,Cts)
ER.add(0,1,Cntrs,Cts)
ER.add(0,2,Cntrs,Cts)
ER.add(1,3,Cntrs,Cts)
ER.add(2,4,Cntrs,Cts)
ER.add(2,5,Cntrs,Cts)
print('_____________')
ER.relinfo(Cntrs, Cts)