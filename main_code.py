import time
import random
import pickle
import pyttsx3

def tts(text):
    engine = pyttsx3.init()
    say_var = text
    engine.say(say_var)
    engine.runAndWait()

def login(c=0, t=0):            #if account action = login
    f= open("D:\\Zamazon.in\credentials.dat","rb")   #binary file storing account credentials
    tts("Please enter your UserID: ")
    id= input("Please enter your UserID: ")               #store id no = id
    tts("Please enter your password: ")
    password= input("Please enter your password: ")      #store password = password
    print(" ")
    creds = [id, password]
    while True:
        try:
            check = pickle.load(f)          #load binary file - check
            if creds[0] == check[0]:
                for i in range(0,2):
                    if creds[1] == check[1]:
                        print("Login Successful!")
                        tts("Login successful!")
                        t=0
                        break
                    else:
                        tts("Password Wrong. Re-enter password: ")
                        password = input("Password Wrong. Re-enter password: ")                        
                        creds = [id,password]
                        c=c+1
                if c==2:
                    print("You have reached maximum tries. Try again later.")
                    tts("You have reached maximum tries. Try again later.")
                    t = 1
                return t
                break
        except EOFError:
            print("Accound does not exist.")
            tts("Accound does not exist.")
            break
        
def signup():           #if account = signup
    f = open("D:\\Zamazon.in\credentials.dat","ab")     #binary file storing account credentials
    tts("Please enter an acceptable UserID: ")
    id = input("Please enter an acceptable UserID: ")                 #id for new account = id
    tts("Create a new password: ")
    password= input("Create a new password: ")         #password for new account - password
    tts("Please enter your name: ")
    name = input("Please enter your name: ")                #name for new account - name
    creds = [id,password,name]
    pickle.dump(creds,f)                       #push account details to binary file 
    print("Account creation done. You are Successfully Logged In.")
    tts("Account creation done. You are Successfully Logged In.")
    
def add_to_cart(bill=0):      #add products to be delivered
    tts("Enter name of items you want one by one: ")
    while True:
        itemname = input("Enter name of items you want one by one: ")   #name of item variable - itemname
        stocklist = open("D:\\Zamazon.in\stocks.dat","rb")  #open binary file containing stock
        while True:
            try:
                item = pickle.load(stocklist)               #load item lists
                if item[0] == itemname:
                    quan = int(input("Enter number of items: "))    #quantity of item = quan
                    print(" ")
                    if int(item[1]) >= quan:
                        bill = bill + (quan*item[2])                #create bill amount
            except EOFError:
                break
        tts("Do you want to enter another item?: ")
        cont = input("Do you want to enter another item?(Y/N): ")   #enter more items
        print(" ")
        if cont != "Y" and cont != "y":
            return bill
            break
    
def pincode():          #check if pincode deliverable
    tts("Please enter your pincode: ")
    pin = int(input("Please enter your pincode: "))      #pin for addresss delivery - pin
    print(" ")
    while True:
        a= pin//100000                   #checking procedure for pin availability
        if a==7:                       #checking procedure for pin availability
            print("Proceed to enter complete address:")
            tts("Proceed to enter complete address:")
            return 0
        else:
            print("Order will not be placed")
            tts("Order will not be placed")
            print("We only deliver items in West Bengal.") 
            tts("We only deliver items in West Bengal.")
            tts("Enter 1.Re-enter the PIN  2.Exit : ")
            options= int(input("Enter 1.Re-enter the PIN  2.Exit : "))     #choice for pin re-enter/exit - options
            if options==1:
                tts("Please re-enter your pincode:")
                pin= int(input("Please re-enter your pincode:"))                           #re-enter pin 
            else:
                return 1
    
def address_check(u=0):    #check if address is deliverable
    print(" ")
    tts("Please enter name of recipient: ")
    delivname = input("Please enter name of recipient: ")      #name of recipient - delivname
    tts("Please enter complete address: ")
    addressinp= input("Please enter complete address: ")                 #variable for storing address of user - addressinp
    print(" ")
    addressinp=addressinp.upper()
    addcheck= open("D:\\Zamazon.in\\addbook.dat","rb")      #binary file containing deliverable address - addcheck
    retlist = list()
    while True:
        try:
            ncheck = pickle.load(addcheck)              #load address from binary file - ncheck
            for i in range(0,2):
                if addressinp==ncheck[0]:
                    r=random.randint(2,10)
                    r=str(r)
                    disp = str("Delivery possible within "+r+" days!")
                    print(disp)
                    tts(disp)
                    print(" ")
                    print("Mobile NO:",mobileno)
                    tts("Mobile number:"+str(mobileno))
                    print("Address:",addressinp)
                    tts("Address:"+str(addressinp))
                    print(" ")
                    retlist = [delivname,addressinp,0]
                    return retlist 
                elif addressinp!=ncheck[0]:
                    print("We dont deliver to this address yet.")
                    tts("We dont deliver to this address yet.")
                    tts("Press 1 to re enter complete address and 2 to exit. ")
                    options = input("1. Re-enter complete address. 2. Exit. :")
            if options==1:
                tts("Please re-enter your address: ")
                addressinp=input("Please re-enter your address: ")
            else:                                   
                retlist = [0,0,1]
                return retlist                       
            if i == 2:
                print("You have reached maximum tries. Try again later.")
                tts("You have reached maximum tries. Try again later.")
                u=1
                break
        except EOFError:
            break
    
