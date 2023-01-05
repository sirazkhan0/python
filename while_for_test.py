"table"
# num = int(input("enter the number  "))
# for i in range(1,11):
#     # print(str(num) + "x" + str(i) + "=" + str(i*num))

#      print(f"{num}x{i}={num*i}")







# li=["siraz","rahul","sohan","mukesh"]

# for name in li:
#     if name.startswith("s"):
#         print("hello   "  + name)







"prime number"

# num = int(input("enter the number: "))
# prime = True
# for i in range(2,num):
#     if (num%i == 0 ):
#         prime = False
#         break
# if prime:
#     print("this number is prime")
# else:
#     print("this number is not prime")        








# n! = 1 x 2 x 3 x ....... x n
# 5! = 1 x 2 x 3 x 4 x 5
# "factorial no"
# num = int(input("enter the number: "))
# factorial = 1
# for i in range (1,num+1):
#     factorial = factorial * i
# print(f"the factorial of {num} is {factorial}")    




"star pattern"

# n = 4
# for i in range (4):
#     print("*"*(i+1))





n=3
for i in range(3):
    print(" " *(n-i-1), end="")
    print("*" *(2*i+1), end="")
    print(" " *(n-i-1))

