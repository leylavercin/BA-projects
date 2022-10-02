from swampy.TurtleWorld import *
import random
import math
world = TurtleWorld()

first_turtle = Turtle()                        # First, I created my turtles (also in line 8)
first_turtle.delay = 0.01                      # Set their speed
second_turtle = Turtle()
second_turtle.delay = 0.01


def straight_line(starter_turtle_turtle, play):           # This is the straight line movement
        fd(starter_turtle_turtle, play)


def stairs(starter_turtle_turtle, play):                  # This one is the stairs move
    play=play/5.0                                         # to equal them in order to make them move with same amount of step
    for i in range(2):
        fd(starter_turtle_turtle, play)
        lt(starter_turtle_turtle, 90)
        fd(starter_turtle_turtle, play)
        rt(starter_turtle_turtle, 90)
    fd(starter_turtle_turtle, play)
    for i in range(2):
        rt(starter_turtle_turtle, 90)
        fd(starter_turtle_turtle, play)
        lt(starter_turtle_turtle, 90)
        fd(starter_turtle_turtle, play)
    return


def half_sphere(starter_turtle_turtle, play):           # This is the half sphere move, I didn't call them yet they are just waiting for it
    x=int(play*math.pi)
    lt(starter_turtle_turtle, 90)
    for i in range(x):
        fd(starter_turtle_turtle, 0.5)
        rt(starter_turtle_turtle, 180.0/x)
    lt(starter_turtle_turtle, 90)
    return


def which_shape(t,p):                  # With this function I aimed to choose the style of the move randomly, it'll be called in line 141 and 175
    shape=random.randint(1,3)
    if shape == 1:                     # I paired every movement style with a number and then randomly choose one of those numbers
        straight_line(t, p)
    elif shape == 2:
         stairs(t, p)
    elif shape == 3:
        half_sphere(t, p)


