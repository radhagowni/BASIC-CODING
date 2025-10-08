# We have used the function called simple_interest to calculate the amount of interest to be paid
def simple_interest(p,t,r):
    return (principle*time*rate)/100
def EMI(p,t,r):
    i=(p*t*r)/100
    emi=(p+i)/(12*t)
    return emi
principle=int(input("Enter the principle amount:"))
time=int(input("enter time: "))
rate=int(input("enter rate of interest:"))
interest=simple_interest(principle,time,rate)
emi=EMI(principle,time,rate)
print("simple interest:",interest)
print("EMI per month:",emi)
print("the amount to be paid from principle amount as emi:",(principle/(12*time)))
print("the amount to be amount from interest as emi:",(interest)/(12*time))