def coupon_apply(bill,coupret=""):     #check coupon apply, discount and bill
    tts("Do you want to enter a coupon code?(Y/N): ")
    coupchoice = input("Do you want to enter a coupon code?(Y/N): ")    #choice for entering coupon - coupchoice
    print(" ")
    if coupchoice == "Y" or coupchoice == "y":
        tts("Enter coupon code: ")
        coupinp = input("Enter coupon code: ")                          #user enters coupon code in - coupinp
        print(" ")
        coupinp = coupinp.lower()                                       #convert coupon code to capitals
        coupon = open("D://Zamazon.in/coupon.dat", "rb")                #open binary file containing coupon codes
        coupret=pickle.load(coupon)
    try:
        for i in range(0,5):
            if coupinp==coupret[i]:
                disc = int(coupinp[len(coupinp)-2:])
                discam = ((disc/100)*bill)
                print(discam)
                bill = bill-discam
                retlist = [coupinp,discam,bill]
                return retlist
            else: 
                discam = 0
                bill = bill
    except EOFError:
        print("That is not a valid coupon code.")
        tts("That is not a valid coupon code.")
        print(" ")
    else:                              #no coupon code applied
        discam = 0                                                      #no discount received
        bill = bill                                                     #bill remains original amount'''
    retlist = [coupinp,discam,bill]
    return retlist
    
def payment_method():   #select payment method
    print("Please select your payment method: ")
    tts("Please select your payment method: ")
    print(" ")
    print("1. Cash on Delivery")
    print("2.Pay Online")
    print(" ")
    tts("Enter payment method choice - 1 or 2: ")
    paychoice = int(input("Enter payment method choice - 1 or 2: "))    #enter choice of payment mode
    print(" ")
    return paychoice
   
def transaction(paychoice): #ensure successful transaction 
    print("Processing transaction...")
    tts("Processing transaction...")
    transid = random.randint(0,1000000000)      #transaction ID = transid
    print(" ")
    if paychoice == 1:                          #if payment method is Cash on Delivery
        print("Transaction successful.")
        tts("Transaction successful.")
    elif paychoice == 2:                        #if payment method is Online Payment
        while True:
            time.sleep(3)
            trans= random.randint(0,10)             #generate random number for transaction success verification
            if trans>3.5:                           #check random number for transaction success verification
                print("Transaction successful")
                tts("Transaction successful")
                print(" ")
                print("Order has been placed.")
                tts("Order has been placed.")
                break
            else:
                print("Transaction not successfull.")
                tts("Transaction not successfull.")
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
t=0
u=0
delivname_add = [0,0,1,1]
#declare variables end

#enter into user's account start
print("Welcome to Zamazon.in!")
tts("Welcome to Zamazon.in!")
print("We wish you a wonderful shopping experience with us!")
tts("We wish you a wonderful shopping experience with us!")
print("Please login to your account for an even better experience!")
tts("Please login to your account for an even better experience!")
print(" ")
tts("Please enter your mobile number : ")
mobileno= int(input("Please enter your mobile number : +91 "))     #mobile number variable - mobileno
tts("Do you wish to login or sign up? : ")
account= str(input("Do you wish to login or sign up? : "))     #choice for login or sign up - account

print(" ")
account= account.lower() 
#enter into user's account end                     

#if account = login
if account=="login":
    exit = login()
    print(" ")
#end account = login

#if account = signup
elif account=="signup" or account=="sign up":
    signup()
    exit=0
#end account = signup

#add to cart items
if exit==0:
    print("Please add the items you want to order to your cart.")
    tts("Please add the items you want to order to your cart.")
    print(" ")
    bill = add_to_cart()
#add to cart ends

#check if pin deliverable
if exit==0:
    pp = pincode()
#end pin deliverable

#start address check for delivery 
if exit == 0 and pp==0:
    delivname_add = address_check()
#end address check for delivery

#coupon code start
if exit==0 and delivname_add[2]==0 and pp==0:
    cou_dis_bil = coupon_apply(bill)
#coupn code end

#payment method start
if exit==0 and delivname_add[2]==0 and pp==0:
    paychoice = payment_method()
#payment method end

#delivery feess start
if exit==0 and delivname_add[2]==0 and pp==0:
    delivery_fee = deliv_fees(bill)
#delivery fee end

#start transaction procedure
if exit==0 and delivname_add[2]==0 and pp==0:
    transid = transaction(paychoice)
#end transaction procedure

#display bill start
if exit==0 and delivname_add[2]==0 and pp==0:
    print(" ")
    print("BILL DETAILS:")
    tts("BILL DETAILS:")
    print(" ")
    print("Name of recipient: ", delivname_add[0])      #print name of receiver
    print("Contact number: ", mobileno)                 #print mobile number
    print("Address: ", delivname_add[1])                #print address
    print("Bill amount: ", cou_dis_bil[2])              #print bill
    print("Delivery Fees: ", delivery_fee)              #delivery fees
    print("Total Bill: ", cou_dis_bil[2]+delivery_fee)  #print total bill 
    if (cou_dis_bil[2]+delivery_fee)>500 and (cou_dis_bil[2]+delivery_fee)<1000:
        print("(Add items worth Rs", (1000-(cou_dis_bil[2]+delivery_fee)), " to avail free delivery!)")
    elif (cou_dis_bil[2]+delivery_fee)<500:
        print("(Add items worth Rs", (500-(cou_dis_bil[2]+delivery_fee)), "to avail delivery at Rs 50!)")
        print("(Add items worth Rs", (1000-(cou_dis_bil[2]+delivery_fee)), "to avail free delivery!)")
    print("Transaction ID: ", transid)                  #print transaction ID
    print("Coupon code applied: ", cou_dis_bil[0])      #print coupon code
    print("You have saved: ", cou_dis_bil[1])           #print discount amount
    print("ORDER SUCCESSFULLY PLACED!")
#display bill end