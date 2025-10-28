#Create a class `Human`.
#Define two static fields for it: `default_name` and `default_age`.
#Create an `__init__()` method that, in addition to `self`, takes two more parameters: `name` and `age`. For these parameters, 
# set default values using the properties `default_name` and `default_age`. In the `__init__()` method, 
# define four properties: Public - `name` and `age`. Private - `money` and `house`.
#Implement a reference method `info()` that will output the fields `name`, `age`, `house` and `money`.
#Implement a private method `make_deal()` that will be responsible for the technical implementation of buying 
# a house: reducing the amount of money in the account and assigning a reference to the just-purchased house. 
# This method takes a house object and its price as arguments.
#Implement an `earn_money()` method that increases the value of the `money` property.
#Implement a `buy_house()` method that will check if the person has enough money to buy and complete the transaction. 
# If there's too little money - you need to output a warning to the console. 
# Method parameters: reference to house and discount size
class Human:
    default_name = "Ahmed Lakosha"
    default_age = 20
    

    
    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None
    
    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Money: rubles{self.__money}")
        print(f"House: {self.__house}")
    
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house
        print(f"Deal completed! {self.name} bought a house for rubles{price}")
    
    def earn_money(self, amount):
        
        self.__money += amount
        print(f"Earned rubles {amount}. Total money: rubles{self.__money}")
    
    def buy_house(self, house, discount=0):
        final_price = house.price * (1 - discount / 100)        
        print(f"\nAttempting to buy house: {house.name}")
        print(f"Original price: rubles{house.price}")
        print(f"Discount: {discount}%")
        print(f"Final price: rubles {final_price}")
        print(f"Available money: rubles {self.__money}")
        
        if self.__money >= final_price:
            self.__make_deal(house, final_price)
        else:
            shortage = final_price - self.__money
            print(f" Warning: Not enough money to buy the house work more poor person")
            print(f"   You need rubles{shortage:.2f} more.")
            return False
        return True
