class Iteration:
    def _init_(self,test):
        self.test = test
    def loop(self):
        for i in test:
            print(i)
test = set("this is MCS software company")

i = Iteration()
i.loop()