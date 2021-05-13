from .Graph import Graph
class PrimAlgo:
    def __init__(self,verticies,edges):
        self.edges =edges
        self.minspantree = []
        self.verticies = verticies
        self.inputgraph = Graph()
        self.constructGraph()
    def constructGraph(self):
        for source, dest, weight in self.edges:
            if(source is not dest):
                self.inputgraph.addEdge(source, dest, int(weight),True)
    def getMinSpanTree(self):
        soureNode=list(self.inputgraph.vertList.keys())[0]
        visited=[]
        queue=[]
        queue.extend(self.getAdjacentEdges(soureNode))
        visited.append(soureNode)
        while (len(visited) != len(self.verticies)):
            queue.sort(key=lambda tup: (tup[2], tup[0], tup[1]))
            element = queue[0]
            if (element[1] not in visited):
                visited.append(element[1])
                self.minspantree.append(element)
                queue.extend(self.getAdjacentEdges(element[1]))
            del queue[0]
        return self.minspantree

    def getAdjacentEdges(self,node):
        neighbour=self.inputgraph.vertList[node]
        return [(node,x.id,neighbour.connectedTo[x]) for x in neighbour.connectedTo.keys()]