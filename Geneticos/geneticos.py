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

m=0.01

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

def binarizar(real):
    binario = ''
    binario2 = ''
    aux1=int(real)
    aux2=str(real-int(real))[2:]
    aux2=int(aux2)
    while aux1 // 2 != 0:
        binario = str(aux1 % 2) + binario
        aux1 = aux1 // 2
    binariofinal=str(aux1) + binario + '.'
    while aux2 // 2 != 0:
        binario2 = str(aux2 % 2) + binario2
        aux2 = aux2 // 2
    binariofinal=binariofinal + str(aux2) + binario2
    return binariofinal


def areal(binario):
    aux0 = 1
    aux1 = ''
    aux2 = ''
    cont1 = 0
    for i in range(len(binario)):
    	if cont1 == 0:
    		if binario[0] == '0':
    			aux0=-1
    		else:
    			aux0 = 1
    		cont1 = 1		
    	else :		
	        if i < 6:
	            aux1=aux1+binario[i]
	        else:
	            aux2=aux2+binario[i]

    aux1=int(aux1,2)
    aux2=int(aux2,2)
    real=''
    real=str(aux1)+'.'+str(aux2)
    real=aux0*float(real)
    return real

def ruleta(costos):
	costor = copy.deepcopy(costos)
	for i in range(5):
		fitness=0.0
		mini=costos[0]

		for j in range(1,5):
			if mini > costos[j]:
				mini = costos[j]

		mini=mini+1
		for j in range(5):
		    costor[j]=mini-costos[j]
		    fitness=fitness+costor[j]

		r=aleatorios.generaAleatorio(1)
		x=0
		fitnessparcial=costor[0]/fitness
		while (r>fitnessparcial):
		    x=x+1
		    fitnessparcial=fitnessparcial+(costor[x]/fitness)
		j=x
	return j

def inicio():
	aleatorios.nuevaSemilla(45454)
	padres = []
	padresB = []
	costo = []
	for i in range(5):
		padre = []
		for k in range(3):
			x = ''
			for j in range(11):
				r = aleatorios.generaAleatorio(1)
				if r < 0.5:
					x = x +'0'
				else:
					x = x + '1'
			padre.append(x)
		padres.append(padre)
	padresB = copy.deepcopy(padres)
	for i in range(5):
		for j in range(3):
			padresB[i][j] = areal(padres[i][j])	
	
	for i in range(5):
		costo.append(aleatorios.funMulGriewank(padresB[i]))

	


inicio()