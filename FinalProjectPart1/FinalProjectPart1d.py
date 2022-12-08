#Name: Becky Tseng
#StudentID: 2038591

import csv

#returns the third index of a list, which is the 4th column (price)
def get_key(item):
    return item[3]

#opens the csv file and adds the values to blank lists
file = [*csv.reader(open("FullInventory.csv"), delimiter = ',')]
FullInventory = []
for row in file:
    FullInventory.append(row)

DamagedList=[]
for row in FullInventory:
#finds the rows that contain the word 'damaged' even if it's written in all caps or capitalized
    if "damaged" in row[-1].lower():
#deletes the last column or index in the list
        del row[-1]
        DamagedList.append(row)

#sorts the list by the 3th index reversed (most expensive to cheapest)
SortedDamagedList = sorted(DamagedList,key=get_key,reverse=True)
#creates new csv file and exports SortedDamagedList's values into the csv file
with open("DamagedInventory.csv", 'a', newline='\n') as file:
    writer = csv.writer(file)
    writer.writerows(SortedDamagedList)










