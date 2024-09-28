import cv2
import os
import numpy as np


def process_image(image):
    # 在这里你可以对图像进行任何处理
    # 例如，将图像转换为灰度图像
    # return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mark = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 在HSV图像中进行阈值处理
    # 选择范围 [0, 0, 5] 到 [180, 29, 255]
    mask = cv2.inRange(mark, np.array([0, 0, 5]), np.array([180, 29, 255]))

    # 反转掩码
    mask = cv2.bitwise_not(mask)


    return mask


def big_or_small(my_point):
    # 将点转为numpy数组
    cp1, cp2, cp3 = np.array(my_point[0]), np.array(my_point[1]), np.array(my_point[2])

    # 计算各边长度
    len_cp1_cp2 = np.linalg.norm(cp1 - cp2)
    len_cp1_cp3 = np.linalg.norm(cp1 - cp3)
    len_cp2_cp3 = np.linalg.norm(cp2 - cp3)

    # 计算最长边
    len_max = max(len_cp1_cp2, len_cp1_cp3, len_cp2_cp3)

    height_width = {'x': 0, 'y': 0}

    # 根据最长边确定长宽
    if len_max == len_cp1_cp2:
        height_width['x'] = min(len_cp1_cp3, len_cp2_cp3)
        height_width['y'] = max(len_cp1_cp3, len_cp2_cp3)
    elif len_max == len_cp1_cp3:
        height_width['x'] = min(len_cp1_cp2, len_cp2_cp3)
        height_width['y'] = max(len_cp1_cp2, len_cp2_cp3)
    elif len_max == len_cp2_cp3:
        height_width['x'] = min(len_cp1_cp2, len_cp1_cp3)
        height_width['y'] = max(len_cp1_cp2, len_cp1_cp3)
    else:
        # 异常处理部分
        len_dis = [len_max - len_cp1_cp2, len_max - len_cp1_cp3, len_max - len_cp2_cp3]
        ind_min = np.argmin(len_dis)

        if ind_min == 0:
            height_width['x'] = min(len_cp1_cp3, len_cp2_cp3)
            height_width['y'] = max(len_cp1_cp3, len_cp2_cp3)
        elif ind_min == 1:
            height_width['x'] = min(len_cp1_cp2, len_cp2_cp3)
            height_width['y'] = max(len_cp1_cp2, len_cp2_cp3)
        elif ind_min == 2:
            height_width['x'] = min(len_cp1_cp2, len_cp1_cp3)
            height_width['y'] = max(len_cp1_cp2, len_cp1_cp3)
        else:
            raise ValueError("Unexpected length discrepancy.")

    # 计算长宽比
    wh_ratio = height_width['y'] / height_width['x']

    return wh_ratio > 2.3


def extract_numbers(src, lights_vertices, is_small):
    if not src.size:
        return None

    # Light length in image
    light_length = 12
    # Image size after warp
    warp_height = 28
    small_armor_width = 32
    large_armor_width = 54
    # Number ROI size
    roi_size = (20, 28)
    top_light_y = (warp_height - light_length) // 2 - 1
    bottom_light_y = top_light_y + light_length
    warp_width = small_armor_width if is_small else large_armor_width

    target_vertices = np.float32([
        [0, bottom_light_y],
        [0, top_light_y],
        [warp_width - 1, top_light_y],
        [warp_width - 1, bottom_light_y]
    ])

    # Perspective transformation
    lights_vertices = np.float32(lights_vertices)
    rotation_matrix = cv2.getPerspectiveTransform(lights_vertices, target_vertices)
    number_image = cv2.warpPerspective(src, rotation_matrix, (warp_width, warp_height))

    # Get ROI
    x = (warp_width - roi_size[0]) // 2
    y = 0
    number_image = number_image[y:y + roi_size[1], x:x + roi_size[0]]
    # Binarize
    # number_image = cv2.cvtColor(number_image, cv2.COLOR_BGR2GRAY)
    # _, number_image = cv2.threshold(number_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    return number_image

def batch_process_images(input_path, output_path):
    # 确保输出路径存在
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 遍历输入路径中的所有文件
    for filename in os.listdir(input_path):
        input_file = os.path.join(input_path, filename)

        # 检查是否是文件（避免目录）
        if os.path.isfile(input_file):
            # 读取图像
            image = cv2.imread(input_file)

            if image is not None:
                # 处理图像
                processed_image = process_image(image)

                # 生成输出文件路径
                basename, _ = os.path.splitext(filename)
                output_file = os.path.join(output_path, f"{basename}.jpg")

                # 保存图像为JPEG格式
                cv2.imwrite(output_file, processed_image)
                print(f"Processed and saved: {output_file}")
            else:
                print(f"Error reading image: {input_file}")


if __name__ == "__main__":
    input_dir = 'input_images'  # 输入路径
    output_dir = 'output_images'  # 输出路径

    batch_process_images(input_dir, output_dir)
