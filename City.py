class City(object):
    # Arguments:
    #   ctname - city name
    #   ctpop - city population
    #   cntrname - country name
    def __init__(self, ctname, ctpop):
        self.name = ctname
        self.pop = ctpop

    def info(self):
        print(self.name + " " + str(self.pop))
