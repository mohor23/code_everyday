#!/usr/bin/env python
# coding: utf-8

# # DICTIONARY

# In[1]:


data={1:'Navin',2:'Kiran',4:'Harsh'}
data


# In[2]:


data[1]


# In[3]:


data[3]


# In[8]:


data.get(1)


# In[9]:


print(data.get(3))


# In[10]:


data.get(1,"not found")


# In[11]:


data.get(3,"not found")


# In[19]:


keys=['navin','harsh','kiran']
values=['python','java','react']
data=dict(zip(keys,values))
print(data)
data['monica']='wt'
print(data)
del data['harsh']
print(data)


# # To return the address of a variable

# In[20]:


num=5
id(num)


# In[22]:


a=10
b=a
print(id(a))
print(id(b))
print(id(10))


# In[23]:


list(range(2,10,2))


# # Number System Conversion

# In[25]:


bin(25)#conversion of decimal to binary 0b represents any binary number


# In[26]:


0b11001#we can convert any binary no to decimal by adding 0b in front 


# In[27]:


oct(25)#to convert decimal to octal


# In[28]:


hex(25)#to convert decimal to hexadecimal


# In[30]:


0xf


# # Swapping of two numbers 

# In[31]:


a=5
b=6
a,b=b,a
print(a,b)


# #  Bitwise Operator

# In[32]:


~12


# In[33]:


12&13


# In[34]:


12|13


# In[35]:


12^13


# In[36]:


12<<2


# In[38]:


12>>2


# In[39]:


result=eval(input("enter an expression"))
print(result)


# # print values from 1 to 20 skipping the values divisible with 3 and 5

# In[9]:


i=1
for i in range(1,21):
    if i%3==0 or i%5==0:
        continue
    print(i,end=" ")
    


# # implementation of pass..print all even nos

# In[10]:


for i in range(101):
    if i%2!=0:
        pass
    else:
        print(i,end=" ")
        


# # patterns

# In[14]:


n=int(input("enter the number"))
for i in range(n):
    for j in range(n):
        print("#",end=" ")
    print( )


# In[16]:


n=int(input("enter the number"))
for i in range(n):
    for j in range(i+1):
        print("#",end=" ")
    print()
        


# In[17]:


n=int(input("enter the number"))
for i in range(n):
    for j in range(n-i):
        print("#",end=" ")
    print()


# # implementation of for else in python

# In[18]:


#implementation wothout using for else for understanding
for i in range(20):
    if i%3==0:
        print(i)
    else:
        print("not found")
    


# In[26]:


#implementing for else
for i in range(20):
    if i%3==0:
        print(i)
        
else:
    print("not found")
    


# # prime no in python 

# In[28]:


n=int(input("enter the number"))
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
else:
    print("Prime")


# #  array in python

# In[34]:


from array import*
vals=array('i',[5,6,10,2,8])
print(vals)
print(vals.buffer_info())#to print the address and size of the array
print(vals.typecode)# to print the type of array
vals.reverse()
print(vals)


# In[37]:


vals=array('i',[5,6,10,2,8])
new_arr=array(vals.typecode,(a for a in vals))# to create a new array with the values of an old array
print(new_arr)
new_arr1=array(vals.typecode,(a*a for a in vals))
print(new_arr1)


# In[4]:


from array import*
arr=array('i',[])
n=int(input("enter the no of elements"))
for i in range(n):
    ele=int(input("enter the elements"))
    arr.append(ele)
print(arr)
val=int(input("enter the element to be searched"))
print(arr.index(val))#to return the index of particular element


# # numpy array

# In[19]:


from numpy import*
arr1=array([1,2,3,4])
print(arr1.dtype)
arr2=array([2.2,3.3,1,10])
print(arr2.dtype)


# In[8]:


arr3=linspace(0,15,20)
print(arr3)


# In[10]:


arr4=linspace(0,15)#by default taking no of parts as 50
print(arr4)


# In[11]:


arr5=logspace(0,15,4)
print(arr5)


# In[13]:


arr6=ones(5,int)
print(arr6)


# In[20]:


print(arr1+5)
print(arr1+arr2)


# In[22]:


a=array([1,2,3,4])
a2=a.view()#to copy an array to another array
print(id(a))
print(id(a2))


# # Multidimensional array i.e numpy array(matrix)

# In[27]:


