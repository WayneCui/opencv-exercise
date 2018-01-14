import cv2

def load_and_display(img_path):
    img = cv2.imread(img_path)
    cv2.namedWindow('IMAGE1')
    cv2.imshow('IMAGE1', img)
    key = cv2.waitKey(0)
    cv2.destroyAllWindows()

def basic_blending(img_path_1, img_path_2):
    img1 = cv2.imread(img_path_1)
    img2 = cv2.imread(img_path_2)
    #cv2.namedWindow('img1')
    #cv2.imshow('img1', img2)

    #cv2.namedWindow('img2')
    #cv2.imshow('img2', img2)

    rows, cols, channels = img2.shape
    img_roi = img1[0: rows, 0: cols]

    cv2.addWeighted(img_roi, 0.6, img2, 0.4, 0, img_roi)
    cv2.imshow('blending', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return img1

def img_write(output_path, img):
    cv2.imwrite(output_path, img)
    cv2.waitKey()

if __name__ == '__main__':
    #load_and_display('../img/new_year.jpeg')
    blended_img = basic_blending('../img/new_year.jpeg', '../img/doge.jpg')
    img_write('../img/blended.jpeg', blended_img)
