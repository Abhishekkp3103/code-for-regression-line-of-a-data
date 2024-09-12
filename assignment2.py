import matplotlib.pyplot as plt
x=[0,5,10,15,20,25]
y=[1,15,17,22,24,30]
sx=sum(x)
sy=sum(y)
sxsy=sx*sy
n=len(x)
sx2=sx*sx
sxx=[]
xy=[]
for i in range(len(x)):
    c=x[i]**2
    d=x[i]*y[i]
    xy.append(d)
    sxx.append(c)
x2=sum(sxx)
sxy=sum(xy)
b=(sxsy-(n*sxy))/(sx2 -(n*x2))
print('value of b is: ',b)
a=2-b
print('value of a is:',a)
n=int(input('enter number of coordinates to be plotted:'))
y1=[]
x1=[]
for z in range(n):
    x1.append(z)
    w=2+z
    y1.append(w)
print(x1)
print(y1)
plt.plot(x1,y1)
plt.scatter(x,y)
plt.xlabel('x1')
plt.ylabel('y1')
plt.title('regression line')
plt.show()


              