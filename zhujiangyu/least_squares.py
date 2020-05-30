from numpy import array,linspace
import matplotlib.pyplot as plt
from sympy import Symbol

class Least_squares:
    '''
    该类用于曲线拟合
    参数x：x轴坐标
    参数y：y轴坐标
    '''
    def __init__(self,x,y):
        self.x = array(x)
        self.y = array(y)
        self.__z1 = self.x ** 2
        self.__a = 0
        self.__b = 0
        self.__c = 0
        self.__d = 0
        self.__e,self.__f = 0,0
        for i in range(len(y)):
            self.__a += self.__z1[i]
            self.__b += self.x[i]
            self.__e += (self.x[i] * self.y[i])
            self.__f += self.y[i]
        self.__c = self.__b
        self.__d = int(len(y))
        self.__D = ((self.__a * self.__d) - (self.__c * self.__b))
        self.__D1 = ((self.__e * self.__d) - (self.__f * self.__b))
        self.A = self.__D1 / self.__D
        self.__D2 = ((self.__a * self.__f) - (self.__c * self.__e))
        self.B = self.__D2 / self.__D

    def show(self):
        '''
        绘制图像
        '''
        self.__X = linspace((self.x[0] - 3),(self.x[-1] + 3),1000)
        self.__Y = (self.A * self.__X) + self.B
        plt.scatter(self.x,self.y,s=50)
        plt.plot(self.__X,self.__Y)
        plt.ylabel('Y')
        plt.xlabel('X')
        plt.show()

    def get_function(self):
        '''
        :return: 返回拟合函数
        '''
        self.__variable = Symbol('x')
        return self.A * self.__variable + self.B

    def get_mean_square_error(self):
        '''
        :return: 返回均方误差
        '''
        self.__M = 0
        for i in range(len(self.y)):
            self.__M += ((self.y[i] - (self.A * self.x[i] + self.B)) ** 2)
        return self.__M ** 0.5

if __name__ == '__main__':
    l = Least_squares([0,1,2,3,4,5,6,7],[27.0,26.8,26.5,26.3,26.1,25.7,25.3,24.8])
    print(f'{l.function()}\n{l.mean_square_error()}')
    l.show()
