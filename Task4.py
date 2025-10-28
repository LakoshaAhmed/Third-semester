###### Task 4. Average Sweetness of Strawberries

#Grandma and her $n$ friends argued about who grew the sweetest strawberries in their gardens this summer.

#Write a function `find_sweetest_strawberry` that takes as input a list of lists of length $n+1$, each containing some integer numbers - 
# sweetness ratings of strawberries on a scale from $1$ to $10$. The "zero" list contains sweetness values for grandma's strawberries, 
# the $i$-th friend corresponds to the $i$-th list.

#Calculate the average value for each row and output who has the sweetest strawberries - $0$ 
# if it's grandma, or the number of the friend whose garden grew the sweetest strawberries.

#In case of a tie, return the minimum index among those with equal sweetness.

def sweetest_strawberry(sweetness_lists):
   
    best_index = 0
    max_avg = -2
    
    for i, strawberry_list in enumerate(sweetness_lists):
        if not strawberry_list:
            current_avg = 0
        else:
            current_avg = sum(strawberry_list) / len(strawberry_list)
        
        if current_avg > max_avg:
            max_avg = current_avg
            best_index = i
    
    return best_index
def get_user_input():
    n = int(input("Enter number of friends: "))
    sweetness_lists = []
    
   
    print("\nEnter Grandma's strawberry sweetness ratings (1-10), separated by spaces:")
    grandma_ratings = list(map(int, input().split()))
    sweetness_lists.append(grandma_ratings)
    
   
    for i in range(1, n + 1):
        print(f"Enter Friend {i}'s strawberry sweetness ratings (1-10), separated by spaces:")
        friend_ratings = list(map(int, input().split()))
        sweetness_lists.append(friend_ratings)
    
    return sweetness_lists

print("=== Strawberry Sweetness Calculator ===")
sweetness_data = get_user_input()
result = sweetest_strawberry(sweetness_data)

if result == 0:
    print("\n Grandma has the sweetest strawberries!")
else:
    print(f"\n Friend {result} has the sweetest strawberries!")