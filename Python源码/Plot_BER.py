# -*- coding:utf-8 -*- 
"""
Author：G3
Time: 2022/5/15 
Software: PyCharm
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def to_percent(temp, position):
    return '%1.3f' % temp + '%'


def cal_sim():
    xpoints = np.array(range(0, 3))
    xpoints = ['txt', 'picture', 'video']
    bpsk_ypoints_sim = [0, 0.0312, 0.0017]
    qpsk_ypoints_sim = [0.0001, 0.0332, 0.0027]

    l = plt.plot(xpoints, bpsk_ypoints_sim, 'o-', xpoints, qpsk_ypoints_sim, 'o-')
    plt.legend(handles=l, labels=['BPSK Simulation', 'QPSK Simulation'], loc='upper right')
    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
    plt.title("BER analysis")
    plt.xlabel("Type")
    plt.ylabel("BER")
    plt.grid()

    plt.show()


def cal_measured():
    xpoints = ['1cm', '15cm', '30cm']

    text_bpsk_ypoints = [0.011494, 0.016476, 0.016798]
    text_qpsk_ypoints = [0.025845, 0.038633, 0.075815]
    plt.subplot(2, 2, 1)
    l = plt.plot(xpoints, text_bpsk_ypoints, 'o-', xpoints, text_qpsk_ypoints, 'o-', linewidth=2.5)
    plt.legend(handles=l, labels=['BPSK Measured', 'QPSK Measured'], loc='upper right')
    plt.title("Text BER analysis",fontsize=15)
    plt.xlabel("Distance",fontsize=13)
    plt.ylabel("BER",fontsize=15)
    plt.grid()

    pic_bpsk_ypoints = [0.040243, 0.109720, 0.109720]
    pic_qpsk_ypoints = [0.180193, 0.258372, 0.258198]
    plt.subplot(2, 2, 2)
    l = plt.plot(xpoints, pic_bpsk_ypoints, 'o-', xpoints, pic_qpsk_ypoints, 'o-', linewidth=2.5)
    plt.legend(handles=l, labels=['BPSK Measured', 'QPSK Measured'], loc='upper right')
    plt.title("Picture BER analysis",fontsize=15)
    plt.xlabel("Distance",fontsize=13)
    plt.ylabel("BER",fontsize=15)
    plt.grid()

    aud_bpsk_ypoints = [0.262478, 0.263236, 0.263545]
    aud_qpsk_ypoints = [0.363901, 0.368187, 0.369229]
    plt.subplot(2, 2, 3)
    l = plt.plot(xpoints, aud_bpsk_ypoints, 'o-', xpoints, aud_qpsk_ypoints, 'o-', linewidth=2.5)
    plt.legend(handles=l, labels=['BPSK Measured', 'QPSK Measured'], loc='upper right')
    plt.title("Audio BER analysis",fontsize=15)
    plt.xlabel("Distance",fontsize=13)
    plt.ylabel("BER",fontsize=15)
    plt.grid()

    vid_bpsk_ypoints = [0.002267, 0.002429, 0.004917]
    vid_qpsk_ypoints = [0.008520, 0.016350, 0.031400]
    plt.subplot(2, 2, 4)
    l = plt.plot(xpoints,vid_bpsk_ypoints, 'o-',xpoints,vid_qpsk_ypoints, 'o-', linewidth=2.5)
    plt.legend(handles=l, labels=['BPSK Measured', 'QPSK Measured'], loc='upper right')
    plt.title("Video BER analysis",fontsize=15)
    plt.xlabel("Distance",fontsize=13)
    plt.ylabel("BER",fontsize=15)
    plt.grid()

    plt.suptitle("BER Analysis",fontsize=15)
    plt.show()


if __name__ == '__main__':
    cal_measured()
