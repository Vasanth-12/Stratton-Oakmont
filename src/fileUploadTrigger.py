import numpy as np
import uvicorn
from PIL import Image, ImageOps
import os
import cv2

from insightface.app import FaceAnalysis
import insightface
from tqdm import tqdm
from utils import config_loader

from pymongo import MongoClient

def lambda_handler():
    print("Hurray")
    return "Success"