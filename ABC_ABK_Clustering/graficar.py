'''
Created on 7Di. 2018	
@author: González Zempoalteca Alfonso
Metodo Congruencial Multiplicativo

Xi+1=(a*Xi)mod(m)
a = constante multiplicativa 		a = 3 + 8K ó 5 + 8K  k=1,2,3,,,,
X0 = semilla con D digitos			debe ser impar
m = periodo o ciclo de vida			m = 2^g  g = es un numero entero

'''
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from matplotlib import pyplot as plt
datos = pd.read_csv('datosO.txt',header=0,delim_whitespace=True)
x = datos.ix[0:29,0]
y = datos.ix[0:29,1]
x1 = datos.ix[30:59,0]
y1 = datos.ix[30:59,1]
x2 = datos.ix[60:89,0]
y2 = datos.ix[60:89,1]
print(datos)
print(x)
print(y)

plt.plot(x,y,'ro',x1,y1,'go',x2,y2,'bo')
plt.ylabel('Y')
plt.xlabel('X')
plt.show