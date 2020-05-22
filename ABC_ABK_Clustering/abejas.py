'''
Created on 3 Diciembre. 2018	
@author: González Zempoalteca Alfonso
'''

import sys
import math
import numpy as np
import aleatorios

sys.setrecursionlimit(10000)

fuentesDeAlimento = []
costoDeFuenteAlimento=[]
costoR=[]
cambio=[]
limitecambios=15
dimencion = 2
nGrupos = 3
fitness=0.0
cantidadDeFuenteAlimento = 10
llamadasALaFoncion = 0
archivo= open ('datos.txt','r')
lineas = len(open('datos.txt').readlines())

def recolectaDatos():
	datos=[]
	datosN=[]
	for i in range(lineas):
		dato=archivo.readline().split()
		datos.append(dato)
	for i in range(lineas):
		d1=[]
		for j in range(dimencion):
			d = float(datos[i][j]);
			d1.append(d)
		datosN.append(d1)
	return datosN

def seleccionaCentroide(datos):
	i = 0
	centroides=[]
	while i < nGrupos:
		r = int(aleatorios.generaAleatorio(lineas))
		if r not in centroides:
			centroides.append(r)
			i=i+1
	for i in range(len(centroides)):
		centroides[i]=datos[centroides[i]]

	return centroides

def distancia(x,y):
	distancias = []
	suma = 0
	for i in range(dimencion):
		d = (x[i]-y[i])**2
		suma = suma + d
	return suma

def aptitud(datos,centroides):
	global llamadasALaFoncion
	llamadasALaFoncion = llamadasALaFoncion+1
	fit = 0
	for i in range(lineas):
		distancias=[]
		for j in range(len(centroides)):
			distancias.append(distancia(centroides[j],datos[i]))
		indice = distancias.index(min(distancias))
		#suma de las distancias para sacar fitnnes( distance = min(i,j))
		fit = fit+min(distancias)
	#calcular el fitnnes segun la formula de la lectura
	return fit/lineas

def K_Means(datos,centroides):
	clusters =  []
	c1=[]
	c2=[]
	c3=[]
	for i in range(lineas):
		distancias=[]
		for j in range(len(centroides)):
			distancias.append(distancia(centroides[j],datos[i]))
		indice = distancias.index(min(distancias))
		if indice == 0:
			c1.append(datos[i])
		elif indice == 1:
			c2.append(datos[i]) 
		else:
			c3.append(datos[i])
	clusters.append(c1)
	clusters.append(c2)
	clusters.append(c3)
	#calcular el fitnnes segun la formula de la lectura
	return clusters
