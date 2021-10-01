import cv2

def compress(img):
    _height = int((img.shape[0])/5)
    _width = int((img.shape[1])/5)
    img = cv2.resize(img, (_width, _height), interpolation=cv2.INTER_AREA)
    return img