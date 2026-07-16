try:
    company = input("enter the comapany name which you want to buy\n1.OPPO\n2.Motorola\n3.Samsung\n:")
    if company.lower() =="oppo":
        print("Ok,I am showing you best model phone of oppo")
    elif company.lower() =="motorola"    :
        print("Ok,I am showing you best model phone of Motorola")
    elif company.lower() =="samsung":
        print("Ok,I am showing you best model phone of samsung")
except:
    print("please select the right company name you want")        
try:
    budget = int(input("enter your budget\n:"))
    if budget<=10000:
        print("Sorry Sir,there is no model below than 10000")
    elif budget>=10000:
        print("Showing you best model sir")        
except:
    print("please the right integer(numberic value)")