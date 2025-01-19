
def encrypt():
    sent=input("Enter a Message to Encrypt: ")
    key=int(input("Enter code:"))
    msg=''
    for char in sent:
        if char==' ':
            msg+=' '
            continue
        ord_no=ord(char)
        cipher_add=ord_no+key
        if (cipher_add>ord('z')):
            diff=cipher_add-ord('z')
            cipher_add=ord('a')+diff-1
        msg+=chr(cipher_add)
    print("Encrypted Message:",msg)

def decrypt():
    code=input("Enter a Message to Decrypt: ")
    key=int(input("Enter code:"))
    msg=''
    for char in code:
        if char==' ':
            msg+=' '
            continue
        ord_no=ord(char)
        cipher_sub=ord_no-key
        if (cipher_sub<ord('a')):
            diff=ord('a')-cipher_sub
            cipher_sub=ord('z')-diff+1
        msg+=chr(cipher_sub)
    print("Decrypted Message:",msg)

print("Welcome to Encryptor/Decryptor")
ch='y'
while(ch=='y'):
    op=int(input("Choose Operation: \n[1]Encrypt\n[2]Decrypt\n[3]Exit\n\t"))
    if op==1:
        encrypt()
    elif op==2:
        decrypt()
    elif op==3:
        ch='n'
