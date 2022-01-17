def discountCalculator(type,price,brand=None):
    if type=="Mobile":
        if brand=="Apple":
            total_price=price-(price*10/100)
            print(total_price)
        else:
            total_price=price-(price*5/100)
            print(total_price)
    if type=="Shoe":
        total_price=price+(price*2/100)
        print(total_price)

discountCalculator("Mobile",100,"Apple")
discountCalculator("Mobile",100)
discountCalculator("Shoe",100)