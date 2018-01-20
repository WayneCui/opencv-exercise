
import cv2
import numpy as np

def ROI_LinearBlending():
    srcImg1 = cv2.imread('../img/interstellar-accretion-disk.jpg')
    srcImg2 = cv2.imread('../img/plane.jpg')

    rows, cols, _ = srcImg2.shape
    img_roi = srcImg1[0 : rows, 100 : cols + 100]
    cv2.addWeighted(img_roi, 0.7, srcImg2, 0.3, 0., img_roi)

    cv2.namedWindow('', 1)
    cv2.imshow('', srcImg1)
    cv2.waitKey()
    cv2.destroyAllWindows()

def ROI_AddImage():
    """
    https://www.learnopencv.com/seamless-cloning-using-opencv-python-cpp/
    """
    # background = cv2.imread('../img/1024px-Big_Tree_with_Red_Sky_in_the_Winter_Night.jpg')
    background = cv2.imread('../img/interstellar-accretion-disk.jpg')
    doge = cv2.imread('../img/plane.jpg')

    mask = 255 * np.ones(doge.shape, doge.dtype)
    width, height, _ = background.shape
    # print(round(height / 2), round(width / 2))
    center = (700, 150) #height, width
    output = cv2.seamlessClone(doge, background, mask, center, cv2.MIXED_CLONE)
    
    cv2.namedWindow('seamlessClone')
    cv2.imshow('seamlessClone', output)
    cv2.waitKey()
    cv2.destroyAllWindows()


def LinearBlending():
    alpha = 0.5
    beta = 1 - alpha

    srcImg1 = cv2.imread('../img/new_year.jpeg')
    srcImg2 = cv2.imread('../img/rain.jpg')
    dstImg = 255 * np.ones(srcImg2.shape, srcImg2.dtype)

    cv2.addWeighted(srcImg1, alpha, srcImg2, beta, 0.0, dstImg)
    
    cv2.namedWindow('LinearBlending', 1)
    cv2.imshow('LinearBlending', dstImg)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # ROI_AddImage()
    # LinearBlending()
    ROI_LinearBlending()