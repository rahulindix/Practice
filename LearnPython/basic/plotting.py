import matplotlib.pyplot as plt
import math
import numpy as np

def f(x): 
  return (x-0.02)*(x-0.05)+5

def df(x):
  return 2*x-0.07

#x=np.linspace(-5.0,5.0,10)
#y=map(lambda i:f(i),x)
#dy=map(lambda i:df(i),x)
#print x
#print y
#print dy
def gradient_descent(curx,alpha,precision,iterations):
  i=0
  output=list()
  slopes=list()
  slope = df(curx)
  output.append(curx)
  slopes.append(slope)
  while i<iterations:
    prevx=curx
    slope = df(prevx)
    curx+=-1*alpha*slope
    output.append(curx)
    slopes.append(slope)
    step_size=abs(curx-prevx)
    if step_size<precision:
      break
    i+=1
  return (output,slopes)

curx=-10
alpha=0.0001
precision=0.000001
iterations=10000
(min_at,slopes)=gradient_descent(curx,alpha,precision,iterations)
print min_at
print slopes
print len(min_at)
print len(slopes)
print "Min Occurs at=",min_at[-1]
print "Min func val=",f(min_at[-1])

x = np.linspace(min(min_at),max(min_at),len(min_at))
fx= map(lambda i: f(i), x)
y = min_at
plt.figure(1)
plt.plot(x,min_at,'g')
plt.plot(x,slopes,'b')

plt.figure(2)
plt.plot(x,fx,'r')
plt.show()

