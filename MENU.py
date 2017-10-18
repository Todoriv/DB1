from Country import Country
from City import City
from Countries import Countries
from Cities import Cities
from Relation import Relation
from GRAPHMENU import Graphmenu
import pickle

with open('Relation.pickle', 'rb') as f:
    ER = pickle.load(f)

with open('Cities.pickle', 'rb') as f:
    Cities = pickle.load(f)

with open('Countries.pickle', 'rb') as f:
    Countries = pickle.load(f)


cntr1 = Country("Ukraine")
cntr2 = Country("Mongolia")
cntr3 = Country("Romania")

ct1 = City("Kyiv", 100000000)
ct2 = City("Chernihiv", 1000000000)
ct3 = City("Zhashkiv", 100000000)
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
Cts.add(ct6)

ER = Relation()

ER.add(0, 0, Cntrs, Cts)
ER.add(0, 1, Cntrs, Cts)
ER.add(0, 2, Cntrs, Cts)
ER.add(1, 3, Cntrs, Cts)
ER.add(2, 4, Cntrs, Cts)
ER.add(2, 5, Cntrs, Cts)

with open('Relation.pickle', 'wb') as f:
    pickle.dump(ER, f)

with open('Cities.pickle', 'wb') as f:
    pickle.dump(Countries, f)

with open('Countries.pickle', 'wb') as f:
    pickle.dump(Cities, f)



Graphmenu(ER, Cntrs, Cts)
