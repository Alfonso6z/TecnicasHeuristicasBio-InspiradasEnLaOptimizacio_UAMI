
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
    bandera=0
    aux1 = ''
    aux2 = ''
    for i in binario:
        if i!='.' and bandera==0:
            aux1=aux1+i
        elif i!='.' and bandera==1:
            aux2=aux2+i
        elif i=='.':
            bandera=1
    aux1=int(aux1,2)
    aux2=int(aux2,2)
    real=''
    real= str(aux1)+'.'+str(aux2)
    real=float(real)
    return real

numero = 827.635
print (numero)
binario=binarizar(numero)
print (binario)
real=areal(binario)
print (real)