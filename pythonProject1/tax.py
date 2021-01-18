
def tax(amount):
    if amount <= 240:
        return 0
    elif amount >= 241 and amount <= 480:
        return (amount * .15)
    else:
        return (amount * .28)
def netpay(grosspay):
    return grosspay - tax(grosspay)

print("Enter amount:")
amount = int(input())
print("The tax is " + str(tax(amount)))
print ("Enter grosspay")
gp= int (input())
print("The netpay is " + str(netpay(gp)))
