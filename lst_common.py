n_lst=[]
ch1=input("Enter 1st string of Integers seperated by space ")
lst1=ch1.split()
for i in range(0,len(lst1)):
    lst1[i]=int(lst1[i])
print(lst1)
ch2=input("Enter 2nd string of Integers seperated by space ")
lst2=ch2.split()
for i in range(0,len(lst2)):
    lst2[i]=int(lst2[i])
print(lst2)
for i in range(0,len(lst1)):
    if lst1[i] in lst2:
        n_lst.append(lst1[i]);
print(n_lst)