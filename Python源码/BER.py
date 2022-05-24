# -*- coding:utf-8 -*- 
"""
Author：G3
Time: 2022/5/14 
Software: PyCharm
"""
"""
    误码率计算
"""
import numpy as np

# 字符串转换为二进制
def str2bin(str):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in str])


# 二进制转换为字符串
def bin2str(bin):
    return ''.join([chr(i) for i in [int(b, 2) for b in bin.split(' ')]])


def int2bin(intarr):
    return ' '.join([bin(i).replace('0b', ' ') for i in intarr])


# 计算字典键和键值总个数
def CalDicNumber(dic_value):
    keyvalue_sum = 0
    key_sum = len(dic_value)
    for i in dic_value:
        keyvalue_sum += dic_value[i]
    return key_sum, keyvalue_sum


def CalBER(original, modify):
    """
    计算误码率
    (错误码元/总码元)*100%

    :param original: 进行对照比特流 numpy类型
    :param modify: 测试误码率比特流 numpy类型
    """

    # 初始码元
    orisymbol_result = {}
    orione_number=np.sum(original)
    orisymbol_result['1'] = orione_number
    orisymbol_result['0']=len(original)-orione_number
    orisymbol_restuple = CalDicNumber(orisymbol_result)
    print(f"发送:{orisymbol_result}", end=' ')
    print(orisymbol_restuple)

    # 接收码元
    modsymbol_result = {}
    modone_number = np.sum(modify)
    modsymbol_result['1'] = modone_number
    modsymbol_result['0'] = len(modify) - modone_number
    modsymbol_restuple = CalDicNumber(modsymbol_result)
    print(f"接收:{modsymbol_result}", end=' ')
    print(modsymbol_restuple)
    ber=f"{(orisymbol_restuple[1] - modsymbol_restuple[1]) / orisymbol_restuple[1] * 100}%"
    print(f"误码率:{ber}")
    return ber
