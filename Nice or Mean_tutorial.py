##
## Python: 3.10.6
##
## Author: Jason Rodgers
##
## Purpose: The Tech Academy - Python Course, Creating our first program together.
##          Demonstrating how to pass variables from function to function
##          while producing a functional game.

##          Remember, function_name(variable) _means that we pass in the variable.
##          return variable _means that we are returning the variable
##          back to the calling function.






def start(nice = 0,mean = 0,name = ""):
    #get users name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        check if this a new game or not.
        If it is a new game get the users name.
        If it is not a new game, thank the player for
        playing and continue the game.
    """
    #meaning that if we do not already have this users name,
    #than they are a new user and we need to get their name
    if name != "":
        print("\nThank you for playing again, {}".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby all sorts of people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name



def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice\nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger jumps up and down and twirls around with glee...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nstarts fuming and then \nmenacingly storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #pass the 3 variables to the score()

def show_score(nice,mean,name):
    print ("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))
        
def score(nice,mean,name):
    #score function is being passed the values stored within the 3 variables
    if nice > 2: #if condition is valid, call win function passing in variables so it can use them
        win(nice,mean,name)
    if mean > 2: #if condition is valid, call lose function passing in variables so it can use them
        lose(nice,mean,name)
    else: # call mice_mean function passing in variables so it can use them
        nice_mean(nice,mean,name)

    
    
def win(nice,mean,name):
    # Substitute the {} wildcards with our variable values
    print("\nWow you did it! {}, you win! \nIt's gotta be hard holding that smile all the time!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)


def lose(nice,mean,name):
    # Substitute the {} wildcards with our variable values
    print("Your game has come to an end, nobody likes a miser! \n{}, you need therapy\n!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name) 

    

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ".lower())
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'Yes', ( N ) for 'NO':\n>>> ")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice I do not reset the name variable because the user has elected to play again
    start(nice,mean,name)















if __name__ == "__main__":
    start()
