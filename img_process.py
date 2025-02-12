from PIL import Image

# 纵向拼接图片
def concatenate_images_vertically(image_paths):
    images = [Image.open(image_path).convert("RGBA") for image_path in image_paths]

    # 计算总高度和最大宽度
    total_height = sum(image.height for image in images)
    max_width = max(image.width for image in images)

    # 创建新图片
    new_image = Image.new('RGBA', (max_width, total_height))

    # 复制图片到新图片
    y_offset = 0
    for image in images:
        new_image.paste(image, (0, y_offset))
        y_offset += image.height

    return new_image


