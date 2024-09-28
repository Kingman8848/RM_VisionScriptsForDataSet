import os
import glob
import shutil
import random

def copy_images(input_dir, class_name, num_per_class, output_dir):
    # 创建输出目录
    class_dir = os.path.join(output_dir, class_name)
    os.makedirs(class_dir, exist_ok=True)

    # 获取图片路径列表
    img_paths = glob.glob(os.path.join(input_dir, '*.jpg'))

    # 随机选择图片并复制到指定目录
    selected_paths = random.sample(img_paths, num_per_class)
    for path in selected_paths:
        filename = os.path.basename(path)
        output_path = os.path.join(class_dir, filename)
        shutil.copy2(path, output_path)



input_dir = r'G:\data_check\myadd\kk\BG\LZZ'
output_dir = r'G:\data_check\myadd\kk\BG\LZZ_divide2'
num_per_class = 450
class_names = ["red1", "red2", "red3", "red4", "red5", "red_sentry", "blue1", "blue2", "blue3", "blue4", "blue5", "blue_sentry"]

for class_name in class_names:
    copy_images(input_dir, class_name, num_per_class, output_dir)

'''
其中，input_dir为原始图片所在文件夹路径，output_dir为保存图片的目录路径，num_per_class为每个类别需要的图片数量
，class_names为自定义的类别名列表，按照此代码将每个类别所需的图片复制到对应目录即可。
'''
