class A :
    __length = 0
    __width = 0
    __area = 0
    def __init__(self,l,b):
          self.__length = l
          self.__width = b
    def area1(self) :
          self.__area=self.__length*self.__width
    def __gt__(self,other) :
          if(self.__area > other.__area) :
             return True
          else :
             return False
ob1 = A(2,4)
ob1.area1()
ob2 = A(3,5)
ob2.area1()
if(ob1>ob2):
    print("ob1 is greater than ob2")
else :
    print("ob2 is greater than ob1")
    
          
