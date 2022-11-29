print('employee name')
a=str(input())
print('enter phone number')
b=int(input())
print('basic salary of employee')
c=int(input())
print('travelling charges')
d=int(input())
print('house rent')
e=int(input())
net=c+d+e
print('net salary :',net)
if net>100000:
    tax=net*10/100
elif net>50000:
    tax=net*7/100
elif net>40000:
    tax=net*4/100 
elif net>20000:
    tax=net*2/100  
elif net<20000:
    tax=net*0
print('tax:',tax)