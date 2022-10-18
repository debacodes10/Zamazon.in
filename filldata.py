import pickle
f=open("D:\\Zamazon.in\\coupon.dat", "wb")
dp = list()
for i in range(0,5):
    add=input("Enter coupon: ")
    dp = [add]
    pickle.dump(dp,f)