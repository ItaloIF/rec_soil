import openseespy.postprocessing.ops_vis as opsv
import matplotlib.pyplot as plt

# plot model with tag labels
#fig = plt.figure(figsize=(10,10))
#opsv.plot_model()

# plot deformation
opsv.plot_defo()

# plot mode shape
#opsv.plot_mode_shape(2)

# plot stress 2D
#sig_out = opsv.quad_sig_out_per_node() # components: sxx, syy, sxy, svm, s1, s2, angle. Size (n_nodes x 7)
#opsv.plot_stress_2d(sig_out[:, 0], mesh_outline=1, cmap='viridis')

# plot stress 2D - values at integration points and nodes
#eles_ips_crd, eles_nds_crd, nds_crd, quads_conn = opsv.quad_crds_node_to_ip()
#eles_ips_sig_out, eles_nds_sig_out = opsv.quad_sig_out_per_ele()
#opsv.plot_mesh_with_ips_2d(nds_crd, eles_ips_crd, eles_nds_crd, quads_conn,
#                           eles_ips_sig_out, eles_nds_sig_out, 3)
plt.show()