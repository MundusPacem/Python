


class Person(object):

    def __init__(self,name,age,SSN,sex):

        self.name = name
        self.age  = age
        self.SSN  = SSN
        self.sex  = sex

    def getName(self):
        return name

    def getAge(self):
        return age

    def getSSN(self):
        return SSN

    def getSex(self):
        return sex

    def updateName(self,name):

        self.name = name

    def updateage(self,age):

        self.age = age

    def updateSSN(self,SSN):

        self.SSN = SSN

    def updateSex(self,sex):

        self.sex = sex
