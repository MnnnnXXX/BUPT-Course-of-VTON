from PIL import Image
import os

def resize_image(image_path, target_width, target_height, save_path=None):
    # 打开图像
    image = Image.open(image_path)

    # 获取原始图像大小
    original_width, original_height = image.size

    # 计算调整后的图像大小
    if original_width / original_height > target_width / target_height:
        # 基于目标宽高比例调整高度
        resized_height = int(original_height * target_width / original_width)
        resized_image = image.resize((target_width, resized_height))
    else:
        # 基于目标宽高比例调整宽度
        resized_width = int(original_width * target_height / original_height)
        resized_image = image.resize((resized_width, target_height))

    # 创建白色背景
    new_image = Image.new("RGB", (target_width, target_height), "white")

    # 计算粘贴位置
    paste_x = (target_width - resized_image.width) // 2
    paste_y = (target_height - resized_image.height) // 2

    # 在白色背景上粘贴调整后的图像
    new_image.paste(resized_image, (paste_x, paste_y))

    # 如果指定了保存路径，则保存修改后的图像
    if save_path:
        new_image.save(save_path)

    return new_image

# 图像路径和目标大小
# 图像路径和目标大小
image_paths = ["Input\\cloth\\0.jpg", "Input\\image\\0.jpg"]
target_width = 768
target_height = 1024

# 每张图像对应的保存路径
save_paths = ["Output\\resized_cloth\\0.jpg", "Output\\resized_image\\0.jpg"]

# 处理每张图像并保存到对应位置
for image_path, save_path in zip(image_paths, save_paths):
    # 调整图像大小
    resized_image = resize_image(image_path, target_width, target_height)

    # 保存修改后的图像到本地
    resized_image.save(save_path)
    print("Resized image saved at:", save_path)

    # 如果保存路径中包含 "Output\\resized_image"，则再保存一次到指定文件夹中
    if "Output\\resized_image" in save_path:
        # 获取另一个保存路径
        another_save_path = save_path.replace("Output\\resized_image", "image-densepose\\image_path")
        # 保存修改后的图像到另一个指定文件夹中
        resized_image.save(another_save_path)
        print("Resized image saved at:", another_save_path)


# 处理每张图像并保存到对应位置
for image_path, save_path in zip(image_paths, save_paths):
    # 调整图像大小
    resized_image = resize_image(image_path, target_width, target_height)

    # 保存修改后的图像到本地
    resized_image.save(save_path)
    print("Resized image saved at:", save_path)
