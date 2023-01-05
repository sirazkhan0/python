# num1 = int( input("enter no 1:"))
# num2 = int( input("enter no 2:"))
# num3 = int( input("enter no 3:"))
# num4 = int( input("enter no 4:"))

# if(num1>num4):
#     f1 = num1
# else:
#     f1 = num4


# if(num2>num3):
#     f2 = num2
# else:
#     f2 = num3

# if(f1>f2):
#     print(str(f1) + "  is greatest")
# else:
#      print(str(f2 ) + "  is greatest")    










# sub1 = int(input("enter first subject marks\n"))
# sub2 = int(input("enter second subject marks\n"))
# sub3 = int(input("enter third subject marks\n"))

# if(sub1<33 or sub2<33 or sub3<33):
#     print("you are fail because you have less than 33% in one of the subject")

# elif(sub1+sub3+sub2)/3 <40:
#     print("you are fail due t total percentage less than 40")
# else:
#     print("congutulations! you passed the exam")        









# text = input("enter the text   ")
# spam = False

# if("make a lot f money" in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# elif("subscribe this" in text):
#     spam = True
# else:
#     spam = False        

# if(spam):
#     print("this text is spam")
# else:
#     print("this text is not spam")   







# names = ["hello","hi","bye","tata"]
# name = input("enter the name to check\n")

# if name in names:
#     print("your name is present in the list ")
# else:
#     print("your name is not present in the list ")








marks = int(input("enter your marks\n"))

if marks>90:
    grade = "ex"
elif marks>=80:
    grade = "a"  
elif marks>=70:
    grade = "b"     
elif marks>=60:
    grade = "c"     
elif marks>=50:
    grade = "d"

else:
     grade = "f"  

print("your grade is  " + grade)
