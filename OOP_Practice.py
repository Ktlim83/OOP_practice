class User():
    def __init__(self, name, warrior_type):
        self.name = name
        self.warrior_type = warrior_type 
        self.hp = 100
    # print all use attributes
    def status(self):
        print(f"User is {self.name}, he is a {self.warrior_type} and has {self.hp}hp ")
        return self
        
        
tobin = User("tobin","ninja")
raj = User("raj","knight")

print(tobin.name, raj.name, tobin.warrior_type, raj.warrior_type)

tobin.status()