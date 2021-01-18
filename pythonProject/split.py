
def splitArr(arr, n, k):
    b = arr[:k]
    return (arr[k::] + b[::])


from array import *
arr = array('i',[])
n=int(input('enter length of array'))
for i in range(n):
    x=int(input("Enter next number"))
    arr.append(x)

n = len(arr)
k = int(input('Enter the index number'))
arr = splitArr(arr, n, k)
for i in range(0, n):
    print(arr[i], end=' ')
