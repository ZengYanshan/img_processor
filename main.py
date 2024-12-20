from img_file import *
from img_process import *
from gui import *

if __name__ == '__main__':
    # 用户选择图片
    image_paths = select_image_files()
    print_image_paths(image_paths)

    # 用户确认结果是否正确
    user_input = input("图片及其顺序是否正确？(y/n): ")
    if user_input.lower() == 'y':
        print("拼接图片中...")
        output_path = concatenate_images_vertically(image_paths)
        open_in_explorer(output_path)
    else:
        print("中止")