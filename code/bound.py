# make viscous boundarys
Lame = nu*E/((1+nu)*(1-2*nu))
Vc = math.sqrt((Lame + 2*G)/rho)

Cn = -rho*Vc
Ct = -rho*Vs

ops.uniaxialMaterial('Viscous', 100, Cn, 1.0)
ops.uniaxialMaterial('Viscous', 101, Ct, 1.0)

for i in range(n_node):
    if (Node[i][0] == 1):
        ops.node(n_node + i+1, *Node[i][1:])
        ops.fix(n_node + i+1, *[1,1])
        ops.element('zeroLength', n_ele + i+1, i+1, n_node + i+1,'-mat', 100, 101,'-dir', 1, 2)
    