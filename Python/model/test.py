import datetime
import json
import cv2
import mediapipe as mp
import pandas as pd
import socketio

# df_temp = pd.read_csv('../Data/TempData2.csv').drop('Unnamed: 0', axis=1)
df_temp = pd.read_csv('../Data/TempData2.csv').drop('Unnamed: 0', axis=1)
print(df_temp)