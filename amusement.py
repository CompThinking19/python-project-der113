#Save csv datatset to github project folder then import, open, read
import csv
source = open('Saferparks-dataset-2017.csv')
amusement = csv.reader(source)
#(0 = id, 2=state, 8=ride type, 12=number injured/killed), print dictionary to see results
#first create empty dictionary
ride_accidents = {}
#skip first row in amusement because it takes the heading columns from row 1
next(amusement)
#iterate through rows and add specific columns to dictionary
#when I take out id num column, it's not giving me all the states because of duplicates
#so I added id back to make sure I had everything for each state
for col in amusement:
    id = col[0]
    state = col[2]
    ride_type = col[8]
    num_injured = col[12]
    ride_accidents[id] = state, ride_type, num_injured
print ride_accidents
#I need to total each state by ride type, then grand total
#I would like to have a matching game for parents to teach the true risks of amusement rides
