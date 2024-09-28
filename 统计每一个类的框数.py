import os
import re
def count_labels(label_file, label_count):
    with open(label_file, 'r') as f:
        for line in f:
            match = re.match(r'^([a-zA-Z0-9_-]+)\s', line)
            if match is not None:
                cls = match.group(1)
                if cls not in label_count:
                    label_count[cls] = 0
                label_count[cls] += 1
def count_labels_in_folder(folder_path, output_file):
    label_count = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            count_labels(file_path, label_count)
    with open(output_file, 'w') as f:
        for cls, count in label_count.items():
            f.write(f"{cls}: {count}\n")
        print(f"统计结果已保存到文件 {output_file} 中")
if __name__ == '__main__':
    folder_path = r'E:\dataUPdate\直播截图数据集\labels' #输入标签文件夹路径：
    output_file = r'E:\dataUPdate\直播截图数据集\test.txt' #统计结果保存的文件路径
    count_labels_in_folder(folder_path, output_file)

    #
    #     # = r'C:\NewData\yolov8data\test\labels' #输入标签文件夹路径：
    #     # output_file1 = r'C:\NewData\yolov8data\test统计.txt' #统计结果保存的文件路径
    # folder_path2 = r'C:\NewData\yolov8data\val\labels' #输入标签文件夹路径：
    # output_file2 = r'C:\NewData\yolov8data\val统计.txt' #统计结果保存的文件路径
    # count_labels_in_folder(folder_path1, output_file1)
    # count_labels_in_folder(folder_path2, output_file2)
