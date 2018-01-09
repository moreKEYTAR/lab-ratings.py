"""Restaurant rating lister."""


# put your code here
# Reads the ratings in from the file
# Stores them in a dictionary
# And finally, spits out the ratings in alphabetical order by restaurant

import sys


def update_ratings_dict(filename, dictionary):
    """Takes data from txt file and returns a dictionary.
       - takes filename as the argument
       - returns a dictionary with restaurants as keys and ratings as values
    """

    for line in filename:
        restaurant_name, rating = line.strip().split(":")
        # unpacks the list as the list is made...in one line!
        dictionary[restaurant_name] = rating
    return dictionary


def sort_dict_into_list(dictionary):
    """Makes a sorted list with the dictionary data"""
    lst_restaurant = dictionary.items()
    # setting list of tuples to variable
    lst_restaurant.sort()
    return lst_restaurant


def print_ratings(ratings_list):
    """Prints restaurants with ratings.
        input: list of tuples
        output: None. Prints.
    """
    
    for restaurant, rating in ratings_list:
        print "{} is rated at {}.".format(restaurant, rating)


def get_restaurant_rating(dictionary):
    """Asks users for restaurant and rating and add it to the dictionary"""
    input_restaurant = raw_input("Enter the restaurant name >>> ").title()
    input_rating = raw_input("Enter the restaurant rating >>> ")
    dictionary[input_restaurant] = input_rating
    # return not needed; the dictionary is global and was modified



def update_random_rating(dictionary):
    from random import choice
    rand_restaurant = choice(dictionary.keys())
    new_rating = raw_input("What rating would you like to give to {}? \n>>>".format(rand_restaurant))
    dictionary[rand_restaurant] = new_rating

def main_function():
    scores_file = open(sys.argv[1])

    ratings_dictionary = {}

    while True:
        print """
        What would you like to do?
        'q' to QUIT
        'n' to add a NEW restaurant and rating
        'p' to PRINT all current ratings
        'r' to update a RANDOM restaurant rating from the current list """

        user_choice = raw_input(">>> ")

        if user_choice.lower() == "q":
            break

        elif user_choice.lower() == "n":
            get_restaurant_rating(ratings_dictionary)

        elif user_choice.lower() == "p":
            updated_dictionary = update_ratings_dict(scores_file, ratings_dictionary)
            ratings_list = sort_dict_into_list(updated_dictionary)
            print_ratings(ratings_list)

        elif user_choice.lower() == "r":
            updated_dictionary = update_ratings_dict(scores_file, ratings_dictionary)
            update_random_rating(updated_dictionary)


    scores_file.close()

main_function()
