##### Task 3. Peppers and Greenhouses

#It's spring now, and grandma has already planted pepper seedlings in the greenhouse. However, she's worried about frost. 
# Your task is to write a function `get_greenhouse_advice` that takes as input a temperature value - an integer $t$:

#- If $t < 5$, return "Please close the greenhouse completely - it's cold outside";

#- If $t$ is from $5$ to $10$, return "Please partially cover the greenhouse - it's cool outside";

#- If $t$ is greater than $10$, return "Please open the greenhouse completely - it's warm outside".

def get_greenhouse_advice(Temperature): 
    if Temperature < 5:
        return "Please close the greenhouse completely - it's cold outside"
    elif 5 <= Temperature <= 10:
        return "Please partially cover the greenhouse - it's cool outside"
    elif Temperature > 10:
        return "Please open the greenhouse completely - it's warm outside"

try:
    Temperature = int(input("Enter the current temperature : "))    
    advice = get_greenhouse_advice(Temperature)
    print(advice)
except ValueError:
    print("Please enter a valid integer temperature!")