import os
import time
import re

#########################################################################
#Paths et autres variables communes du projet NewYork Taxi
#
#########################################################################



# Paths du projet NewYork Taxi
# Path_project_root = os.path.basename(__file__)
Path_project_root = os.path.abspath(os.chdir(".."))

Path_Data_warehouse = os.path.join(Path_project_root, 'Data_warehouse')
Path_data_Sources = os.path.join(Path_Data_warehouse, 'A_Sources')
Path_External_Sources = os.path.join(Path_Data_warehouse, 'B_External_sources')
Path_Features = os.path.join(Path_Data_warehouse, 'F_Features')
Path_Model_input = os.path.join(Path_Data_warehouse, 'M_Model_input')
Path_to_training_data = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Data_warehouse', 'A_Sources')

Path_Models = os.path.join(Path_project_root, 'Models')
Path_Models_data_prep = os.path.join(Path_project_root, 'Models_data_prep')
Path_Profiling = os.path.join(Path_project_root, 'Profiling')
Path_Mod_linear_reg = os.path.join(Path_Models, 'Mod_linear_reg')

Path_Reports = os.path.join(Path_project_root, 'reports')
Path_Models_scores = os.path.join(Path_Reports, 'M_Models_scores')
Path_Profiling_results = os.path.join(Path_Reports, 'A_Profiling_results')

Path_Commun = os.path.join(Path_project_root, 'x_commun')
print(' ')
print('Path du projet NewYork Taxi')
print(' ')
print('NewYork Taxi root:             ', Path_project_root)
print('NewYork Taxi Data_warehouse:   ', Path_Data_warehouse)
print('NewYork Taxi Models:           ', Path_Models)
print('NewYork Taxi Models_data_prep: ', Path_Models_data_prep)
print('NewYork Taxi Profiling:        ', Path_Profiling)
print('NewYork Taxi Reports:          ', Path_Reports)
print('NewYork Taxi Commun:           ', Path_Commun)
print(' ')
print('Path du datawarehouse NewYork Taxi')
print(' ')
print('DW Path_data_Sources:           ', Path_data_Sources)
print('DW Path_External_Sources:       ', Path_External_Sources)
print('DW Path_Features:               ', Path_Features)
print('DW Path_Model_input:            ', Path_Model_input)

print(' ')
print('Path du reports NewYork Taxi')
print(' ')
print('Reports Profiling results:      ', Path_Profiling_results)
print('Reports Models_scores:          ', Path_Models_scores)
print('Models linear reg report:              ', Path_Mod_linear_reg)

print(Path_to_training_data)

# datetime du projet NewYork Taxi
datetime = re.sub('[ :]', '_', time.asctime(time.localtime(time.time())))