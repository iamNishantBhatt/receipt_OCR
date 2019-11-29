from PIL import Image
import pytesseract
from receipt_OCR.settings import BASE_DIR
import cv2
import os
import re


def img_preprocessing(imgpath):
    imagepath = os.path.join(BASE_DIR, imgpath.strip("/"))
    image = cv2.imread(filename=imagepath)
    image = cv2.resize(image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    image = cv2.cvtColor(cv2.UMat(image), cv2.COLOR_BGR2GRAY)
    return img_temp_saving(image)


def img_temp_saving(img):
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, img)
    return img_ocr(filename)


def img_ocr(file):
    monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthDict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    text = pytesseract.image_to_string(Image.open(file))
    os.remove(file)
    try:
        regtext = re.search(r'[Date:]*([0-9]{0,2}[\/-]([0-9]{0,2}|[a-z]{3}|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[\/-][0-9]{0,4})', text).group(1)

    except:
        try:
            regtext = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)([,]|[\s])([0-9]{0,2})([,]|[\s])([\s][0-9]{0,4})',text).group(1)

        except:
            regtext = "null"
    return regtext
