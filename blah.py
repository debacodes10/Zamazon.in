def add_to_cart():
  prod_details = {"grocery":[["detergent", 50],["milk powder", 20],["toothpaste",60],["shampoo",150],["noodles",120]], 
  "electronics":[["fridge",30000],["micro oven",10000],["induction",5000],["television",30000],["geyser",20000],["air conditioner",50000]], 
  "beauty":[["foundation",500],["mascara",1200],["nail polish",800],["face powder",300],["primer", 400]],
  "furniture":[["double bed", 35000],["sofa",22000],["bean bag", 2500],["bookshelf",8000],["shoe rack",5000]],
  "clothing":[["shirt", 2000],["trousers", 2500],["hoodie", 1500],["shoes", 3000],["saree", 8000]]}
  bill = 0

  print("Categories: ")
  for i in prod_details:
    print(i)

  cat_choice = input("Enter category you want to explore: ")

  while True:
    for i in prod_details:
      if cat_choice==i:
        print(prod_details[cat_choice][0][0])
        print(prod_details[cat_choice][1][0])
        print(prod_details[cat_choice][2][0])
        print(prod_details[cat_choice][3][0])
        print(prod_details[cat_choice][4][0])

    prodch = input("Enter product you want to purchase: ")
    while True:
      if prodch == prod_details[cat_choice][0][0]:
        quan = int(input("Enter number of items you want: "))
        bill = bill + (prod_details[cat_choice][0][1]*quan)
      elif prodch == prod_details[cat_choice][1][0]:
        quan = int(input("Enter number of items you want: "))
        bill = bill + (prod_details[cat_choice][1][1]*quan)
      elif prodch == prod_details[cat_choice][2][0]:
        quan = int(input("Enter number of items you want: "))
        bill = bill + (prod_details[cat_choice][2][1]*quan)
      elif prodch == prod_details[cat_choice][3][0]:
        quan = int(input("Enter number of items you want: "))
        bill = bill + (prod_details[cat_choice][3][1]*quan)
      elif prodch == prod_details[cat_choice][4][0]:
        quan = int(input("Enter number of items you want: "))
        bill = bill + (prod_details[cat_choice][4][1]*quan)
      options = int(input("1. Enter another item. 2. Exit: "))
      if options==2:
        return bill
      else:
          cat_choice = input("Enter category: ")
          break

print(add_to_cart())