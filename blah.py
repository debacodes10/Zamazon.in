import pickle
f=open("D://Zamazon.in/coupon.dat", "rb")
while True:
    try:
        c=pickle.load(f)
        print(c[0])
    except EOFError:
        print("end of file.")
        break