result = 0
answer = False
for a in range(1,101):
    if answer == False:
        result = result + a

    if a == 100:
        answer == True
        print(result)