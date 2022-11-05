import pickle
import pyttsx3

def tts(text):
    engine = pyttsx3.init()
    say_var = text
    engine.say(say_var)
    engine.runAndWait()

def coupon_apply(bill=1000,coupret=""):     #check coupon apply, discount and bill
    tts("Do you want to enter a coupon code?")
    coupch = input("Do you want to enter a coupon code?(Y/N) : ")
    if coupch == "Y" or coupch == "y":
        coupon = open("D://Zamazon.in/coupon.dat", "rb")                #open binary file containing coupon codes
        print("List of available coupon codes: ")
        tts("List of available coupon codes.")
        while True:
            try: 
                coupret = pickle.load(coupon)
                print(coupret[0])
            except EOFError:
                break
        coupon.close()
        
        coupon = open("D://Zamazon.in/coupon.dat", "rb")
        coupinp = input("Enter coupon code: ")
        while True:
            try:
                coupret = pickle.load(coupon)
                if coupinp == coupret[0]:
                    disc = int(coupinp[len(coupinp)-2:])
                    discam = ((disc/100)*bill)
                    bill = bill-discam
                    print("You have saved",discam)
                    retlist = [coupinp,discam,bill]
                    return retlist
            except EOFError:
                break
    else:
        retlist = ["None", 0, bill]
        return retlist

fuck = coupon_apply()
print(fuck)