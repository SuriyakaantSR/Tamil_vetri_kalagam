'''
rollno = int(input("Enter your rollno : "))
Name = input("Enter your name : ")
English = int(input("Enter your English mark : "))
Tamil = int(input("Enter your Tamil marks : "))
Maths = int(input("Enter your Maths mark : "))
Total = (English + Tamil + Maths)
print("English marks = ",English)
print("Tamil Marks = ",Tamil)
print("Maths marks = ",Maths)
print("Total marks",Total)
Percent = Total/3
print("Percentage = ",Percent)
'''
'''
Conditional Statement:
    1. if...else
    2. Nested if else
    3. elif Ladder
    
    if...else:
        Syntax: 
        if condition:
            True Statement(s)
        else:                       #else Optional
            False Statement(s)         

age = int(input("Enter Age : "))
if age>= 18:
    print(age," Eligible to Vote")
else:
    print(age," Not Eligible to Vote")
'''
'''
A = int(input("Enter A value : "))
B = int(input("Enter B value : "))
if A>=B:
    print(A," is greater than ",B)
else:
    print(B," is greater than ",A)
'''
'''
num = int(input("Enter a name for Num : "))
if num % 2 ==0 :
    print(num,"is Even")
else:
    print(num,"is Odd")
'''
'''A = int(input("Enter A value : "))
B = int(input("Enter B value : "))
if A == B :
    print(A,"is equal",B)
else:
    if A>B:
        print(A," is greater than ",B)
    else:
        print(B," is greater than ",A)
'''
'''
a = int(input("Enter a value of a : "))
b = int(input("Enter b value of b : "))
c = int(input("Enter c value of c : "))
if (a==b and b==c and c==a):
    print(a,"=",b,"=",c,"are equal")
else:
    if a > b and a > c:
        print(a," is greater than ", b, " & ", c)
    else:
        if ((b > a) and (b > c)):
            print(b,"b is greater than", a," & ",c)
        else:
            print(c,"is greater than",a," & ",b)
'''
'''
a = int(input("Enter a value of a : "))
b = int(input("Enter b value of b : "))
c = int(input("Enter c value of c : "))
d = int(input("Enter d value of d : "))
if (a==b and a==c and a==d and b==c and b==d and c==d):
    print(a,"=",b,"=",c,"=",d,"are equal")
else:
    if a > b and a > c and a > d:
        print(a," is greater than ", b," & ", c," & ",d)
    else:
        if b > c and b > d:
            print(b,"b is greater than", a," & ",c," & ",d)
        else:
            if c > d:
                print(c,"c is greater than",a," & ",b,"&",d)
            else:
                print(d, "is greater than", a, " & ", b, " & ", c)
'''
'''
a = int(input("Enter a value of a : "))
b = int(input("Enter b value of b : "))
c = int(input("Enter c value of c : "))
d = int(input("Enter d value of d : "))
e = int(input("Enter e value of e : "))
if (a==b and a==c and a==d and a==e and b==c and b==d and b==e and c==d and d==e):
    print(a,"=",b,"=",c,"=",d,"=",e,"are equal")
else:
    if ((a < b) and (a < c) and (a < d) and (a < e)):
        print(a," is lesser than ", b," & ", c," & ",d," & ",e)
    else:
        if ((b < a) and (b < c) and (b < d) and (b < e)):
            print(b," is lesser than ", a," & ", c," & ",d," & ",e)
        else:
            if ((c < a) and (c < b) and (c < d) and (c < e)):
                print(c," is lesser than ", a," & ",b," & ",d," & ",e)
            else:
                if ((d < a) and (d < b) and (d < c) and (d < e)):
                    print(d," is lesser than ",a," & ",b," & ",c," & ",e)
                else:
                    print(e," is lesser than ",a," & ",b," & ",c," & ",d)
'''
'''
rollno = int(input("Enter your rollno : "))
Name = input("Enter your name : ")
English = int(input("Enter your English mark : "))
Tamil = int(input("Enter your Tamil marks : "))
Maths = int(input("Enter your Maths mark : "))
print("English marks = ",English)
print("Tamil Marks = ",Tamil)
print("Maths marks = ",Maths)
total = English + Tamil + Maths
percentage = total/3
if (English >= 35 and Tamil >= 35 and Maths >= 35 ):
    print(rollno,Name,"pass")
else:
    print(rollno, Name, "Fail")

if (percentage >=90):
    print(percentage,"And Grade = A1")
else:
    if (percentage >=75):
        print(percentage,"And Grade = A2")
    else:
        if (percentage >= 65):
            print(percentage,"And Grade = B ")
        else:
            if (percentage >= 50):
                print(percentage,"And Grade = C")
            else:
                print("D Grade")
'''
'''
a = int(input("Enter a value of a : "))
b = int(input("Enter b value of b : "))
c = int(input("Enter c value of c : "))
d = int(input("Enter d value of d : "))
e = int(input("Enter e value of e : "))
if (a==b and a==c and a==d and a==e and b==c and b==d and b==e and c==d and d==e):
    print(a,"=",b,"=",c,"=",d,"=",e,"are equal")
elif ((a < b) and (a < c) and (a < d) and (a < e)):
    print(a," is lesser than ", b," & ", c," & ",d," & ",e)
elif ((b < a) and (b < c) and (b < d) and (b < e)):
    print(b," is lesser than ", a," & ", c," & ",d," & ",e)
elif ((c < a) and (c < b) and (c < d) and (c < e)):
    print(c," is lesser than ", a," & ",b," & ",d," & ",e)
elif ((d < a) and (d < b) and (d < c) and (d < e)):
    print(d," is lesser than ",a," & ",b," & ",c," & ",e)
else:
    print(e," is lesser than ",a," & ",b," & ",c," & ",d)
'''
'''
print(list(range(100,1100,100)))

print(list(range(1000,500,-50)))

print(list(range(-10,11)))
'''
'''
for i in range(1,11):
    print("suriya -",i)
'''
'''
for i in range(1,11):
    print(i,end=" ")
    '''








