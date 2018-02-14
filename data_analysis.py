# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 09:20:19 2018

@author: Administrator
"""

#!/bin/python

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
#import math


encode_data = np.genfromtxt('encode_data.txt', delimiter=',', skip_header=0,
	skip_footer=0, names=['encode', 'time'])

imu_data = np.genfromtxt('imu_data.txt', delimiter=',', skip_header=0,
	skip_footer=0, names=['ax', 'ay','az','wx','wy','wz','roll','pitch','yaw','hx','hz','hy','time'])


fig = plt.figure()


ax1 = fig.add_subplot(511)
ax1.set_xlabel('time (ms)')
ax1.set_ylabel('all')
# ax2.set_ylim([-0.0025,0.0025])
ax1.plot(imu_data['time'], imu_data['ax'], color='g', label='ax')
ax1.plot(imu_data['time'], imu_data['ay'], color='b', label='ay')
ax1.plot(imu_data['time'], imu_data['az'], color='r', label='az')

ax2 = fig.add_subplot(512)
ax2.set_xlabel('time (ms)')
ax2.set_ylabel('Pitch estimated (deg)')
# ax2.set_ylim([-0.0025,0.0025])
ax2.plot(encode_data['time'], encode_data['encode'], color='g', label='encode')

ax3 = fig.add_subplot(513)
ax3.set_xlabel('time (ms)')
ax3.set_ylabel('all')
# ax2.set_ylim([-0.0025,0.0025])
ax3.plot(imu_data['time'], imu_data['wx'], color='g', label='wx')
ax3.plot(imu_data['time'], imu_data['wy'], color='b', label='wy')
ax3.plot(imu_data['time'], imu_data['wz'], color='r', label='wz')

ax4 = fig.add_subplot(514)
ax4.set_xlabel('time (ms)')
ax4.set_ylabel('all')
# ax2.set_ylim([-0.0025,0.0025])
ax4.plot(imu_data['time'], imu_data['hx'], color='g', label='hx')
ax4.plot(imu_data['time'], imu_data['hy'], color='b', label='hy')
ax4.plot(imu_data['time'], imu_data['hz'], color='r', label='hz')

ax5 = fig.add_subplot(515)
ax5.set_xlabel('time (ms)')
ax5.set_ylabel('all')
# ax2.set_ylim([-0.0025,0.0025])
ax5.plot(imu_data['time'], imu_data['roll'], color='g', label='roll')
ax5.plot(imu_data['time'], imu_data['pitch'], color='b', label='pitch')
ax5.plot(imu_data['time'], imu_data['yaw'], color='r', label='yaw')


handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels, loc=2)
handles, labels = ax2.get_legend_handles_labels()
ax2.legend(handles, labels, loc=2)
handles, labels = ax3.get_legend_handles_labels()
ax3.legend(handles, labels, loc=2)
handles, labels = ax4.get_legend_handles_labels()
ax4.legend(handles, labels, loc=2)
handles, labels = ax5.get_legend_handles_labels()
ax5.legend(handles, labels, loc=2)

plt.show()