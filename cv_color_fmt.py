import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

with open('cv_color_format.txt', 'wt') as f:
    for fmt in flags:
        f.write('%s\n'%fmt)

print('done')