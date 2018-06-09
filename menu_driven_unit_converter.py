import sys
def bin_to_dec():
    print("Decimal Is:",int(usr_input(),2))

def dec_to_hex():
    print("Hex Is :",hex(int(usr_input())))

def dec_to_octal():
    print("Octal Is:",oct(int(usr_input())))

def usr_input():
    usr_in=input("Enter Number:")
    return usr_in

print("""Enter: 
    1)Binary To Decimal
    2)Decimal To Hex
    3)Decimal To Octal
    4)Any Key To Exit\n""")

choice=int(input("Enter Choice:"))

if choice==1:
    bin_to_dec()
elif choice==2:
    dec_to_hex()
elif choice==3:
    dec_to_octal()
else:
    sys.exit()
