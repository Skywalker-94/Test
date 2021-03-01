from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides=sides
        
    def roll_die(self):
        print(randint(1,self.sides))
        
die6=Die()
die20=Die(20)
for i in range(10):
    die6.roll_die()
    
for i in range(10):
    die20.roll_die()