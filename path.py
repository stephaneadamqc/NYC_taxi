import os
import time
import re

report = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports')
datetime = re.sub('[ :]', '_', time.asctime(time.localtime(time.time())))
path_to_training_data = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'load_data', 'data_warehouse')


