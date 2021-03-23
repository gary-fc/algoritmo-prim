class Prim:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.visitados_nodes = {}
        self.cola_edges = []
        self.min_exp_tree = []
        self.flag_while = True

    # ['A','B','C']
    def prepare_nodes(self, node):
        # Buscamos dentro de los nodos aquel valor ingresado, en caso de no existir se crea el dato
        self.nodes[node] = 0
        

    # [{'A':['B',1]},{'A':['C',3]},{'A':['D',4]}]
    def prepare_edges(self, edge):
        for key, value in edge.items(): 
            self.edges.append({key:value})

    def generate_opposites(self):
        edges = self.edges
        aux_list = []
        
        for edge in edges:
            
            for key, value in edge.items():
                aux_list.append({value[0]:[key,value[1]]})
        self.edges.extend(aux_list)

    def my_func(self, edge):
        return edge[2]

    def get_edges_by_node(self,node):
        next_node = ""
        if self.nodes[node] != 1:
            print("No Visitado")
            self.visitados_nodes[node] = 1
            self.nodes[node] = 1
            for edge in self.edges:
                for key, value in edge.items():
                    if key == node:
                        self.cola_edges.append([key,value[0],value[1]])   
            self.cola_edges.sort(key=self.my_func,reverse=True)
            #print(self.cola_edges) 
            next_node = self.cola_edges[-1][1]
            flag = True
            while flag:
                if len(self.cola_edges) > 0:
                    if self.cola_edges[-1][1] in self.visitados_nodes:
                        self.cola_edges.pop()
                        #print(self.min_exp_tree)
                    else:
                        #print(self.cola_edges)
                        if len(self.cola_edges) > 0:
                            next_node = self.cola_edges[-1][1]
                        else: 
                            self.flag_while = False 
                        self.min_exp_tree.append(self.cola_edges.pop())
                        flag = False
                else:
                    self.flag_while = False
            print("resultado",self.min_exp_tree)
            print(len(self.cola_edges))
            print(self.cola_edges)
            return next_node
        else:
            print('Visitado')
            self.flag_while = False 
        

    

        
    def apply_prim(self,nodes,edges,nd):        
        for node in nodes:
            self.prepare_nodes(node)
        
        #print(self.nodes)
        
        for edge in edges:
            self.prepare_edges(edge)

        self.generate_opposites()
        #print(len(self.cola_edges))


        while self.flag_while:
            #print(len(self.cola_edges))
            nd = self.get_edges_by_node(nd)

            print(nd)
        
        return self.min_exp_tree