import cv2
import numpy as np
import os
#print directorty where this script is located
from os.path import dirname, abspath
script_path = abspath(dirname(__file__))
print(script_path)
image = cv2.imread(script_path+"/image.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, bw_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite(script_path+"/image_bw.png", bw_image)
image = cv2.imread(script_path+"/image_bw.png")
height, width, channels = image.shape
total_pixels = height * width
array = []
array2 = []
array3 = [] 
array4 = [] #idk
x = 0
for i, j in np.ndindex(image.shape[:-1]):
    x += 1
    array2.append(image[i, j].tolist())  
    if x == width:
        x = 0
        print("new row")
        array.append(array2)
        array2 = [] 
red = (255, 0, 0)
with open(script_path+"/a.txt", 'w') as f:
    f.write(str(array))
print("ok")
abc = []
print("done")
import casioplot
for x in range(height):
    array3 = [] 
    for i in range(width):
        #print(array[x][i]) #print first row
        if array[x][i] == [0,0,0]:
            #print("X: ", x)
            #print("Y: ", i)
            abc.append((x,i))
        #print("Y: ", i)
        array3.append(array[x][i])
    array4.append(array3)
print("HEIGHT", height, "WIDTH", width) #idk about this
print(array4)

for i in range(5):
    print('\n')
print(abc)
code = []
for i in range(len(abc)):
    casioplot.set_pixel(abc[i][1], abc[i][0], (0,0,0))
    code.append(f"casioplot.set_pixel({abc[i][1]}, {abc[i][0]}, {0,0,0})")
print(code)

with open(script_path+"/code.py", 'w') as f:
    f.write("import casioplot" + '\n')
    for i in range(len(code)):
        f.write(code[i] + '\n')
    f.write("casioplot.show_screen()" + '\n')
while True:
    casioplot.show_screen()