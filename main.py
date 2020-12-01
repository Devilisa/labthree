import math
import struct


File_Width = 100
File_Height = 100
File_Size = 0
Color_depth = 4
Color_num = 32
File_Offset = 54
maxt = 10*math.pi

points = []
for t in range(0, round(maxt) + 1):
    x = round(24.8 * (math.cos(t) + math.cos(6.2 * t) / 6.2))
    y = round(24.8 * (math.sin(t) + math.sin(6.2 * t) / 6.2))
    if [t, y] not in points:
        points.append([t, y])
    if [t, x] not in points:
        points.append([t, x])


with open("graph.bmp", "wb") as fail:
    fail.write(struct.pack("<2ci2hi", b'B', b'M', File_Size, 0, 0, File_Offset))
    # создали блок BITMAPFILEHEADER
    fail.write(struct.pack("<3i2h6i", 40, File_Width, File_Height, 1, Color_num, 0, File_Size*Color_depth, 0, 0, 0, 0))
    # создали блок BITMAPINFOHEADER
    for y in range(-50, 50):
        for x in range(-50, 50):
            coords = [x, y]
            if coords in points:
                fail.write(struct.pack("<i", 0))
            else:
                fail.write(struct.pack("<i", 16777215))
