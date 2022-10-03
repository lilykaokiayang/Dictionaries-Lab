"""Restaurant rating lister."""


# put your code here
rating_file = open('scores.txt')


rest_rating = {}
def print_restaurant_rating(rating):
    
    # rest_rating = {}
    for line in rating:
        line = line.rstrip().split(":") 
        rest_rating[line[0]] =line[1]
    sorted_restaurants = dict(sorted(rest_rating.items()))
    
    for name, score in sorted_restaurants.items():
        print(f"{name} is rated at {score}")

    # for key in sorted(rest_rating):
    #   print(f'{key} is rated at {rest_rating[key]}')


def add_restaurant_rating():
    rest_input = input("Restaurant's name?")
    rating_input = int(input("Enter your rating."))
    while rating_input > 5 or rating_input < 1:
        print("Please enter a rating from 1-5: ")
        rating_input = int(input('Enter your rating.'))

         
    rest_rating[rest_input] = rating_input
        


add_restaurant_rating()
print_restaurant_rating(rating_file)

