def calc_sum (a,b):
    return a+b

sum = calc_sum(1,2)
print(sum)

def print_hello():
    return

output = print_hello()
print (output)

def avg_num(a,b,c):
    return (a+b+c)/3

avg = avg_num(1,2,3)
print (avg)

#default parameter
def  calc_mul (a=2, b=3):
    print(a*b)

calc_mul()

#or
def cal_mul (a,b=2):
    print(a*b)

cal_mul(1)

#Recursion
def show(n):
    if(n==0):
        return
    print(n)
    show (n-1)
   
show(5)

def fact (n):
    if (n==0):
        return 1
    return fact(n-1)*n
    
output = fact(5)
print(output)