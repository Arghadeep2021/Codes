def fact(number):
    count=1
    for i in range (1,number+1):
        count = count * i
    return count
print ("Enter a number")
num=int(input())
print(str(num) + " equals to " + str(fact(num)))