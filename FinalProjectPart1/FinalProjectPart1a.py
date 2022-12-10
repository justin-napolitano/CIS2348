# Name: Becky Tseng
# StudentID: 2038591

import csv


# from collections import defaultdict

# this function returns a key for the built in sorted function
def get_key(item):
    # returns the first index of the list (which is Manufacturer name)
    return item[ 1 ]


# reads the csv file and creates a dictionary
file = [ *csv.DictReader(open("ManufacturerList.csv"),
                         fieldnames=("item_id", "Man_name", "Type", "Condition", "Price", "Date")) ]
# announces the list variable ManufacturerList
ManufacturerList = [ ]
# for loop to read each row in the csv file
for row in file:
    # adds each row to ManufacturerList
    ManufacturerList.append(row)

file = [ *csv.DictReader(open("PriceList.csv"), fieldnames=("item_id", "Price")) ]
PriceList = [ ]
for row in file:
    PriceList.append(row)

file = [ *csv.DictReader(open("ServiceDatesList.csv"), fieldnames=("item_id", "Date")) ]
ServiceDates = [ ]
for row in file:
    ServiceDates.append(row)

# defaultdict(dict) is basically a 'blank' dictionary that lets it replace it with new values
# merges PriceList and ServiceDates into one dictionary

for a in (PriceList, ServiceDates):
    # updates the combined dictionary with the values found
    for combined in a:
        i=0
        while i in range(len(PriceList)):
            # item_id is used to merge
            PriceList[i].update(combined)
            i = i+1

print(PriceList)

# combines ManufacturerList and PriceList
for l in (ManufacturerList, PriceList):
    for elem in l:
        for j in range(len(ManufacturerList)):
            c = ManufacturerList[j].update(elem)

e = defaultdict(dict)
# combines ManufacturerAndPrice and PriceAndServiceDates
for x in (ManufacturerAndPrice, PriceAndServiceDates):
    for z in x:
        e[z['item_id']].update(z)
# Contains the list of the full inventory
CombinedList = list(e.values())

CombinedData = []

for x in CombinedList:
    CombinedData.append(list(x.values()))

# puts the third index (condition) last in the list by using a for loop
for item in CombinedData:
    item[ 3 ], item[ 4 ], item[ 5 ] = item[ 4 ], item[ 5 ], item[ 3 ]

# sorts the list
SortedCombinedData = sorted(CombinedData, key=get_key)

# creates new csv file
with open('FullInventory.csv', 'w', newline='\n') as file:
    # create the csv writer
    writer = csv.writer(file, delimiter=',')
    # writes the list SortedCombinedData into the csv file
    writer.writerows(SortedCombinedData)
