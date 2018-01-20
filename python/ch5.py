import cv2
import numpy as np

def MultiChannelBlending(channel_index):
    srcImg1 = cv2.imread('../img/new_year.jpeg')
    srcImg2 = cv2.imread('../img/doge.jpg', 0)  #GRAYSCALE

    channels = cv2.split(srcImg1) #b,g,r
    channel = channels[channel_index]

    rows, cols = srcImg2.shape
    roi = srcImg1[100 : rows + 100, 0 : cols, channel_index]

    cv2.addWeighted(channel[100 : rows + 100, 0 : cols], 0.5, 
        srcImg2, 1.5, 
        0.0, 
        channel[100 : rows + 100, 0 : cols])

    srcImg1 = cv2.merge(channels)

    cv2.namedWindow('')
    cv2.imshow('', srcImg1)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    MultiChannelBlending(0)
    MultiChannelBlending(1)
    MultiChannelBlending(2)
