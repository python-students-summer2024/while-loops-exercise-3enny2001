def get_starting_number():

#asks user to input starting # of beers until user inputs valid input any integer 1 or greater
#The returns integer equivalent of the value 


    while True:
        starting_number = input("Enter the number of beers you want to start singing with: ")
        if starting_number.isnumeric() and int(starting_number) >= 1:
            return int(starting_number)
        else:
            continue
    return starting_number


def sing(starting_number):

#takes an argument specifying how many bottles of beer to start with
#outputs lyrics to the song starting from that # of bottles 
#flag variable indicates whether a condition has been met using a boolean true or false
    found = False
    i = starting_number
    while i >= 1:
        print(f"{i} bottle{'s' if i != 1 else ''} of beer on the wall, {i} bottle{'s' if i != 1 else ''} of beer.")
        print(f"Take {'one' if i != 1 else 'it'} down, pass it around, {i-1 if i-1 != 0 else 'no more'} bottle{'s' if i-1 != 1 else ''} of beer on the wall{'.' if i != 1 else '!'}\n")
        if i == 1:
            found = True
        i -= 1