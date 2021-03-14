s=int(input("Enter the year:"))
print("Future leap years from 2021 to ",s)
for i in range(2021,s+1):
    if (i%4==0):
        print(i)
