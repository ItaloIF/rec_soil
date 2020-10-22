from collections import defaultdict
f = open(f_name,'r')

# types of nodes and elements
N_dic = {(0,2): 1, (0,3): 1, (0,4): 1, (0,5): 1,
         (1,2): 1, (1,3): 1, (1,4): 1}
# 1 : damp
E_dic = {(2,1): 1}
# i : soil_i (material id)

N_dic = defaultdict(lambda:0, N_dic)
E_dic = defaultdict(lambda:0, E_dic)

Node = []
Ele = []

# read nodes
while True:
    if(f.readline().split()[0] == "$Nodes"):
        break
[n_ent, n_node]= list(map(int,f.readline().split()))[0:-2]
for i in range(n_ent):
    Data_ent = list(map(int,f.readline().split()))
    for i in range(Data_ent[3]):
            f.readline()
    for i in range(Data_ent[3]):
            Node.append([N_dic[Data_ent[0],Data_ent[1]]] + list(map(float,f.readline().split()))[0:-1])

# read elements
while True:
    if(f.readline().split()[0] == "$Elements"):
        break     
[n_ent, n_ele]= list(map(int,f.readline().split()))[0:-2]
for i in range(n_ent):
    Data_ent = list(map(int,f.readline().split()))
    if (E_dic[Data_ent[0],Data_ent[1]]>0) :
        for i in range(Data_ent[3]):
            Ele.append([E_dic[Data_ent[0],Data_ent[1]]] + list(map(int,f.readline().split())))
    else:
        for i in range(Data_ent[3]):
           f.readline()