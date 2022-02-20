class Hero(): #template
    #class variable
    jumlah = 0
    def __init__(self, inputName, inputHealth ,inputPower, inputArmour): #constructor __init__
        #instance variables
        self.name = inputName
        self.Health = inputHealth
        self.Power = inputPower
        self.Armour = inputArmour
        Hero.jumlah += 1
        print("Create A Hero " + inputName)

hero1 = Hero("James", 100, 25, 5)
print(Hero.jumlah)
hero2 = Hero("Ucup", 110, 20, 3 )
print(Hero.jumlah)
hero3 = Hero("Anto",1000, 55, 10)
print(Hero.jumlah)
