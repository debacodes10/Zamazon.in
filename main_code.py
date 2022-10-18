import pickle
import random

def login(c=0, t=0):            #if account action = login
    f= open("D:\\Zamazon.in\credentials.dat","rb")   #binary file storing account credentials
    id= input("enter id no:")               #store id no = id
    password= input("enter password:")      #store password = password
    creds = [id, password]
    while True:
        try:
            check = pickle.load(f)          #load binary file - check
            if creds[0] == check[0]:
                for i in range(0,2):
                    if creds[1] == check[1]:
                        print("Login Successful.")
                        t=0
                        break
                    else:
                        password = input("Password Wrong. Re-enter password: ")
                        creds = [id,password]
                        c=c+1
                if c==2:
                    print("You have reached maximum tries. Try again later.")
                    t = 1
                return t
                break
        except EOFError:
            print("Accound does not exist.")
            break
        
def signup():           #if account = signup
    f = open("D:\\Zamazon.in\credentials.dat","ab")     #binary file storing account credentials
    id = input("enter id no:")                 #id for new account = id
    password= input("enter password:")         #password for new account - password
    name = input("Enter name:")                #name for new account - name
    creds = [id,password,name]
    pickle.dump(creds,f)                       #push account details to binary file 
    print("Account creation done. You are Successfully Logged In.")
    
def add_to_cart(bill=0):      #add products to be delivered
    while True:
        itemname = input("Enter name of item you want: ")   #name of item variable - itemname
        stocklist = open("D:\\Zamazon.in\stocks.dat","rb")  #open binary file containing stock
        while True:
            try:
                item = pickle.load(stocklist)               #load item lists
                if item[0] == itemname:
                    quan = int(input("Enter number of items: "))    #quantity of item = quan
                    if int(item[1]) >= quan:
                        bill = bill + (quan*item[2])                #create bill amount
            except EOFError:
                break
        cont = input("Do you want to enter another item?(Y/N): ")   #enter more items
        if cont != "Y" and cont != "y":
            return bill
            break
    
def pincode():          #check if pincode deliverable
    pin = int(input("enter pin:"))      #pin for addresss delivery - pin
    while True:
        a= pin//100000                   #checking procedure for pin availability
        if a==7:                       #checking procedure for pin availability
            print("Proceed to enter complete address:")
            break
        else:
            print("Order will not be placed")
            print("We only deliver items in West Bengal.")   
            options= int(input("Enter 1.Re-enter the PIN  2.Exit"))     #choice for pin re-enter/exit - options
            if options==1:
                pin= int(input("Enter pin:"))                           #re-enter pin 
            else:
                break
    
def address_check(t=0):    #check if address is deliverable
    delivname = input("Enter name of recipient: ")      #name of recipient - delivname
    addressinp= input("enter address:")                 #variable for storing address of user - addressinp
    addcheck= open("D:\\Zamazon.in\\addbook.dat","rb")      #binary file containing deliverable address - addcheck
    while True:
        try:
            ncheck = pickle.load(addcheck)              #load address from binary file - ncheck
            if addressinp==ncheck[0]:
                print("Delivery possible within ", (random.randint(2,10)), " days!")
            elif addressinp!=ncheck[0]:
                print("We dont deliver to this address yet.")
        except EOFError:
            break
    print("Mobile NO:",mobileno)
    print("Address:",addressinp)
    retlist = list()                                    #list to return value
    retlist = [delivname,addressinp]
    return retlist
    
