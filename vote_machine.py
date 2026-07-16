
citizen =input("are you citizen of India: ")
if citizen.lower() =="yes":
    print("ok,You can vote: ")
    voter_id = input("do you have voter id: ")
    if voter_id.lower() == "yes":
        print("Ok you can vote")
        age =int(input("enter your age: "))
        if age >=18:
            print("you can vote")
            parties = input("Please choose your voting party\nTOM\nJERRY\n:")
            if parties.lower() == "tom":
                print("your vote is given to TOM")
            elif parties.lower() =="jerry":
                print("your vote is given jerry")
            else:
                print("invalid statement")
        elif age <18:
            print("sorry,below 18 are not allowed to vote")        
    else:
        print("sorry without voter id you cannot vote")
else:
    print("sorry,Only Indian citizen are allow to vote")