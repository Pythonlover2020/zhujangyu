from random import random
from numpy import array

class LenError(Exception):
    def __str__(self):
        return '事件列表的长度和概率列表的长度不同'

class ProbabilityError(Exception):
    def __str__(self):
        return '概率之和不等于1'

class CannotFoundError(Exception):
    def __init__(self,list,element):
        self.list = list
        self.element = element
    def __str__(self):
        return '在{}中没有找到{}'.format(self.list,self.element)

class DelError(Exception):
    def __init__(self,user_object):
        self._object = user_object
    def __str__(self):
        return '不能删除事件的\'{}\'属性'.format(self._object)

def probability(events,Probabilitys):
    '''
    该函数用于按概率返回事件
    参数events: 该参数为列表，用于传递事件
    参数Probabilitys: 该参数为列表，用于传递概率
    注意：概率和必须为1
    '''
    he = 0
    for every in Probabilitys:
        he += every
    if len(events) != len(Probabilitys):
        raise LenError
    elif he != 1:
        raise ProbabilityError
    else:
        axis = 0
        for event,Probability in zip(events,Probabilitys):
            axis += Probability
            if random() < axis:
                return event

def statistics(list,element):
    '''
    该函数用于统计列表中element的个数
    参数list: 要统计的列表
    参数element: 列表中的一个数据
    注意：element必须在list里
    '''
    if element not in list:
        raise CannotFoundError
    else:
        _list = array(list)
        return (_list == element).sum()