def coupon_apply(bill,coupret=""):     #check coupon apply, discount and bill
    coupchoice = input("Do you want to enter a coupon code?(Y/N): ")    #choice for entering coupon - coupchoice
    if coupchoice == "Y" or coupchoice == "y":
        coupinp = input("Enter coupon code: ")                          #user enters coupon code in - coupinp
        coupinp = coupinp.upper()                                       #convert coupon code to capitals
        coupon = open("D://Zamazon.in/coupon.dat", "rb")                #open binary file containing coupon codes
        while True:
            try: 
                coupret=pickle.load(coupon)
                if coupinp==coupret[0]:
                    disc = int(coupinp[len(coupinp)-2:])
                    discam = (disc*bill)                                            #calculate discount amount
                    bill = bill-discam                                              #calculate complete bill
                else: 
                    coupinp = "None"
                    discam = 0
                    bill = bill
            except EOFError:
                print("That is not a valid coupon code.")
                break
    else:
        coupinp = "No coupon code applied"                              #no coupon code applied
        discam = 0                                                      #no discount received
        bill = bill                                                     #bill remains original amount
    retlist = [coupinp,discam,bill]
    return retlist
    
def payment_method():   #select payment method
    print("1. Cash on Delivery")
    print("2.Pay Online")
    paychoice = int(input("Enter payment method choice - 1 or 2: "))    #enter choice of payment mode
    return paychoice
   
def transaction(paychoice): #ensure successful transaction 
    print("Proceed to transaction:")
    transid = random.randint(0,1000000000)      #transaction ID = transid
    print(" ")
    if paychoice == 1:                          #if payment method is Cash on Delivery
        print("Transaction successful.")
    elif paychoice == 2:                        #if payment method is Online Payment
        while True:
            trans= random.randint(0,10)             #generate random number for transaction success verification
            if trans>3.5:                           #check random number for transaction success verification
                print("Transaction successful")
                print("Order has been placed.")
                break
            else:
                print("Transaction not successfull.")
    return transid
    
def deliv_fees(bill):       #delivery fees applicable
    if bill<500:
        delfee = 100
    elif bill>=500 and bill<=1000:
        delfee = 50
    elif bill>1000:
        delfee = 0
    return delfee
    
    
#declare variables start
creds = list()                              #list to store account credentials - creds
c=0                                         #counter for checking no. of wrong attempts - c
#declare variables end

#enter into user's account start
mobileno= int(input("Enter Mobile No : "))     #mobile number variable - mobileno
account= str(input("Login or sign up : "))     #choice for login or sign up - account
account= account.lower() 
#enter into user's account end                     

print("Welcome to Zamazon.in!",)
print("We wish you a wonderful shopping experience with us!")

#if account = login
if account=="login":
    exit = login()
#end account = login

#if account = signup
elif account=="signup":
    signup()
#end account = signup

#add to cart items
if exit==0:
    bill = add_to_cart()
#add to cart ends

#check if pin deliverable
if exit==0:
    pincode()
#end pin deliverable

#start address check for delivery 
if exit == 0:
    delivname_add = address_check()
#end address check for delivery

#coupon code start
if exit==0:
    cou_dis_bil = coupon_apply(bill)
#coupn code end

#payment method start
if exit==0:
    paychoice = payment_method()
#payment method end

#delivery feess start
if exit==0:
    delivery_fee = deliv_fees(bill)
#delivery fee end

#start transaction procedure
if exit==0:
    transid = transaction(paychoice)
#end transaction procedure

#display bill start
if exit==0:
    print(" ")
    print("BILL DETAILS:")
    print("Name of recipient: ", delivname_add[0])      #print name of receiver
    print("Contact number: ", mobileno)                 #print mobile number
    print("Address: ", delivname_add[1])                #print address
    print("Bill amount: ", cou_dis_bil[2])              #print bill
    print("Delivery Fees: ", delivery_fee)              #delivery fees
    print("Total Bill: ", cou_dis_bil[2]+delivery_fee)  #print total bill
    print("Transaction ID: ", transid)                  #print transaction ID
    print("Coupon code applied: ", cou_dis_bil[0])      #print coupon code
    print("You have saved: ", cou_dis_bil[1])           #print discount amount
    print("ORDER SUCCESSFULLY PLACED!")
#display bill end