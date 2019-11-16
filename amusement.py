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

#Create a guessing game for number of injuries per state or ride type at random
#Display welcome and instructions on screen
#Person will guess a number and if incorrect, the right answer will display
#import random to be able to select random keys(states, ride types) into question
import random
print "Welcome to an informational guessing game about amusement ride accidents from 2007-2017."
print "To play, you must guess how many injuries occured on amusement park rides over the period of 10 years by state or ride type."
#Ask if the user wants to play. Use lower function in case user types uppercase. If yes, start quiz. If not, say goodbye.
start = raw_input("Would you like to start? ").lower()

if start == "yes":
    print "Okay, let's begin!"
    print "Learn the number of injuries on amusement rides from 2007-2017.\n\n"

    #create question that grabs random keys; store incorrect in list to display to user at end
    incorrect_answers = []
    while len(test_dict) > 0:
        choice = random.choice(test_dict.keys())
        correct_answer = test_dict.get(choice)
        print "Please guess a total number of injuries over 10 years for",choice+"?"

        #take user answer (number only), if answer is correct, remove it from choices
        answer = raw_input("")
        try:
            val = float(answer)
        except ValueError:
            print("That's not a number!")

        if answer == correct_answer:
            print "That's correct!\n"
            del test_dict[choice]
        else:
            print "That's incorrect."
            print "The correct answer is",correct_answer
            incorrect_answers.append(choice)
            del test_dict[choice]

    print "\nYou missed",len(incorrect_answers),"answers.\n"

    if incorrect_answers:
        print "Here's the ones that you may want to brush up on:\n"
        for each in incorrect_answers:
            print each
    else:
        print "Perfect!"

else:
    print "Sorry you don't want to learn about amusement ride accidents!"
