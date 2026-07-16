print("Welcome to Kaun Banega Crorepati\nThere are total 5 question and you have to answer all question correctly  ")
Name = input("Enter your Name: ")
print("So let get started",Name)
print("*******YOU HAVE TO ANSWER QUESTION IN NUMBER********")


#first question
firstqna = int(input("What is the capital of India?\n1.Uttar Pradesh\n2.Delhi\n3.Maharastra\n:"))
if firstqna == 1:
    print("Wrong")
    a=0 
elif firstqna == 2:
    print("Right\nYou Got 1 Point")    
    a =1
else:
    print("Wrong")
    a=0

#second question    
secondqna = int(input("which city is called pink city\n1.Mumbai\n2.Jaipur\n3.Delhi\n:"))    
if secondqna == 1:
    print("Wrong")
    b=0
elif secondqna ==2:
    print("Right \n You got 1 point")    
    b = a+1
else:
    print("wrong")    
    b=0

#third question
thirdqna = int(input("Which planet is Closet to Sun\n1.Venus\n2.Earth\n3.Neptune\n4.Mercury\n:"))  
if thirdqna ==1:
    print("Wrong\nYou got Zero point")
    c = b+0
elif thirdqna ==2:
    print("Wrong\nYou got zero point")    
    c =b+0
elif thirdqna == 3:
    print("Wrong\nYou got zero point")
    c = b+0
elif thirdqna==4:
    print("Right\nYou got 1 point")    
    c = b+1

#fourth question
fourthquestion  = int(input("Which River is found in Varansi\n1.Krishna\n2.Gomti\n3.Ganga\n4.Kaveri\n:"))
if fourthquestion==1:
    print("Wrong")
    d = c+0
elif fourthquestion==2:
    print("Wrong")
    d=c+0
elif fourthquestion ==3:
    print("Right \nYou got 1 point")
    d =c+1
elif fourthquestion==4:
    print("wrong")
    d = c+0

#fifth question 
fifthquestion = int(input("What is National Fruit of India\n1.Mango\n2.Banana\n3.Apple\n4.Graphes\n:"))
if fifthquestion ==1:
    print("Right\nYou Got 1 point")
    e = d+1
elif fifthquestion== 2:
    print("Wrong")
    e = d+0
elif fifthquestion ==3:
    print("Wrong")
    e =d+ 0
elif fifthquestion == 4:
    print("worng")    
    e = d+0


totalpoint =("you get total",e,"points")
print(totalpoint)


points = e # Initialize points to a numerical value

# Construct the message string using f-strings for cleaner formatting
total_message = f"You get {points} points"
print(total_message)

if points == 0:
    print("Sorry,You got 0 rupees")
elif 1 <= points <= 2:
    print("Congrats,You got ₹500")
elif 3 <= points <= 4:
    print("Congrats,You got ₹1000")
elif points == 5:
    print("Congrats,You got ₹2000")
