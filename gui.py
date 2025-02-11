from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import *
import os
import ctypes

from img_file import image_paths2str

root = None

# 弹窗选择多个图片
def select_image_files():
    global root
    root = Tk()
    root.withdraw()  # 隐藏root窗口

    # 告诉操作系统使用程序自身的dpi适配
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    # 获取屏幕的缩放因子
    scale_factor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
    # 设置程序缩放
    root.tk.call('tk', 'scaling', scale_factor / 75)

    file_paths = filedialog.askopenfilenames(
        title="选择图片",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )
    return list(file_paths)

def confirm_selected_images(image_paths):
    response = messagebox.askokcancel("确认图片", "图片及其顺序是否正确？\n" + image_paths2str(image_paths))
    if response:
        return True
    else:
        return False

# 打开文件管理器并选中图片
# 需保证路径正确，否则会打开“此电脑”
def open_in_explorer(image_path):
    image_path = image_path.replace('/', '\\') # 修正路径
    cmd = f'explorer /select, \"{image_path}\"'
    print(cmd)
    os.system(cmd)