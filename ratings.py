"""Restaurant rating lister."""


# put your code here
# Reads the ratings in from the file
# Stores them in a dictionary
# And finally, spits out the ratings in alphabetical order by restaurant

import sys


def make_ratings_dict(filename):
    """Takes data from txt file and returns a dictionary.
       - takes filename as the argument
       - returns a dictionary with restaurants as keys and ratings as values
    """
    restaurant_rating = {}

    for line in filename:
        restaurant_name, rating = line.strip().split(":")
        # unpacks the list as the list is made...in one line!
        restaurant_rating[restaurant_name] = rating
    return restaurant_rating

def sort_dict_into_list(dictionary):
    """Makes a sorted list with the dictionary data"""
    lst_restaurant = dictionary.items()
    # setting list of tuples to variable
    lst_restaurant.sort()
    return lst_restaurant

def print_ratings(lst_of_tuples):
    """Prints restaurants with ratings"""
    for restaurant, rating in lst_of_tuples:
        print "{} is rated at {}.".format(restaurant, rating)


scores_file = open(sys.argv[1])

dictionary = make_ratings_dict(scores_file)

lst_of_tuples = sort_dict_into_list(dictionary)

print_ratings(lst_of_tuples)

scores_file.close()
