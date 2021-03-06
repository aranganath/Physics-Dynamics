import cv2
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc
from pdb import set_trace
import matplotlib.pyplot as plt
import torch
from torch import nn



def GenerateData():
	
	VideoData = []
	width = 64
	height = 64
	FPS = 10
	seconds = 10
	radius = 1
	paint_h = int(height/2)

	fourcc = VideoWriter_fourcc(*'MP42')
	video = VideoWriter('./data/circle_noise.avi', fourcc, float(FPS), (width, height))

	if not VideoData:
		for paint_x in range(-radius, width+radius, 6):
		    frame = np.zeros((height, width), dtype=np.uint8)

		    cv2.circle(frame, (paint_x, paint_h), radius, (255, 255, 255), -1)
		    
		    # Store the frames in the list

		    VideoData.append(frame)

		    video.write(cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR))

		video.release()
		VideoData = np.stack(VideoData, axis=0)

		Vc = cv2.VideoCapture('./data/circle_noise.avi')
		ret, frame = Vc.read()
	else:
		print("Data is already generated")


GenerateData()