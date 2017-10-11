class Cities(object):

    def __init__(self):
        self.lastid = 0
        self.DB = []

    def add(self, ct):
        ct.id = self.lastid
        self.lastid += 1
        self.DB.append(ct)

    def delete(self, ID):

        if ID < 0 or ID > self.lastid:
            print("There's no such ID")
        else:
            for ct in self.DB:
                if ct.id == ID:
                    self.DB.remove(ct)
                    i = 0
                    while i < len(self.DB):
                        if self.DB[i].id != i:
                            self.DB[i].id = i
                            self.DB[i-1] = self.DB[i]
                        i += 1


    def idinfo(self, ID):
        if ID < 0 or ID > self.lastid:
            print("There's no such ID")
        else:
            for ct in self.DB:
                if ct.id == ID:
                    self.DB[ID].info()


