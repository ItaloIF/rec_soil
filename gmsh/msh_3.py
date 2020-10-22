# mesh using transfinite and 2 or more layereds

import numpy as np
import gmsh

# initial commands
gmsh.initialize()
gmsh.clear()
gmsh.option.setNumber('General.Terminal', 1)
m_tag = 'mesh_3'
gmsh.model.add(m_tag)
gmg = gmsh.model.geo

# geometry (m)
L = 50
H1 = 50
H2 = 80

# define points 
ms = 1 # mesh size
gmg.addPoint(0, 0, 0, ms, 1) # load point
gmg.addPoint(L, 0, 0, ms, 2)
gmg.addPoint(L, -H1, 0, ms, 3)
gmg.addPoint(-L, -H1, 0, ms, 4)
gmg.addPoint(-L, 0, 0, ms, 5)
gmg.addPoint(L, -H2, 0, ms, 6)
gmg.addPoint(-L, -H2, 0, ms, 7)

# define lines
gmg.addLine(1, 2, 1)
gmg.addLine(2, 3, 2)
gmg.addLine(3, 4, 3)
gmg.addLine(4, 5, 4)
gmg.addLine(5, 1, 5)
gmg.addLine(4, 7, 6)
gmg.addLine(7, 6, 7)
gmg.addLine(6, 3, 8)


gmg.addCurveLoop([1, 2, 3, 4, 5] , 1)
gmg.addCurveLoop([3, 6, 7, 8] , 2)


# define surface
gmg.addPlaneSurface([1], 1)
gmg.addPlaneSurface([2], 2)

# transfinite
tf1 = int(L/ms)
tf2 = int(H1/ms)
tf3 = int((H2-H1)/ms)
gmg.mesh.setTransfiniteSurface(1,'Left',[2, 3, 4, 5])
gmg.mesh.setTransfiniteCurve(1, tf1+1)
gmg.mesh.setTransfiniteCurve(2, tf2+1)
gmg.mesh.setTransfiniteCurve(3, 2*tf1+1)
gmg.mesh.setTransfiniteCurve(4, tf2+1)
gmg.mesh.setTransfiniteCurve(5, tf1+1)
gmg.mesh.setTransfiniteSurface(2,'Left',[3, 4, 7, 6])
gmg.mesh.setTransfiniteCurve(3, 2*tf1+1)
gmg.mesh.setTransfiniteCurve(6, tf3+1)
gmg.mesh.setTransfiniteCurve(7, 2*tf1+1)
gmg.mesh.setTransfiniteCurve(8, tf3+1)


# transforme tri to  quad
gmsh.model.geo.synchronize()
gmsh.model.geo.mesh.setRecombine(2, 1)
gmsh.model.geo.mesh.setRecombine(2, 2)

#mesh generate
gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(2)
gmsh.fltk.run()
gmsh.write(m_tag + '.msh')
gmsh.finalize()