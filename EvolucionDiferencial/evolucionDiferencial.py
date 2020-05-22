'''
Created on 29 Octubre. 2018	
@author: González Zempoalteca Alfonso
evolucion diferencial
'''

import sys
import math
import aleatorios
import copy
sys.setrecursionlimit(10000)


cR = 0.6
f = 0.4


f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
f7 = 0
def solucionInicial(rang,tup):
	return aleatorios.arregleN(1,rang,tup)

def funcionDePrueba(n,vect):
	if n == 1:
		global f1
		f1 = f1 + 1 
		return aleatorios.funSchwefel(vect)
	elif n == 2:
		global f2
		f2 = f2 + 1 
		return aleatorios.funRosenbrock(vect)
	elif n == 3:
		global f3
		f3 = f3 + 1 
		return aleatorios.funPaso(vect)
	elif n == 4:
		global f4
		f4 = f4 + 1 
		return aleatorios.funMulSchwefel(vect)
	elif n == 5:
		global f5
		f5 = f5 + 1 
		return aleatorios.funMulRastrigin(vect)
	elif n == 6:
		global f6
		f6 = f6 + 1 
		return aleatorios.funMulAckley(vect)
	elif n == 7:
		global f7
		f7 = f7 + 1 
		return aleatorios.funMulGriewank(vect)

def iniciaHijo(n,tuplas):
	hijosV = []
	for i in range(n):
		for j in range(tuplas):
			hijo=solucionInicial(0,tuplas)
			hijosV.append(hijo)
	return hijosV

def mutantes(n,nTuplas,padresV,intervalo):
	mutante=[]
	mutantesV=[]
	for j in range(n):	
		for i in range(nTuplas):
			aleP=[]
			while len(aleP)<nTuplas:
				rnd = int(aleatorios.generaAleatorio(nTuplas))
				if rnd not in aleP:
					aleP.append(rnd)

			aleP.remove(i)
			m = padresV[j][aleP[0]]+f*(padresV[j][aleP[1]]-padresV[j][aleP[2]])
			if m > intervalo:
				m = intervalo
			elif m < -intervalo:
				m = -intervalo
			mutante.append(m)
		mutantesV.append(mutante)
		mutante=[]

	for i in range(n):
		mutantesV[i]
	return mutantesV	

def evolucionDiferencial(n,nTuplas,intervalo,criterioP,funcion,padresV):
	c = 0
	hijosV = iniciaHijo(4,5)
	while criterioP > c:
		mutantesV = mutantes(n,nTuplas,padresV,intervalo)

		for j in range(n):
			for i in range(nTuplas):
				r = aleatorios.generaAleatorio(1)
				if r < cR:
					hijosV[j][i]=copy.deepcopy(mutantesV[j][i])
				else:
					hijosV[j][i]=copy.deepcopy(padresV[j][i])	

		for i in range(n):
			fP = funcionDePrueba(funcion,padresV[i])
			fH = funcionDePrueba(funcion,hijosV[i])
			if fH < fP:
				padresV[i]=copy.deepcopy(hijosV[i])
			else:
				padresV[i]=padresV[i]

			#print(i,"valor funcion =  ", round(aleatorios.funSchwefel(padresV[i]),2))
		c=c+1
	return padresV

