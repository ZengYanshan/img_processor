import tkinter as tk
from tkinter import filedialog
import os

# 弹窗选择多个图片
def select_image_files():
    root = tk.Tk()
    root.withdraw()  # 隐藏root窗口
    file_paths = filedialog.askopenfilenames(
        title="选择图片",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )
    return list(file_paths)

# 打开文件管理器并选中图片
# 需保证路径正确，否则会打开“此电脑”
def open_in_explorer(image_path):
    image_path = image_path.replace('/', '\\')
    cmd = f'explorer /select, \"{image_path}\"'
    print(cmd)
    os.system(cmd)