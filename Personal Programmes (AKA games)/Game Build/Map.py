from random import randint, random
import CaveChooser, random
rows, cols = (5, 5)
arr = [[0 for i in range(cols)] for j in range(rows)]
x,y=2,2
arr[y][x]=1
arr[randint(0,4)][randint(0,4)], arr[randint(0,4)][randint(0,4)]=1,1
outOfBounds = "You can't go that far!"
while True:
    for row in arr:
        print(row)
    move = input("U, D, L, R: ")
    if move == "U" or move == "u":
        arr[y][x]-=1
        if y-1 >= 0:
            y -= 1
            arr[y][x]+=1
        else:
            print (outOfBounds)
            arr[y][x]+=1
    elif move == "D" or move == "d":
        arr[y][x]-=1
        if y+1 <= 4:
            y += 1
            arr[y][x]+=1
        else:
            print (outOfBounds)
            arr[y][x]+=1
    elif move == "L" or move == "l":
        arr[y][x]-=1
        if x-1 >= 0:
            x -= 1
            arr[y][x]+=1
        else:
            print (outOfBounds)
            arr[y][x]+=1
    elif move == "R" or move == "r":
        arr[y][x]-=1
        if x+1 <= 4:
            x += 1
            arr[y][x]+=1
        else:
            print (outOfBounds)
            arr[y][x]+=1
    else:
        print("Input not understood")
    if arr[y][x]==2:
        CaveChooser.main()
        arr[y][x]-=1