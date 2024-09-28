import os

def editor_name_jpg(source_folder,source_info,your_new_info):
    path = source_folder  # 文件所在路径
    files = os.listdir(path)  # 获取所有文件名
    i = 1
    target_info = source_info
    name_len = len(target_info)  # 要更改的字符长度
    new_info = your_new_info
    for file in files:
        if file.endswith(".jpg"):  # 只处理图片文件
            old_name = file
            new_name = new_info + str(i) + ".jpg"
            if len(old_name) >= name_len:
                new_name = new_info + old_name[name_len:]  # 截取要更改的字符长度后面的子串拼接新名称
            os.rename(os.path.join(path, old_name), os.path.join(path, new_name))  # 对文件进行重命名
            i += 1

def editor_name_txt(source_folder,source_info,your_new_info):
    path = source_folder  # 文件所在路径
    files = os.listdir(path)  # 获取所有文件名
    i = 1
    target_info = source_info
    name_len = len(target_info)  # 要更改的字符长度
    new_info = your_new_info
    for file in files:
        if file.endswith(".txt"):  # 只处理txt文件
            old_name = file
            new_name = new_info + str(i) + ".txt"
            if len(old_name) >= name_len:
                new_name = new_info + old_name[name_len:]  # 截取要更改的字符长度后面的子串拼接新名称
            os.rename(os.path.join(path, old_name), os.path.join(path, new_name))  # 对文件进行重命名
            i += 1

img_path = r"E:\TempData\Temp2N3\red3_ff\images"
txt_path = r"E:\TempData\Temp2N3\red3_ff\images"
target_info = "red1_ff"
new_info = "red3_ff"
editor_name_jpg(img_path, target_info, new_info)
editor_name_txt(txt_path, target_info, new_info)
