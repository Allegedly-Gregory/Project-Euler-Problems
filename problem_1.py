

#way I tried
def multiples(num):
    numlist = []
    for x in range(num):
        if x % 3 == 0:
            numlist.append(x)
        elif x % 5 == 0:
            numlist.append(x)
    return numlist[1:]

print(multiples(1000))


#smarter solution
def problem1():
    x=0
    for i in range (0, 1000, 3):
        if not (i % 3 and i % 5): x+=i
    return x

problem1()









