class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0,isPrims=False):
        if(isPrims is False):
            self.connectedTo[nbr] = weight
        else:
            if(nbr not in self.connectedTo or self.connectedTo[nbr]>weight):
                self.connectedTo[nbr] = weight
    def removeNeighbor(self,nbr):
        del self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([(x.id,self.connectedTo[x]) for x in self.connectedTo.keys()])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]