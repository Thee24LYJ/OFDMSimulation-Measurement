# -*- coding:utf-8 -*- 
"""
Author：G3
Time: 2022/4/28 
Software: PyCharm
"""

"""
    误码率计算
"""
from BER import *
import os

path = r"所接收文件所在父目录"
file_ber_dic = {}

def txt_BER():
    words = "abcdefghijklmnopqrstuvwxyz\nABCDEFGHIJKLMNOPQRSTUVWXYZ\n0123456789\nhello world!\nHELLO WORLD!\n~!@#$%^&*()-_=+[{]}\|;:'\",<.>/?\n"

    files = os.listdir(path)
    for i in files:
        file = f"{path}\\{i}"
        count = 0
        errsymbol = []
        with open(file, 'r') as f:
            content = f.read()
            contentdic = content.split("----------------\n")
            print(f"receive.txt:{contentdic}")
            for j in contentdic:
                if j == words:
                    count = count + 1
                else:
                    errsymbol.append(j)
            print(f"正确个数:{count} 总个数:{len(contentdic)} 错误个数:{len(contentdic) - count}")
            print(f"错误信息:{errsymbol}")
            if len(contentdic) - count - 1:
                words_bin = "".join(str2bin((len(contentdic) - count - 1)*2 * words).split(' '))
                ber=f"{(len(contentdic) - count - 1)/count*100}%"
                errsymbol_str = "".join(errsymbol[0:-1])
                errsymbol_bin = "".join(str2bin(errsymbol_str).split(' '))
                np_words_bin = np.array(list(words_bin), dtype=int)
                np_errsymbol_bin = np.array(list(errsymbol_bin), dtype=int)
                # ber = CalBER(np_words_bin, np_errsymbol_bin)
                ber_dic = {i: ber}
                file_ber_dic.update(ber_dic)
            else:
                print("误码率:0%")
                ber_dic = {i: "0%"}
                file_ber_dic.update(ber_dic)

    for k in file_ber_dic.items():
        print(k)

def pic_BER():
    file_lena = r"../File Source/lena.jpg"
    files = os.listdir(path)
    for i in files:
        file = f"{path}\\{i}"
        with open(file_lena, 'rb') as f:
            fb = f.read()
            image = "".join(int2bin([x for x in fb]).split(' '))
            np_image = np.array(list(image), dtype=int)

        with open(file, 'rb') as f:
            fb = f.read()
            image_test = "".join(int2bin([x for x in fb]).split(' '))
            np_image_test = np.array(list(image_test), dtype=int)

        ber = CalBER(np_image, np_image_test)
        ber_dic = {i: ber}
        file_ber_dic.update(ber_dic)
    for k in file_ber_dic.items():
        print(k)


def audio_BER():
    file_audio = r"../File Source/陈致逸,HOYO-MiX - Moonlike Smile 皎洁的笑颜.wav"
    files = os.listdir(path)
    for i in files:
        file = f"{path}\\{i}"
        with open(file_audio, 'rb') as f:
            fb = f.read()
            audio = "".join(int2bin([x for x in fb]).split(' '))
            np_audio = np.array(list(audio), dtype=int)

        with open(file, 'rb') as f:
            fb = f.read()
            audio_test = "".join(int2bin([x for x in fb]).split(' '))
            np_audio_test = np.array(list(audio_test), dtype=int)

        ber = CalBER(np_audio, np_audio_test)
        ber_dic = {i: ber}
        file_ber_dic.update(ber_dic)
    for k in file_ber_dic.items():
        print(k)


def video_BER():
    file_video = r"../File Source/video.mp4"
    files = os.listdir(path)
    for i in files:
        file = f"{path}\\{i}"
        with open(file_video, 'rb') as f:
            fb = f.read()
            video = "".join(int2bin([x for x in fb]).split(' '))
            np_video = np.array(list(video), dtype=int)

        with open(file, 'rb') as f:
            fb = f.read()
            video_test = "".join(int2bin([x for x in fb]).split(' '))
            np_video_test = np.array(list(video_test), dtype=int)

        ber = CalBER(np_video, np_video_test)
        ber_dic = {i: ber}
        file_ber_dic.update(ber_dic)
    for k in file_ber_dic.items():
        print(k)


def get_max_count(str):
    d = {}
    for i in str:
        # 统计每个字符出现的次数
        count = str.count(i)
        d[i] = count
    list = []
    for i, v in d.items():
        list.append((i, v))
    print(list)
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i][1] < list[j][1]:
                list[i], list[j] = list[j], list[i]

    return list[0][0], list[0][1]


if __name__ == '__main__':
    audio_BER()
