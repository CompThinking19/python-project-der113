#Save excel csv dataset of amusement ride accidents (2010-2017) then import it.
#Open and read assigning it to variable amusement.
import csv
source = open('Saferparks-dataset-2017.csv')
amusement = csv.reader(source)
#print specific columns in the dataset rows to filter only the data I need
#(0=id, 2=state, 8=ride type, 12=number injured/killed )
for row in amusement:
    print row[0, 2, 8, 12]
#create dictionary (or two) for number injured per ride type and maybe also by state
#I would like to have a matching game for parents to teach the true risks of amusement rides
