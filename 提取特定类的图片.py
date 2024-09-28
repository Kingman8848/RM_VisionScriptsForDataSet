import os
import shutil

'''此代码用于提取特定数据标签的数据集到另一个文件，提取时为移动的方式，所以请先提前备份以免出问题'''

# 原始文件夹路径
img_folder = r'E:\TempData\Changsha\myFu\mypart1\images'
txt_folder = r'E:\TempData\Changsha\myFu\mypart1\labels'

# 新文件夹路径
new_img_folder = r'E:\TempData\Changsha\myFu\mypart1'
new_txt_folder = r'E:\TempData\Changsha\myFu\mypart1'

#设定目标值、最大移动数量
target_value = 12
max_num = 200 #400份，一份包含一张图片与一个jpg
start_num = 0
print("当前设置的提取类的值为：{}，最大提取数量为：{}".format(target_value,max_num-start_num))

#判断文件路径是否存在
if not os.path.exists(new_img_folder):
    os.makedirs(new_img_folder)
    print("存放提取后图片存放的文件夹路径不存在，已自动创建为' {} '目录下".format(new_img_folder))
if not os.path.exists(new_txt_folder):
    os.makedirs(new_txt_folder)
    print("存放提取后标签存放的文件夹路径不存在，已自动创建为' {} '目录下".format(new_txt_folder))

print("正在提取中.....请稍后...")
# 遍历文件夹中的所有txt文件
for txt_file in os.listdir(txt_folder):
    # 获取txt文件名和对应的jpg文件名
    txt_name = os.path.splitext(txt_file)[0]
    jpg_file = os.path.join(img_folder, txt_name + '.jpg')
    # 判断jpg文件是否存在
    if not os.path.isfile(jpg_file):
        continue
    # 读取txt文件内容并逐行判断
    with open(os.path.join(txt_folder, txt_file), 'r') as f:
        content = f.readlines()
    for line in content:
        value = int(line.split()[0])
        # 如果整数值等于目标值，则将txt文件和jpg文件移动到新文件夹
        if value == target_value and start_num < max_num:
            # 判断两个新文件夹中是否已存在同名文件
            if os.path.exists(os.path.join(new_txt_folder, txt_file)) and os.path.exists(os.path.join(new_img_folder, jpg_file)):
                print('文件已存在:', txt_file, jpg_file)
                break
            # 移动文件
            try:
                shutil.move(os.path.join(txt_folder, txt_file), new_txt_folder)
                shutil.move(jpg_file, new_img_folder)
                print('文件已移动:', txt_file, jpg_file)
                start_num = start_num + 1
                break
            except Exception as e:
                print('文件移动失败:', txt_file, jpg_file, e)
                break


print("提取完成")

'''
if not os.path.exists(new_folder):
    os.makedirs(new_folder)
# 遍历所有txt文件
for txt_file in os.listdir(txt_folder):
    # 获取txt文件名（不包含扩展名）
    txt_name = os.path.splitext(txt_file)[0]
    # 拼接对应图片文件名
    img_file = os.path.join(img_folder, txt_name + '.jpg')
    # 判断图片文件是否存在
    if not os.path.isfile(img_file):
        continue
    # 读取txt文件内容
    with open(os.path.join(txt_folder, txt_file), 'r') as f:
        content = f.read().strip()
    # 解析整数值
    value = int(content.split()[0])
    # 如果整数值等于6，则将该txt文件和对应的图片文件移动到新文件夹
    if value == 1:
        shutil.move(os.path.join(img_folder, img_file), new_folder)
        shutil.move(os.path.join(txt_folder, txt_file), new_folder)
'''
