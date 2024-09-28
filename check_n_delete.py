import os

'''此代码用于检查数据集删除不匹配的标签和图片，但目前没有删除空txt功能'''

jpg_folder = r"E:\dataUPdate\outpost\images"
txt_folder = r"E:\dataUPdate\outpost\labels"

choice = 1  # 设置为1则是删除多余jpg文件
            # 设置为2则是删除多余txt文件

if choice == 1:
    print('当前执行模式为删除多余的jpg文件')
    for jpg_file in os.listdir(jpg_folder):
        if not jpg_file.endswith(".jpg"):
            continue
        txt_file = os.path.join(txt_folder, jpg_file[:-4] + ".txt")
        if not os.path.isfile(txt_file):
            os.remove(os.path.join(jpg_folder, jpg_file))
elif choice == 2:
    print('当前执行模式为删除多余的txt文件')
    for txt_file in os.listdir(txt_folder):
        if not txt_file.endswith(".txt"):
            continue
        jpg_file = os.path.join(jpg_folder, txt_file[:-4] + ".jpg")
        if not os.path.isfile(jpg_file):
            os.remove(os.path.join(txt_folder, txt_file))

'''
其中，`txt_folder`和`jpg_folder`需要替换为实际的文件夹路径。我们使用`os.listdir`函数遍历`jpg_folder`文件夹中的所有文件，
对于每一个以".txt"结尾的文件，我们找到其对应的同名jpg/txt文件，如果该jpg文件不存在，则删除该jpg文件。
'''
