#diff types-single,multiple,hierarchical
#single- child/sub class inherit properties from one parent/super class
class Vehicle:
    def accelerates(self):
        print("vehicle accelerates")
class Car(Vehicle):
    def breaks(self):
        print("Car breaks")


c=Car()
c.accelerates()
c.breaks()
#EXAMPLE-2
class Student:
    def __init__ (self,name,num):
        self.name=name
        self.num=num
    def showdetails(self):
        print(f"name of the student is {self.name}")
        print(f"roll num of the student is {self.num}")
class Exam(Student):
    def __init__(self,name,num,subject):
        super() .__init__(name,num)
        self.subject=subject
    def show(self) :
        print(f"subject name is{self.subject}")

e1=Exam("anvi", 77 ,"maths")
e1.showdetails()
e1.show()
#EXAMPLE-3
class Bank:
    def __init__(self,holdername,holdernum):
        self.holdername=holdername
        self.holdernum=holdernum
    def showdetails1(self):
        print(f"name of the account holder is {self.holdername}")
        print(f"account number of holder is{self.holdernum}")

class Person(Bank):
    def __init__(self,holdername,holdernum,balance):
        super().__init__(holdername,holdernum)
        self.balance=balance
    def display1(self):
        print(f"the account balance is {self.balance}")

p=Person("anvitha",1019890,100000)
p.showdetails1()
p.display1()
 
 #TYPE-2
 #MULTIPLE INHERITENCE
class Mother:
    def __init__(self,hobbies):
        self.hobbies=hobbies
    def display(self):
        print(f"hobbies of mom are: {self.hobbies}")
class Father:
    def __init__(self,activites):
        self.activites=activites
    def show(self):
        print(f"activites father does: {self.activites}")

class child(Mother,Father):
    def __init__(self,hobbies,activites,own):
        Mother.__init__(self,hobbies)
        Father.__init__(self,activites)
        self.own=own
    def show_deets(self):
        print(f"child's hobbies and activites are similar to parents but his own interests are {self.own}")
    
c=child("badminton,kathak","racing","playing games")
c.display()
c.show()
c.show_deets()
#exmp-2
class Animal:
    def speaks(self):
        print("animal speaks")
class Birds:
    def flies(self):
        print("birds fly")

class kingfisher(Animal,Birds):
    def bird(self):
        print("flies,echoes")
    
k=kingfisher()
k.speaks()
k.flies()
k.bird()
 #multi-level - child class inherit properties from another child class
class School:
    def works(self):
        print("school has a working day")
    
class Teacher(School):
    def comes(self):
        print("teacher teaches students")

class Student(Teacher):
    def learns(self):
        print("student learns from teacher")

s=Student()
s.works()
s.comes()
s.learns()
#HERARCHICAL-INHERITENCE
class Animal:
    def speaks(self):
        print("Animal speaks")
class dog(Animal):
    def speaks(self):
        print("dog barks")
class cat(Animal):
    def speaks(self):
        print("cat meows")

a=Animal()
d=dog()
c=cat()
a.speaks()
d.speaks()
c.speaks()

 

