def ftoc(temp):
    return (temp - 32.0)*(5.0/9.0)
def ctof(temp):
    return (temp) * (9.0/5.0) + 32.0

def convert(temp,scaleto):
    if scaleto.lower()== "c":
        return ftoc(temp)
    else:
        return ctof(temp)

print("Enter the temp")
temp = int(input())
print("Enter the scale to be converted")
scale=(input())
convertedtemperature= convert(temp, scale)
print(temp, convertedtemperature, scale)