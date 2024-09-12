import matplotlib.pyplot as plt
A=[50,450,780,1200,4400,4800,5300]
D=[28,30,32,36,51,58,69]
b=(D[1]/D[0])**(1/(A[1]-A[0]))
a=D[0]/(b**A[0])
n=int(input('enter number of coordinates to plot:'))
x1=[]
y1=[]
for i in range(n):
    x1.append(i)
    c=a*(b**i)
    y1.append(c)
print(x1)
print(y1)
plt.plot(x1,y1)
plt.scatter(A,D)
plt.xlabel('x1')
plt.ylabel('y1')
plt.title("regression line of ab^x")
plt.show()