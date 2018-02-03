from 华哥需求.CreateMvpProject import *
import numpy as np

# create_template_project(TEMPLATE_FILE, TEMPLATE_INFO_JSON_FILE)

# help(np)

a = np.array([1, 2, 3, 4])
print(a)
np.add.at(a, [0, 1, 2, 3], 1)
print(a)
