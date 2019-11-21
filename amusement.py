#Create a guessing game for the number of injuries per state or ride type at random
#Most parents assume accidents are freak occurences and giving them the shocking truth will force more amusement parks and carnivals to make rides safer
#Display welcome and instructions on screen
#Person will guess a number and if incorrect, the right answer will display. Total incorrect will display at the end.

#Save csv datatset to github project folder then import, open, read
import csv
source = open('Saferparks-dataset-2017.csv')
amusement = csv.reader(source)
#(columns: 2=state, 8=ride type, 12=number injured/killed)
#first create empty dictionary for injuries per state, then one per ride type
state_accidents = {}
ride_types = {}
#skip first row in amusement because it takes the heading columns from row 1
next(amusement)

#iterate through rows and add injuries per state in one dictionary
#iterate through rows and add injuries per ride type in another dictionary
#check if state isn't in state_accidents dict and if not, add it in
#check if ride type isn't in ride_type dict and if not, add it in
#if a field is missing, skip it by setting greater than 0
for col in amusement:
    if (col[2] not in state_accidents):
        state_accidents[col[2]] = 0

    if len(col[12]) > 0:
        state_accidents[col[2]] += int(col[12])

    if (col[8] not in ride_types):
        ride_types[col[8]] = 0

    if len(col[12]) > 0:
        ride_types[col[8]] += int(col[12])

#merge dictionaries into a new one called test_dict
test_dict = state_accidents.copy()
test_dict.update(ride_types)

#import random to be able to select random keys(states, ride types) from test_dict into question
import random
print "Welcome to an informational guessing game about amusement ride accidents from 2007-2017."
print "We expect that our children are safe and hope any accident is a 'freak accident' but depending on the state and ride type, that isn't always so."
print "My game is to test parents guesses about ride injuries. I'm sure you will be shocked by some of the numbers."
print "To play, you must guess how many injuries occured on amusement park rides over the period of 10 years by state or ride type."
print "The information used is based on the states that are required to report hospital injuries/deaths on rides."

#Ask if the user wants to play. Use lower function in case user types uppercase. If yes, start quiz. If not, say goodbye.
start = raw_input("Would you like to start? yes or no\n").lower()
if start == "yes":
    print "Okay, let's begin! You can quit at any time by entering q, there are approximately 62 questions if you take the whole test."
    print "Learn the number of injuries on amusement rides from 2007-2017.\n\n"

    #create question that grabs random keys; store incorrect and correct answers in list to display to user at end
    incorrect_answers = []
    correct_answers = []
    while len(test_dict) > 0:
        choice = random.choice(test_dict.keys())
        correct_answer = test_dict.get(choice)
        print "\nPlease guess a total number of injuries over 10 years for",choice+"?"

        #take user input and assign to variable answer, exception below is q for quit
        answer = raw_input("")
        #throw an error if not an int
        try:
            val = int(answer)
        except ValueError:
            print("That's not a number!")

        #Give user option to quit at any time by typing q and display message
        if answer == 'q':
            print "Sorry you don't want to keep going! Please go to saferparks.org for tips on ride saftey."
            break

        #If answer matches, display correct, store number of correct and delete that question/answer set from displaying again
        elif int(answer) == correct_answer:
            print "That's correct!\n"
            correct_answers
            correct_answers.append(choice)
            del test_dict[choice]

        #Keep a tally of wrong answers for user; remove the choice from repeating on screen
        else:
            print "That's incorrect."
            print "The correct answer is",correct_answer
            incorrect_answers.append(choice)
            del test_dict[choice]

    #Tell user how many they got wrong, then show them
    print "\nYou were incorrect",len(incorrect_answers),"times."
    print "You were correct",len(correct_answers),"times.\n"
    if incorrect_answers:
        print "Here's the ones that you may want to brush up on at saferparksdata.org:\n"
        for each in incorrect_answers:
            print each
    #If they guesssed all right, they get a message
    else:
        print "Perfect!"

#If user doesn't want to play by typing no, display the message below
else:
    print "Sorry you don't want to play. To learn more about ride safety tips and statistics, please visit saferparks.org."
