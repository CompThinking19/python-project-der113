#Save csv datatset to github project folder then import, open, read
import csv
source = open('Saferparks-dataset-2017.csv')
amusement = csv.reader(source)
#(columns: 2=state, 12=number injured/killed), print dictionary to see results
#first create empty dictionary for injuries per state, then one per ride type to have a variety of questions
state_accidents = {}
ride_types = {}

#skip first row in amusement because it takes the heading columns from row 1
next(amusement)
#iterate through rows and add specific columns to dictionary
#check if state isn't in dict and if not, add it in and total number injured for that state/ridetype

for col in amusement:
    if (col[2] not in state_accidents):
        state_accidents[col[2]] = 0

    if len(col[12]) > 0:
        state_accidents[col[2]] += int(col[12])

    if (col[8] not in ride_types):
        ride_types[col[8]] = 0

    if len(col[12]) > 0:
        ride_types[col[8]] += int(col[12])

#print state_accidents
#print ride_types

#Create q&a with multiple choice
#Display welcom and instructions on screen
#Person will guess which answer is correct out of 3 choices
#Counter will total how many right

print "Welcome to an informational guessing game about amusement ride accidents from 2007-2017."
print "To play, you must guess how many injuries occured on amusement park rides over the period of 10 years."
#Ask if the user wants to play. Use lower function in case uppercase in yes. If yes, start quiz. If not, say goodbye.
start = raw_input("Would you like to start? ").lower()

if start == "yes":
    print "Okay, let's begin!"

else:
    print "Sorry you don't want to take the quiz."
