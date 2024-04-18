import numpy as np
from PIL import Image

im = Image.open('Output/image-parse-v3/0.png')

print(np.unique(np.array(im)))
np_im = np.array(im)
np_im[np_im==0] = 0
np_im[np_im==2] = 0
np_im[np_im==5] = 255
np_im[np_im==9] = 0
np_im[np_im==10] = 0
np_im[np_im==12] = 0
np_im[np_im==13] = 0
np_im[np_im==14] = 0
np_im[np_im==15] = 0
np_im[np_im==16] = 0
np_im[np_im==17] = 0
new_im = Image.fromarray(np_im)

# 保存图像到本地，以JPEG格式保存
new_im.save("./Output/gt_cloth_warped_mask/0.jpg", format="JPEG")

print("新的图像已保存到本地：new_image.jpg")
