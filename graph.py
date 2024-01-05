
from collections import defaultdict

                
                #Graph construction
class Graph:
    vertices=set()
    g=defaultdict(set)

    def addvertex(self,v):
        self.vertices.add(v)
        
    
    def addEdge(self,frm,to):
        if frm not in self.vertices or to not in self.vertices:
            raise Exception('vertex not found')
        self.g[frm].add(to)
        
        
    def print(self):
        for v in self.vertices:
            if v in self.g:
                print(v,'==>',self.g[v])

#-----------------------------------------------------------------------------------
                # Transpose vertex

    def transpose(self):
        tg=defaultdict(list)
        for v in self.vertices:
            self.addTedge(tg,v,self.g[v])
        print('transposed graph is -> ', tg)
                

    def addTedge(self,tg,v,vlist):
        for vtx in vlist:
            tg[vtx].append(v)
#-----------------------------------------------------------------------------------------------
        # Traversals
            #Breadth First Search

    def bfs(self,v):
        visited=[] # visited cannot be set, as we need to preserve the order
        queue=[]
        queue.append(v)
        while queue:
            vtx = queue.pop(0)
            if vtx not in visited:
                visited.append(vtx)
                queue.extend(self.g[vtx])
        print('bfs traversal->', visited)
    
    def bfs_recur(self,v):
        visited=[]
        queue=[]
        queue.append(v)
        self._bfs_recur(queue,visited)
        print('recursive bfs- >',visited)

    def _bfs_recur(self,queue,visited):
        if not queue:
            return
        vtx=queue.pop(0)
        if vtx not in visited:
            visited.append(vtx)
            queue.extend(self.g[vtx])
        self._bfs_recur(queue,visited)
#---------------BFS OVER-------------------------------------------------------------
    
    # Depth first traversal
    
    def dfs(self,v):
        visited=[]
        stack=[]
        stack.append(v)
        while stack:
            vtx=stack.pop()
            if vtx not in visited:
                visited.append(vtx)
                stack.extend(self.g[vtx])
        print('dfs traversal -> ',visited)
    
    def dfs_recur(self,v):
        visited=[]
        self._dfs_recur(v,visited)
        print('recursive dfs traversal -> ',visited)
    
    def _dfs_recur(self,v,visited):
        if v not in visited:
            visited.append(v)
            for vx in self.g[v]:
                self._dfs_recur(vx,visited)

            #---------DFS OVER---------
#-------------------Traversal over-----------------------------        



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
g.transpose()
g.bfs(0)
g.bfs_recur(0)
g.dfs(0)
g.dfs_recur(0)