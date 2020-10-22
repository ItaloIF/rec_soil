# node recorder command
rtag = 41
rdof = 2
f_out = 'out_node'+ str(rtag) +'.txt'
ops.recorder('Node', '-file', f_out, '-precision', 6, '-node', rtag, '-dof', rdof, 'disp')