def main_game():                         # This is my general function, lets me call the whole thing whenever I want
    print "----- First Turtle -----"
    first_turtle_name = raw_input("What is the name of first Turtle? \n")       # Choosing a name for turtle
    first_color = raw_input(str("Please select a color for your Turtle, red-blue-yellow? \n"))   #choosing color
    if first_color == "red" or first_color == "blue" or first_color == "yellow":   #Checking whether the chosen color fits with our defined colors or not
        pass
    while first_color != "red" and first_color != "blue" and first_color != "yellow": # same here
        print first_color + " is not a valid color,",
        first_color = raw_input("please select a color for your Turtle, red-blue-yellow? \n")
    first_turtle.set_color(first_color)                    # color of turtle now defined and can seen in window
    print first_turtle_name + " is READY TO GO!"
    first_turtle.pu()                                  # turtle taking its position for the race
    first_turtle.bk(130)
    first_turtle.pd()

    print "----- Second Turtle -----"
    second_turtle_name = raw_input("What is the name of second Turtle? \n")    # Choosing a name for turtle
    while first_turtle_name == second_turtle_name:            # Need two different name, this is the part that checks name similarity
        print second_turtle_name + " is taken, please choose another name! \n",
        second_turtle_name = raw_input()
    second_color = raw_input("Please select a color for your Turtle, red-blue-yellow? \n") #choosing color
    if second_color == "red" or second_color == "blue" or second_color == "yellow":     #Checking whether the chosen color fits with our defined colors or not
        pass
    while second_color != "red" and second_color != "blue" and second_color != "yellow":  # same here
        print second_color + " is not a valid color,",
        second_color = raw_input("please select a color for your Turtle, red-blue-yellow? \n")
    second_turtle.set_color(second_color)             # color of turtle now defined and can seen in window
    print second_turtle_name + " is READY TO GO!"
    second_turtle.pu()
    second_turtle.bk(130)             # turtle taking its position for the race
    second_turtle.rt(90)
    second_turtle.fd(65)
    second_turtle.lt(90)
    second_turtle.pd()

    roundd = 1                 # counter for round number
    first_turtle_score = 0     # counter for scores
    second_turtle_score = 0    # same

    turtles_name = [first_turtle_name, second_turtle_name]  # In dirty hands society one of assistant showed me the list way
    starter_turtle = str(random.choice(turtles_name))      # randomly choosing which turtle will be the starter turtle
    if starter_turtle == first_turtle_name:
        starter_turtle_turtle = first_turtle
        secondary_turtle_name = second_turtle_name     # if starter turtle will be the first turtle then secondary should be second turtle
        secondary_turtle_turtle = second_turtle        # Need to define with another name because name doesnt count as turtle

    else:
        starter_turtle_turtle = second_turtle
        secondary_turtle_name = first_turtle_name
        secondary_turtle_turtle = first_turtle      # if starter turtle will be the second turtle then secondary should be first turtle

    while first_turtle_score < 200 and second_turtle_score < 200:  # game should end when scores reach 200
        print "****** ROUND {} ******".format(roundd)       # also thought by assistant, inside of the braces take their value from the parantese at the end
        print first_turtle_name + "'s score: " + str(first_turtle_score)      # we'll see the score with these
        print second_turtle_name + "'s score: " + str(second_turtle_score)

        if roundd % 2 == 0:     # this means run those when round's number is even, THIS IS THE BIG IF FOLLOWING ELSE WILL CONTAIN THE SAME CODE
            print (secondary_turtle_name) + " plays !"     # which turtle needs to move as a second player
            play1 = input("How many steps would you like to take? \n")    # we'll gtting information that how many step you like to move for your turtle

            def step_take(play):   # checking the step, whether it' in the correct range, (line 116)
                while play > 100:
                    print "Please select a number between 0-100: ",
                    play = input()          # if not try again, we changed the name of input to stop the function from getting value from play1
                return play

            play = step_take(play1)    # here, we again equalize play1 and play
            if play <= 100:
                probability = (100 - play)  # this function calculates change of fail or success
                s = probability

            random_number = random.randint(1, 100)    # picking a number to use for calculating whether move was succesful or not(line 133 and 136)
            def success_or_not(random_number):  # this function allows to see whether my move was successful or not, it'll be calling in line 138
                if random_number >= s:   # leads us to failure
                    return False
                elif random_number < s:  # leads us to success
                    return True

            success = success_or_not(random_number)
            if success == True:
                print "Success!"
                second_turtle_score += play     # if turtle achieved success then it needs score increase
            else:
                print "You Failed!"

            success_or_not(random_number)  # this function allows to see whether my move was successful or not
            if success == True:    # means if it successful, choose your shape to move
                which_shape(secondary_turtle_turtle, play)
        else:  # I copied the same code from IF part (line 109), same code because they have to do same thing differences they have are the round numbers and turtles.
            print str(starter_turtle) + " plays !"
            play1 = input("How many steps would you like to take? \n")
            def step_take(play):
                while play > 100:
                    print "Please select a number between 0-100: ",
                    play = input()
                return play

            play = step_take(play1)
            if play <= 100:
                probability = (100 - play)  # this function calculates how many chance i can to move
                s = probability
            random_number = random.randint(1, 100)
            def success_or_not(random_number):  # this function allows to see whether my move was successful or not
                if random_number >= s:
                    return False
                elif random_number < s:
                    return True

            success = success_or_not(random_number)
            if success == True:
                print "Success!"
                first_turtle_score += play
            else:
                print "You Failed!"
            success_or_not(random_number)
            shape = random.randint(1, 3)

            if success == True:
                which_shape(starter_turtle_turtle,play)

        roundd += 1  # after a round, round count needs to increase, this is doing that function

    if first_turtle_score > 199: # first turtle that reached the ending ending will be the winner, so we are checking whether winner is the first turtle or not
        print "++++++++++++++++ \n" + first_turtle_name + " WINS!!!!! \n" + "++++++++++++++++ \n"
    elif second_turtle_score > 199:   #we are checking whether winner is the second turtle or not
        print "++++++++++++++++ \n" + second_turtle_name + " WINS!!!!! \n" + "++++++++++++++++ \n"
    return

def playy_again():      # after a match, if you want to restart the game that is the function that needs to be called
    play_again = raw_input("DO YOU WANT TO PLAY ANOTHER ROUND(yes/no)? ")
    if play_again == "yes":
        print main_game()
    elif play_again == "no":
        print "Thanks for playing! See you again!"
    else:
        print "yes or no ? ",
        play_again = raw_input()
        if play_again == "yes" or play_again == "no":
            playy_again()
    return

main_game()    #calling this basically at the bottom, because everything is in this function

playy_again()
wait_for_user()



