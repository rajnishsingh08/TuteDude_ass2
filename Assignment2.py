#ASSESMENT-2
#TASK 1
print("task 1 \n")

try:

    a=int(input("enter a no."))
    if(a%2==0):
        print(f"{a} is even no.")
    else:
        print(f"{a} is odd no.")
except ValueError:
    print("invalid ! wrong input ")

#TASK 2
print("\n task 2 \n")

total=0
for i in range(1,50):
    
    total+=i
    print("The sum of number from 1 to 50 :",total)

