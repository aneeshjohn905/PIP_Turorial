ch=input("Enter string of Integers seperated by space ")
lst=ch.split()
for i in range(0,len(lst)):
    lst[i]=int(lst[i])
print("Minimum Element",min(lst))
print("Maximum Element",max(lst))