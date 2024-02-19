str = int(input("Enter initial value: "))
last = int(input("Enter last value: "))
for i in range(str,last+1):
    if(i>1):
        for num in range(2,i):
            if(i%num==0):
                break
        else:
            print(i)