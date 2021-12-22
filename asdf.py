class Man:
    def __init__(self, name):
        self.name=name
        print("inittt")

    def hello(self):
        print("hello" + self.name +"!!!")

    def good(self):
        print("Good"+self.name+"222")


m=Man("Hyr")
m.hello()
m.good()
