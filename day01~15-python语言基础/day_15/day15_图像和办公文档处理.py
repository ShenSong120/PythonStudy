from PIL import Image

# # 打印照片基本信息
# image = Image.open('/home/ss/Downloads/women.jpg')
# print(image.format)
# print(image.size)
# print(image.mode)
# image.show()

# # 裁剪图像
# image = Image.open('/home/ss/Downloads/women.jpg')
# rect = 80, 20, 310, 360
# image.crop(rect).show()

# # 生成缩略图
# image = Image.open('/home/ss/Downloads/women.jpg')
# size = 128, 128
# image.thumbnail(size)
# image.show()

# # 缩放和粘贴图像
# image1 = Image.open('/home/ss/Downloads/women.jpg')
# image2 = Image.open('/home/ss/Downloads/sex_women.jpg')
# rect = 80, 20, 310, 360
# guido_head = image2.crop(rect)
# width, height = guido_head.size
# image1.paste(guido_head.resize((int(width/1.5), int(height/1.5))), (172, 40))
# image1.show()

# # 旋转和翻转
# image = Image.open('/home/ss/Downloads/women.jpg')
# # 下面两句话意思相同
# # image.rotata(180).show()
# # image.transpose(Image.ROTATE_180).show()
# image.show()
# image.transpose(Image.FLIP_LEFT_RIGHT).show()

# # 操作像素
# image = Image.open('/home/ss/Downloads/women.jpg')
# for x in range(80, 310):
#     for y in range(20, 360):
#         image.putpixel((x, y), (128, 128, 128))
# image.show()

# # 滤镜效果
# from PIL import Image, ImageFilter
# image = Image.open('/home/ss/Downloads/women.jpg')
# image.filter(ImageFilter.CONTOUR).show()