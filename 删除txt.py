import os

folder_path = 'D:\\FU_data\\KingmanV5_2\\KingmanV5_2\\train\\images'  # 替换为你的文件夹路径

# 获取文件夹中所有文件和子文件夹的列表
file_list = os.listdir(folder_path)

# 循环处理文件夹中的每个文件
for file in file_list:
    file_path = os.path.join(folder_path, file)  # 获取文件的完整路径
    if file.endswith('.txt') and os.path.isfile(file_path):  # 检查是否为 .txt 文件并且是文件而不是文件夹
        os.remove(file_path)  # 删除文件
