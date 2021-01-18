def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("Enter the required operator: \n 1. Addition \n 2. Substraction \n 3. Multiplication \n 4. Division")
select = int(input("Select operations from (1, 2, 3, 4) :"))
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
if select == 1:
    print(num_1, "+", num_2, "=", add(num_1, num_2))

elif select == 2:
    print(num_1, "-", num_2, "=",sub(num_1, num_2))

elif select == 3:
    print(num_1, "*", num_2, "=",mul(num_1, num_2))

elif select == 4:
    print(num_1, "/", num_2, "=",div(num_1, num_2))
else:
    print("Invalid input")