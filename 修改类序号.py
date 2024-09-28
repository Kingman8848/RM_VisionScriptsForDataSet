import os

# 设置txt文件夹的路径
txt_dir = r'E:\\dataUPdate\\Red_station\\labels'

# 定义替换函数
def replace_num(line):
    num_list = line.split()  # 将一行字符串按空格分隔成列表
    if num_list[0] == '12':
        num_list[0] = '0'
    # elif num_list[0] == '1':
    #     num_list[0] = '0'
    # elif num_list[0] == '2':
    #     num_list[0] = '0'
    # elif num_list[0] == '3':
    #     num_list[0] = '0'
    # elif num_list[0] == '4':
    #     num_list[0] = '0'
    # elif num_list[0] == '11':
    #     num_list[0] = '1'
    # elif num_list[0] == '6':
    #     num_list[0] = '0'
    # elif num_list[0] == '7':
    #     num_list[0] = '0'
    # elif num_list[0] == '8':
    #     num_list[0] = '1'
    # elif num_list[0] == '9':
    #     num_list[0] = '1'
    # elif num_list[0] == '10':
    #     num_list[0] = '1'
    # elif num_list[0] == '11':
    #     num_list[0] = '1'
    # elif num_list[0] == '12':
    #     num_list[0] = '1'
    # elif num_list[0] == '13':
    #     num_list[0] = '1'
    # elif num_list[0] == '14':
    #     num_list[0] = '1'
    # elif num_list[0] == '15':
    #     num_list[0] = '1'
    # if num_list[0]=='6':
    #     num_list[0]='0'
    # elif num_list[0]=='5':
    #     num_list[0]='0'
    # elif num_list[0]=='2':
    #     num_list[0]='0'
    # elif num_list[0]=='3':
    #     num_list[0]='0'
    # elif num_list[0]=='4':
    #     num_list[0]='0'
    # elif num_list[0]=='1':
    #     num_list[0]='0'
    return ' '.join(num_list)+'\n'   # 将列表转换为字符串，加上换行符


# 遍历文件夹内的所有txt文件
i = 1
for filename in os.listdir(txt_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(txt_dir, filename), 'r') as f:
            lines = f.readlines()  # 读取每一行
        with open(os.path.join(txt_dir, filename), 'w') as f:
            for line in lines:
                f.write(replace_num(line))  # 写入修改后的内容
        print("已完成第{}个标签 {} 的处理".format(i, filename))  # 输出循环次数和处理的文件名
        i += 1
'''   
原VOC的类别顺序转我定义的V8顺序（红1-5，红哨兵，蓝1-5，蓝哨兵）用的
    if num_list[0] == '11':
        num_list[0] = '1'
    elif num_list[0] == '10':
        num_list[0] = '1'
    elif num_list[0] == '8':
        num_list[0] = '1'
    elif num_list[0] == '6':
        num_list[0] = '1'
    elif num_list[0] == '3':
        num_list[0] = '1'
    elif num_list[0] == '2':
        num_list[0] = '1'
    elif num_list[0] == '7':
        num_list[0] = '1'
    elif num_list[0] == '5':
        num_list[0] = '1'
    elif num_list[0] == '0':
        num_list[0] = '1'
    elif num_list[0] == '1':
        num_list[0] = '1'
    elif num_list[0] == '9':
        num_list[0] = '1'
    elif num_list[0] == '4':
        num_list[0] = '1'
'''

'''
原来那个杂乱的VOC顺序的
    if num_list[0] == '0':
        num_list[0] = '1'
    elif num_list[0] == '12':
        num_list[0] = '1'
    elif num_list[0] == '2':
        num_list[0] = '1'
    elif num_list[0] == '3':
        num_list[0] = '1'
    elif num_list[0] == '4':
        num_list[0] = '1'
    elif num_list[0] == '5':
        num_list[0] = '1'
    elif num_list[0] == '6':
        num_list[0] = '1'
    elif num_list[0] == '7':
        num_list[0] = '1'
    elif num_list[0] == '8':
        num_list[0] = '1'
    elif num_list[0] == '9':
        num_list[0] = '1'
    elif num_list[0] == '10':
        num_list[0] = '1'
    elif num_list[0] == '11':
        num_list[0] = '1'

'''
