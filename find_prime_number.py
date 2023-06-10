a = 1
b = 10
for x in range(a, b+1):
    if x > 1:
        for y in range(2,x):
            if x % y == 0:
                print("Not Prime",x)
                break
        else:
            print("prime",x)