arr=array([[1,2,3],[4,5,6]])
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
arr2=arr.flatten()
print(arr2)


# In[32]:


m=matrix('1 2 3;4 5 6;7 8 9')
m1=matrix('1 7 3;4 9 6;7 0 9')
print(m)
print("..........")
print(diagonal(m))
print(m *m1)


# # Function argument

# In[34]:


def update(x):
    x=8
    print("x:",x)
a=10
update(a)#this is called by value that is why the original value is not changed
print("a:",a)


# In[2]:


#to take number of values in one argument
def sum(a,*b):#b taking input as tuple
    c=a
    print(a)
    print(b)
    for i in b:
        c=c+i
    print(c)
sum(1,2,3,4,5)


# In[4]:


#keyworded variable length argument
#**means passing multiple agruments with the help of keywords
def person(name,**data):
    print(name)
    print(data)
person('navin',age=28,city='kolkata',mob=967352719)


# In[5]:


#another methord of printing the tuple
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('navin',age=28,city='kolkata',mob=967352719)


# # fibonacci in python

# In[9]:


n=int(input("enter the number of elements"))
def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(n)
    


# # recursion in python

# In[ ]:


import sys
print(sys.getrecursionlimit())# to know the limit of recursion in an infininite recursion
def rec():
    print("hello")
    rec()
rec()


# # Factorial using recursion 

# In[1]:


def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter the no"))
fact(n)


# # anonymous function

# In[2]:


f=lambda a:a*a
result=f(5)
print(result)


# # filters map and reduce

# In[8]:


#from funtools import reduce
num=[2,9,5,1,6,3,8]
even=list(filter(lambda a:a%2==0,num))
doubles=list(map(lambda a:a*a,even))
#s=list(reduce(lambda a,b:a+b,doubles))
print(even)
print(doubles)
#print(s)


# # decorators

# In[12]:


def div(a,b):
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return(func(a,b))
    return inner
div1=smart_div(div)
div1(2,4)


# # class and object

# In[16]:


class coumpter:
    def config(self):
        print("i5",'1tb','64gb')
a=10
print(type(a))
com1=coumpter()
print(type(com1))
coumpter.config(com1)
com1.config()#this and the above line is same


# In[23]:


class coumpter:
    def __init__(self,ram,cpu):
        self.ram=ram
        self.cpu=cpu
    def config(self):
        print('config is:',self.ram,self.cpu)
com3=coumpter('i5',16)
com2=coumpter('windows',8)
com3.config()
com2.config()


# In[31]:


class example:
    def __init__(self):
        self.name="navin"#for default variable
        self.age="28"
    def compare(self,other):
        if self.age==other.age:
            print("the ages are same")
        else:
            print("the ages are different")
c1=example()
c1.age=48#for changing the value of age
c2=example()
c1.compare(c2)


# # types of variables

# In[36]:


class car:
    wheels=4#class or static variable
    def __init__(self):
        self.mil="10"#instance variable
        self.com="Honda"#instance variable
c1=car()
c2=car()
car.wheels=5#changing the value of class variable,it will change for both the objects
print(c1.wheels)
print(c2.wheels)


# In[ ]:
types of methords
class student:
    college='kiit'#class or static variable
    def __init__(self,m1,m2,m3):
        self.m1=m1#instance variable
        self.m2=m2
        self.m3=m3
    def avg(self):# instance methord as it is using self
        return(self.m1+self.m2+self.m3)/3
    @classmethod #decorator needed to use while using class methord
    def info(cls):#class methord using cls
        return cls.college
    @staticmethod
    def func():# static method which doesnt involve any static or class method
        print("this is static methord which doesnt use any instance or class variable")
s1=student(23,98,65)
s2=student(34,78,65)
print(s1.info())
student.func()
        
kiit
this is static methord which doesnt use any instance or class variable
class student:
    
    def __init__(self,name,rollno):
        self.name=name#instance variable
        self.rollno=rollno
        self.lap=self.laptop()#creating object of inner class inside outer class
    def show(self):
        print(self.name,self.rollno)
    class laptop:
        def __init__(self,company):
            self.company="HP"
s1=student("rahul",15)
s1.lap.company
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-48-37480550b8f1> in <module>
     10         def __init__(self,company):
     11             self.company="HP"
---> 12 s1=student("rahul",15)
     13 s1.lap.company

<ipython-input-48-37480550b8f1> in __init__(self, name, rollno)
      4         self.name=name#instance variable
      5         self.rollno=rollno
