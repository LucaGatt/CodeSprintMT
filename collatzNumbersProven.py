from math import log2
numbersProven = pow(10,18)+393272845 # 330573472 # 296384925 # 210885780 # 79787091 - all these numbers have been run iteratively
def collatzDec(x):
    if (x <= numbersProven): return 1 # end of sequence
    elif (x%2==0):
        if (log2(x).is_integer): return 1 # end of sequence
        else: return int(x/2)
    else: return int((x*3+1) /2) # /2 variant
def collatz(x):
    while x != 1:
        # print(x)
        x=collatzDec(x)
    return True

''' # to enter specific number:
x= int(input("Enter number: "))
result = collatz(x)
'''

# run numbers through collatz conjecture
# Notice that even numbers are not run since the even number /2 would be proven already
for x in range(numbersProven+1,200000000000000000001,2):
    if (x%11111) == 0 : print(str(x) + " leads to 1")
    elif not collatz(x): print(str(x)+ " is a counterexample")
    # else: print("error")
