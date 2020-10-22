import numpy as np
import gmsh

# profile file (L,Z)(m)
f_name = 'profile.txt'
C_pf = np.loadtxt(f_name, skiprows=1)
n_pf = len(C_pf[:,1])

# initial commands
gmsh.initialize()
gmsh.clear()
gmsh.option.setNumber('General.Terminal', 1)
m_tag = 'mesh_1'
gmsh.model.add(m_tag)

# define points
ms = 1 # mesh size
for i in range(n_pf):
    gmsh.model.geo.addPoint(C_pf[i,0], C_pf[i,1], 0, ms, i+1)

# define lines
for i in range(n_pf-1):
    gmsh.model.geo.addLine(i+1, i+2, i+1)
gmsh.model.geo.addLine(n_pf, 1, n_pf)

gmsh.model.geo.addCurveLoop([*range(1, n_pf+1, 1)] , 1)

# define surface
gmsh.model.geo.addPlaneSurface([1], 1)

# transforme tri to  quad
gmsh.model.geo.synchronize()
gmsh.model.geo.mesh.setRecombine(2, 1)

#mesh generate
gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(2)
#gmsh.fltk.run()
gmsh.write(m_tag + '.msh')
gmsh.finalize()


