def mostrarNodosGrafo(graph,nodos):
    """
    Funcion que permite mostrar los nodos de nuestro grafo

    Parametro
    -------------------------------------------------------
    graph:Grafo a leer
    nodos:El nombre de los nodos 

    Retorna
    -------------------------------------------------------
    No retorna ningun valor
    """
    #variable para buscar el nombre del nodo
    i=0
    #recorremos el grafo
    for dato in graph:
        #mostramos los nodos con sus nombre y sus respectivas aristas
        print("Nodo {}: {}".format(nodos[i],dato))
        #ingrementamos mi variable par mostrar el nodo
        i+=1
def nodoGrafo(graph,numNodo):
    """
    Funcion que retorna los elementos que posee un nodo

    Parametros
    ----------------------------------------
    graph: Grafo a recorrer
    numNodo: El nodo que retornamremos

    Retorna
    ----------------------------------------
    un nodo
    """
    if len(graph[numNodo])==1:
        return graph[numNodo][0] 
    return graph[numNodo]

def viasAvio(nodos,costos,vias):
    """
    Funcion que muestra las vias a recorrer

    Parametros
    ---------------------------------------
    nodos: el nombre de los nodos
    costos:costos de las paradas
    vias: vias que recorre

    Retorna
    ---------------------------------------
    Retorna ningun valor
    """
    #costos inicial
    cost=costos[(18,19)]
    #recorremos las vias
    for i in range(len(vias)):
        #recorremos las vias
        for j in vias[i]:
            #mostramos las rutas
            print("Ruta {}-{}".format(nodos[j[0]],nodos[j[1]]))
            #costos acumulados
            cost+=costos[(j)]
        #imrpimimos los costos
        print("Costo Total de horas:",cost)
        print("----------------------------------")

if __name__=='__main__':
    #creacion de los grafos
    graph, cost = [[] for i in range(19)], {}
    #nodos que poseera nuestro grafo
    nodos=['ecuador','honalulu','lima','bogota','cdGuatemala','sanJose','venzuela','sanFransisco','losAngeles','panamaCity','houston','seul','nicaraguas','honduras','mexico','miami','costaRica','newyotCity','tokio','japon']
    #desiganamos las  variables de nuestros nodos 
    ecuador=0
    honalulu=1
    lima=2
    bogota=3
    cdGuatemala=4
    sanJose=5
    venzuela=6
    sanFransisco=7
    losAngeles=8
    panamaCity=9
    houston=10
    seul=11
    nicaraguas=12
    honduras=13
    mexico=14
    miami=15
    costaRica=16
    newyotCity=17
    tokio=18
    japon=19
    #ingresamos los grafos designados a cada nodo y sus vecinos
    graph[ecuador].append(honalulu)
    graph[ecuador].append(lima)
    graph[ecuador].append(bogota)
    graph[ecuador].append(cdGuatemala)
    graph[ecuador].append(sanJose)
    graph[ecuador].append(venzuela)
    graph[ecuador].append(sanFransisco)
    graph[ecuador].append(losAngeles)
    graph[ecuador].append(panamaCity)
    graph[losAngeles].append(houston)
    graph[sanFransisco].append(houston)
    graph[venzuela].append(panamaCity)
    graph[sanJose].append(panamaCity)
    graph[cdGuatemala].append(mexico)
    graph[bogota].append(nicaraguas)
    graph[bogota].append(costaRica)
    graph[lima].append(seul)
    graph[lima].append(nicaraguas)
    graph[honalulu].append(tokio)
    graph[houston].append(miami)
    graph[panamaCity].append(tokio)
    graph[mexico].append(houston)
    graph[mexico].append(miami)
    graph[nicaraguas].append(honduras)
    graph[nicaraguas].append(tokio)
    graph[seul].append(tokio)
    graph[tokio].append(japon)
    graph[honduras].append(mexico)
    graph[newyotCity].append(tokio)
    graph[costaRica].append(mexico)
    graph[miami].append(newyotCity)
    graph[miami].append(tokio)
    #mostrarNodosGrafo(graph,nodos)

    cost[(ecuador,losAngeles)]=15
    cost[(ecuador,sanFransisco)]=14
    cost[(ecuador,venzuela)]=3
    cost[(ecuador,panamaCity)]=6
    cost[(ecuador,sanJose)]=6
    cost[(ecuador,cdGuatemala)]=10
    cost[(ecuador,bogota)]=3
    cost[(ecuador,lima)]=2
    cost[(ecuador,honalulu)]= 19
    cost[(losAngeles,houston)]= 3
    cost[(houston,miami)]=2
    cost[(houston,newyotCity)]=2
    cost[(miami,tokio)]=15
    cost[(tokio,japon)]= 2
    cost[(miami,newyotCity)]=2
    cost[(newyotCity,tokio)]=15
    cost[(sanFransisco,houston)]=5
    cost[(venzuela,panamaCity)]=2
    cost[(panamaCity,tokio)]= 16
    cost[(sanJose,panamaCity)]=3
    cost[(cdGuatemala,mexico)]=2
    cost[(mexico,houston)]=5
    cost[(mexico,miami)]=4
    cost[(bogota,costaRica)]=2
    cost[(costaRica,mexico)]= 4
    cost[(bogota,nicaraguas)]=3
    cost[(nicaraguas,honduras)]=1
    cost[(nicaraguas,tokio)]=23
    cost[(honduras,mexico)]=2
    cost[(lima,nicaraguas)]=12
    cost[(lima,seul)]=15
    cost[(seul,tokio)]=3
    cost[(honalulu,tokio)]=12
    #total de vias que recorre la persona
    vias=[
        [(ecuador,losAngeles),(losAngeles,houston),(houston,newyotCity)],
        [(ecuador,sanFransisco),(sanFransisco,houston),(houston,newyotCity)],
        [(ecuador,venzuela),(venzuela,panamaCity)],
        [(ecuador,panamaCity)],
        [(ecuador,sanJose),(sanJose,panamaCity)],
        [(ecuador,cdGuatemala),(cdGuatemala,mexico),(mexico,miami)],
        [(ecuador,bogota),(bogota,costaRica),(costaRica,mexico),(mexico,houston),(houston,newyotCity)],
        [(ecuador,lima),(lima,seul)],
        [(ecuador,lima),(lima,nicaraguas)],
        [(ecuador,honalulu)]
        ]
    viasAvio(nodos,cost,vias)



    

   