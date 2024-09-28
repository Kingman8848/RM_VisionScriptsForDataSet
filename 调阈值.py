import cv2

# 创建窗口和滑动条
cv2.namedWindow("Image")
cv2.createTrackbar("H_min", "Image", 0, 180, lambda x: None)
cv2.createTrackbar("H_max", "Image", 0, 180, lambda x: None)
cv2.createTrackbar("S_min", "Image", 0, 255, lambda x: None)
cv2.createTrackbar("S_max", "Image", 0, 255, lambda x: None)
cv2.createTrackbar("V_min", "Image", 0, 255, lambda x: None)
cv2.createTrackbar("V_max", "Image", 0, 255, lambda x: None)

# 读取图片并转为HSV格式
img = cv2.imread(r"E:\\fire053.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:
    # 读取滑动条的值
    h_min = cv2.getTrackbarPos("H_min", "Image")
    h_max = cv2.getTrackbarPos("H_max", "Image")
    s_min = cv2.getTrackbarPos("S_min", "Image")
    s_max = cv2.getTrackbarPos("S_max", "Image")
    v_min = cv2.getTrackbarPos("V_min", "Image")
    v_max = cv2.getTrackbarPos("V_max", "Image")

    # 应用阈值
    lower = (h_min, s_min, v_min)
    upper = (h_max, s_max, v_max)
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    # 显示图片和结果
    cv2.imshow("Image", img)
    cv2.imshow("Result", result)

    # 按下Esc键退出
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
