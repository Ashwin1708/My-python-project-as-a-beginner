choice = input("which festival is close in following reason \nkite \nholi \ndiwali \n :")
if choice.lower() =="kite":
    print("happy kite day 'sir")
    choice=(int(input("how many kite you want to order sir\n:")))
    if choice >=1:
        print("order")
    else:
        print("error")    
elif choice.lower() == "holi":
    print("happy Holi Sir")
    b = input("do you want pichkari \n YES \n NO \n :")
    if b.lower=="yes":
        print("order")
    else:
        print("ok sir")    
elif choice.lower() == "diwali":
    print("happy diwali papa")
    c =input("Do you want cracker \n Yes \n No\n:")
    if c.lower=="yes":
        print("ok, sir ")
        cracker =int(input("how much cracker do you want sir \n 1 \n 2 \n 3  :"))
        if cracker ==1:
            print("order sir")
        elif cracker==2:
            print("order sir")    
        else:
            print("order sir")    
    else:
        print("thank you sir \n cracker pollute our environment")        
else:
    print("invaild statement \n please select the right festival in given condition")            