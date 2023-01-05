myDict = {
    "pankha":"fan",
    "dil":"heart",
    "bola":"speak",
    "kya haal h": "how r u",
    "tujhe":"you"
}

print("option are ",myDict.keys())
a = input("enter the hindi world\n")
# print("The meaning of your world is:", myDict[a])  
#get keyword error

print("the meaning of your word is:", myDict.get(a))
#get none not get keyword error  



num1 = int(input("enter number 1\n"))
num2 = int(input("enter number 2\n"))
num3 = int(input("enter number 3\n"))
num4 = int(input("enter number 4\n"))
num5 = int(input("enter number 5\n"))
num6 = int(input("enter number 6\n"))

m = {num1,num2,num3,num4,num5,num6}
print(m)