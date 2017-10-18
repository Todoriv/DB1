

class Relation(object):
    def __init__(self):
        self.cntrDB = []
        self.cntrid = 0
        self.ctDB = []
        self.ctid = 0
        self.lastid = 0
        self.sortedDB = []

    def add(self, cntrid, ctid, Countries, Cities):
        if cntrid > Countries.lastid or cntrid < 0:
            print("No such country's ID")
            return 1
        else:
            if ctid > Cities.lastid or ctid < 0:
                print("No such City's ID")
                return 1
            else:
                if self.ctid != self.cntrid:
                    print("Something wasn't appended, or wasn't deleted")
                else:

                    self.cntrDB.append(cntrid)
                    self.ctDB.append(ctid)
                    self.lastid += 1
                    self.cntrid += 1
                    self.ctid += 1


    def ctdelete(self, ctid, Countries, Cities):
        if ctid > Cities.lastid or ctid < 0:
            print("No such City's ID")
        else:
            #del self.cntrDB[ctid]
            #del self.ctDB[ctid]
            self.cntrDB.pop(ctid)
            self.ctDB.pop(ctid)
            self.lastid -= 1


    def cntrdelete(self, cntrid, Countries, Cities):
        print("Don't do this!")
#        if cntrid > Countries.lastid or cntrid < 0:
#            print("No such country's ID")
#        else:
#            i = 0
#            while i < self.lastid:
#                if self.cntrDB[i] == cntrid:
#                    print(str(i))
#                    print(self.ctDB[i])
#                    self.ctDB.pop(self.ctDB[i])
#                    #self.ctDB.pop(self.ctDB[i])
#                    self.lastid -= 1
#                    self.cntrDB.remove(cntrid)
#                   self.ctDB.remove(self.ctDB[i])
 #               i += 1
  #          self.cntrDB.pop(cntrid)

    def idinfo(self, ID, Countries, Cities, ER):

        Countries.idinfo(ER.cntrDB[ID])
        Cities.idinfo(ER.ctDB[ID])

    def relinfo(self, Countries, Cities):
        i = 0
        while i < self.lastid:
            print(str(i + 1))
            Countries.idinfo(self.cntrDB[i])
            Cities.idinfo(self.ctDB[i])
            i += 1

    def sort(self, Countries, Cities):
        CTID = []
        CNTRID = []
        count = 1
        i = 0

        while i < Cities.lastid:
            if Cities.DB[i].pop >= 1000000:
                CTID.append(i)

            i += 1


        i = 0
        while i < len(CTID):
            CNTRID.append(self.cntrDB[CTID[i]])
            i += 1
        i = 0

        while i < len(CNTRID):
            ans = CNTRID.count(i)


            if ans >= 3:
                Countries.idinfo(i)
            i += 1


