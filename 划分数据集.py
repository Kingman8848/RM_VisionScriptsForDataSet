import os
import random
from shutil import copyfile

# 只需填写数据集所在路径，该路径下包含images文件夹与labels文件夹
dataset_path = r"E:\fire"
# 生成的文件夹排布格式：dataset文件夹内生成train、test、val文件夹，这三个文件夹中均包含images与labels文件夹

# 划分比例
train_ratio = 0.8
test_ratio = 0
val_ratio = 0.2

# 遍历图片文件夹，获取所有图片文件名
image_folder = os.path.join(dataset_path, "images")
image_files = os.listdir(image_folder)
# 打乱图片文件名顺序
random.shuffle(image_files)
# 计算划分数量
num_images = len(image_files)
num_train = int(num_images * train_ratio)
num_val = int(num_images * val_ratio)
num_test = num_images - num_train - num_val
# 按比例划分图片文件名
train_files = image_files[:num_train]
val_files = image_files[num_train:num_train+num_val]
test_files = image_files[num_train+num_val:]

print("正在进行图片数据集划分...")

# 复制图片文件到对应的文件夹
temp_file = os.path.join(dataset_path, "train", "images")
if not os.path.exists(temp_file):
    os.makedirs(temp_file)
for filename in train_files:
    src_file = os.path.join(image_folder, filename)
    dst_file = os.path.join(dataset_path, "train", "images", filename)
    copyfile(src_file, dst_file)
print(f"训练集img：已将{num_train}张图片划分复制到 {temp_file} 中")

temp_file = os.path.join(dataset_path, "test", "images")
if not os.path.exists(temp_file):
    os.makedirs(temp_file)
for filename in test_files:
    src_file = os.path.join(image_folder, filename)
    dst_file = os.path.join(dataset_path, "test", "images", filename)
    copyfile(src_file, dst_file)
print(f"测试集img：已将{num_test}张图片划分复制到 {temp_file} 中")

temp_file = os.path.join(dataset_path, "val", "images")
if not os.path.exists(temp_file):
    os.makedirs(temp_file)
for filename in val_files:
    src_file = os.path.join(image_folder, filename)
    dst_file = os.path.join(dataset_path, "val", "images", filename)
    copyfile(src_file, dst_file)
print(f"验证集img：已将{num_val}张图片划分复制到 {temp_file} 中")

print("--------------------------------------")
print("数据集图片划分结束，正在进行数据集标签划分...")
print("--------------------------------------")

# 遍历标注文件夹，获取所有标注文件名
label_folder = os.path.join(dataset_path, "labels")
label_files = os.listdir(label_folder)
# 复制标注文件到对应的文件夹
temp_file = os.path.join(dataset_path, "train", "labels")
if not os.path.exists(temp_file):
    os.makedirs(temp_file)
for filename in train_files:
    src_file = os.path.join(label_folder, filename[:-4] + ".txt")
    dst_file = os.path.join(dataset_path, "train", "labels", filename[:-4] + ".txt")
    copyfile(src_file, dst_file)
print(f"训练集lab：已将{num_train}个标签划分复制到 {temp_file} 中")

temp_file = os.path.join(dataset_path, "test", "labels")
if not os.path.exists(temp_file):
    os.makedirs(temp_file)
for filename in test_files:
    src_file = os.path.join(label_folder, filename[:-4] + ".txt")
    dst_file = os.path.join(dataset_path, "test", "labels", filename[:-4] + ".txt")
    copyfile(src_file, dst_file)
print(f"测试集lab：已将{num_test}个标签划分复制到 {temp_file} 中")

temp_file = os.path.join(dataset_path, "val", "labels")
if not os.path.exists(temp_file):
    os.makedirs(temp_file)
for filename in val_files:
    src_file = os.path.join(label_folder, filename[:-4] + ".txt")
    dst_file = os.path.join(dataset_path, "val", "labels", filename[:-4] + ".txt")
    copyfile(src_file, dst_file)
print(f"验证集lab：已将{num_val}个标签划分复制到 {temp_file} 中")

print("数据集图片对应标签划分结束")
