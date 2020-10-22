# define loads
tsTag = 1
id_nload = 104
ti = 0*s
tf = 0.2*s
fr = 10*Hz
period = 1/fr
Fx = 0*N
Fy = 10000*N
ops.timeSeries('Trig', tsTag, ti, tf, period, '-factor', 1.0)
ops.pattern('Plain', 1, tsTag, '-fact', 1.0)
ops.load(id_nload, Fx, Fy)

# constraints nodes
ops.equalDOF(104, 102, *[1, 2])
ops.equalDOF(104, 103, *[1, 2])
ops.equalDOF(104, 105, *[1, 2])
ops.equalDOF(104, 106, *[1, 2])