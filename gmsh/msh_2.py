import numpy as np
import gmsh

# profile file (L,Z)(m)
f_name = 'profile.txt'
C_pf = np.loadtxt(f_name, skiprows=1)
n_pf = len(C_pf[:,1])
id_m = 104

# initial commands
gmsh.initialize()
gmsh.clear()
gmsh.option.setNumber('General.Terminal', 1)
m_tag = 'mesh_2'
gmsh.model.add(m_tag)
gmo = gmsh.model.occ

# define points
ms = 2 # mesh size
for i in range(n_pf):
    gmo.addPoint(C_pf[i,0], C_pf[i,1], 0, ms, i+1)

# define lines
gmo.addLine(1, 2, 1)
gmo.addSpline(range(2,id_m-1), 2)
gmo.addLine(id_m-2, id_m-1, 3)
gmo.addLine(id_m-1, id_m, 4)
gmo.addLine(id_m, id_m+1, 5)
gmo.addLine(id_m+1, id_m+2, 6)
gmo.addSpline(range(id_m+2, n_pf), 7)
gmo.addLine(n_pf-1, n_pf, 8)
gmo.addLine(n_pf, 1, 9)

gmo.addCurveLoop([1, 2, 3, 4, 5, 6, 7, 8, 9], 1)

# define surface
gmo.addPlaneSurface([1], 1)

# transforme tri to  quad
gmo.synchronize()
gmsh.model.mesh.setRecombine(2, 1)

#mesh generate
gmo.synchronize()
gmsh.model.mesh.generate(2)
gmsh.fltk.run()
gmsh.write(m_tag + '.msh')
gmsh.finalize()