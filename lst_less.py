ch=input("Enter string of Integers seperated by space ")
lst=ch.split()
visited=[]
for i in range(0,len(lst)):
    lst[i]=int(lst[i])
num=int(input("Enter a number"))
for i in range(0,len(lst)):
    if lst[i]<num:
        visited.append(lst[i])
print(visited)