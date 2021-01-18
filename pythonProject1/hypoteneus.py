import math
def hypoteneus(s1,s2):
    def square(number):
        return number*number
    return math.sqrt(square(s1)+square(s2))
print("Enter the side 1:")
side1= int(input())
print("Enter the side 2:")
side2= int(input())
hyp= hypoteneus(side1,side2)
print("The hypoteneus is : " + str(hyp))
