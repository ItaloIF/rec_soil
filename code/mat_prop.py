# material properties

# material 1
mTg = 1
rho = 1.7
Vs = 250.0
G = rho*Vs*Vs # Soil shear modulus
nu = 0.0 # Poisson's ratio of soil
E = 2*G*(1+nu)
ops.nDMaterial('ElasticIsotropic', mTg, E, nu, rho)
#damp[mTg] = get_damParam(0.02, 0.02, 0.2, 20)

# material 2
mTg = 2
rho = 1.7
Vs = 250
G = rho*Vs*Vs # Soil shear modulus
nu = 0.0 # Poisson's ratio of soil
E = 2*G*(1+nu)
ops.nDMaterial('ElasticIsotropic', mTg, E, nu, rho)
#damp[mTg] = get_damParam(0.02, 0.02, 0.2, 20)