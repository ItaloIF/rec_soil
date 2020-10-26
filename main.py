import openseespy.opensees as ops
import os
import math
from collections import defaultdict
#import openseespy.postprocessing.Get_Rendering as opsplt

# set model builder
ops.wipe()
ops.model('basic', '-ndm', 2, '-ndf', 2)

# paraview out
data_name = 'out/model_1'
exec(open('code/out_paraview.py').read())

exec(open('code/units.py').read())

# define and make nDMaterial
exec(open('code/mat_prop.py').read())

# read 'msh' file
f_name = 'gmsh/mesh_3.msh'
exec(open('code/read_msh.py').read())
n_ele = len(Ele)

# create nodes
for i in range(n_node):
    ops.node(i+1, *Node[i][1:])

# element thickness
b = 1*m

# rayleigh damping parameters
exec(open('code/damp.py').read())

# create elements
for i in range(n_ele):
    if (Ele[i][0] > 0):
        ops.element('quad', i+1, *Ele[i][2:], b, 'PlaneStrain', Ele[i][0])
        ops.setElementRayleighDampingFactors(i+1,a0,0,0,a1)

#opsplt.plot_model()

# make viscous boundarys
#exec(open('code/bound.py').read())
exec(open('code/fix_bound.py').read())

# rayleigh damping
#ops.rayleigh(a0,0,0,a1)

#opsplt.plot_model()

exec(open('code/load.py').read())

# analysis commands
ops.constraints('Plain')
ops.numberer('Plain')
ops.system('UmfPack')
#ops.test('EnergyIncr', 1.0e-8, 6)
ops.algorithm('Linear')
ops.integrator('Newmark', 0.5, 0.25)
ops.analysis('Transient')

#exec(open('code/rec.py').read())

# timers
ops.start()
ops.analyze(10,0.001)
ops.stop()
