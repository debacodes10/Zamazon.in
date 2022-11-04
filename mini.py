import pickle
bill=100
discam = 0
coup = open("D://Zamazon.in/coupon.dat", "rb")
coupch = input("Do you want to enter a coupon code? ")
coupbuff = pickle.load(coup)
if coupch == "Y" or coupch == "y":
    coupinp=input("Enter coupon code: ")
    coupinp = coupinp.lower()
    try:
        for i in range (0,5):
            if coupinp==coupbuff[i]:
                disc = int(coupinp[len(coupinp)-2:])
                discam = ((disc/100)*bill)
                print(discam)
                bill = bill-discam
                break
            else:
                discam = 0
                bill = bill
    except EOFError:
            print("That is not a valid coupon code.")
print(bill)

