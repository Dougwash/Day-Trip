print()
print ("Suggested day Trip")
print()

from ast import While
from importlib.metadata import distributions
import random
from turtle import end_fill

destinations = ['Philly','D.C.','Baltimore','New York City']

resturants =['Capital Grill','Mixto','Steak 48','Flor de Mayo']

transportations =['Car','Train','Bus','Uber/Lift']

entertainment =['Theater','Concert','Club','Museum']

def pick_dest (destination):
    final_dest = random.choice (destinations) 
    print (f"Destination: {final_dest}")
    # print (final_dest)
    return final_dest

def pick_rest (resturant):
    final_rest = random.choice (resturants) 
    print (f"Resturant: {final_rest}")
    return final_rest

def pick_trans (transortation):    
    final_trans = random.choice (transportations) 
    print (f"Transportation: {final_trans}")
    return final_trans

def pick_ent (ent):
    final_ent = random.choice (entertainment) 
    print (f"Entertainment: {final_ent}")
    return final_ent


def run_trip():
    pick_dest(destinations)
    pick_rest(resturants)
    pick_trans(transportations)
    pick_ent(entertainment)
    print()
run_trip()

sat= False

    
answer = input ('Are you happy with your trip itinerary? y/n ')
print()
while sat is False:

    if answer == "n":
        print()
        print("Here is an updated itinerary: ")
        print()
        run_trip()
        print()
    answer = input ('Are you happy with your trip itinerary? y/n ')
    print()

    if answer == 'y':
        # answer = input ('Are you happy with your trip itinerary? y/n ')
        # print()
        print ('Your trip itinerary is: ')   
        print()
        run_trip ()
        sat = True   
        # change_d = run; final_dest