def inicio():
	semillero=aleatorios.semillero(6,30)
	print(semillero)
	criterioP=1000

	print("funSchwefel")
	for i in range(30):
		global f1
		f1 = 0
		padresV=[]
		mejorSolucion=[]
		aleatorios.nuevaSemilla(semillero[i])
		for j in range(4):
			padre=solucionInicial(10,5)
			padresV.append(padre)
		evolucionDiferencial(4,5,10,criterioP,1,padresV)# numeroVec,tamañoTuplas,rangoSolucion,nIteraciones,funcion,padres
		
		for k in range(4):
			mejorSolucion.append(round(funcionDePrueba(1,padresV[k]),4))
		print(min(mejorSolucion))
	print("llamadas a la funcion ",f1)
	
	print("funRosenbrock")
	for i in range(30):
		global f2
		f2 = 0
		padresV=[]
		mejorSolucion=[]
		aleatorios.nuevaSemilla(semillero[i])
		for j in range(4):
			padre=solucionInicial(30,5)
			padresV.append(padre)
		evolucionDiferencial(4,5,30,criterioP,2,padresV)# numeroVec,tamañoTuplas,rangoSolucion,nIteraciones,funcion,padres
		
		for k in range(4):
			mejorSolucion.append(round(funcionDePrueba(2,padresV[k]),4))
		print(min(mejorSolucion))
	print("llamadas a la funcion ",f2)

	print("funPaso")
	for i in range(30):
		global f3
		f3 = 0
		padresV=[]
		mejorSolucion=[]
		aleatorios.nuevaSemilla(semillero[i])
		for j in range(4):
			padre=solucionInicial(100,5)
			padresV.append(padre)
		evolucionDiferencial(4,5,100,criterioP,3,padresV)# numeroVec,tamañoTuplas,rangoSolucion,nIteraciones,funcion,padres
		
		for k in range(4):
			mejorSolucion.append(round(funcionDePrueba(3,padresV[k]),4))
		print(min(mejorSolucion))
	print("llamadas a la funcion ",f3)
	
	print("funMulSchwefel")
	for i in range(30):
		global f4
		f4 = 0
		padresV=[]
		mejorSolucion=[]
		aleatorios.nuevaSemilla(semillero[i])
		for j in range(4):
			padre=solucionInicial(500,5)
			padresV.append(padre)
		evolucionDiferencial(4,5,500,criterioP,4,padresV)# numeroVec,tamañoTuplas,rangoSolucion,nIteraciones,funcion,padres
		
		for k in range(4):
			mejorSolucion.append(round(funcionDePrueba(4,padresV[k]),4))
		print(min(mejorSolucion))
	print("llamadas a la funcion ",f4)

	print("funMulRastrigin")
	for i in range(30):
		global f5
		f5 = 0
		padresV=[]
		mejorSolucion=[]
		aleatorios.nuevaSemilla(semillero[i])
		for j in range(4):
			padre=solucionInicial(5.2,5)
			padresV.append(padre)
		evolucionDiferencial(4,5,5.2,criterioP,5,padresV)# numeroVec,tamañoTuplas,rangoSolucion,nIteraciones,funcion,padres
		
		for k in range(4):
			mejorSolucion.append(round(funcionDePrueba(5,padresV[k]),4))
		print(min(mejorSolucion))
	print("llamadas a la funcion ",f5)
	
	print("funMulAckley")
	for i in range(30):
		global f6
		f6 = 0
		padresV=[]
		mejorSolucion=[]
		aleatorios.nuevaSemilla(semillero[i])
		for j in range(4):
			padre=solucionInicial(32,5)
			padresV.append(padre)
		evolucionDiferencial(4,5,32,criterioP,6,padresV)# numeroVec,tamañoTuplas,rangoSolucion,nIteraciones,funcion,padres
		
		for k in range(4):
			mejorSolucion.append(round(funcionDePrueba(6,padresV[k]),4))
		print(min(mejorSolucion))
	print("llamadas a la funcion ",f6)

	print("funMulGriewank")
	for i in range(30):
		global f7
		f7 = 0
		padresV=[]
		mejorSolucion=[]
		aleatorios.nuevaSemilla(semillero[i])
		for j in range(4):
			padre=solucionInicial(600,5)
			padresV.append(padre)
		evolucionDiferencial(4,5,600,criterioP,7,padresV)# numeroVec,tamañoTuplas,rangoSolucion,nIteraciones,funcion,padres
		
		for k in range(4):
			mejorSolucion.append(round(funcionDePrueba(7,padresV[k]),4))
		print(min(mejorSolucion))
	print("llamadas a la funcion ",f7)
	

inicio()