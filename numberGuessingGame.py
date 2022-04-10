for i in range(5):
    a=int(input("guess a number"))
    b=15
    if a<b:
        print("you are little lesser that the number")
    elif a==b:
        print("congratultions!! you have won the game")
        break
    else :
        print("you are little higher than the number ")
