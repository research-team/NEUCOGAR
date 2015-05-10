import root
import os
import numpy as np
from pybrain.datasets import SupervisedDataSet
__author__ = 'kamil'
import cv2

def get_number_of_files(path):
    count = 0
    for file in os.listdir(path):
        type = file.split(".")[1]
        if type == "DS_Store":
            continue
        count += 1
    return count

def get_cat_dog_trainset():
    count = 0
    images = os.listdir(root.path() + '/res/cats_proc/')
    shape = cv2.imread(root.path() + '/res/cats_proc/'+images[0],0).shape
    ds = SupervisedDataSet(shape[0]*shape[1], 2)
    for image in os.listdir(root.path() + '/res/cats_proc/'):
        img = cv2.imread(root.path() + '/res/cats_proc/'+image,0)
        inp = np.reshape(img, shape[0]*shape[1])
        target = [1,0]
        ds.addSample(inp, target)
        count += 1
    for image in os.listdir(root.path() + '/res/dogs_proc/'):
        img = cv2.imread(root.path() + '/res/dogs_proc/'+image,0)
        img = cv2.resize(img, img.shape, fx=0.5, fy=0.5)
        inp = np.reshape(img, shape[0]*shape[1])
        target = [0,1]
        ds.addSample(inp, target)
        count += 1
    return ds

def get_cat_dog_testset():
    count = 0
    images = os.listdir(root.path() + '/res/cats_proc/')
    shape = cv2.imread(root.path() + '/res/cats_proc/'+images[0],0).shape
    ds = SupervisedDataSet(shape[0]*shape[1], 2)
    for image in os.listdir(root.path() + '/res/cats_proc/'):
        img = cv2.imread(root.path() + '/res/cats_proc/'+image,0)
        inp = np.reshape(img, shape[0]*shape[1])
        target = [1,0]
        ds.addSample(inp, target)
        count += 1
    for image in os.listdir(root.path() + '/res/dogs_proc/'):
        img = cv2.imread(root.path() + '/res/dogs_proc/'+image,0)
        img = cv2.resize(img, img.shape, fx=0.5, fy=0.5)
        inp = np.reshape(img, shape[0]*shape[1])
        target = [0,1]
        ds.addSample(inp, target)
        count += 1
    return ds

# img = cv2.resize(img,(280, 280), interpolation = cv2.INTER_CUBIC)
# cv2.imwrite(root.path()+"/images/proc.jpg", img)
