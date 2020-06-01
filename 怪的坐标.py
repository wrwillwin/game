# author=wrwillwin
author = 'Yanxiang'

version = '1.0'

date = '10/06/2019'

import cv2

import numpy as np

import time


def detective(img_path, flag):
    kernel_4 = np.ones((4, 4), np.uint8)  # 4x4的卷积核

    def separate_color_yellow(hsv):
        # 怪物颜色提取
        lower_hsv = np.array([0, 0, 255])  # 提取颜色的低值..
        high_hsv = np.array([0, 0, 255])  # 提取颜色的高值
        mask = cv2.inRange(hsv, lowerb=lower_hsv, upperb=high_hsv)
        print("怪物坐标提取完成")
        return mask

    def separate_color_door(hsv):
        # 门颜色提取
        lower_hsv = np.array([120, 255, 255])  # 提取颜色的低值
        high_hsv = np.array([120, 255, 255])  # 提取颜色的高值
        mask = cv2.inRange(hsv, lowerb=lower_hsv, upperb=high_hsv)
        print("门的坐标提取完成")
        return mask

    def erocode_dilate(mask):
        erosion = cv2.erode(mask, kernel_4, iterations=1)
        erosion = cv2.erode(erosion, kernel_4, iterations=1)
        dilation = cv2.dilate(erosion, kernel_4, iterations=1)
        dilation = cv2.dilate(dilation, kernel_4, iterations=1)
        return dilation

    # flag = 0  表示找到怪物的平均坐标
    # flag = 1  表示找到人物坐标
    def contours(dilation, flag):
        # target是把原图中的非目标颜色区域去掉剩下的图像
        target = cv2.bitwise_and(Img, Img, mask=dilation)
        # 将滤波后的图像变成二值图像放在binary中
        ret, binary = cv2.threshold(dilation, 127, 255, cv2.THRESH_BINARY)
        # 在binary中发现轮廓，轮廓按照面积从小到大排列
        img_contours, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        p = 0
        inumber = 1
        # 新建数组存放所有怪物 X,Y坐标的中心值
        monster_x = []
        monster_Y = []
        # pos_x =0
        # pos_y =0
        if (len(contours) != 0):
            for i in contours:  # 遍历所有的轮廓
                x, y, w, h = cv2.boundingRect(i)  # 将轮廓分解为识别对象的左上角坐标和宽、高
                if w * h > 100:
                    if flag == 0:
                        p += 1
                        print('第 %d 个怪物的底中的位置为' % (p), x + w / 2, y + h)
                        monster_x.append(x + w / 2)
                        monster_Y.append(y + h)
                        return monster_x, monster_Y
                    if flag == 2:
                        p += 1
                        print('第 %d 个的中心像素位置为' % (p), x + w / 2, y + h / 2)
                        pos_xx = x
                        pos_yy = y
                        return pos_xx, pos_yy
        else:
            if flag == 0:
                return monster_x, monster_Y
            if flag == 2:
                return 0, 0

    Img = cv2.imread(img_path)  # 读入一幅图像
    if Img is not None:  # 判断图片是否读入
        HSV = cv2.cvtColor(Img, cv2.COLOR_BGR2HSV)  # 把BGR图像转换为HSV格式
        # 提取颜色
        if flag == 0:
            mask_yellow = separate_color_yellow(HSV)
            dilation_yellow = erocode_dilate(mask_yellow)
            pos_x, pos_y = contours(dilation_yellow, flag)
            return pos_x, pos_y

        elif flag == 2:
            mask_door = separate_color_door(HSV)
            dilation_red = erocode_dilate(mask_door)
            pos_x, pos_y = contours(dilation_red, flag)
            return pos_x, pos_y
