# This is a python program that outputs whether or not today is a weekday #

from _datetime import datetime   # date time module supplies classes for manipulating dates and times #

def weekday ():
    week_num_today = datetime.today () .weekday() # returns the day in number format from (1-7) #

    if week_num_today < 5:
        print("Yes, unfortunately today is a weekday")
    else:
        print ("It is the weekend, yay! ")

    
if __name__ == "__main__":
    weekday()   
