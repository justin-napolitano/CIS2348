# Name: Becky Tseng
# StudentID Number: 2038591

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print()

first_service = input("Select first service:\n")
second_service = input("Select second service:\n")

print()
print("Davy's auto shop invoice")
print()
total = 0

if (first_service.lower() == "oil change"):
    print("Service 1: Oil change, $35")
    total = total + 35

elif (first_service.lower() == "tire rotation"):
    print("Service 1: Tire rotation, $19")
    total = total + 19

elif (first_service.lower() == "car wash"):
    print("Service 1: Car wash, $7")
    total = total + 7

elif (first_service.lower() == "car wax"):
    print("Service 1: Car wax, $12")
    total = total + 12


elif (first_service.lower() == "-"):
    print("Service 1: No service")
    total = total + 0

else:
    print("First service input error")

if (second_service.lower() == "oil change"):
    print("Service 2: Oil change, $35")
    total = total + 35

elif (second_service.lower() == "tire rotation"):
    print("Service 2: Tire rotation, $19")
    total = total + 19

elif (second_service.lower() == "car wash"):
    print("Service 2: Car wash, $7")
    total = total + 7

elif (second_service.lower() == "car wax"):
    print("Service 2: Car wax, $12")
    total = total + 12

elif (second_service.lower() == "-"):
    print("Service 2: No service")
    total = total + 0


else:
    print("Second service input error")

print()

print("Total: $", total, sep="")


