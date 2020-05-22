global seed
seed=180
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


#Funcion para obtener la medivecinaa
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
FuentesAlimento=[]
costoFuentes=[]
generaciones=0
fitness=0.0
fitnessparcial=0.0
maxim=0.0
costor=[]
cambio=[]
limitecambios=50
r=0.0

for i in range(7):
	FuentesAlimento.append(generadorLCGrango(seed,5,(-600,600)))
	costoFuentes.append(griewank(FuentesAlimento[i]))
	costor.append(griewank(FuentesAlimento[i]))
	cambio.append(0)

mejorconocida=FuentesAlimento[0][:]
mejorcosto=griewank(mejorconocida)
FuenteVecina=generadorLCGrango(seed,5,(-600,600))

print(FuentesAlimento)
print('Costos de las Fuentes')
print(costoFuentes)
print ('La fuente vecina es:')
print (FuenteVecina)
print ('El costo de la fuente vecina es:'
print (griewankFuenteVecina)
print ('El numero de cambios es:')
print (cambio)
print ('La mejor conocida es:')
print (mejorconocida)
print ('Con un costo:')
print (mejorcosto)

while (generaciones<5000):
    generaciones=generaciones+1
	#Inician empleadas
    for i in range(7):
        j=i
        while(j==i):
            j=int(generadorLCGrango(seed,1,(1,7))[0])
        for k in range(5):
            aleatorio1=generadorLCG(seed,1)[0]
            resultado=round(FuentesAlimento[i][k]+aleatorio1*(FuentesAlimento[i][k]-FuentesAlimento[j][k]),3)
            if resultado>600:
				resultado=600
            if resultado<-600:
				resultado=-600
            FuenteVecina[k]=resultado
            c=griewank(FuenteVecina)
            if(costoFuentes[i]>=c):
                for k in range(5):
					FuentesAlimento[i][k]=FuenteVecina[k]
                costoFuentes[i]=c
                cambio[i]=0
                if (mejorcosto>=c):
					mejorconocida=FuenteVecina[:]
					mejorcosto=c
                FuenteVecina=generadorLCGrango(seed,5,(-600,600))
            else:
				cambio[i]=cambio[i]+1
	#Terminan abejas empleadas
	#Inician abejas observadoras
    for i in range(7):
        fitness=0.0
        maxim=costoFuentes[0]
        for j in range(1,7):
            if(maxim<costoFuentes[j]):
				maxim=costoFuentes[j]
        maxim=maxim+1
        for j in range(7):
            costor[j]=maxim-costoFuentes[j]
            fitness=fitness+costor[j]
        r=generadorLCG(seed,1)[0]
        while r==1:
            r=generadorLCG(seed,1)[0]
        x=0
        fitnessparcial=costor[0]/fitness
        while (r>fitnessparcial):
            x=x+1
            fitnessparcial=fitnessparcial+(costor[x]/fitness)
        j=x
        while(j==x):
            j=int(generadorLCGrango(seed,1,(1,7))[0])
        for k in range(5):
			aleatorio1=generadorLCG(seed,1)[0]
			resultado=round(FuentesAlimento[x][k]+aleatorio1*(FuentesAlimento[x][k]-FuentesAlimento[j][k]),3)
			if resultado>600:
				resultado=600
			if resultado<-600:
				resultado=-600
			FuenteVecina[k]=resultado
			c=griewank(FuenteVecina)
			if(costoFuentes[x]>=c):
				for k in range(5):
					FuentesAlimento[x][k]=FuenteVecina[k]
				costoFuentes[x]=c
				cambio[x]=0
				if (mejorcosto>=c):
					mejorconocida=FuenteVecina[:]
					mejorcosto=c
			else:
				cambio[x]=cambio[x]+1
	#Terminan observadoras
	#print costoFuentes
	#Inician exploradoras
    for i in range(7):
        if(cambio[i]>=limitecambios):
            FuentesAlimento[i]=generadorLCGrango(seed,5,(-600,600))
            costoFuentes[i]=griewank(FuentesAlimento[i])
            cambio[i]=0
	#Terminan exploradoras
#Terminan generaciones


print ('\nLas fuentes de alimento finales son:')
print (FuentesAlimento)
print ('Los costos finales son:')
print (costoFuentes)
print ('\nLa mejor solucion conocida es:')
print (mejorconocida)
print ('El mejor costo es:')
print (mejorcosto)