## Import libraries - source : https://docs.python.org/3.4/library/index.html
import pickle
import random
from datetime import datetime

import numpy as np
from numpy import newaxis

import os, sys
import PIL
from PIL import Image

import time

import cv2
import csv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
from matplotlib import gridspec

import prettyplotlib as ppl
import brewer2mpl

import glob

import tensorflow as tf
from tensorflow.contrib.tensorboard.plugins import projector
from tensorflow.contrib.layers import flatten
import urllib
import urllib.request

from sklearn.utils import shuffle