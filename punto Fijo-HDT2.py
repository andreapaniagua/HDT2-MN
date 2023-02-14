#Andrea Paniagua
#carne 18733
#seccion 20

from tabulate import tabulate
from sympy import *
#Funcion % de error
def error(a,b):
    x=abs((a-b)/a)*100
    return x
#Ejercicio 1
def func(a):
    x=symbols('x')
    F= (x**2 -3*x +1)
    f1=F.evalf(subs={x:a})
    return f1
#Ejercicio 2
def func2(a):
    x=symbols('x')
    F=asin(5/(9*exp(-x)))/(2*pi)
    f1=F.evalf(subs={x:a})
    return f1
#EJERCICIO 1 PUNTO FIJO
n=0
er=100
flag = True
imax=int(input("cuantas iteraciones desea: "))
err=float(input("ingrese el % de error deseado: "))
temp=100
x=float(input("ingrese un valor x_0: "))
l=[]
l.append([n,x,er])

while flag!=False:
    if  n>imax-2 or err>er :
        flag=False
    n+=1
    temp=float(x)
    x=float(func(temp))
    if x !=0:
        er=round(error(x,temp),15)
    l.append([n,x,er])
    
print(tabulate(l,headers=['n','x','%error']))


input("Presione enter")

#EJERCICIO 2 PUNTO FIJO
n=0
er=100
flag = True
imax=int(input("cuantas iteraciones desea: "))
err=float(input("ingrese el % de error deseado: "))
temp=100
x=float(input("ingrese un valor x_0: "))
l2=[]
l2.append([n,x,er])

while flag!=False:
    if  n>imax-2 or err>er :
        flag=False
    n+=1
    temp=float(x)
    x=float(func2(temp))
    if x !=0:
        er=round(error(x,temp),15)
    l2.append([n,x,er])
    
print(tabulate(l2,headers=['n','x','%error']))
