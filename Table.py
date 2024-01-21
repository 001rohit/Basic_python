# print the table and Take input any number 

num = int(input("Enter any number to print table: "))
a=1
while(a<=10):
       print(a,"*",num,"=",a*num)
       a+=1

lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    print(i,"*",num,"=",i*num)
