import cv2
import os

# 设置数据集路径和标签文件后缀 不能存在中文路径
data_path = r"E:\\RM_datas\\blue_small"
label_suffix = ".txt"

# 读取所有图像和标签
img_files = sorted(os.listdir(os.path.join(data_path, "images")))
label_files = sorted([f for f in os.listdir(os.path.join(data_path, "labels")) if f.endswith(label_suffix)])

# 创建类别文件夹
class_names = ["red1", "red2", "red3", "red4", "red5", "red_sentry","red_outpost","red_base",
               "blue1", "blue2", "blue3", "blue4", "blue5", "blue_sentry","blue_outpost","blue_base"]
# class_names = ["red1", "red2", "red3", "red4", "red5", "red_sentry",
#                "blue1", "blue2", "blue3", "blue4", "blue5", "blue_sentry"]
# class_names=["red1","2","3","4","5","7","blue1","2","3","4","5","7"]
# class_names=["red1"]
# class_names=["red","blue"]
# class_names = ["R_centry", "Target"]
for class_name in class_names:
    os.makedirs(os.path.join(data_path, class_name), exist_ok=True)

# 循环处理每个图像
for img_file, label_file in zip(img_files, label_files):
    # 读取图像和标签
    img = cv2.imread(os.path.join(data_path, "images", img_file))
    with open(os.path.join(data_path, "labels", label_file), "r") as f:
        lines = f.read().splitlines()

    # 循环处理每个目标
    for line in lines:
        class_id, center_x, center_y, width, height = [float(x) for x in line.split()]
        class_name = class_names[int(class_id)]
        # width=width*0.8
        # height=height*0.8

        # 计算目标在图像中的坐标
        left = int((center_x - width / 2) * img.shape[1])
        top = int((center_y - height / 2) * img.shape[0])
        right = int((center_x + width / 2) * img.shape[1])
        bottom = int((center_y + height / 2) * img.shape[0])

        # 在图像中框出目标
        #cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

        # 将目标保存到对应类别的文件夹中
        obj_id = len(os.listdir(os.path.join(data_path, class_name))) + 1
        obj_filename = f"{img_file[:-4]}_{obj_id}.jpg"
        obj_path = os.path.join(data_path, class_name, obj_filename)
        obj_img = img[top:bottom, left:right].copy()
        cv2.imwrite(obj_path, obj_img)
