import os

# 获取指定目录下的所有图片
def get_image_paths(directory):
    supported_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    image_paths = [os.path.join(directory, file) for file in os.listdir(directory) if file.lower().endswith(supported_extensions)]
    print(f"共找到{len(image_paths)}张图片：")
    print_image_paths(image_paths)
    return image_paths

# 打印图片路径
def print_image_paths(image_paths):
    for img_path in image_paths:
        print(img_path)