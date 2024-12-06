def myfunction(n):
    if n==5:
        print("Thank you")
        return 
    print(n)
    myfunction(n+1)

myfunction(1)