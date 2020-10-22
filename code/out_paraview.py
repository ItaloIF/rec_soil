import os
data_name = 'model_1'
if not os.path.exists(data_name):
	os.makedirs(data_name)
ops.recorder('PVD', data_name, 'disp')