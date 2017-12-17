from random import  randint
number = randint(1,100)
win = False
print("guess")
while win == False:
    answer = int(input())

    if answer > number:
        print("%d is too big" % answer)

    if answer < number:
        print("%d is too small" % answer)

    if answer == number:
        print("Excellent! %d is the right answer" % answer)
        win == True
