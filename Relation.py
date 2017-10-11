
from Countries import Countries
from Cities import Cities

class Relation(object):
    def __init__(self):
        self.cntrDB = []
        self.cntrid = 0
        self.ctDB = []
        self.ctid = 0
        self.lastid = 0

    def add(self, cntrid, ctid, Countries, Cities):
        if cntrid > Countries.lastid or cntrid < 0 :
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
            self.ctDB[ctid].remove()
            self.cntrDB[ctid].remove()
            self.lastid -= 1
            while ctid < self.lastid:
                self.ctDB[ctid] = self.ctDB[ctid+1]
                self.cntrDB[ctid] = self.cntrDB[ctid+1]
                ctid += 1

    def cntrdelete(self, cntrid, Countries, Cities):
        if cntrid > Countries.lastid or cntrid < 0 :
            print("No such country's ID")
        else:
            i = 0
            while i < len(self.cntrDB):
                if self.cntrDB[i] == cntrid:
                    self.cntrDB[i].remove()
                    self.ctDB[i].remove()
                    self.lastid -= 1
                    i += 1
            i = 0
            while cntrid < len(self.cntrDB)-1:
                self.cntrDB[i] = self.cntrDB[i+1]
                self.ctDB[i] = self.ctDB[i+1]
                cntrid += 1

    def idinfo(self, ID):
        Countries.idinfo(self.cntrDB[ID])

    def relinfo(self, Countries, Cities):
        i = 0
        while i < self.lastid:
            print(str(i+1))
            Countries.idinfo(self.cntrDB[i])
            Cities.idinfo(self.ctDB[i])
            i += 1


