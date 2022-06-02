# 基于GNU Radio的OFDM通信系统仿真及实测

> 本次课题所做工作是在GNU Radio上搭建OFDM通信系统，并基于该系统进行仿真和实际环境中的测试，以下是本次设计使用的相关代码目录结构。

# 目录结构

```
OFDM-Simulation-Measurement
├─File Source
│ ├─lena.jpg
│ ├─send.txt
│ ├─video.mp4
│ └─陈致逸,HOYO-MiX - Moonlike Smile 皎洁的笑颜.wav
├─OFDM通信系统源码
│ ├─Hardware
│ │ ├─rx_ofdm_hardware_audio.grc
│ │ ├─rx_ofdm_hardware_audio.py
│ │ ├─rx_ofdm_hardware_picture.grc
│ │ ├─rx_ofdm_hardware_picture.py
│ │ ├─rx_ofdm_hardware_text.py
│ │ ├─rx_ofdm_hardware_txt.grc
│ │ ├─rx_ofdm_hardware_video.grc
│ │ ├─rx_ofdm_hardware_video.py
│ │ ├─tx_ofdmr_hardware_picture.py
│ │ ├─tx_ofdm_hardware_audio.grc
│ │ ├─tx_ofdm_hardware_audio.py
│ │ ├─tx_ofdm_hardware_picture.grc
│ │ ├─tx_ofdm_hardware_text.py
│ │ ├─tx_ofdm_hardware_txt.grc
│ │ ├─tx_ofdm_hardware_video.grc
│ │ └─tx_ofdm_hardware_video.py
│ └─Simulation
│    ├─ofdm_loopback_audio.grc
│    ├─ofdm_loopback_audio.py
│    ├─ofdm_loopback_picture.grc
│    ├─ofdm_loopback_picture.py
│    ├─ofdm_loopback_text.py
│    ├─ofdm_loopback_txt.grc
│    ├─ofdm_loopback_video.grc
│    └─ofdm_loopback_video.py
├─Python源码
│ ├─BER.py
│ ├─Cal_BER.py
│ └─Plot_BER.py
├─README.md
└─SDR相关环境配置.pdf
```

+ File Source文件夹存放的是发射端用以发射的信源文件

+ OFDM通信系统源码文件夹分为Hardware和Simulation两个子文件夹，分别是实测和仿真的程序源码

> *.grc是该OFDM通信系统的信号流图
>
> *.py是该OFDM通信系统的代码实现

+ Python源码文件夹存放的是计算和绘制误码率的源代码
+ SDR相关环境配置.pdf 是本次课题所需环境的搭建过程
