import networkx as nx
f=file('data.txt','r')
n,m=f.readline().split()
n,m=int(n),int(m)
es=[(1,2),(2,3),(3,1),(3,4),(4,5),(5,6),(3,6)]
g=nx.Graph()
g.add_edges_from(es)
print nx.matching.max_weight_matching(g)