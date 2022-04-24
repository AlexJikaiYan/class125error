from cv2 import imreadmulti
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from PIL import Image
import PIL.ImageOps
X,Y=fetch_openml("mnist_784",version=1 return_X_Y=True)
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=7)
X_train_scaied = X_train/250
X_test_scaied= X_test/250
clf= LogisticRegression(solver="saga",multi_class= "multinomin").fit(X_train_scaied,Y_train)
def get_prediction(image):
    im_PIL=Image.open(image)
    pixelfilter=20