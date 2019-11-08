#Save csv datatset to github project folder then import, open, read
import csv
source = open('Saferparks-dataset-2017.csv')
amusement = csv.reader(source)
#(columns: 2=state, 8=ride type, 12=number injured/killed), print dictionary to see results
#first create empty dictionary
ride_accidents_state = {}
#skip first row in amusement because it takes the heading columns from row 1
next(amusement)
#iterate through rows and add specific columns to dictionary
#check if state isn't in dict and if not, add it in
#create list of num injured by state
for col in amusement:
    if col[2] in ride_accidents_state:
        ride_accidents_state[col[2]].append(col[12])
        #tried adding ride type column, but can't see a way to combine the str and int by str
        #commented out the ride type addition
        #ride_accidents_state[col[2]].append(col[8])
    else:
        ride_accidents_state[col[2]] = [col[12]] #+ [col[8]]

print ride_accidents_state
