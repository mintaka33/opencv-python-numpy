import os
import numpy as np
import cv2

w, h = 320, 240

def split_nv12():
    y = a[:w*h:].reshape(h, w)
    uv = a[w*h:].reshape(h//2, w)
    u = uv[:, 0::2]
    v = uv[:, 1::2]
    y.tofile('y.bin')
    u.tofile('u.bin')
    v.tofile('v.bin')
    os.system('ffmpeg -s 320x240 -pix_fmt gray -f rawvideo -i y.bin y.bmp -y')
    os.system('ffmpeg -s 160x120 -pix_fmt gray -f rawvideo -i u.bin u.bmp -y')
    os.system('ffmpeg -s 160x120 -pix_fmt gray -f rawvideo -i v.bin v.bmp -y')

def gen_nv12(w, h):
    cmd = 'ffmpeg -f lavfi -i testsrc2 -s %dx%d -vframes 1 -pix_fmt nv12 -f rawvideo -y test.nv12' % (w, h)
    os.system(cmd)
    cmd = 'ffmpeg -f lavfi -i testsrc2 -s %dx%d -vframes 1 -y test.bmp' % (w, h)
    os.system(cmd)

#gen_nv12(w, h)

a = np.fromfile('test.nv12', dtype=np.uint8)
img = cv2.cvtColor(a.reshape(h*3//2, w), cv2.COLOR_YUV2BGR_NV12)
cv2.imwrite('out.bmp', img)

img2 = cv2.resize(img, (w*2, h*2))
cv2.imwrite('out2.bmp', img2)

#split_nv12(a)

print('done')