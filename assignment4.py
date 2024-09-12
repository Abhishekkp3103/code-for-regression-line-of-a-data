import math
import matplotlib.pyplot as plt
v=[350,400,50,600]
t=[61,26,7,2.6]
x=(v[1]/v[0])-(t[1]/t[0])
b=math.log(x)
g=float(b)
a=v[0]/(t[0]**b)
print(a)
print(b)
n=int(input('enter number of coordinate you want to plot:'))
v1=[]
t1=[]
for i in range(1,n):
    v1.append(i)
    if b>=0:
        c=(i/a)**(1/b)
        t1.append(c)
    else:
        f=(a/i)**(1/g)
        t1.append(f)
print(v1)
print(t1)
plt.plot(v1,t1)
plt.scatter(v,t)
plt.xlabel('v1')
plt.ylabel('t1')
plt.title('regression line of v=at^b')
plt.show()