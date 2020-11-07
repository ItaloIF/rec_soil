# make viscous boundarys
# material 1
mTg = 1
rho = 1.7
Vs = 250.0
G = rho*Vs*Vs # Soil shear modulus
nu = 0.0 # Poisson's ratio of soil
E = 2*G*(1+nu)
Lame = nu*E/((1+nu)*(1-2*nu))
Vc = math.sqrt((Lame + 2*G)/rho)

Cn = -2*rho*Vc
Ct = -2*rho*Vs

ops.uniaxialMaterial('Viscous', 100, Cn, 1.0)
ops.uniaxialMaterial('Viscous', 101, Ct, 1.0)

for i in range(n_node):
    if (Node[i][0] == 1):
        ops.node(n_node + i+1, *Node[i][1:])
        ops.fix(n_node + i+1,1,1)
        ops.element('zeroLength', n_ele + i+1, i+1, n_node + i+1,'-mat', 100, 101,'-dir', 1, 2)
    