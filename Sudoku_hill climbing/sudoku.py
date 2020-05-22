'''
Created on 9 Octubre. 2018	
@author: González Zempoalteca Alfonso
Sudoku

'''
import sys
import math
import aleatorios
import tablaSudoku
import copy
sys.setrecursionlimit(10000)

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

def vecindario1(tabla):
	tablaAnterior = copy.deepcopy(tabla)
	pA = penalizacion(tablaAnterior)
	j = int(aleatorios.generaAleatorio(9))
	b=[]

	while len(b)<9:
		a = int(aleatorios.generaAleatorio(9))+1
		if a not in b:
			b.append(a)

	for i in range(len(tabla[j])):
		if tabla[j][i][1]==False:
			tabla[j][i][0]=0

	for i in range(len(tabla[j])):
		if tabla[j][i][0] in b:
			b.remove(tabla[j][i][0])

	for i in range(len(b)):
		if tabla[j][i][1]==False:
			tabla[j][i][0]=b.pop()

	pS = penalizacion(tabla)	
	if pS<pA:
		return tabla
	else:
		return tablaAnterior

def vecindario2(tabla):
	tablaAnterior = copy.deepcopy(tabla)
	pA = penalizacion(tablaAnterior)
	j=int(aleatorios.generaAleatorio(9)) #cuadrante
	k=int(aleatorios.generaAleatorio(9)) #casilla 1
	a = int(aleatorios.generaAleatorio(9)) #casilla 2

	if tabla[j][k][1]==False:
		if tabla[j][a][1]==False:
			aux = tabla[j][k][0]
			tabla[j][k][0]=tabla[j][a][0]
			tabla[j][a][0]=aux
	pS = penalizacion(tabla)
	if pS<pA:
		return tabla
	else:
		return tablaAnterior

def firstImprovement(tabla,vecindario,numeroI):
	p = penalizacion(tabla)
	if(vecindario==1):		
		while numeroI >0:
			tabla=vecindario1(tabla)
			p=penalizacion(tabla)
			#print(p)
			numeroI=numeroI-1
		#print("termine")
		print(p)
		#tablaSudoku.imprimeSudoku(tabla)

	elif vecindario==2:
		while numeroI >0:
			tabla=vecindario2(tabla)
			p=penalizacion(tabla)
			#print(p)
			numeroI=numeroI-1
		#print("termine")
		print(p)
		#tablaSudoku.imprimeSudoku(tabla)
	else:
		print("Elige un vecindario 1 o 2")

def inicio():
	print("Sudoku hardB")
	semillero=aleatorios.semillero(6,30)
	tabla = tablaSudoku.hardB()
	#print(semillero)
	#tablaSudoku.imprimeSudoku(tabla)
	for i in range(len(semillero)):
		aleatorios.nuevaSemilla(semillero[i])
		tabla=solucionInicial(tabla)
		firstImprovement(tabla,1,10000)
	print("vecindario2")
	for i in range(len(semillero)):
		aleatorios.nuevaSemilla(semillero[i])
		tabla=solucionInicial(tabla)
		firstImprovement(tabla,2,10000)
inicio()