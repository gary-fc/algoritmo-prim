from prim import Prim


nodes = ['A','B','C','D','E','F']
edges = [
    {'A':['B',1]},
    {'A':['C',3]},
    {'A':['D',4]},
    {'B':['C',2]},
    {'C':['F',5]},
    {'D':['E',7]},
    {'E':['F',3]}
    
]

prim = Prim()
nd = input("Ingresa un nodo inicio")
test = prim.apply_prim(nodes,edges,nd)
print(test)