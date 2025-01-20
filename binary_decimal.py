print("Welcome to the program")
ch='y'
while(ch=='y'):
    bin=input("Enter a Binary Sequence: ")
    bin_len=len(bin)
    dec=0
    op=0
    for i in bin:
        if (bin_len>=0):
            if (i=='1'):
                op=2**(bin_len-1)
                dec += op
        bin_len-=1
    print("The Decimnal Value is:",dec)
    ch=input("Do you want to continue?[y/n]: ")
