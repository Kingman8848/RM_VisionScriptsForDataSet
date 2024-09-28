import os
import shutil


def rename_images(folder_path, new_name_prefix='image'):
    # 获取指定路径下的所有文件
    file_list = os.listdir(folder_path)

    # 初始化计数器
    count = 1

    # 遍历文件列表
    for file_name in file_list:
        # 检查文件是否为图片文件
        if file_name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        # if file_name.endswith(('.txt')):
            # 获取文件的扩展名
            _, ext = os.path.splitext(file_name)

            # 构建新文件名
            # new_file_name = f"{new_name_prefix}_{count}{ext}"
            new_file_name=f'newadd_{12545+count}.jpg'

            # 构建完整的旧路径和新路径
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_file_name)

            try:
                # 重命名文件
                os.rename(old_path, new_path)
                print(f"Renamed {file_name} to {new_file_name}")

                # 更新计数器
                count += 1
            except Exception as e:
                print(f"Failed to rename {file_name}: {str(e)}")


# 要处理的文件夹路径
folder_path = "E:\\RM_datas\\QX_v5_add\\val\\images"

# 调用函数重新命名图片文件
rename_images(folder_path)
