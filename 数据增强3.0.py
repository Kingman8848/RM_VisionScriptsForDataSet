import os
import random
import cv2

# 设置随机种子，以保证每次运行的结果一致
# random.seed(0)

img_num = 3     #粘贴数量

'''类序号↓'''
classNum = 1
myname = "target1"        #保存时的命名
# 各组成文件夹的路径
folder_background = r"E:\TempData\Changsha\TTT"       #存放干扰背景图片
folder_target = r"G:\data_check\buff\CropsV2\target"       #用于存放抠出来的装甲板图片
folder_txt = r"G:\data_check\FinallyFu\add\labels"       #用于存放生成的与背景图片txt文件
folder_result = r"G:\data_check\FinallyFu\add\images"              #用于存放操作后的图片

rate = 1  #装甲板目标的缩放倍数

if not os.path.exists(folder_background):
    os.makedirs(folder_background)
    print("存放背景图片的文件夹路径不存在！")

if not os.path.exists(folder_txt):
    os.makedirs(folder_txt)
    print("生成的txt存放的文件夹路径不存在，已自动创建为' {} '目录下".format(folder_txt))

if not os.path.exists(folder_result):
    os.makedirs(folder_result)
    print("存放操作后图片的文件夹路径不存在，已自动创建为' {} '目录下".format(folder_result))

def is_intersected(rect1, rect2):
    """
    :param rect1: 矩形1，主对角线坐标（(x1, y1), (x2, y2)）
    :param rect2: 矩形2，主对角线坐标（(x1, y1), (x2, y2)）
    :return: True or False，表示两个矩形是否有面积相交部分
    """
    x1_1, y1_1 = rect1[0]
    x2_1, y2_1 = rect1[1]
    x_min_1, x_max_1 = min(x1_1, x2_1), max(x1_1, x2_1)
    y_min_1, y_max_1 = min(y1_1, y2_1), max(y1_1, y2_1)
    x1_2, y1_2 = rect2[0]
    x2_2, y2_2 = rect2[1]
    x_min_2, x_max_2 = min(x1_2, x2_2), max(x1_2, x2_2)
    y_min_2, y_max_2 = min(y1_2, y2_2), max(y1_2, y2_2)
    if x_max_2 < x_min_1 or x_max_1 < x_min_2:
        return False
    if y_max_2 < y_min_1 or y_max_1 < y_min_2:
        return False
    return True


# 遍历文件夹 背景 中的所有图片
count = 1
for idx, file_A in enumerate(os.listdir(folder_background)):
    if file_A.endswith(".jpg"):
    # 获取 背景 图片的路径和文件名（不包含扩展名）
        img_path = os.path.join(folder_background, file_A)

        # 在 txt 文件夹中创建同名的 txt 文件
        # filename = os.path.splitext(file_A)[0]
        # txt_path = os.path.join(folder_txt, filename + ".txt")
        txt_path = (os.path.join(folder_txt, myname + f'_{count}.txt'))

        # 加载 背景 图片
        img_source_bg = cv2.imread(img_path)
        img_bg = img_source_bg

        # 如果 背景 图片为空，则直接跳过该图片
        if img_bg is None:
            print("背景图为空")
            continue

        # 已有区域列表
        occupied_areas = []

        # 对于每张 背景 图片，都粘贴 5 张 C 文件夹中的随机图片
        for i in range(img_num):
            # 随机选择一张 target 文件夹中的图片
            file_T = random.choice(os.listdir(folder_target))
            while not file_T.endswith(".jpg"):
                file_T = random.choice(os.listdir(folder_target))
            img_path_T = os.path.join(folder_target, file_T)

            # 加载 用于粘贴上去的 图片
            img_T = cv2.imread(img_path_T)

            # 如果 粘贴 图片为空，则直接跳过该图片
            if img_T is None:
                continue

            #如果待粘贴图片比原图片大则跳过该图片
            if img_T.shape >= img_bg.shape:
                continue

            # 调整 粘贴 图片的大小为两到三倍，以适应 背景 图片的大小
            # scale = min(img_bg.shape[0] / img_T.shape[0], img_bg.shape[1] / img_T.shape[1])
            # img_resized_C = cv2.resize(img_T, (int(img_T.shape[1] * scale), int(img_T.shape[0] * scale)))
            T_height, T_width, _ = img_T.shape
            new_height, new_width = T_height*rate, T_width*rate
            img_TT = cv2.resize(img_T, (new_width, new_height))

            # 随机选择 粘贴 图片粘贴的位置
            h_c, w_c, _ = img_TT.shape
            h_a, w_a, _ = img_bg.shape
            x_c = random.randint(0, w_a - w_c)
            y_c = random.randint(0, h_a - h_c)

            #判断 粘贴 图片是否会与已有的粘贴图片重叠
            overlap = False
            for area in occupied_areas:
                x1, y1, x2, y2 = area
                rect1 = ((x1, y1), (x2, y2))
                rect2 = ((x_c, y_c), (x_c+w_c, y_c+h_c))
                overlap = is_intersected(rect1, rect2)
                if overlap:
                    print("发生重叠")
                    break
            if overlap:
                continue

            # 粘贴 目标 图片到 背景 图片上
            img_bg[y_c:y_c + h_c, x_c:x_c + w_c] = img_TT

            #这个则是类似融合，半透明化了
            #img_bg[y_c:y_c + h_c, x_c:x_c + w_c] = cv2.addWeighted(img_bg[y_c:y_c + h_c, x_c:x_c + w_c], 0.5, img_T, 0.5,0)

            # 记录新的已有区域
            occupied_areas.append([x_c, y_c, x_c+w_c, y_c+h_c])


            #计算要写入的信息
            t_x = (x_c+w_c/2)/w_a
            t_y = (y_c+h_c/2)/h_a
            t_w = w_c/w_a
            t_h = h_c/h_a

            # 将 目标 图片在 背景 图片上的相关写入 背景图片 的 txt 文件
            with open(txt_path, 'a') as f:
                f.write('{} {} {} {} {}\n'.format(classNum, t_x, t_y, t_w, t_h))
                #f.write(f"{i+1} {t_x:.6f} {t_y:.6f} {t_w:.6f} {t_h:.6f}\n")
            # 保存处理完的 A 图片
        #cv2.imwrite(os.path.join(folder_result, filename + ".jpg"), img_bg)
        cv2.imwrite(os.path.join(folder_result, myname + f'_{count}.jpg'), img_bg)
        print("已处理第{}张图片".format(count))
        count = count+1
