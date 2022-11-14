#Name: Becky Tseng
#StudentID: 2038591

import csv

#open and reads the csv file
with open('FullInventory.csv','r', newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter =',')
#create an empty list called InventoryList to put values in
    InventoryList = []
#for loop that reads each row of the csv file
    for row in reader:
#adds each row to InventoryList
        InventoryList.append(row)

#for loop to find all values of the item type
types = [item[2] for item in InventoryList]
#removes duplicates
types=list(set(types))
#I just wanted to call it "unique"
UniqueTypes = types

#for loop to find the values in the unique types list
for value in UniqueTypes:
    TypesList = []
#reading each row in InventoryList
    for row in InventoryList:
#if the same value in UniqueTypes is found in row
        if value in row:
#that value will be used to create the filename
            path = f"./{value.capitalize()}Inventory.csv"
#deletes the second index (third column) of the list
            del row[2]
#adds the rows of the designated device type into a list
            TypesList.append(row)
#opens the new csv file
            with open(path, 'w',newline='\n') as file:
                writer = csv.writer(file)
#writes values of TypesList into the csv file, it also sorts by the first column or 0 index
#with the built in sorted function
                writer.writerows(sorted(TypesList))







