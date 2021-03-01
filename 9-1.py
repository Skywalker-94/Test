class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
        
    def describe_restaurant(self):
        print(self.restaurant_name+' has '+self.cuisine_type+' cuisine, '+str(self.number_served)+' has eaten in '+self.restaurant_name+'.')

    def open_restaurant(self):
        print(self.restaurant_name+ ' is now open')
        
    def set_number_served(self, number_served):
        self.number_served=number_served
        
    def increment_number_served(self, increment_number):
        self.number_served+=increment_number
        
'''
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors=['apple','lemon','strawberry']
        
    def describe_flavors(self):
        print('Flavors include '+str(self.flavors))
        
restaurant=Restaurant('KFC','hot') 
res1=Restaurant('MC','sweet')
res2=Restaurant('BJ','delicious') 

restaurant.describe_restaurant()
restaurant.increment_number_served(23)
restaurant.describe_restaurant()

restaurant.open_restaurant() 
res1.open_restaurant()
res2.open_restaurant()

icecream=IceCreamStand('icebest','sweet')
icecream.describe_flavors()
'''