#### Task 1. Tomato Harvest

#Write a function `calculate_total_days` that takes three values as input:

 #- number of days for seed germination

# - number of days for seedling growth

 #- number of days until fruiting

#Add all three variables. Return the result - the number of days from the start of seed germination to when the tomatoes ripen.
def calculate_total_days(number_days_of_germination, number_of_days_for_seedling_growth, number_of_days_until_fruiting):

    total_days = number_days_of_germination + number_of_days_for_seedling_growth + number_of_days_until_fruiting

    return total_days

X = int(input("Enter number of days for seed germination: "))
Y = int(input("Enter number of days for seedling growth: "))
Z = int(input("Enter number of days until fruiting: "))
total = calculate_total_days(X, Y, Z)
print("the number of days from the start of seed germination to when the tomatoes ripen:", total)


