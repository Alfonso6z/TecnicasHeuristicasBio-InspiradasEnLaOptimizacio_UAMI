

def orden3():
	tabla=[]
	for j in range(9):
		cuadrante=[]
		for i in range(9):
			valor = [0,False]
			cuadrante.append(valor)
		tabla.append(cuadrante)

	tabla[0][0][0]=1
	tabla[0][6][0]=8
	tabla[1][0][0]=7
	tabla[1][1][0]=3
	tabla[2][3][0]=2
	tabla[2][4][0]=5
	tabla[3][5][0]=5
	tabla[3][7][0]=2
	tabla[4][1][0]=4
	tabla[4][5][0]=6
	tabla[5][2][0]=1
	tabla[6][0][0]=4
	tabla[7][5][0]=2
	tabla[7][6][0]=5
	tabla[8][1][0]=3
	tabla[8][3][0]=4
	tabla[6][7][0]=1

	for i in range(9):
		for j in range(9):
			if tabla[i][j][0]!=0:
				tabla[i][j][1]=True
	return tabla

def easy():
	tabla=[]
	for j in range(9):
		cuadrante=[]
		for i in range(9):
			valor = [0,False]
			cuadrante.append(valor)
		tabla.append(cuadrante)

	tabla[0][2][0]=2
	tabla[0][4][0]=1
	tabla[0][6][0]=4
	tabla[1][3][0]=7
	tabla[1][5][0]=5
	tabla[1][7][0]=9
	tabla[2][0][0]=5
	tabla[2][4][0]=2
	tabla[2][8][0]=7
	tabla[3][1][0]=4
	tabla[3][2][0]=9
	tabla[3][3][0]=8
	tabla[3][5][0]=1
	tabla[3][7][0]=3
	tabla[3][8][0]=6
	tabla[4][4][0]=3
	tabla[5][0][0]=7
	tabla[5][1][0]=3
	tabla[5][3][0]=4
	tabla[5][5][0]=9
	tabla[5][6][0]=2
	tabla[5][7][0]=1
	tabla[6][0][0]=2
	tabla[6][4][0]=8
	tabla[6][8][0]=7
	tabla[7][1][0]=8
	tabla[7][3][0]=9
	tabla[7][5][0]=2
	tabla[8][2][0]=4
	tabla[8][4][0]=6
	tabla[8][6][0]=8

	for i in range(9):
		for j in range(9):
			if tabla[i][j][0]!=0:
				tabla[i][j][1]=True
	return tabla

def medium():
	tabla=[]
	for j in range(9):
		cuadrante=[]
		for i in range(9):
			valor = [0,False]
			cuadrante.append(valor)
		tabla.append(cuadrante)
			
	tabla[0][4][0]=7
	tabla[0][5][0]=9
	tabla[0][6][0]=8
	tabla[1][4][0]=5
	tabla[2][3][0]=1
	tabla[2][4][0]=8
	tabla[2][8][0]=7
	tabla[3][2][0]=7
	tabla[3][3][0]=4
	tabla[3][4][0]=5
	tabla[3][8][0]=3
	tabla[4][0][0]=3
	tabla[4][2][0]=6
	tabla[4][3][0]=7
	tabla[4][5][0]=8
	tabla[4][6][0]=5
	tabla[4][8][0]=2
	tabla[5][0][0]=8
	tabla[5][4][0]=9
	tabla[5][5][0]=6
	tabla[5][6][0]=7
	tabla[6][0][0]=7
	tabla[6][4][0]=1
	tabla[6][5][0]=6
	tabla[7][4][0]=3
	tabla[8][2][0]=5
	tabla[8][3][0]=4
	tabla[8][4][0]=2

	for i in range(9):
		for j in range(9):
			if tabla[i][j][0]!=0:
				tabla[i][j][1]=True
	return tabla

def hardA():
	tabla=[]
	for j in range(9):
		cuadrante=[]
		for i in range(9):
			valor = [0,False]
			cuadrante.append(valor)
		tabla.append(cuadrante)

	tabla[0][4][0]=1
	tabla[0][5][0]=5
	tabla[0][7][0]=6
	tabla[1][2][0]=3
	tabla[1][5][0]=9
	tabla[2][1][0]=1
	tabla[2][2][0]=7
	tabla[2][5][0]=8
	tabla[3][0][0]=1
	tabla[3][5][0]=9
	tabla[4][2][0]=7
	tabla[4][6][0]=5
	tabla[5][3][0]=2
	tabla[5][8][0]=4
	tabla[6][3][0]=5
	tabla[6][6][0]=3
	tabla[6][7][0]=4
	tabla[7][3][0]=6
	tabla[7][6][0]=2
	tabla[8][1][0]=2
	tabla[8][3][0]=3
	tabla[8][4][0]=4

	for i in range(9):
		for j in range(9):
			if tabla[i][j][0]!=0:
				tabla[i][j][1]=True

	return tabla

def hardB():
	tabla=[]
	for j in range(9):
		cuadrante=[]
		for i in range(9):
			valor = [0,False]
			cuadrante.append(valor)
		tabla.append(cuadrante)

	tabla[0][0][0]=3
	tabla[0][1][0]=8
	tabla[0][8][0]=9
	tabla[1][3][0]=4
	tabla[1][7][0]=2
	tabla[2][3][0]=7
	tabla[2][4][0]=8
	tabla[2][5][0]=5
	tabla[2][6][0]=3
	tabla[3][1][0]=6
	tabla[3][3][0]=8
	tabla[4][1][0]=9
	tabla[4][3][0]=3
	tabla[4][5][0]=2
	tabla[4][7][0]=4
	tabla[5][5][0]=9
	tabla[5][7][0]=7
	tabla[6][2][0]=1
	tabla[6][3][0]=4
	tabla[6][4][0]=9
	tabla[6][5][0]=5
	tabla[7][1][0]=7
	tabla[7][5][0]=6
	tabla[8][0][0]=5
	tabla[8][7][0]=9
	tabla[8][8][0]=2

	for i in range(9):
		for j in range(9):
			if tabla[i][j][0]!=0:
				tabla[i][j][1]=True

	return tabla

def imprimeTabla(tabla,r,s,r2,s2):
	for i in range(r,r2):
		print(' |',end='')
		for j in range(s,s2):
			if i == r2-1:
				if j == s2-1:
					print(' ',tabla[i][j][0],' |')
				else:
					print(' ',tabla[i][j][0],end=' ')	
			else:
				print(' ',tabla[i][j][0],end=' ')
				
def imprimeSudoku(tabla):
	print("--------------------------------------------")
	imprimeTabla(tabla,0,0,3,3)
	imprimeTabla(tabla,0,3,3,6)
	imprimeTabla(tabla,0,6,3,9)
	print("--------------------------------------------")
	imprimeTabla(tabla,3,0,6,3)
	imprimeTabla(tabla,3,3,6,6)
	imprimeTabla(tabla,3,6,6,9)
	print("--------------------------------------------")
	imprimeTabla(tabla,6,0,9,3)
	imprimeTabla(tabla,6,3,9,6)
	imprimeTabla(tabla,6,6,9,9)
	print("--------------------------------------------")