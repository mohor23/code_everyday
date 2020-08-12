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




