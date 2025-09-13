#python,by default doesnt support method-overloading instead you can acheive it by 1. passing default args 2. *args 3.type checking
#polymorphism
class Calculator:
    def add(self,a=0,b=0,c=0,d=0):
        return a+b+c+d
c=Calculator()
print(c.add(5))
print(c.add(1,2,3))
print(c.add(2,2,2,2))

#2. passing flexibile args *Args
class Calculator1:
    def add1(self,*args):
        return sum(args)
c1=Calculator1()
print(c1.add1(1))
print(c1.add1(1,2,4))
print(c1.add1(1,1,1,1,1,1,1,1,1,1,1))
