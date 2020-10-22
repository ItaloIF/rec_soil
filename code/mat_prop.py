# material properties
mTag = 1
rho = 1700*kg/m**3
Vs = 250.0*m/s # Soil shear wave velocity
G = rho*Vs*Vs # Soil shear modulus
nu = 0.0 # Poisson's ratio of soil
E = 2*G*(1+nu)
ops.nDMaterial('ElasticIsotropic', mTag, E, nu, rho)