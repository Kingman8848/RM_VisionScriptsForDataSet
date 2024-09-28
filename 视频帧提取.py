import cv2
import os

#不能存在中文路径
input_path= r'E:\\num_datasets\\9000_red.avi'
save_path = r'E:\\num_datasets\\images5'

#如果路径不存在则创建路径
if not os.path.exists(save_path):
    os.makedirs(save_path)

# 打开视频文件
video = cv2.VideoCapture(input_path)
# 每10帧提取一帧作为jpg图片保存
count = 0
MISSING = 5 #每间隔多少帧提取一张
while True:
    ret, frame = video.read()
    if not ret:
        break
    count += 1
    if count %MISSING== 0:
        cv2.imwrite(os.path.join(save_path, f'base_{0+count//MISSING}.jpg'), frame)#保存时以数字序列命名
# 释放资源
video.release()
cv2.destroyAllWindows()

'''说明：
1. 首先用`cv2.VideoCapture()`打开视频文件，获取一个视频对象`video`；
2. 然后使用`video.read()`读取视频的每一帧，返回一个布尔值`ret`和一帧图像`frame`；
3. 如果`ret`为`True`，说明读取成功，继续执行；
4. 如果`count`模5余0，说明取到了10的倍数帧，就使用`cv2.imwrite()`将该帧图像保存为jpg文件，文件名为`frame_数字.jpg`；
5. 最后用`video.release()`释放视频资源，用`cv2.destroyAllWindows()`关闭所有窗口。
注意：以上代码只适用于opencv版本为3.x及以上，如果使用opencv2.x版本，请将`cv2.destroyAllWindows()`改为`cv2.cv.DestroyAllWindows()`。
'''

