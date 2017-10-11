class Country(object):
    #Arguments:
    # cname - country name
    # cloc - country location
    def __init__(self, cntrname, cntrpop):
        self.name = cntrname
        self.id = 0

    def info(self):
      print(self.name)