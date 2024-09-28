from lxml import etree
from PIL import Image
import sys
import csv
import os

#请在终端先运行这个指令
#pip3 install lxml -i https://pypi.tuna.tsinghua.edu.cn/simple

#注意事项
# If your OS is Mac, there's a case when '.DS_Store' file is  automatically created.
# In that case, you have to remove '.DS_Store' file through the terminal.
# Ref : http://leechoong.com/posts/2018/ds_store/

'''--------------------------------------------------------------------------------------------'''
#这里填入txt文件对应的jpg文件夹的路径
IMG_PATH = r'E:\RM_datas\QX_model_v3\train\images'
if not os.path.exists(IMG_PATH):
    print("标签对应的jpg文件路径找不到，请检查是否填写正确")
    sys.exit(1)#直接终止程序并抛出异常
#这里填入txt文件夹路径
txt_folder = r'E:\RM_datas\QX_model_v3\train\labels'
if not os.path.exists(txt_folder):
    print("待转换的txt标签文件路径找不到，请检查是否填写正确")
    sys.exit(1)#直接终止程序并抛出异常
#xml文件的保存路径
save_path = r'E:\RM_datas\VOC2007\Annotations'
if not os.path.exists(save_path):
    os.makedirs(save_path)
    print("你所填写的转换后的xml文件保存路径找不到，已根据你目前填写的自动创建")
#填写原来的txt文件对应的标签名
# labels = ['red1', 'red2', 'red3', 'red4', 'red5',
#           'red_sentry', 'blue1', 'blue2', 'blue3', 'blue4', 'blue5', 'blue_sentry']
labels = ["red", "blue"]
'''--------------------------------------------------------------------------------------------'''

global label
label = ''

fw = os.listdir(IMG_PATH)

def csvread(fn):
    with open(fn, 'r') as csvfile:
        list_arr = []
        reader = csv.reader(csvfile, delimiter=' ')

        for row in reader:
            list_arr.append(row)
    return list_arr


def convert_label(txt_file):
    global label
    for i in range(len(labels)):
        if txt_file == str(i):
            label = labels[i]
            return label

    return label

# core code = convert the yolo txt file to the x_min,x_max...


def extract_coor(txt_file, img_width, img_height):
    x_rect_mid = float(txt_file[1])
    y_rect_mid = float(txt_file[2])
    width_rect = float(txt_file[3])
    height_rect = float(txt_file[4])

    x_min_rect = ((2 * x_rect_mid * img_width) - (width_rect * img_width)) / 2
    x_max_rect = ((2 * x_rect_mid * img_width) + (width_rect * img_width)) / 2
    y_min_rect = ((2 * y_rect_mid * img_height) -
                  (height_rect * img_height)) / 2
    y_max_rect = ((2 * y_rect_mid * img_height) +
                  (height_rect * img_height)) / 2

    return x_min_rect, x_max_rect, y_min_rect, y_max_rect


for line in fw:
    root = etree.Element("annotation")

    # try debug to check your path
    img_style = IMG_PATH.split('/')[-1]
    img_name = line
    image_info = IMG_PATH + "/" + line
    img_txt_root = txt_folder + "/" + line[:-4]
    # print(img_txt_root)
    txt = ".txt"

    txt_path = img_txt_root + txt
    # print(txt_path)
    txt_file = csvread(txt_path)
    ######################################

    # read the image  information
    img_size = Image.open(image_info).size

    img_width = img_size[0]
    img_height = img_size[1]
    img_depth = Image.open(image_info).layers
    ######################################

    folder = etree.Element("folder")
    folder.text = "%s" % (img_style)

    filename = etree.Element("filename")
    filename.text = "%s" % (img_name)

    path = etree.Element("path")
    path.text = "%s" % (IMG_PATH)

    source = etree.Element("source")
    ##################source - element##################
    source_database = etree.SubElement(source, "database")
    source_database.text = "Unknown"
    ####################################################

    size = etree.Element("size")
    ####################size - element##################
    image_width = etree.SubElement(size, "width")
    image_width.text = "%d" % (img_width)

    image_height = etree.SubElement(size, "height")
    image_height.text = "%d" % (img_height)

    image_depth = etree.SubElement(size, "depth")
    image_depth.text = "%d" % (img_depth)
    ####################################################

    segmented = etree.Element("segmented")
    segmented.text = "0"

    root.append(folder)
    root.append(filename)
    root.append(path)
    root.append(source)
    root.append(size)
    root.append(segmented)
    print("正在执行转换...")

    for ii in range(len(txt_file)):
        label = convert_label(txt_file[ii][0])
        x_min_rect, x_max_rect, y_min_rect, y_max_rect = extract_coor(
            txt_file[ii], img_width, img_height)

        object = etree.Element("object")
        ####################object - element##################
        name = etree.SubElement(object, "name")
        name.text = "%s" % (label)

        pose = etree.SubElement(object, "pose")
        pose.text = "Unspecified"

        truncated = etree.SubElement(object, "truncated")
        truncated.text = "0"

        difficult = etree.SubElement(object, "difficult")
        difficult.text = "0"

        bndbox = etree.SubElement(object, "bndbox")
        #####sub_sub########
        xmin = etree.SubElement(bndbox, "xmin")
        xmin.text = "%d" % (x_min_rect)
        ymin = etree.SubElement(bndbox, "ymin")
        ymin.text = "%d" % (y_min_rect)
        xmax = etree.SubElement(bndbox, "xmax")
        xmax.text = "%d" % (x_max_rect)
        ymax = etree.SubElement(bndbox, "ymax")
        ymax.text = "%d" % (y_max_rect)
        #####sub_sub########

        root.append(object)
        ####################################################

    file_output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
    # print(file_output.decode('utf-8'))
    ff = open('%s.xml' % (img_name[:-4]), 'w', encoding="utf-8")
    ff.write(file_output.decode('utf-8'))
