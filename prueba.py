
terreno=[[300,298,293,300,185],[299,295,290,180,175],
        [400,270,260,200,174],[110,280,230,250,170],
        [110,280,230,250,165],[118,120,130,145,160]]


i=0
while i < len(terreno):
    x=0
    while x < len(terreno[i]):
        print terreno[i][x],
        x+=1
    print 
    i+=1

def menor(fila,columna):
    menor = terreno[fila][columna]
    posicion=fila,columna
    if fila-1>=0 and terreno[fila-1][columna]<menor:
        menor = terreno[fila-1][columna]
        posicion = fila-1,columna
    
    if columna -1 >=0 and terreno[fila][columna-1]<menor:
        menor = terreno[fila][columna-1]
        posicion=fila,columna-1
    if fila +1 <len(terreno) and terreno[fila+1][columna]<menor:
        menor = terreno[fila+1][columna]
        posicion=fila+1,columna
    if columna +1 <len(terreno[fila]) and terreno[fila][columna+1]<menor:
        menor = terreno[fila][columna+1]
        posicion=fila, columna+1

    return posicion

def recorre(fila,columna):
    x,y = menor(fila,columna)
    momento = terreno[fila][columna]
    
    if momento == terreno[x][y]:
        print "terminado"
    else:
        print "valor: ",terreno[x][y], "posicion :(%d,%d)"%(x,y)
        recorre(x,y)
        


recorre(0,0)


