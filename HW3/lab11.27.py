pdict={}#dictionary
for i in range(1,6):#accpting 5 inputs from user
    print("Enter player "+str(i)+"'s jersey number:")
    key=int(input())
    print("Enter player "+str(i)+"'s rating:\n")
    value=int(input())
    pdict[key]=value
print("ROSTER")
for i in sorted(pdict):#printing the values in dictionary
    print("Jersey number: "+str(i)+", Rating: "+str(pdict[i]))
while(1):#menu
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print("\nChoose an option:")
    n=input()#loop control variable
    if(n=="o"):#output the roster
        print("ROSTER")
        for i in sorted(pdict):
            print("Jersey number: "+str(i)+", Rating: "+str(pdict[i]))
    elif(n=="a"):#adds a new player
        print("Enter a new player's jersey number:")
        key=int(input())
        print("Enter the player's rating:")
        value=int(input())
        pdict[key]=value
    elif(n=="d"):#delete a player
        print("Enter a jersey number:")
        key=int(input())
        pdict.pop(key)
    elif(n=="u"):#updates a player's rating
        print("Enter a jersey number:")
        key=int(input())
        print("Enter a new rating for player:")
        value=int(input())
        pdict[key]=value
    elif(n=="r"):#prints ratings above a particular value
        print("Enter a rating:")
        rating=int(input())
        print("ABOVE "+str(rating))
        for i in sorted(pdict):
            if(pdict[i]>rating):
                print("Jersey number: "+str(i)+", Rating: "+str(pdict[i]))
    else:#exits the program
        exit(0)