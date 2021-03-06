import cv2
import numpy as np

def find_split_index(arr, h, w, thresh=5):
    dem = 0
    arr_ = arr
    # print(w, h)
    if w/h < 0.3:
        # print("1dong")
        return -1
    for i in range(0, len(arr)-1, 1):
        if arr[i] == 0:
            dem = i
        else:
            break
    arr = arr[dem+1:]
    dem = len(arr)-1
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] == 0:
            dem = i
        else:
            break
    arr = arr[:dem-1]
    if len(arr)==0 or np.min(arr) != 0:
        # print("1dong")
        return -1
    min_index = np.argmin(arr)
    max_index = len(arr)-1 - np.argmin(np.array(list(reversed(arr))))

    if (min_index == 0 and max_index == 0) or (min_index == len(arr)-1 and max_index == len(arr-1)):
        if w/h > 0.45:
            return len(arr_)//2
        # print("1dong", arr)
        return -1
    # print(max_index, min_index, len(arr)-1)
    return ((max_index+min_index)//2)


def plate_line_recognition(img):
    h, w = img.shape[:2]
    ori_img = img.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    temp = 255 - img
    split_index = -1
    for i in range(2):
        img = img[h//5:4*h//5, w//5: 4*w//5]
        img =  cv2.equalizeHist(img)
        ret,thresh = cv2.threshold(img,75,150,cv2.THRESH_BINARY)
        indexs = np.count_nonzero(thresh==0, axis=1)
        # mean = np.mean(indexs)
        split_index = find_split_index(indexs, w, h)
        if split_index != -1:
            return split_index, ori_img[:h//5 + split_index, :], ori_img[h//5 + split_index:, :]
        img = temp
    return -1, ori_img, None
