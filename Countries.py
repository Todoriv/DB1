class Countries(object):
    def __init__(self):
        self.DB = []
        self.lastid = 0

    def add(self, cntr):
        cntr.id = self.lastid
        self.lastid += 1
        self.DB.append(cntr)


    def delete(self, ID):
        if ID < 0 or ID > self.lastid:
            print("There's no such ID")
        else:

            print(str(len(self.DB)))
            for cntr in self.DB:
                if cntr.id == ID:
                    self.DB.remove(cntr)


    def idinfo(self, ID):

        if ID < 0 :
            print("there's no such ID")
        else:
            if ID > self.lastid:

                print("there's no such ID")
            else:
                for cntr in self.DB:
                    if cntr.id == ID:
                        self.DB[ID].info()
