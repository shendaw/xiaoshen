class LaoGou:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def kc(self):
        str = '%s,%s,%s,love kc!'%(self.name, self.age, self.gender)
        print(str)

    def sj(self):
        str = '%s,%s,%s,love sj!'%(self.name, self.age, self.gender)
        print(str)

    def dbj(self):
        str = '%s,%s,%s,love dbj!'%(self.name, self.age, self.gender)
        print(str)
######################################## laogou #########################################
# lg = LaoGou('cpy', 20, 'male')
# print(lg.name)
# lg.kc()
# lg.sj()
# lg.dbj()

