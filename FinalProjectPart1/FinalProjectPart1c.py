import csv
import datetime #you'll need this to get dates (get it, haha)

#function to return the second from the last of the list
def get_key(item):
    # will be useful to be used as a key in the sorted function
    return item[-2]

#gets today's date
today = datetime.datetime.now()

file = [*csv.reader(open("FullInventory.csv"), delimiter = ',')]
#I explained this in part a, do I have to do this again?
FullInventory = []
for row in file:
    FullInventory.append(row)
    PastServiceDate = []
#find the column that I will need, which is the service date
    date = row[-2]
#converts the string to a date
    ServiceDate = datetime.datetime.strptime(date,"%m/%d/%Y")
#if-statement to see if the service date is past today or not
    if ServiceDate < today:
#adds the rows to the PastServiceDate
        PastServiceDate.append(row)
#sorts the list and assigns it to SortedPastServiceDate
        SortedPastServiceDate = sorted(PastServiceDate,key=get_key)
#assigns a path for the csv file that you will create
        path = "./PastServiceDateInventory.csv"
#opens the new csv file and "a for append" the SortedPastServiceDate list to the csv
        with open(path, 'a', newline='') as file:
            writer = csv.writer(file, delimiter = ',')
#rinse and repeat
            writer.writerows(SortedPastServiceDate)


