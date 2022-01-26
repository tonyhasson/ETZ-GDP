# DataFrames
import pandas as pd

# Network, Crawling and Scraping
import requests
import bs4
from bs4 import BeautifulSoup

# Visualization
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns

# General ## probably should delete time
import re
from re import sub
from typing import Pattern
from collections import Counter
import numpy as np
import os
import time
from subprocess import Popen
from tqdm import tqdm

# ML ## probably should delete LogisticRegression
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import linear_model, metrics, preprocessing
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import confusion_matrix, silhouette_score
from sklearn.metrics import r2_score, f1_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors
