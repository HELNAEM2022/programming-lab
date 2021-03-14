class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
       return self.length * self.breadth
    def perimeter(self):
        return 2*(self.length + self.breadth)
        

    
a=int(input("Enter the length of the first reactangle:"))
b=int(input("Enter the breadth of the first reactangle:"))
c=int(input("Enter the length of the Second reactangle:"))
d=int(input("Enter the breadth of the Second reactangle:"))
obj1=rectangle(a,b)
obj2=rectangle(c,d)
print("Area of first rectangle:",obj1.area())
print("Perimeter of first rectangle:",obj1.perimeter())
print("Area of second rectangle:",obj2.area())
print("Perimeter of second rectangle:",obj2.perimeter())

if obj1.area() == obj2.area():
     print("Both  reactangle have same area ",obj1.area())
elif obj1.area() > obj2.area():
     print("1st reactangle is greater")
else:
    print("2nd reactangle is greater ")




