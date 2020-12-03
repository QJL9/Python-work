import matplotlib.pyplot as plt
import matplotlib
from math import pi,sin
import numpy as np
x=np.linspace(-10,10,100)
f1=np.poly1d([1,2,3,4])
f2=np.polyder(f1)
f3=np.polyder(f1,2)

figure1= plt.figure(1, figsize=(15, 8),dpi=80)

plt.subplot(1,3,1)
plt.title('Polynomial')

plt.plot(x,f1(x),'r-')

plt.subplot(1,3,2)
plt.title('First Derivative')
plt.plot(x,f2(x),'b:')

plt.subplot(1,3,3)
plt.title('Second Derivative')
plt.plot(x,f3(x),'g.')


plt.show()