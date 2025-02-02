ch=input("Enter string of Integers seperated by space ")
lst=ch.split()
large_counter=0
visited=[]
for i in range(0,len(lst)):
    lst[i]=int(lst[i])
lst=sorted(lst,reverse=True)
print("Entered list sorted in descending order:",lst)
for i in range(0,len(lst)):
    if lst[i] in visited:
        continue
    else:
        visited.append(lst[i])
        large_counter+=1
    if large_counter==3:
        print("3rd largest number is",visited[large_counter-1])
        break
print("Exiting program")