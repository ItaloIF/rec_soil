import openseespy.opensees as ops
import os
from collections import defaultdict
#import openseespy.postprocessing.Get_Rendering as opsplt

# parallel parameters
pid = ops.getPID()
np = ops.getNP()

# set model builder
ops.wipe()
ops.model('basic', '-ndm', 2, '-ndf', 2)

# paraview out
data_name = 'out/model_1'
#exec(open('code/out_paraview.py').read())

exec(open('code/units.py').read())

# parallel
if (pid == 0):
    # read 'msh' file
    f_name = 'gmsh/mesh_3.msh'
    exec(open('code/read_msh.py').read())
    n_ele = len(Ele)

    # define and make nDMaterial
    exec(open('code/mat_prop.py').read())

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
    exec(open('code/bound.py').read())

    # rayleigh damping
    #ops.rayleigh(a0,0,0,a1)

    #opsplt.plot_model()

    exec(open('code/load.py').read())
else:
    ops.node(1, 0.0, 0.0)

# analysis commands
ops.constraints('Transformation')
ops.numberer('ParallelPlain')
ops.system('Mumps')
ops.test('NormDispIncr', 1e-6, 6)
ops.algorithm('Newton')
ops.integrator('Newmark', 0.5, 0.25)
ops.analysis('Transient')

# timers
ops.start()
ops.analyze(10,0.001)
ops.stop()