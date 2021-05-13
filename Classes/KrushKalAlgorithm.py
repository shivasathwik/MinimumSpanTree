from .Graph import Graph
from queue import Queue
class KrushkalAlgo:
    def __init__(self,verticies,edges):
        edges.sort(key=lambda tup: (tup[2]))
        self.edges =edges
        self.minspantree=[]
        self.verticies=verticies
        self.output=Graph()
    def getMinSpanTree(self):
        for source,dest,weight in self.edges:
            if source is not dest:
                self.output.addEdge(source, dest, int(weight))
                if(self.checkForCycle(self.output)):
                    self.output.delEdge(source,dest)
                else:
                    self.minspantree.append((source,dest,int(weight)))
        return self.minspantree
    def checkForCycle(self,graph):
        visitied=[]
        vertexFlag={i:-1 for i in graph.vertList.keys()}
        qu = Queue()
        start=list(graph.vertList.keys())[0]
        qu.put(start)
        vertexFlag[start]=0
        while (qu.empty() is not True):
            element=qu.get();
            if element not in visitied:
                visitied.append(element)
                vertexFlag[element] = 1
            hasVisited=False
            hasNeighBourInQ=False
            for neighbour in graph.vertList[element].getConnections():
                if (neighbour.getId() in visitied):
                    hasVisited=True
                elif(vertexFlag[neighbour.getId()]==0):
                    hasNeighBourInQ=True
                else:
                    qu.put(neighbour.getId())
                    vertexFlag[neighbour.getId()] = 0

            if(hasVisited is True and hasNeighBourInQ is True):
                return True
        return False


