import openseespy.opensees as ops
#import openseespy.postprocessing.Get_Rendering as opsplt
import math

ops.wipe()
ops.model('basic', '-ndm', 2, '-ndf', 2)

# paraview out
exec(open('code/out_paraview.py').read())

exec(open('code/units.py').read())

# define and make nDMaterial
exec(open('code/mat_prop.py').read())

# read 'msh' file
f_name = 'input/mesh_2.msh'
exec(open('code/read_msh.py').read())
n_ele = len(Ele)

# create nodes
for i in range(n_node):
    ops.node(i+1, *Node[i][1:])

# element thickness
b = 0.2*m 

# create elements
for i in range(n_ele):
    if (Ele[i][0] > 0):
        ops.element('quad', i+1, *Ele[i][2:], b, 'PlaneStress', Ele[i][0])

# delete extra nodes
for i in range(3,102):
    ops.remove('node', i)
for i in range(107,368):
    ops.remove('node', i)	

# make viscous boundarys
exec(open('code/bound.py').read())

# rayleigh damping 
exec(open('code/damp.py').read())

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

ops.analyze(10,0.001)
