'''
Created on 2 Noviembre. 2018	
@author: González Zempoalteca Alfonso
Sudoku
'''
import sys
import math
import aleatorios
import tablaSudoku
import copy
sys.setrecursionlimit(10000)
tempInicial = 120
tempFinal= 0.01
factorEnfriamiento=0.80
iteracionTemp=160
def solucionInicial(tabla):
	for j in range(len(tabla)):
		b=[]
		while len(b)<9:
			r = int(aleatorios.generaAleatorio(9))+1
			if r not in b:
				b.append(r)
		for i in range(len(tabla[j])):
			if tabla[j][i][0] in b:
				b.remove(tabla[j][i][0])
		for i in range(len(tabla[j])):
			if tabla[j][i][1]==False:
				if len(b)>0:
					tabla[j][i][0]=b.pop()

	return tabla

def penalizacion(tabla):
	penF=[]
	penC=[]
	for t in range(3):
		for k in range(3):
			b=[]
			for i in range(t*3,t*3+3):
				for j in range(k*3,k*3+3):
					if tabla[i][j][0] not in b:	
						b.append(tabla[i][j][0])
			penF.append(9-len(b))
	
	for t in range(3):
		for k in range(3):
			c=[]
			for i in range(3):
				for j in range(3):
					if tabla[i*3+t][j*3+k][0] not in c:	
							c.append(tabla[i*3+t][j*3+k][0])
			penC.append(9-len(c))				
	#print(penC)
	#print(penF)
	return sum(penC)+sum(penF)

def vecindario(tabla):
	j=int(aleatorios.generaAleatorio(9)) #cuadrante
	k=int(aleatorios.generaAleatorio(9)) #casilla 1
	a = int(aleatorios.generaAleatorio(9)) #casilla 2
	if tabla[j][k][1]==False:
		if tabla[j][a][1]==False:
			aux = tabla[j][k][0]
			tabla[j][k][0]=tabla[j][a][0]
			tabla[j][a][0]=aux
	return tabla
def metropoli(tablaA,tabla,t):
	fS = penalizacion(tabla)
	fo = penalizacion(tablaA)
	r = aleatorios.generaAleatorio(1)
	e = math.exp((-1*(fS-fo))/t)
	if(r<e):
		return tabla
	else:
		return tablaA

def enfriamiento(t):
	return t * factorEnfriamiento

def recosidoSimulado(tF,tI,l):
	tabla = tablaSudoku.hardB()
	solucionInicial(tabla)
	mejorS = tabla
	while tI>tF:
		for i in range(l):
			tablaAnterior = copy.deepcopy(tabla)
			tabla = vecindario(tabla)
			fS = penalizacion(tabla)
			fo = penalizacion(tablaAnterior)
			if fS < fo:
				mejorS = tabla
			else:
				mejorS = copy.deepcopy(metropoli(tablaAnterior,tabla,tI))
				tabla = mejorS
		tI=enfriamiento(tI)
	return mejorS

def inicio():
	print("Sudoku hardB segundo parametros")
	semillero = aleatorios.semillero(6,30)
	for i in range(len(semillero)):
		aleatorios.nuevaSemilla(semillero[i])
		tabla = recosidoSimulado(tempFinal,tempInicial,iteracionTemp)
		print(penalizacion(tabla))
	
inicio()