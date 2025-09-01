from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import *
import os
import ctypes

from PIL import Image, ImageTk

from img_file import image_paths2str, save_image

root = None

def init():
    global root
    root = Tk()
    root.withdraw()  # 隐藏root窗口

    # 告诉操作系统使用程序自身的dpi适配
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    # 获取屏幕的缩放因子
    scale_factor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
    # 设置程序缩放
    root.tk.call('tk', 'scaling', scale_factor / 75)

# 弹窗选择多个图片
def select_image_files():
    file_paths = filedialog.askopenfilenames(
        title="选择图片",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )
    return list(file_paths)

def confirm_selected_images(image_paths):
    response = messagebox.askokcancel("确认图片", "图片及其顺序是否正确？\n" + image_paths2str(image_paths))
    return response

def confirm_concat_image(concat_img):
    '''
    预览拼接结果，询问用户是否正确
    :param concat_img: 拼接后的图像
    :return: bool，用户认为图像是否正确
    '''
    top = Toplevel(root)
    top.title("拼接结果预览")

    # 设置图像显示大小：宽度为 min(屏幕宽度, 图片宽度)，高度为 min(屏幕高度, 图片高度)
    # 1. 获取屏幕大小
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    # 2. 计算画布大小
    img_width, img_height = concat_img.size
    canvas_width = min(screen_width, img_width)
    canvas_height = min(screen_height, img_height)

    # 创建画布
    canvas = Canvas(top, width=canvas_width, height=canvas_height)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    # 创建纵横滚动条
    scrollbar_y = Scrollbar(top, orient=VERTICAL, command=canvas.yview)
    scrollbar_y.pack(side=RIGHT, fill=Y)
    scrollbar_x = Scrollbar(top, orient=HORIZONTAL, command=canvas.xview)
    scrollbar_x.pack(side=BOTTOM, fill=X)
    # 滚动条关联到画布
    canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    # 画布显示图片
    img = ImageTk.PhotoImage(concat_img)
    img_id = canvas.create_image(0, 0, anchor='nw', image=img)
    canvas.image = img  # Keep a reference to avoid garbage collection

    # 绑定：鼠标滚轮 -> 纵滚动条
    def scroll_y(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    canvas.bind_all("<MouseWheel>", scroll_y)

    # 弹窗询问用户
    response = messagebox.askokcancel("确认拼接结果", "是否保存拼接后的图片？")
    return response

def save_image_file(img):
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        save_image(img, file_path)
        return file_path
    else:
        print("取消保存")
        return None

# 打开文件管理器并选中图片
# 需保证路径正确，否则会打开“此电脑”
def open_in_explorer(image_path):
    image_path = image_path.replace('/', '\\') # 修正路径
    cmd = f'explorer /select, \"{image_path}\"'
    print(cmd)
    os.system(cmd)