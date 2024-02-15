import random
k=''
while True:
    print("1.press 0 for ROCK\n2.press 1 for PAPER\n3.press 2 for SCISSOR")
    player1="Computer".upper()
    print("player1:",player1)
    player2=input("Player2 please enter your name:").upper()
    while True:
        n1=random.randint(0,2)
        try:
            n2=int(input('Please player2 press any option for rock,paper,scissor:'))
            if type(n2) is not int:
                raise ValueError("Please enter only value from 0 to 2 ")
            elif  n2<0 or n2>2:
                raise ValueError("Please enter only value from 0 to 2 ")
        except ValueError as e:
            print(e)
        else:
            print("Computer's choice:",n1)
            if n1==0 and n2==2:
                print("Cogrates! {} win this game".format(player1))
                print("Oh sorry {}!, you loose this game.Please try some another time".format(player2))
                break
            elif n1==2 and n2==1:
                print("Cogrates! {} win this game".format(player1))
                print("Oh sorry {}!, you loose this game.Please try some another time".format(player2))
                break
            elif n1==1 and n2==0:
                print("Cogrates! {} win this game".format(player1))
                print("Oh sorry {}!, you loose this game.Please try some another time".format(player2))
                break
            if n1==n2:
                print("Game draw!")
                break
            else:            
                print("Cogrates! {} win this game".format(player2))
                print("Oh sorry {}!, you loose this game.Please try some another time".format(player1))
                break
    while True:
        try:
            k=input("if you want to play again then press y otherwise n:")
            if k!='y' and k!='Y' and k!='n' and k!='N':
                raise ValueError("Please enter only y or n for yes or no")
        except ValueError as e:
            print(e)
        else:
            break
    if k=='n' or k=='N':
        break  
        