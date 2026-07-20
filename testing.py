

#comment 
"""

print("Hello 1", end='');
print("Hello 2");
print("Hello 3");

a,b,c=10,20,30;
print(a,b,c);



k=True;
l=False;
str= " ";
print("str");

a=range(5)
print (a)
for x in a:
    print(x)

u=17.9
n=int(u)
print(n)
print(type(n))

for x in "hello":
    print(x)
    
if 'e' in "hello":
    print("present");



e=30
z=30
print(id(e))
print(id(z))

from sys import argv
print(argv[0])

course="python programming lanuage"
print(course.find("p"))
print(course.find("a",1,20))
print(course.find("z"))
# print(course.index("z"))

user="rahul"
x=input("enter name")
if user == x:
    print("valid")
else:
    print("invalid") 



x=int(input("enter number"))
y=int(input("enter number"))
if x>y:
    print("biggest number" , x)
else:
    print("biggest number" , y)

    


u=int(input("enter number"))
v=int(input("enter number"))
w=int(input("enter number"))
if u>v and u>w:
    print("biggest number" , u)
if v>u and v>w:
    print("biggest number" , v)

else:
    print("biggest number" , w)


a,b=10,45
min= a if a>b else b
print(min)


x=10
while(x>=10) and (x<=20):
    print(x)
    x=x+2
print("end")

x=[10,20,30,"python"]
for i in x:
    print(i)



x="python"
for i in x:
    print(i)

costs=[10,20,30]
gst=2
for i in costs:
    print(i+gst, end="\n")

y=[10,40,50]
sum=0
for i in y:
    sum=sum+i;
print(sum)



rows=range(4,0,-1)
for x in rows:
    for star in range(1,x+1):
        print("*", end=" ")
    print()

k=range(1,10,3)
l=range(2,8,2)
m=range(10,-10)
n= range(10,1,-3)
for i in k:
    print(i, end=" ")
print(l, end=" ")
print(m, end=" ")
print(n, end=" ")




group=[1,2,3,4]
search= int(input("enter element to search"))
for i in group:
    if search==i:
        print("element found in group")
        break
    else:
        print("element not found")



total=0
while True:
    num=int(input("enter number or (0 to exit)"))
    if num==0:
        break
    total=total+num
print("total", total)



def process(a,b):
    c=a+b
    d=a-b
    f=None;
    return c,d,f


r,k,l= process(80,13)

print(r,k,l)
    



def sum(a,b):
    c=a+b
    return c

r=sum
l=r(80,13)

print(l)

def display(x):
    print("in display")
def message():
    print("in message")



display(message())




def first():
    print("in first")
    def second():
        print("in second")
    second()

first()

def third():
    print("in third")
    def second():
        print("in second")
    return second()

first()




def cart(item,price,place="lucknow"):
    print(item, "cost is" , price , place)
cart(item="bangles",price=20000,place="mango")
cart(item="hadbag",price=4500, place="himachal")
cart(price=20000,item="shirt")



def total_cost(x,*y):
    sum=0
    for i in y:
        sum=sum+i
    print(x+sum)
total_cost(100,200)
total_cost(100,200,235)
total_cost(100,)


def m1(**x):
    for k,v in x.items():
        print(k,"=",v)
m1(a=10,b=20,c=30)
m1(id=100,name="rahul")



a=1
def m():
    a=2
    print(a)
    print(globals()["a"])
m()



def power(x,n):
    if n==0:
        return 1
    else:
        res=x*power(x,n-1)
    return res


a=power(4,3)
print(a)



sum= lambda a,b: a+b
y=sum(4,5)
print(y)

item_cost=[88,776,555,678,457,44]
gt=filter(lambda x : x>100, item_cost)
x=list(gt)
print(x)
print(gt)
withoutGSTCost=[100,200,300,400]
withGSTcost=map(lambda x : x+10, withoutGSTCost)
x=list(withGSTcost)
print(withGSTcost)
print(x)


from functools import reduce
arr=[111,222,333,444]
max= reduce(lambda x,y : x if x>y else y,arr)
print(max)

"""

def m():
    yield "mahesh"
    yield "suresh"
g=m()
print(g)
print(type(g))
g=list(g)
for y in g:
    print(y)
