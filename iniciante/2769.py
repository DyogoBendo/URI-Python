from math import inf


class Graph():
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = []
    

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])


    def bellman_ford(self):        
        dist = [inf] * self.V
        dist[0] = 0

        for _ in range(self.V -1):            
            for u, v, w in self.graph:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        r = dist[-1]        
        print(r)


if __name__ == '__main__':
    while True:      
        try:  
            n = int (input()) 
            e1, e2 = map(int, input().split())
            n1 = list(map(int, input().split()))
            n2 = list(map(int, input().split()))
            if n > 1:
                t1 = list(map(int, input().split()))
                t2 = list(map(int, input().split()))
            x1, x2 = map(int, input().split())
            grafo = Graph((2*n) + 4)
            c11 = 1            
            c22 = c11 + n + 1            

            grafo.addEdge(0, 1, e1)
            grafo.addEdge(0, c22, e2)

            for i in range(n):                                

                w11 = n1[i]
                w22 = n2[i]                
                grafo.addEdge(c11, c11 + 1, w11)                                        
                grafo.addEdge(c22, c22 + 1, w22) 
                if i < n - 1:                                                       
                    w12 = t1[i]
                    w21 = t2[i]
                    grafo.addEdge(c11, c22, w12)                                        
                    grafo.addEdge(c22, c11, w21)                                        
                c11 += 1                
                c22 += 1                        

            grafo.addEdge(c11, 2*n + 3, x1)
            grafo.addEdge(c22, 2*n + 3, x2)

            grafo.bellman_ford()
        except:
            break