def inicio():
	centroidesM=[]
	soluciones = []
	mejorSolucion = 0
	peorSolucion = 0
	semillero = aleatorios.semillero(6,30) #inicia semillero 
	aleatorios.nuevaSemilla(semillero[0]) #inicia semilla
	datos = []
	print("Clostering con ABK")
	datos = recolectaDatos() # recolectar los datos de txt
	#en este punto ya tenemos nuestor 3 gurpos en poblacion inicial

	for c in range(30):
		global llamadasALaFoncion
		llamadasALaFoncion = 0
		aleatorios.nuevaSemilla(semillero[c])
		generaciones = 0
		for i in range(cantidadDeFuenteAlimento):
			fuentesDeAlimento.append(seleccionaCentroide(datos))
			costoDeFuenteAlimento.append(aptitud(datos,fuentesDeAlimento[i]))	
			costoR.append(aptitud(datos,fuentesDeAlimento[i]))
			cambio.append(0)

		mejorConocida=fuentesDeAlimento[0]
		mejorCosto=aptitud(datos,mejorConocida)
		FuenteVecina=seleccionaCentroide(datos)	

		while  llamadasALaFoncion <= 10000:
			#abejas empleadas
			for i in range(cantidadDeFuenteAlimento):
				j=i
				while j == i:
					j = int(aleatorios.generaAleatorio(cantidadDeFuenteAlimento))
				for k in range(nGrupos):
					resultado = []
					signo = aleatorios.generaAleatorio(1)
					r = aleatorios.generaAleatorio(1)
					if signo > 0.5:
						r=r*-1
					resX = fuentesDeAlimento[i][k][0] + r*(fuentesDeAlimento[i][k][0]-fuentesDeAlimento[j][k][0])
					resY = fuentesDeAlimento[i][k][1] + r*(fuentesDeAlimento[i][k][1]-fuentesDeAlimento[j][k][1])
					resultado.append(resX)	
					resultado.append(resY)
					FuenteVecina[k] = resultado
					cost = aptitud(datos,FuenteVecina)
					if(costoDeFuenteAlimento[i]>=cost):
						fuentesDeAlimento[i] = FuenteVecina
						costoDeFuenteAlimento[i]=cost
						cambio[i]=0
						if(mejorCosto>=cost):
							mejorCosto = cost
							mejorConocida = FuenteVecina
						FuenteVecina=seleccionaCentroide(datos)
					else:
						cambio[i]=cambio[i]+1
			#terminas las abejas empleadas
			#abejas observadoras
			for i in range(cantidadDeFuenteAlimento):
				fitness = 0.0
				maximo = max(costoDeFuenteAlimento)
				for i in range(cantidadDeFuenteAlimento):
					costoR[i]=maximo-costoDeFuenteAlimento[i]
				pi = costoR[i]/sum(costoR)
				r = aleatorios.generaAleatorio(1)
				if r < pi:
					j=i
					while j == i:
						j = int(aleatorios.generaAleatorio(cantidadDeFuenteAlimento))
					for k in range(nGrupos):
						resultado = []
						signo = aleatorios.generaAleatorio(1)
						r = aleatorios.generaAleatorio(1)
						if signo > 0.5:
							r=r*-1
						resX = fuentesDeAlimento[i][k][0] + r*(fuentesDeAlimento[i][k][0]-fuentesDeAlimento[j][k][0])
						resY = fuentesDeAlimento[i][k][1] + r*(fuentesDeAlimento[i][k][1]-fuentesDeAlimento[j][k][1])
						resultado.append(resX)	
						resultado.append(resY)
						FuenteVecina[k] = resultado
						cost = aptitud(datos,FuenteVecina)
						if(costoDeFuenteAlimento[i]>=cost):
							fuentesDeAlimento[i] = FuenteVecina
							costoDeFuenteAlimento[i]=cost
							cambio[i]=0
							if(mejorCosto>=cost):
								mejorCosto = cost
								mejorConocida = FuenteVecina
							FuenteVecina=seleccionaCentroide(datos)
						else:
							cambio[i]=cambio[i]+1
			#terminanObservadoras

			#inician exploradoras
			for i in range(cantidadDeFuenteAlimento):
				if cambio[i]>=limitecambios:
					fuentesDeAlimento[i]=seleccionaCentroide(datos)
					costoDeFuenteAlimento[i]=aptitud(datos,fuentesDeAlimento[i])
					cambio[i]=0
			generaciones=generaciones+1
	#terminan generaciones
		centroidesM.append(mejorConocida)
		soluciones.append(aptitud(datos,mejorConocida))
		print("Semilla = ",semillero[c],"Mejor Solucion = ", aptitud(datos,mejorConocida))
		#print("llamadas a la funcion = : ",llamadasALaFoncion)
	indice = soluciones.index(min(soluciones))
	print("Mejor solucion ",min(soluciones))
	print("Peor solucion",max(soluciones))
	print("promedio = ",sum(soluciones)/30)
	print("indice de la mejorSolucion",indice)

	clusteringFinal = K_Means(datos,centroidesM[indice])
	for i in range(nGrupos):
		for j in range(len(clusteringFinal[i])):
			for k in range(dimencion):
				print(clusteringFinal[i][j][k],end=' ')
			print()
inicio()
