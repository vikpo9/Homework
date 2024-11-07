import cv2 as cv
def equalize_img(src):
    dst = cv.equalizeHist(src)
    return dst