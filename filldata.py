import pickle
f=open("D:\\Zamazon.in\\stocks.dat", "wb")
l1 = list()
for i in range(0,2):
    l2=list()
    add = input("Enter category: ")
    for k in range(0,3):
        l3=list()
        add2 = input("Enter product: ")
        p = int(input("Enter price: "))
        l3.append([add2,p])
    l2.append(l3)
    l1.append([add,l2])
    pickle.dump(l1,f)