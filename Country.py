class Country(object):
    def __init__(self, cntrname):
        self.name = cntrname
        self.id = 0

    def info(self):
        print(self.name)
