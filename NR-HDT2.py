#Andrea Paniagua
#carne 18733
#seccion 20

import math
from tabulate import tabulate
from sympy import *

#Ejercicio 1
def func(a):
    x=symbols('x')
    F=(x**3+2524*x**2+3783)
    f1=F.evalf(subs={x:a})
    dx=diff(F,x)
    f2=dx.evalf(subs={x:a})
    f=f1/f2
    return f
#Función de % de error
def error(a,b):
    x=abs((a-b)/a)*100
    return x

#EJERCICIO 1 NEWTON-RHAPSON
flag =True
temp=int(input("ingrese cuantas iteraciones desea: "))
xn=0
x=float(input("ingrese un número x_0: "))
er=100
err=float(input("cual es el % de error deseado: "))
n=0
l=[]
l.append([n,x,xn,er])
while flag!=False:
    if n==temp or err>er:
        flag=False
    n+=1
    f=func(x)
    temp=xn
    xn=x-f
    x=xn
    er=error(x,temp)
    l.append([n,x,xn,er])
print(tabulate(l,headers=['n','x','xn','%error']))

input("presione enter")
