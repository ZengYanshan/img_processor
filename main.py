from img_file import *
from img_process import *
from gui import *

if __name__ == '__main__':
    init()

    # 用户选择图片
    image_paths = select_image_files()
    print_image_paths(image_paths)

    # 拼接图片
    print("拼接图片中...")
    concat_img = concatenate_images_vertically(image_paths)

    # 用户确认结果是否正确
    confirm = confirm_concat_image(concat_img)
    if confirm:
        # 形成输出路径（“首个输入路径_concat”）
        # directory, filename = os.path.split(image_paths[0])
        # name, ext = os.path.splitext(filename)
        # new_filename = f"{name}_concat{ext}"
        # output_path = os.path.join(directory, new_filename)

        output_path = save_image_file(concat_img)
        if output_path != None:
            open_in_explorer(output_path)
    else:
        print("拼接图片不正确")
