from collections import defaultdict
class Graph:
    vertices=set()
    g=defaultdict(list)

    def addvertex(self,v):
        self.vertices.add(v)
        
    
    def addEdge(self,frm,to):
        if frm not in self.vertices or to not in self.vertices:
            raise Exception('vertex not found')
        self.g[frm].append(to)
        
        
    def print(self):
        for v in self.vertices:
            if v in self.g:
                print(v,'==>',self.g[v])

#------------------- Graph construction over ------------------------------------------
                



g=Graph()
for i in range(5):
    g.addvertex(i)

g.addEdge(0,1)
g.addEdge(0,4)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,2)

g.print()