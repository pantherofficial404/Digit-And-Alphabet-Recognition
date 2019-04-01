from io import BytesIO
import re
import base64
from PIL import Image
import numpy as np
import cv2

def imageProcess(image):
    image = re.sub("^data:image/png;base64,", "", image)
    image = base64.b64decode(image)
    image = BytesIO(image)
    image = Image.open(image)
    image = np.asarray(image)
    image = cv2.resize(image,(28,28))
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image = image.reshape(1,28,28,1)
    return image