----> 6         self.lap=self.laptop()#creating object of inner class inside outer class
      7     def show(self):
      8         print(self.name,self.rollno)

TypeError: __init__() missing 1 required positional argument: 'company'

inheritance
#multilevel inheritance
class A:
    def feature1(self):
        print("this is feature 1")
class B(A):
    def feature2(self):
        print("this is feature 2")#inheriting class A
class C(B):
    def feature3(self):
        print("this is feature 3")#inheriting class B
​
        
c=C()
c.feature1()
c.feature2()
c.feature3()
​
​
this is feature 1
this is feature 2
this is feature 3
#multiple inheritance
class A:
    def feature1(self):
        print("this is feature 1")
class B:
    def feature2(self):
        print("this is feature 2")
class C(A,B):
    def feature3(self):
        print("this is feature 3")#inheriting class A &B
​
        
c=C()
c.feature1()
c.feature2()
c.feature3()
this is feature 1
this is feature 2
this is feature 3
constructor in inheritance
class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("this is feature 1")
class B(A):
    def feature2(self):
        print("this is feature 2")
b=B()
in A init
#when B init is there it will exucute that.. if it cant find any init in B then will go to A init
class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("this is feature 1")
class B(A):
    def __init__(self):
        print("in B init")
    def feature2(self):
        print("this is feature 2")
b=B()
in B init
#to access both the init at the same time
class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("this is feature 1")
class B(A):
    def __init__(self):
        super().__init__()
        print("in B init")
    def feature2(self):
        print("this is feature 2")
b=B()
in A init
in B init
#methord resolution order(MRO)
class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("this is feature 1")
class B:
    def __init__(self):
        print("in B init")
    def feature2(self):
        print("this is feature 2")
class C(A,B):
    def __init__(self):
        super().__init__()# iit will print the A because of MRO
        print("in C init")
    def feature3(self):
        print("this is feature 3")#inheriting class A &B
​
        
c=C()
​
in A init
in C init
duck typing polymorhism
class jupyter:
    def execute(self):
        print("type checking")
        print("execution")
class pycharm:
    def execute(self):
        print("compiling")
        print("convention check")
        
class coumpter:
    def code(self,ide):
        ide.execute()
ide1=jupyter()
ide2=pycharm()
l=coumpter()
l.code(ide1)
l.code(ide2)
type checking
execution
compiling
convention check
operator overloading
a=6
b=7
print(a+b)# the below is wt actually happens when we do any sum
print(int.__add__(a,b))
13
13
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):# operator overloading
        m1=self.m1+other.m1
        m2=self.m2=other.m2
        a=student(m1,m2)
        return a
s1=student(56,89)
s2=student(67,90)
s3=s1+s2
print(s3.m1)
123
methord overloading
class a:
    def sum(self,a=None,b=None,c=None):
        c=0
        if a!=None and b!=None and c!=None:
            c=a+b+c
        elif a!=None and b!=none:
            c=a+b
        else:
            c=a
        return c
s1=a()
print(s1.sum(5,9))
14
method overridding
class A():
    def show(self):
        print("in class A")
class B(A):
    pass
t=B()
t.show()
in class A
class A():
    def show(self):
        print("in class A")
class B(A):
    def show(self):
        print("in class B")#here show methord is overridding the show methord of class A,,,, refer to previous program
t=B()
t.show()
in class B
abstract method
from abc import ABC,abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
        pass
com=computer()# this error is because we cannot create object of abstract method
com.process
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-32-30b1035ee4b3> in <module>
      4     def process(self):
      5         pass
----> 6 com=computer()
      7 com.process

TypeError: Can't instantiate abstract class computer with abstract methods process

from abc import ABC,abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
        pass
class laptop(computer):
    def process(self):
        print("its running")
com1=laptop()
com1.process()
its running
iterator
num=[1,2,3,4]
it=iter(num)
print(it.__next__)
print(next(it))
print(next(it))
<method-wrapper '__next__' of list_iterator object at 0x000001867675F248>
1
2
class topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
d=topten()
for i in d:
    print(i)
1
2
3
4
5
6
7
8
9
10
generators
 def c():
    n=1
    while n<10:
        sq=n*n
        yield sq
        n+=1
values=c()
for i in values:
    print(i)
    
1
4
9
16
25
36
49
64
81




