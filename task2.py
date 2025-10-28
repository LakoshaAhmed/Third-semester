#### Task 2. Tomato Productivity

#The productivity of a tomato variety is calculated using a simple formula - [number of kg harvested from all bushes] / [number of bushes]

#Write a function `calculate_productivity` that takes as input a list of numbers, each representing the number of kilograms harvested from each bush.

#The function should return the productivity value of this variety, rounded to two decimal places.

def calculate_productivity ( numbers_of_kg_harvested_from_all_bushes):
    total = sum(numbers_of_kg_harvested_from_all_bushes)
    The_productivity_value= total / len(numbers_of_kg_harvested_from_all_bushes)
    return round (The_productivity_value, 2)
        


user_input = input("Enter kilograms harvested from each bush (separated by spaces):\n ") 

user_input = [float(x) for x in user_input.split()]

productivity = calculate_productivity (user_input)
print("The productivity value of this variety= " ,productivity)