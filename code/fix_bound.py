# make fix boundarys
for i in range(n_node):
    if (Node[i][0] == 1):
        ops.fix(i+1, *[1,1])