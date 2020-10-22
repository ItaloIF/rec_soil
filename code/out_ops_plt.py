
ops.wipe() #Make sure to issue a 'wipe' command to close all the recorders.

# plot model with tag labels
#opsplt.plot_model()
#opsplt.plot_model('nodes', Model='beam')

# plot mode shape
#opsplt.plot_modeshape(5, 2, Model='beam')  # mode, scale, model name

# plot deformation
opsplt.plot_deformedshape(Model='model_1', LoadCase='load1', scale=20000, overlap='yes')