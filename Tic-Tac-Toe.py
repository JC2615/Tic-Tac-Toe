'''
Author: Joshua Curry
Description: Tic-Tac=Toe
'''

#Variable declaration
a, b, c, d, e, f, g, h, i, count = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0

#Game board
def printBoard():
    print(a, " | ", b, " | ", c)
    print(d, " | ", e, " | ", f)
    print(g, " | ", h, " | ", i)

while True:
    
    printBoard()

    #Player choice
    if count % 2 == 0:
        userInput = int(input("\nX, enter a number to replace: "))
        if userInput < 10 and userInput > 0:
            if userInput == 1 and a != "O" and a != "X":
                a = "X"
            elif userInput == 2 and b != "0" and b != "X":
                b = "X"
            elif userInput == 3 and c != "O" and c != "X":
                c = "X"
            elif userInput == 4 and d != "O" and d != "X":
                d = "X"
            elif userInput == 5 and e != "O" and e != "X":
                e = "X"
            elif userInput == 6 and f != "O" and f != "X":
                f = "X"
            elif userInput == 7 and g != "O" and g != "X":
                g = "X"
            elif userInput == 8 and h != "O" and h != "X":
                h = "X"
            elif userInput == 9 and i != "O" and i != "X":
                i = "X"
            else:
                print("Your input is invalid. Try again.")
                count -= 1
        else:
            print("Your input is invalid. Try again.")
            count -= 1

    else:
        userInput = int(input("\nO, enter a number to replace: "))
        if userInput < 10 and userInput > 0:
            if userInput == 1 and a != "O" and a != "X":
                a = "O"
            elif userInput == 2 and b != "O" and b != "X":
                b = "O"
            elif userInput == 3 and c != "O" and c != "X":
                c = "O"
            elif userInput == 4 and d != "O" and d != "X":
                d = "O"
            elif userInput == 5 and e != "O" and e != "X":
                e = "O"
            elif userInput == 6 and f != "O" and f != "X":
                f = "O"
            elif userInput == 7 and g != "O" and g != "X":
                g = "O"
            elif userInput == 8 and h != "O" and h != "X":
                h = "O"
            elif userInput == 9 and i != "O" and i != "X":
                i = "O"
            else:
                print("Your input is invalid. Try again.")
                count += 1
        else:
            print("Your input is invalid. Try again.")
            count += 1

    #Win and draw conditions
    if a == b and b == c and c == a:
        printBoard()
        print(a, ", you are the winner!")
        break
    elif d == e and e == f and f == d:
        printBoard()
        print(d, ", you are the winner!")
        break
    elif g == h and h == i and i == g:
        printBoard()
        print(g, ", you are the winner!")
        break
    elif a == d and d == g and g == a:
        printBoard()
        print(a, ", you are the winner!")
        break
    elif b == e and e == h and h == b:
        printBoard()
        print(b, ", you are the winner!")
        break
    elif c == f and f == i and i == c:
        printBoard()
        print(c, ", you are the winner!")
        break
    elif a == e and e == i and i == a:
        printBoard()
        print(a, ", you are the winner!")
        break
    elif c == e and e == g and g == c:
        printBoard()
        print(c, ", you are the winner!")
        break
    elif a != 1 and b != 2 and c != 3 and d != 4 and e != 5 and f != 6 and g != 7 and h != 8 and i != 9:
        printBoard()
        print("It's a tie!")
        break;

    count += 1