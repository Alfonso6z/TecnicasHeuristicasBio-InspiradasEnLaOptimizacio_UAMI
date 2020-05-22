global seed
seed=3
global llamadasfuncion
llamadasfuncion=0
import collections
import math

# Al llamar a la funcion generadorLCG se da como entrada la semilla y la cantidad
# de aleatorios que se desea obtener.
def generadorLCG(semilla,cantidadaleatorios):
    m=pow(2,31)
    global seed
    semilla=seed
    a=314159269
    c=453806245
    z=[0]
    z[0]=semilla
    aleatorios=[]
    for i in range(cantidadaleatorios):
        z.append(((a*z[i])+c)%m)
    for j in range(len(z)-1):
        aleatorios.append(round(float(z[j+1])/m,5))
    seed=(seed+1)%m
    return aleatorios

#Esta funcion genera numeros aleatorios dentro del rango dado.
def generadorLCGrango(semilla,cantidadaleatorios,rango):
    m=pow(2,31)
    a=314159269
    c=453806245
    global seed
    semilla=seed
    z=[0]
    z[0]=semilla
    aleatorios=[]
    x1=rango[0]
    x2=rango[1]
    if rango[0]<0:
        x1=x1*-1
    for i in range(cantidadaleatorios):
            z.append(((a*z[i])+c)%m)
    for j in range(len(z)-1):
        if rango[0]==1:
            aleatorios.append(round(((x2)*(float(z[j+1])/m))-.1,5))
        else:
            aleatorios.append(round(((x1+x2)*(float(z[j+1])/m))-x2,5))
    seed=(seed+1)%m
    return aleatorios


#Funcion para obtener la media
def media(m):
    aux=0
    for i in m:
        aux=aux+i
    return (float(aux)/len(m))

# Funcion para obtener la desviacion
def desviacion(m):
    x=media(m)
    aux=0
    for i in m:
        res=pow((i-x),2)
        aux=aux+res
    if len(m)>1:
        desv=(aux/(len(m)-1))
    else:
        desv=(aux/(len(m)))
    desv=pow(desv,0.5)
    return desv

#Funcion de Griewank multimodal
def griewank(lista):
    costo=0
    aux3=0
    aux4=0
    res1=0
    res2=1
    res3=0
    res4=0
    for j in range(len(lista)):
        aux3=(lista[j]*lista[j])
        res1=res1+aux3
        aux4=math.cos(lista[j]/math.sqrt(j+1))
        res2=res2*aux4
    res3=(float(1)/4000)*res1
    res4=res3-res2+1
    costo=round(res4,4)

    return costo

#Numero maximo de llamadas a la funcion objetivo igual a 10,000
Particulas=[]
Mp=[]
velocidades=[]
costosparticulas=[]
mejorescostosp=[]
r1=0.7
r2=0.3
for i in range(4):
	Particulas.append(generadorLCGrango(seed,5,(-600,600)))
	Mp.append(Particulas[i][:])
for i in range(4):
	aux=[]
	for j in range(5):
		aux.append(0.0)
	velocidades.append(aux)

mejorcosto=griewank(Particulas[0])
mejorconocido=Particulas[0][:]
for i in Particulas:
	if (griewank(i)<mejorcosto):
		mejorcosto=griewank(i)
		mejorconocido=i[:]

for i in range(4):
	costosparticulas.append(griewank(Particulas[i]))
	mejorescostosp.append(griewank(Mp[i]))

print ('Particulas')
print (Particulas)
print (costosparticulas)
print ('\nMejores particulas')
print (Mp)
print (mejorescostosp)
print ('\nMejor conocido y mejor costo')
print (mejorconocido, mejorcosto)
print ('\nLas velocidades son:')
print (velocidades,'\n')

for i in range(10000):
	for j in range(4):
		for k in range(5):
			aleatorio1=generadorLCG(seed,1)[0]
			aleatorio2=generadorLCG(seed,1)[0]
			resultado=velocidades[j][k]+aleatorio1*r1*(Mp[j][k]-Particulas[j][k])+aleatorio2*r2*(mejorconocido[k]-Particulas[j][k])
			velocidades[j][k]=round(resultado,3)
		for k in range(5):
			posicionnueva=Particulas[j][k]+velocidades[j][k]
			if posicionnueva<-600:
				posicionnueva=-600
			if posicionnueva>600:
				posicionnueva=600
			Particulas[j][k]=round(posicionnueva,4) #Actualiza posicion
		costosparticulas[j]=griewank(Particulas[j])
		if(costosparticulas[j]<mejorescostosp[j]):
			Mp[j]=Particulas[j][:]
			mejorescostosp[j]=costosparticulas[j]
	for j in range(4):
		if(costosparticulas[j]<=mejorcosto):
			mejorcosto=costosparticulas[j]
			mejorconocido=Particulas[j][:]

print ('Mejor costo')
print (mejorcosto)
print ('Mejor solucion')
print (mejorconocido,'\n')
