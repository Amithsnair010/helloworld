'''python program to check amstrong no or not'''
#inputting the no.
num=int(input("enter the no."))
#intialise sum
Sum=0
temp=num
order=len(str(num))
while(temp>0):
    r=temp%10
    Sum+=r**(order)
    temp//=10
#display the output
if(Sum==num):
    print("amstrong no.")
else:
    print("not an amstrong no.")
