terreno=[[300,298,293,300,185],[299,295,290,180,175],
        [400,270,260,200,174],[110,280,230,250,170],
        [110,280,230,250,165],[118,120,130,345,360]]

lados=[0,1,2,3,4,5,6,8]
#
def menor(fila,columna):
    menor = terreno[fila][columna]
    posicion =0
    if fila-1 >=0:
        if columna-1>=0 and terreno[fila-1][columna-1]<menor:
            menor = terreno[fila-1][columna-1]
            posicion=6
        if terreno[fila-1][columna]<menor:
            menor= terreno[fila-1][columna]
            posicion = 7
        if columna+1<len(terreno[fila-1]) and terreno[fila-1][columna+1]<menor:
            menor=terreno[fila-1][columna+1]
            posicion=8
    if columna-1 >=0 and terreno[fila][columna-1]<menor:
        menor = terreno[fila][columna-1]
        posicion=5
    if columna+1<len(terreno[fila]) and terreno[fila][columna+1]<menor:
        menor = terreno[fila][columna+1]
        posicion=1
    if fila +1 < len(terreno):
        if columna-1>=0 and terreno[fila+1][columna-1]<menor:
            menor= terreno[fila+1][columna-1]
            posicion=4
        if terreno[fila+1][columna]<menor:
            menor = terreno[fila+1][columna]
            posicion=3
        if columna+1<len(terreno[fila+1]) and terreno[fila+1][columna+1]<menor:
            menor=terreno[fila+1][columna+1]
            posicion=2
    return posicion
    #terreno[fila][columna]=posicion

def recorre():
    fila=0
    while fila < len(terreno):
        columna=0
        while columna<len(terreno[fila]):
            print menor(fila,columna),
          #  print terreno[fila][columna],
            columna+=1
        print
        fila+=1


def verifica(valor):
    #fila,columna=0
    if valor ==0:
        fila=0
        columna=0
    #derecha
    elif valor==1:
        columna=1
        fila=0
    #diag der/abajo
    elif valor == 2:
        columna=1
        fila=1
    #abajo
    elif valor == 3:
        columna=0
        fila=1
    #diag izq /abajo
    elif valor == 4:
        columna=-1
        fila=1
    #izquierda
    elif  valor == 5:
        fila=0
        columna=-1
    #diag izq/arriba
    elif valor==6:
        fila=-1
        columna=-1
    #arriba
    elif valor == 7:
        fila = -1
        columna=0
    #diag der/arriba
    elif valor == 8:
        fila = -1
        columna=1
    posicion=fila,columna
    return posicion

def corre(fila,columna):
    valor = menor(fila,columna)
    x,y = verifica(valor)
        
    if fila == len(terreno)-1 or (fila==fila+x and columna==columna+y):
        print terreno[fila][columna]
    else:
        #print x, y
        corre(fila+x,columna+y)
        terreno[fila+x][columna+y]=0



recorre()
corre(0,0)
i=0
while i < len(terreno):
    x=0
    while x < len(terreno[i]):
        if terreno[i][x]==0:
            print terreno[i][x],
        else:
            print "#" ,#terreno[i][x],
        x+=1
    print 
    i+=1
