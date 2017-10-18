import pickle

def Graphmenu(ER, Countries, Cities):
    answer = 0
    while answer != 7:





        print ("""
           1.Add a relation
           2.Delete a country
           3.Delete a city
           4.Watch a relation by ID
           5.Watch a full relation
           6.Watch sorting result
           7.Exit
           """)
        answer = int(raw_input("Hit the key\n"))

        if answer == 1:
            print("_____________1")
            country = int(raw_input("Write country's ID\n"))
            city = int(raw_input("Write city's ID\n"))
            ER.add(country, city, Countries,Cities)


        if answer == 2:
            country = int(raw_input("Write country's ID\n"))
            ER.cntrdelete(country, Countries, Cities)

        if answer == 3:
            city = int(raw_input("Write city's ID\n"))
            ER.ctdelete(city, Countries, Cities)


        if answer == 4:
            #print(Countries.lastid ,"Cntries last id")
            ID = int(raw_input("Write the ID"))
            ER.idinfo(ID, Countries, Cities, ER)
            exit = raw_input("Press something")

        if answer == 5:
            ER.relinfo(Countries, Cities)
            exit = raw_input("Press something")

        if answer == 6:
            ER.sort(Countries, Cities)
            exit = raw_input("Press something")

        if answer == 7:
            return 1

        if answer !=[0,1,2,3,4,5,6,7]:
            print("invalid Number")
