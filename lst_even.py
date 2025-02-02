ch=input("Enter string of Integers seperated by space ")
lst=ch.split()
visited=[]
for i in range(0,len(lst)):
    lst[i]=int(lst[i])
print("Entered List",lst)
for i in range(0,len(lst)):
    if lst[i]%2==0:
        visited.append(lst[i])
visited=sorted(visited)
print("Even List",visited)