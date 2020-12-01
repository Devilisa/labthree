import struct
import matplotlib.pyplot as plt
import numpy as np
import math
from base64 import b64encode as enc


def bin_pic(pic):
    with open(pic, 'rb')as f:
        binary = enc(f.read())
    return binary


File_Width = 100
File_Height = 100
File_Size = (2*File_Width) % 4
# расчет размера файла для 16-ричного представления
Color_depth = 8
Color_num = 256
File_Offset = 1078

t = np.arange(0, 10*math.pi)
x = 24.8*(np.cos(t) + np.cos(6.2*t)/6.2)
y = 24.8*(np.sin(t) + np.sin(6.2*t)/6.2)
plt.title('Lab3')
plt.xlabel('Axe x')
plt.ylabel('Axe y')
plt.grid()
plt.plot(t, x, label="cos", marker='o')
plt.plot(t, y, label="sin", marker='^')
plt.legend()
plt.show()
img = 'Figure_1.jpeg'
# с помощью plt.show() мы видим график и сохраняем его как Figure_1.jpeg
with open("graph.bmp", "wb") as fail:
    fail.write(struct.pack("<2ci2hi", b'B', b'M', File_Size, 0, 0, File_Offset))
    # создали блок BITMAPFILEHEADER
    fail.write(struct.pack("<3i2h6i", 40, File_Width, File_Height, 1, Color_num, 0, File_Size*Color_depth, 0, 0, 0, 0))
    # создали блок BITMAPINFOHEADER
    for i in bin_pic(img):
        fail.write(struct.pack("<h", i))
