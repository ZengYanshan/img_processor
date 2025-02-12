import os

# 获取指定目录下的所有图片
def get_image_paths(directory):
    supported_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    image_paths = [os.path.join(directory, file) for file in os.listdir(directory) if file.lower().endswith(supported_extensions)]
    print(f"共找到{len(image_paths)}张图片：")
    print_image_paths(image_paths)
    return image_paths

# 生成图片路径字符串
def image_paths2str(image_paths):
    img_path_str = ""
    for img_path in image_paths:
        img_path_str += img_path + '\n'
    return img_path_str

# 打印图片路径
def print_image_paths(image_paths):
    print(image_paths2str(image_paths))

# 保存图片
def save_image(img, output_path):
    img.save(output_path)
    print(f"拼接完成，已保存为{output_path}")
