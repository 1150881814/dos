from random import  randint
number = randint(1,100)
win = False
print("guess")
winpoint = 3
while win == False:
    answer = int(input())

    if answer > number:
        print("%d is too big" % answer)
        winpoint = winpoint - 1
        if winpoint != 0:
            print("You still have %d chance"% winpoint)
        if winpoint == 0:
            print("You lose")
            break

    if answer < number:
        print("%d is too small" % answer)
        winpoint = winpoint - 1
        if winpoint != 0:
            print("You still have %d chance"% winpoint)
        if winpoint == 0:
            print("You lose")
            break

    if answer == number:
        print("Excellent! %d is the right answer" % answer)
        break
