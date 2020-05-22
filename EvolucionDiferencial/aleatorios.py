'''
Created on 24 Septiembre. 2018	
@author: González Zempoalteca Alfonso
Metodo Congruencial Multiplicativo

Xi+1=(a*Xi)mod(m)
a = constante multiplicativa 		a = 3 + 8K ó 5 + 8K  k=1,2,3,,,,
X0 = semilla con D digitos			debe ser impar
m = periodo o ciclo de vida			m = 2^g  g = es un numero entero

'''
import sys
import math
import numpy as np
sys.setrecursionlimit(10000)
xcero = 677 
k = 5
ai = 3 + (8*k)
g = 31
m = 2**g
semilla = 6
def semillero(inicial,n):
	semillas=[]
	for i in range(n):
		inicial=inicial+6
		semillas.append(inicial)
	return semillas

def nuevaSemilla(n):
	global semilla
	semilla = n

def generaAleatorio(inter):
	c=0
	global semilla
	semilla = (ai*semilla)%m;
	r = semilla/(m-1)
	#print(round(r,7))
	c=r*inter
	return c

def arregleN(cant,rang,tup):
	rdn=[]
	valx=[]
	valy=[]
	valz=[]
	vala=[]
	valb=[]
	vector=[]
	if tup>=3:	

		for i in range(cant):
			x=generaAleatorio(rang)
			rdn=generaAleatorio(1)
			if(rdn<0.5):
				vector.append(-1*x)
			else:
				vector.append(x)

		for i in range(cant):
			y=generaAleatorio(rang)
			rdn=generaAleatorio(1)
			if(rdn<0.5):
				vector.append(-1*y)
			else:
				vector.append(y)

		for i in range(cant):
			z=generaAleatorio(rang)
			rdn=generaAleatorio(1)
			if(rdn<0.5):
				vector.append(-1*z)
			else:
				vector.append(z)

		if tup == 5:
			for i in range(cant):
				a=generaAleatorio(rang)
				rdn=generaAleatorio(1)
				if(rdn<0.5):
					vector.append(-1*a)
				else:
					vector.append(a)

			for i in range(cant):
				b=generaAleatorio(rang)
				rdn=generaAleatorio(1)
				if(rdn<0.5):
					vector.append(-1*b)
				else:
					vector.append(b)
	return vector

def funSchwefel(vect):
	mi=0
	s=0
	ms=1
	for j in range(len(vect)):
		s=s+(vect[j]**2)
		ms=abs(vect[j])*ms
	mi=s*ms
	return mi

def funRosenbrock(vect):
	s=0
	for j in range(len(vect)-1):
		s=s+(100*(vect[j+1]-(vect[j]**2))**2)+(vect[j])**2
	return s

def funPaso(vect):
	s=0
	for j in range(len(vect)):
		s=s+math.floor((vect[j]+0.5)**2)
	return s

def funMulSchwefel(vect):
	s=0
	res=0
	aux=0
	for j in range(len(vect)):
		s=s+vect[j]*(math.sin(abs((vect[j]))**(1/2)))
	res=418.9829-s
	return res

def funMulRastrigin(vect):
	s=0
	for j in range(len(vect)):
		s=s+((vect[j])**2)-10*math.cos((2*math.pi)*vect[j])+10
	return s
def funMulAckley(vect):
	s1 = 0
	s2 = 0
	for i in range(len(vect)):
		s1 = s1 + (vect[i]**len(vect))
		s2 = s2 + (math.cos((2*math.pi*vect[i])))

	return -20*np.exp(-0.2*(((s1)/len(vect)))**1/2)-np.exp(s2/len(vect))+20+np.exp(1)

def funMulGriewank(vect):
	s1 = 0
	s2 = 0
	for i in range(len(vect)):
		s1 = s1 + vect[i]**2
		s2 = s2*(math.cos(vect[i]/((i+1)**1/2)))

	return (s1/4000)-s2+1

def inicio():
		'''print("Schwefel 3 = ",funSchwefel(1000,10,3))
		print("Schwefel 5 = ",funSchwefel(1000,10,5))
		print("Rosenbrock 3 = ",funRosenbrock(1000,30,3))
		print("Rosenbrock 5 = ",funRosenbrock(1000,30,5))
		print("Paso 3 = ",funPaso(1000,100,3))
		print("Paso 5 = ",funPaso(1000,100,5))
		print("MulSchwefel 3 = ",funMulSchwefel(1000,100,3))
		print("MulSchwefel 5 = ",funMulSchwefel(1000,100,5))
		print("Rastrigin 3 = ",funMulRastrigin(1000,100,3))
		print("Rastrigin 5 = ",funMulRastrigin(1000,100,5))'''


