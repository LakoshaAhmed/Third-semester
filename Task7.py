#Create a class `SmallHouse`, inheriting its functionality from the `House` class

#Inside the `SmallHouse` class, override the `__init__()` method so that it creates an object with an area of $40$m$^2$
class house:
    def __init__(self, area, price):
        self._area = area
        self._price = price
    
    def final_price(self, discount):
        return self._price - discount
    
class Small_House():
        def __init__(self, price):
            super().__init__(area=40, price=price)