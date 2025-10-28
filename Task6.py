class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price
        self.name = f"House ({area} sqm)" 
    def final_price(self, discount=0):
        return self._price * (1 - discount / 100)
class SmallHouse(House):
    def __init__(self, price):
        # Create a SmallHouse with fixed area of 40 sqm
        super().__init__(area=40, price=price)
        self.name = f"SmallHouse ({self._area} sqm)"

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
        print(f"done {self.name} bought a house for rubles{price}")
    
    def earn_money(self, amount):
        self.__money += amount
        print(f"Earned rubles {amount}. Total money: rubles{self.__money}")
    
    def buy_house(self, house, discount=0):
        final_price = house.final_price(discount)
        print(f"\nAttempting to buy house: {house.name}")
        print(f"Original price: rubles{house._price}")
        print(f"Discount: {discount}%")
        print(f"Final price: rubles {final_price}")
        print(f"Available money: rubles {self.__money}")
        
        if self.__money >= final_price:
            self.__make_deal(house, final_price)
            return True
        else:
            shortage = final_price - self.__money
            print(f" Warning: Not enough money. Try to work more ")
            print(f"You need rubles{shortage:f} more.")
            return False


# Create a small house costing 50000 rubles
small_house = SmallHouse(50000)

# Create a human and try to buy it
human = Human()
human.earn_money(60000)
human.buy_house(small_house)
