" recursin in python"
"factorial"

def factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))
inp = int(input("enter no for factorial :"))
print("the factorial f", inp, "is", factorial(inp))