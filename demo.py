

""" 

import addMultiplication
print(addMultiplication.x)
addMultiplication.sum(1,2)
addMultiplication.multiplication(2,3)




from tools.addMultiplication import x as y,sum as add
print(y)
add(10,20)


x=10
y=20
def f1():
    print("hello")
print(dir())




names=["mohan","prasad","ramesh","mohan",10,20,True,None]
print(names)
print(names[-5])
names[-3]= "new"
print(names)

n=[1,2,3,4,5,6]
print(n)
print(n[2:5:2])
print(n[4::2])
print(n[3:5])

print()

print(n[-4:-1:2])
print(n[-2:-1:2])
print(n[-3:-1])



a=[100,200,300,400]
    
a.insert(0,76)
print(a)

l1=[1,2,3]
l2=["rakesh","rahul","regina"]
print("before extend l1 is", l1)
print("before extend l2 is", l2)
l2.extend(l1)
print("after extend l1 is", l1)
print("after extend l2 is", l2)

print(sum(l1))

n=[1,2,3,4]
n.remove(1)
print(n)
# n.remove(10) value error
# print(n)

# print(n.pop(10)) index error

print(n.pop(1))



n=[3,2,4,1,5,"two"]

print(n)
n.reverse()
print(n)


num=[1,5,4,3,2]
num.sort()
print(num)


x=[10,20,30]
y=x # aliasing
print(x)
print(y)
print(id(x))
print(id(y))
x[1]=99
print(x)
print(y)
print(id(x))
print(id(y))



x=[10,20,30]
y=x[::] cloning
print(x)
print(y)
print(id(x))
print(id(y))
x[1]=99
print(x)
print(y)
print(id(x))
print(id(y))



x=[10,20,30]
y=x.copy() cloning
print(x)
print(y)
print(id(x))
print(id(y))
x[1]=99
print(x)
print(y)
print(id(x))
print(id(y))



a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

# error 

a=[1,2,3]
b="balu"
c=a+b
print(c)


a=[1,2,3]
print(a)
print(2*a)

print([1,2,3]<[2,2,3])
print([1,2,3]<[1,2,3])
print([1,2,3]<=[1,2,3])
print([1,2,3]<[1,2,4])
print([1,2,3]<[0,2,3])
print([1,2,3]==[1,2,3])

x=["abc","def","ghi"]
y=["abc","def","ghi"]
z=["ABC","DEF","GHI"]
a=["abc","def","ghi","jkl"]
print(x==y)
print(x==z)
print(x==a)





x=[1,2,3,4]
y=[]
for i in x:
    y.append(i*2)
print(y)




x=[1,2,3,4]
y=[i*2 for i in x]
print(y)

s=range(1,20,3)
for i in s:
    print(i)



m=[x for x in s if x%5==0]
print(m)




name=("sushant")
print(name)
print(type(name))

name1=("sushant1" ,)
print(name1)
print(type(name1))


std=120,
print(std)
print(type(std))

t=(10,20,30,40,50,60)
print(t[2:100])

t1=(966,77,4400)
t2=t+t1
print(t2)

t3=t1*2
print(t3)


print(t.index(40))

t=(40,10,30,20)
t1=sorted(t)
print(t)
print(t1)

t2=sorted(t,reverse=True)
print(t2)

t=(10,20,30,50)
print(min(t))
print(max(t))

l=100,"suresh",196627

roll,name,sal=l

print(roll)
print(name)
print(sal)


d={1:"ramesh", 2:"arjun" , 3:"nireekshan"}
print(d)


if 400 in d:
    print(d[400])
else:
    print("no key")




d={}
n=int(input("enter number"))
i=1
while i<=n:
    name=input("enter employee name")
    salary=input("enter employee salary")
    d[name]=salary
    i=i+1
for x in d:
    print("the name is",x,"and salary",d[x])




d={1:"ramesh", 2:"arjun" , 3:"nireekshan"}
print(d.get(1))
print(d.get(100),"key not found")

print("before pop",d)
print(d.pop(1))
print("after pop",d)



d={1:"ramesh", 2:"arjun" , 3:"nireekshan"}
print("before pop item",d)
print(d.popitem())
print("after pop item",d)

for k in d.keys():
    print(k)


for k in d.values():
    print(k)

squares={a:a*a for a in range(1,6)}
print (squares)




s={10,20,30,40,10}
print(s)
print(type(s))

s=set(range(5))
print(s)

d={}
print(d)
print(type(d))

s=set()
print(s)
print(type(s))

s={10,20,30,40,10}
s.add(40)
print(s)
print(type(s))

s={10,20,30}
l=[40,50,60,10]
s.update(l)
print(s)


s={10,20,30}
l=[40,50,60,10]
s.update(l,range(5))
print(s)

s=set()
s.add(13)
print(s)
s.update(range(1,10,2),range(0,10,2))
print(s)

s1=s.copy()
print(s1)
print(s.pop())
print(s)
print(s1)
s.remove(1)
print(s)
s.discard(8)
s.discard(89)
print(s)



x={10,20,30,40}
y={30,40,50,60}

print(x.union(y))
print(x|y)

print(x.intersection(y))
print(x&y)

print(x.difference(y))
print(y.difference(x))

print(x.symmetric_difference(y))
print(x^y)

s={1,2,3,"Shark"}
print(s)
print(1 in s)
print('S' in s)
print(2 not in s)

s={x*x for x in range(5)}
print(s)

vow=("a",'e','i','o','u')
fSet=frozenset(vow)
print(fSet)
print(type(fSet))

print('one')
print('two')
try:
    print(10/3)
except ZeroDivisionError :
    print("Exception passed")
print("four")
print("five")

print('one')
print('two')
try:
    print(10/0)
except ZeroDivisionError as z:
    print("Exception passed", z)
print("four")
print("five")



try:
    x=int(input("enter number"))
    y=int(input("enter number"))
    print(x/y)
except ZeroDivisionError:
    print("cant divide with zero")
except ValueError:
    print("wrong value type inserted")




try:
    x=int(input("enter number"))
    y=int(input("enter number"))
    print(x/y)
except (ZeroDivisionError,ValueError) as e:
    print("problem incoming",e)



try:
    x=int(input("enter number"))
    y=int(input("enter number"))
    print(x/y)
except ZeroDivisionError:
    print("problem incoming",e)
except:
    print("Default Except : please provide valid entry")



try:
    print("try block")
    print(10/0)
except ZeroDivisionError:
    print("except block")
finally:
    print("finally block")




try:
    print("try block")
    print(10/0)
except NameError:
    print("except block")
finally:
    print("finally block")



try:
    print("outer try block")
    try:
        print("inner try block")
    except ZeroDivisionError:
        print("inner exception block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")



try:
    print("outer try block")
    print(10/0)
    try:
        print("inner try block")
    except ZeroDivisionError:
        print("inner exception block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")



try:
    print("outer try block")
    try:
        print("inner try block")
        print(10/0)
    except ZeroDivisionError:
        print("inner exception block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")



try:
    print("outer try block")
    try:
        print("inner try block")
        print(10/0)
    except NameError:
        print("inner exception block")
    finally:
        print("inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block")



try:
    print("try block")
    print(10/0)
except:
    print("except handling block")
else:
    print("else block")
finally:
    print("finally block")


try:
    print("try block")
except:
    print("except handling block")
else:
    print("else block")
finally:
    print("finally block")

    
    
try:
    x=int(input("enter positive number only"))
    if x<0:
        raise ValueError(x)
except ValueError as e:
    print("You provided {}. please provide positive integer values only".format(e))




print("Filename",f.name)
print("File mode",f.mode)
print("Is File readable",f.readable())
print("Is File writable",f.writable())
print("Is File closed",f.closed)


f=open("abc.txt", "w")
f.write("welcome \n")
f.write("to \n")
f.write("python world \n")
print("Data written")
f.close()

f=open("wish.txt", "a")
f.write("welcome \n")
f.write("to \n")
f.write("python world \n")
print("Data written")
list=["ramesh\n","Arjum\n","umesh\n"]
f.writelines(list)
print("list of lines written successfully")



data=f.read(20)
print(data)


lines=f.readlines()
for line in lines:
    print(line, end='')



f=open("abc.txt",'r')
data=f.read()
print(data)



f=open("abc.txt",'r')
line1=f.readline()
print(line1 , end='')
line2=f.readline()
print(line2 , end='')
line3=f.readline()
print(line3 , end='')




with open("test.txt", "w") as f:
    f.write("welcome\n")
    f.write("to\n")
    f.write("python\n")
    print("is file closed", f.closed)
print("is file closed", f.closed)

f=open("test.txt",'r')
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.read(3))
print(f.tell())
f.close()




data="python language is excellent"
f=open("new.txt","w")
f.write(data)
with open("new.txt","r+") as f:
    text=f.read()
    print(text)
    print("current position",f.tell())
    f.seek(2)
    print("current position",f.tell())
    f.write(" britania biscuit")
    f.seek(0)
    text=f.read()
    print("data after modification")
    print(text)




import os,sys
fname=input("enter file name")
if os.path.isfile(fname):
    print("file exists",fname)
    f=open(fname,"r")
else:
    print("not exist",fname)
    sys.exit(0)
print("the content of file is")
data=f.read()
print(data)

"""


import csv
with open("emp.csv","w",newline='') as f:
    w=csv.writer(f)
    w.writerow(["emp no","emp name","emp sal","emp addr"])
    n=int(input("enter number of employees"))
    for i in range(n):
        eno=input("employee no")
        ename=input("employee name")
        esalary=input("employee salary")
        eadd=input("employee add")
        w.writerow([eno,ename,esalary,eadd])
print("total enployees written to csv file successfully")