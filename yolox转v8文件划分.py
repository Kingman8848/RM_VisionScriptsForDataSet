import os
import shutil

# 定义原始图片目录和新的图片目录
original_jpg_dir = r"G:\data_check\all2\yoloxWay\images"  # 填入原始图片文件夹的路径
original_txt_dir = r"G:\data_check\all2\yoloxWay\labels"
new_jpg_dir = r"G:\data_check\all2\yoloxWay\test\images"  # 填入新的图片文件夹的路径
new_txt_dir = r"G:\data_check\all2\yoloxWay\test\labels"

# 定义 txt 文件路径
txt_file = r"G:\data_check\all2\yoloxWay\test.txt"  # 填入 txt 文件的路径

if not os.path.exists(new_jpg_dir):
    os.makedirs(new_jpg_dir)
if not os.path.exists(new_txt_dir):
    os.makedirs(new_txt_dir)


# 读取 txt 文件中的所有图片名称
with open(txt_file, 'r') as f:
    names = [line.strip() for line in f.readlines()]

# 遍历原始图片目录，将名称与 txt 文件中的名称匹配的图片移动到新的文件夹
for name in names:
    src_path = os.path.join(original_jpg_dir, name + '.jpg')  # 拼接原始图片路径
    dst_path = os.path.join(new_jpg_dir, name + '.jpg')  # 拼接新的图片路径

    if os.path.exists(src_path):  # 判断原始图片是否存在
        shutil.move(src_path, dst_path)  # 移动图片文件
    else:
        print(f"{src_path} does not exist!")  # 如果原始图片不存在，则打印提示信息

# 遍历原始图片目录，将名称与 txt 文件中的名称匹配的标签移动到新的文件夹
for name in names:
    src_path = os.path.join(original_txt_dir, name + '.txt')  # 拼接原始标签路径
    dst_path = os.path.join(new_txt_dir, name + '.txt')  # 拼接新的标签路径

    if os.path.exists(src_path):  # 判断原始标签是否存在
        shutil.move(src_path, dst_path)  # 移动标签文件
    else:
        print(f"{src_path} does not exist!")  # 如果原始标签不存在，则打印提示信息

