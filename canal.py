
terreno=[[300,298,293,300,185],[299,295,290,180,175],
        [400,270,260,200,174],[110,280,230,250,170],
        [110,280,230,250,165],[118,120,130,145,160]]
#vueltas manecillas del reloj
dir_fila=   [-1,-1,0,1,1,1,0,-1]
dir_columna=[0,1,1,1,0,-1,-1,-1]
#
def verificar(fila,columna,k):
    if fila+dir_fila[k]>=0 and fila +dir_fila[k]<len(terreno) and dir_columna[k]+columna>=0 and dir_columna[k]+columna<len(terreno[0]):
        return True
    else:
        return False

def verMenor(fila,columna):
    menor=terreno[fila][columna]
    nfila=fila
    ncolumna=columna
    k=0
    while k< 8:
        #ve is esta dentro de una posicion valida
        if verificar(fila,columna,k)==True:
            #print k,fila,columna
            if terreno[fila+dir_fila[k]][columna+dir_columna[k]]<menor:
                menor = terreno[fila+dir_fila[k]][columna+dir_columna[k]]
                nfila = fila+dir_fila[k]
                ncolumna = columna+dir_columna[k]

        k+=1
    return nfila,ncolumna

def recorrer(fila,columna):
    nfila,ncolumna=verMenor(fila,columna)
    print "(", fila,",",columna,") (",terreno[fila][columna],")"
    if nfila==fila and columna==ncolumna:
        print "termino"

    else:
        recorrer(nfila,ncolumna)



recorrer(0,4)
i=0
while i< len(terreno):
    print terreno[i]
    i+=1
