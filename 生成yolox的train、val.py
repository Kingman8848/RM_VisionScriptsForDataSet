import os
import random

random.seed(0)

# xmlfilepath = r'C:\myVOCdata\dataset\Annotations'  # xml文件存放地址,在训练自己数据集的时候，改成自己的数据路径
# saveBasePath = r'C:\myVOCdata\dataset'  # 存放test.txt，train.txt，trainval.txt，val.txt文件路径

xmlfilepath = r'G:\data_check\all2\yoloxWay\labels'  # xml文件存放地址,在训练自己数据集的时候，改成自己的数据路径
saveBasePath = r'G:\data_check\all2\yoloxWay'  # 存放test.txt，train.txt，trainval.txt，val.txt文件路径

# ----------------------------------------------------------------------#
#   根据自己的需求更改trainval_percent和train_percent的比例
# ----------------------------------------------------------------------#
trainval_percent = 0.8
train_percent = 1

if not os.path.exists(saveBasePath):
    os.mkdir(saveBasePath)

temp_xml = os.listdir(xmlfilepath)
total_xml = []
for xml in temp_xml:
    if xml.endswith(".txt"):
        total_xml.append(xml)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

print("train and val size", tv)
print("traub suze", tr)
ftrainval = open(os.path.join(saveBasePath, 'trainval.txt'), 'w')
ftest = open(os.path.join(saveBasePath, 'test.txt'), 'w')
ftrain = open(os.path.join(saveBasePath, 'train.txt'), 'w')
fval = open(os.path.join(saveBasePath, 'val.txt'), 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()

'''
|-- VOCdevkit
   |-- VOC2007
       |-- Annotations
           |-- ***.xml
       |-- ImageSets
           |-- Main
               |-- test.txt
               |-- train.txt
               |-- trainval.txt
               |-- val.txt
       |-- JPEGImages
           |-- ***.jpg
'''
