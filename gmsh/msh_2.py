# mesh using transfinite
import numpy as np
import gmsh

# initial commands
gmsh.initialize()
gmsh.clear()
gmsh.option.setNumber('General.Terminal', 1)
m_tag = 'mesh_2'
gmsh.model.add(m_tag)
gmg = gmsh.model.geo

# geometry (m)
L = 50
H = 50

# define points 
ms = 1 # mesh size
gmg.addPoint(0, 0, 0, ms, 1) # load point
gmg.addPoint(L, 0, 0, ms, 2)
gmg.addPoint(L, -H, 0, ms, 3)
gmg.addPoint(-L, -H, 0, ms, 4)
gmg.addPoint(-L, 0, 0, ms, 5)

# define lines
gmg.addLine(1, 2, 1)
gmg.addLine(2, 3, 2)
gmg.addLine(3, 4, 3)
gmg.addLine(4, 5, 4)
gmg.addLine(5, 1, 5)

gmsh.model.geo.addCurveLoop([1, 2, 3, 4, 5] , 1)

# define surface
gmsh.model.geo.addPlaneSurface([1], 1)

# transfinite
tf1 = int(L/ms)
tf2 = int(H/ms)
gmg.mesh.setTransfiniteSurface(1,'Left',[2, 3, 4, 5])
gmg.mesh.setTransfiniteCurve(1, tf1+1)
gmg.mesh.setTransfiniteCurve(2, tf2+1)
gmg.mesh.setTransfiniteCurve(3, 2*tf1+1)
gmg.mesh.setTransfiniteCurve(4, tf2+1)
gmg.mesh.setTransfiniteCurve(5, tf1+1)

# transforme tri to  quad
gmsh.model.geo.synchronize()
gmsh.model.geo.mesh.setRecombine(2, 1)

#mesh generate
gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(2)
gmsh.fltk.run()
gmsh.write(m_tag + '.msh')
gmsh.finalize()
