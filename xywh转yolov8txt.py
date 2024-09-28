import os


# 定义转换函数
def convert_yolo_to_yolov8(label_path, new_label_path, org_w, org_h):
    # 打开旧的标签文件
    with open(label_path, 'r') as f:
        lines = f.readlines()

    # 遍历每一行标签
    for line in lines:
        # 将标签按空格拆分成列表
        label_list = line.strip().split(' ')

        # 获取标签中的四个坐标点，以及类别号
        cls, x_center, y_center, width, height = map(float, label_list)

        # 计算出新的yolov8格式标签
        cls = int(cls)
        x_min = (x_center + (width / 2)) / org_w
        y_min = (y_center + (height / 2)) / org_h
        w = width / org_w
        h = height / org_h

        # 将yolov8格式标签以字符串格式保存到新的标签文件中
        with open(new_label_path, 'a') as f:
            f.write(f"{cls} {x_min} {y_min} {w} {h}\n")


# 定义标签文件夹路径和新标签文件夹路径，以及原图片信息
label_folder = r"G:\data_check\buff\999"
new_label_folder = r"G:\data_check\buff\666"
#895-2391
original_width = 960
original_height = 540

if not os.path.exists(new_label_folder):
    os.makedirs(new_label_folder)

count = 1

# 遍历标签文件夹中的所有标签文件，进行格式转换
for filename in os.listdir(label_folder):
    label_path = os.path.join(label_folder, filename)
    new_label_path = os.path.join(new_label_folder, filename)

    # 将YOLO格式的标签文件转换为YOLOv8格式的标签文件
    convert_yolo_to_yolov8(label_path, new_label_path, original_width, original_height)
    print(f"已转换{count}个标签数据")
    count = count + 1