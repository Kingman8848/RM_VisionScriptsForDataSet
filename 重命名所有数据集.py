import os
txt_folder = r"E:\\RM_datas\\QX_v5_add\\train\\labels"
jpg_folder = r"E:\\RM_datas\\QX_v5_add\\train\\images"
new_txt_folder = r"E:\\RM_datas\\QX_v5_add\\train\\labels1"

class ImageRename():
    def __init__(self):
        self.path = jpg_folder

    def rename(self):
        txt_file = open('E:\\RM_datas\\QX_v5_add\\train\\labels','r')  # 原始labels.txt的地址
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        piclist = []
        for parent, dirnames, filenames in os.walk(self.path):
            for pic_name in filenames:
                pic_name = pic_name[:-4]

                piclist.append(pic_name)
        pic_set = set(piclist)
        i = 0
        for eachline in txt_file:
            data = eachline.strip().split(',')
            filename = data[0]
            filename = filename[:-4]

            for each_pic in pic_set:
                if each_pic == filename:
                    for item in filelist:
                        item_name = item[:-4]

                        if item_name == filename:
                            if item.endswith('.JPG'):
                                src = os.path.join(os.path.abspath(self.path), item)
                                dst = os.path.join(os.path.abspath(self.path),
                                                   '0000' + format(str(i), '0>3s') + '.jpeg')
                                os.rename(src, dst)
                                #                                print('converting %s to %s ...' % (src, dst))
                                txt_path = r'C:\NewData\test\new\train_f.txt'  # 生成的txt标注文件地址
                                txt = open(txt_path, 'a')
                                new_line = '0000' + format(str(i), '0>3s') + '.JPG' + ' ' + data[1]
                                txt.writelines(new_line)
                                txt.write('\n')
                                txt.close()
                                i = i + 1

                            elif item.endswith('.jpg'):
                                src = os.path.join(os.path.abspath(self.path), item)
                                dst = os.path.join(os.path.abspath(self.path), '0000' + format(str(i), '0>3s') + '.jpg')
                                os.rename(src, dst)
                                #                                print('converting %s to %s ...' % (src, dst))
                                txt_path = r'C:\NewData\test\new\train_f.txt'   # 生成的txt标注文件地址
                                txt = open(txt_path, 'a')
                                new_line = '0000' + format(str(i), '0>3s') + '.jpg' + ' ' + data[1]
                                txt.writelines(new_line)
                                txt.write('\n')
                                txt.close()
                                i = i + 1

        txt_file.close()
        print('total %d to rename & converted %d jpgs' % (total_num, i))


if __name__ == '__main__':
    newname = ImageRename()
    newname.rename()
