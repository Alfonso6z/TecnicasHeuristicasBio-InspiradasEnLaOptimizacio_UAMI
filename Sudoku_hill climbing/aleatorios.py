'''
@author: González Zempoalteca Alfonso
Metodo Congruencial Multiplicativo

Xi+1=(a*Xi)mod(m)
a = constante multiplicativa 		a = 3 + 8K ó 5 + 8K  k=1,2,3,,,,
X0 = semilla con D digitos			debe ser impar
m = periodo o ciclo de vida			m = 2^g  g = es un numero entero

Fenerador de números aleatorios

'''
import sys
import math
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

def funSchwefel(vect):
	mi=0
	s=0
	ms=1
	for j in range(len(vect[0])):
		s=s+(vect[0][j]**2)
		ms=abs(vect[0][j])*ms
	mi=s*ms
	return mi
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
				valx.append(-1*x)
			else:
				valx.append(x)
		for i in range(cant):
			y=generaAleatorio(rang)
			rdn=generaAleatorio(1)
			if(rdn<0.5):
				valy.append(-1*y)
			else:
				valy.append(y)
		for i in range(cant):
			z=generaAleatorio(rang)
			rdn=generaAleatorio(1)
			if(rdn<0.5):
				valz.append(-1*z)
			else:
				valz.append(z)
		if tup == 5:
			for i in range(cant):
				a=generaAleatorio(rang)
				rdn=generaAleatorio(1)
				if(rdn<0.5):
					vala.append(-1*a)
				else:
					vala.append(a)
			for i in range(cant):
				b=generaAleatorio(rang)
				rdn=generaAleatorio(1)
				if(rdn<0.5):
					valb.append(-1*b)
				else:
					valb.append(b)
		for i in range(cant):
			aux=[]
			aux.append(valx[i])
			aux.append(valy[i])
			aux.append(valz[i])
			if tup == 5:
				aux.append(vala[i])
				aux.append(valb[i])
			vector.append(aux)
	return vector
def funRosenbrock(vect):
	s=0
	for j in range(len(vect[0])-1):
		s=s+(100*(vect[0][j+1]-(vect[0][j]**2))**2)+(vect[0][j])**2
	return s

def funPaso(vect):
	s=0
	for j in range(len(vect[0])):
		s=s+math.floor((vect[0][j]+0.5)**2)
	return s	
def funMulSchwefel(vect):
	s=0
	res=0
	aux=0
	
	for j in range(len(vect[0])):
		s=s+vect[0][j]*math.sin(abs((vect[0][j]))**(1/2))
	res=418.9829-s
	return res

def funMulRastrigin(vect):
	s=0
	aux=0	
	for j in range(len(vect[0])):
		s=s+((vect[i][j])**2)-10*math.cos((2*math.pi)*vect[i][j])+10
	return s
def funMulAckley(vect):
	v=0.0
	sc=0
	s=0
	aux=0
	for j in range(len(vect[0])):
		s=float(s+(((vect[0][j])**tup))**(1/2))
		sc=sc+math.cos((2*math.pi)*vect[0][j])
	v=-20*(math.exp(-0.2*((1/tup)*s)))
	return v


