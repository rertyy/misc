##https://www.youtube.com/watch?v=oikZlz1GNbo

def addEdge(adj, v, w):
    adj[v].append(w)
    adj[w].append(v)
    return adj


#         0    1    2    3     4     5
graph = [[1],[0,2],[1],[4,5],[3,5],[3,4],[]]
V = 6 #no of vertices
colours = [0] * V
permutations = 0
print("------------")

#undirected graph
#index 0 is connected to vertices 1, vertex 1 is connected to vertex 2

#check if n colours is a valid graphcolouring
#n is the number of colours you are checking
#colours is the colours at each index of the graph
#v_ind is the index of the node
flag = True


def checkNColours(n, colours, v_ind):
    if v_ind == V:
        #global permutations
        #permutations += 1
        #global flag
        #flag = False
        #return print(max(colours))
        return True
    for c in range(1, n + 1): #colours are from 1 to n inclusive
        if isValid(c, colours, v_ind, graph): #and flag:
            colours[v_ind] = c
            if checkNColours(n, colours, v_ind + 1):
                return True
                #pass
            colours[v_ind] = 0 #if fail, backtrack by setting v_ind = 0
            return False
    ### false value


def isValid(c, colours, v_ind, graph): #check adjacent colours
##    print(f"aaaaaaaaaaa ind {v_ind} and {graph[v_ind]} and {colours}")
    for i in graph[v_ind]:
##        print(i)
        if colours[i] == c:
            return False
    return True

x = checkNColours(3, colours, 0)
print(x)



    
    
