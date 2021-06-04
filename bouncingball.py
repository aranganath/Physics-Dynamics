import cv2
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc
from pdb import set_trace
import matplotlib.pyplot as plt
import torch
from torch import nn


class RNNgenerator(nn.Module):
	"""docstring for RNNgenerator"""
	def __init__(self, height, FPS, seconds, radius):
		super(RNNgenerator, self).__init__()
		self.arg = arg
		self.VideoData = []
		self.width = 1280
		self.height = 720
		self.FPS = 24
		self.seconds = 10
		self.radius = 150
		self.paint_h = int(height/2)


	def GenerateData(self):
		

		fourcc = VideoWriter_fourcc(*'MP42')
		video = VideoWriter('./data/circle_noise.avi', fourcc, float(FPS), (width, height))

		if not self.VideoData:
			for paint_x in range(-radius, width+radius, 6):
			    frame = 255*np.ones( 
			                   (height, width, 3), 
			                              dtype=np.uint8)
			    
			    cv2.circle(frame, (paint_x, paint_h), radius, (0, 0, 0), -1)
			    
			    # Store the frames in the list

			    self.VideoData.append(frame)

			    video.write(frame)

			video.release()
			self.VideoData = np.stack(self.VideoData, axis=0)

			Vc = cv2.VideoCapture('./data/circle_noise.avi')
			ret, frame = Vc.read()
		else:
			print("Data is already generated")



while ret:
	set_trace()
	ret, frame = Vc.read()

	plt.figure()
	plt.imshow(frame)