import numpy as np
import scipy

csv_red_file = np.loadtxt(r'D:\New project\venv\share\man\data\winequality\winequality-red.csv',delimiter=',',dtype=str)
csv_white_file = np.loadtxt(r'D:\New project\venv\share\man\data\winequality\winequality-white.csv',delimiter=',',dtype=str)

wine_red = np.array(csv_red_file)
wine_white = np.array(csv_white_file)

print(wine_white)
print(wine_red)

data_red = wine_red[1:,:].astype(np.float)
data_white = wine_white[1:,:].astype(np.float)
lable_red = wine_red[0,0:]
lable_white = wine_white[0,0:]
print (lable_white)
print (lable_red)

red_array = np.array(wine_red)
white_array = np.array(wine_white)
print(red_array.shape)
pass
