from array import *
arr = array('i',[])
n=int(input('enter length of array'))
for i in range(n):
    x=int(input("Enter next number"))
    arr.append(x)
print(arr)

max= arr[0];
for i in range(0,len(arr)):
    if arr[i]>max :
        max = arr[i]

print(max)