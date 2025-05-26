class Pet :
    
    def __init__(self, name, hunger_lvl=10):
        self.name = name
        self.hunger_lvl = hunger_lvl
    
    def check_hunger_lvl(self):
        if self.hunger_lvl < 5:
            print(f"{self.name} is not hungry.")
        else :
            print(f"{self.name} is hungry ")
    
    def add_hunger(self, a):
        if a < 0 :
            print(f"Please Add a proper value ! ")
        else :
            self.hunger_lvl -= a
            print(f"{self.name} huger lvl is reduced to {self.hunger_lvl}")
    
    def show_hunger_lvl(self):
        print(f"{self.name} hunger lvl is {self.hunger_lvl}")

dog = Pet("Dog", 20)

dog.show_hunger_lvl()
dog.check_hunger_lvl()
dog.add_hunger(3)
dog.show_hunger_lvl()
dog.check_hunger_lvl()
dog.add_hunger(2)
dog.show_hunger_lvl()
dog.check_hunger_lvl()