'''
for i in range(0,22,2):
    print(i,end=" ")
'''
'''
print(list(range(0,22,2)))
'''
'''for j in range(5,55,5):
    print(j,end =" ")
'''
'''n
for k in range(100,0,-1):
    print(k,end=" ")
'''
'''
for l in range(1000,51000,1000):
    print(l,end=" ")
'''
'''
for m in range(10,-11,-1):
    print(m,end=" ")
'''
'''
n = int(input("Enter a value of n : "))
for i in range(1,n + 1):
    print(i,end=" ")
'''
'''
n = int(input("Enter a value of n : "))
m = int(input("Enter a value of m : "))
for i in range(n,m + 1):
    print(i,end=" ")
'''
'''
n = int(input("Enter a value of n : "))
m = int(input("Enter a value of m : "))
x = int(input("Enter a value of x : "))
for i in range(n,m,x):
    print(i,end=" ")
'''
'''
n = int(input("Enter the value of n : "))
m = int(input("Enter the value of m : "))
sum = 0
for x in range(n,m + 1):
    sum = (sum + x)
    print(sum,end=" ")
'''
'''
n = int(input("Enter the value of n : "))
fac = 1
for x in range(1,n+1):
    fac = fac * x
print(fac,end=" ")
'''
'''
n = int(input("Enter the value of n : "))
sum = 0
for x in range(1,n+1):
    sum = sum + x * x
print(sum,end=" ")
'''
# check weather it is prime or not prime number
'''
n = int(input("Enter a value of n : "))
s = 0 # switch off
for i in range(2,n):
    if n % i == 0:
        s = 1   # Switch On if not a prime
        break
if s == 0:
    print(n,"is Prime")
else:
    print(n,"Not Prime")
'''
'''
# maths tables
n = int(input("Enter a value of n : "))
for i in range(1,11):
    print(n,"X",i,"=",n * i)
'''
# this is the normal form of fibanocci series
# Fibanocci series : 0 , 1 ,1,2,3,5,8,13,....
'''fi= int(0)
se = int(1)
th = fi + se
fo = th + se
fv = fo + th
si = fv + fo
sev = si + fv
ei = sev + si
nine = ei + sev
ten = nine + ei
ele = ten + nine
print(fi,end=" ")
print(se,end=" ")
print(th,end=" ")
print(fo,end=" ")
print(fv,end=" ")
print(si,end=" ")
print(sev,end=" ")
print(ei,end=" ")
print(nine,end=" ")
print(ten,end=" ")
print(ele,end=" ")
'''
'''
# shortcut of fibanocci series 
f = 0
s = 1
print(f,s,end=" ")
# because i have printed first 2 number before itself remaining i required
n = int(input("Enter how much number of want : "))
for i in range(3,11) :
t = f + s
print(t,end=" ")
f = s
s = t
'''
'''
f = 0
s = 1
n = int(input("Enter the number terms: "))
print(f, end=" ")
print(s, end=" ")
for i in range(n):
    t = f + s
    print(t, end=" ")
    f = s
    s = t
'''
'''
f = 0
s = 1
n = int(input("Enter the number terms: "))
print(f, end=" ")
print(s, end=" ")
for i in range(2,n):
    t = f + s
    print(t, end=" ")
    f = s
    s = t
'''
'''
f = 0
s = 1
n = int(input("Enter the number terms: "))
print(f, end=" ")
print(s, end=" ")
for i in range(2,n):
    t = f + s
    print(t, end=" ")
    f = s
    s = t
'''
'''
# Nested Loop:
for i in range(1,5):
    for j in range(1,6):
        print(j,end=" ")
    print()
'''
'''
n = int(input("Enter the value of n : "))
for i in range(n+1):
    print(" ",end=" ")
    for j in range(i+1):
        print("_",end=" ")
        for k in range(j+1):
            print("*",end=" ")
    print()

''''''
for i in range(1,6):
    print("_",end=" ")
    for j in range(1,i+1):
        print("_",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
    '''
'''
n = int(input("Enter the value of n : "))
for i in range(1,n + 1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

'''
'''
n = int(input("Enter the value of n : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
'''
'''
n = int(input("Enter the value of n : "))
for i in range(1,n + 1):
    for j in range(1,i + n):
        print("*",end=" ")
    print()
    
'''
'''
print("      *")
print("    * *")
print("  * * *")
print("* * * *")
'''
'''
n = int(input("Enter the value of n : "))
for i in range(1,n + 1):

    for j in range(n - i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
'''
