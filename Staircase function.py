def staircase(n):
    k=n-1
    for i in range(n):
        for i in range(k):
            print(" ",end="")
        k-=1
        for i in range(n-k-1):
            print("#",end="")
        print()
n=int(input("enter the height of staircase:"))
staircase(n)
