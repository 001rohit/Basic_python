# sum of Odd number in list

lst = [1,12,13,14,5,16,7,18,9,20]
new_lst=[]
for i in lst:
    if(i%2!=0):
      new_lst.append(i)

print(new_lst)

s2=0
for i in new_lst:
    s2+=i

print(s2)