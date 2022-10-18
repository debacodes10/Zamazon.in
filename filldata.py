import pickle
f=open("D:\\Zamazon.in\\addbook.dat", "wb")
dp = list()
for i in range(0,5):
    add=input("Enter address: ")
    dp = [add]
    pickle.dump(dp,f)