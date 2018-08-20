#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author : zkk
"""
题目：
    请使用面向对象的方法,编写出双色球。
要求:
    按照双色球开奖规则.将每次开奖的双色球保存到本地的txt文档里面,
并在双色球后面跟上日期.(提示,可能使用到库,random,time,os,sys等)。
"""
"""
双色球选号规则:
    双色球采用６＋１的方式，前区红色球可以在1～33个编号中任意选择6个，
蓝色球可以在1～16个编号中选择一个。每周二、四、日21:30开奖；每周三期。
双色球通过摇奖器确定中奖号码。摇奖时先摇出6个红色球号码，再摇出1个蓝色
球号码，摇出的红色球号码按从小到大的顺序和蓝色球号码一起公布。
"""
"""
双色球常规奖级分为6级:
    一等奖 7个号码完全相符（6个红球和1个蓝球）浮动奖金，最高奖金为一千万元 
    二等奖 6个红球相符 浮动奖金 
    三等奖 5个红球和1个蓝球相符 固定奖金每注3000元 
    四等奖 5个红球或4个红球和1个蓝球号码相符 固定奖金每注200元 
    五等奖 4个红球或3个红球＋1个蓝球号码相符 固定奖金每注10元 
    六等奖 1个蓝球号码相符（有无红球号码相符均可）固定奖金每注5元
"""

import re
import time
import random
import os
from datetime import datetime


class Bingo_ball(object):
    '一次模拟购买双色球到兑奖的过程'
    def __init__(self):
        self.amount = 1
        self.bingo_ball = None
        self.your_ball = None
        self.buy_date = datetime.now()
        self.open_time = False
        # 奖励等级，(红球，蓝球）相同个数
        self.bonus_pool = {(6,1):'first', (6,0): 'second', (5,1): 'third', (5,0):'fourth', (4,1):'fourth',
                            (4,0):'fifth', (3,1):'fifth', (0,1):'sixth', (1,1):'sixth', (2,1):'sixth'}

# *********************买彩票******************************
    def shop(self):
        print('Welcome! Would you like to buy the double balls?')
        ans1 = input('Enter (N/n) to quit,others continue.\n>')
        # 输入N/n退出
        if ans1 in ('N', 'n'):
            print('Welcome to visit again!')
            exit()
        print('Well,how many notes do you want? Or enter N/n to quit.')
        # 输入非零正整数
        notes = re.compile(r'^[+]?[0-9]+$')
        # 输入错误，就继续输入
        while True:
            ans2 = input('>')
            result = notes.match(ans2)
            if result and ans2 != '0':
                self.amount = int(ans2)
                break
            elif ans2 in ('N', 'n'):
                print('Welcome to visit again!')
                exit()
            else:
                print('Sorry,please enter a positive integer.Or enter N/n to quit.')
        print('Loading ...')
        for i in range(1, 6):
            print('%ss' % (6-i))
            time.sleep(0.5)
        print('You have bought %s notes and you should pay ￥%s' % (self.amount, self.amount*5))

# ************************生成6+1球号码*********************
    def produce_ball(self):
        blue_number = [random.randint(1, 16)]
        red_number = random.sample([i for i in range(1, 34)], 6)   # eg red:[1,25,32,5,6,7]
        red_number.sort()                                          # eg red:(1,5,6,7,25,32)
        ball = [red_number, blue_number]                           # eg:[[1,5,6,7,25,32],[12]]
        return ball

# **********************判断当天是否可以兑奖****************
    def open_date(self):
        string = self.buy_date.strftime('%a%H%M')  # 星期,小时，分钟
        result = re.match('^(\w+)(\d\d)(\d\d)$', string)
        wk_day = result.group(1)
        tm_day = int(result.group(2))
        m_day = int(result.group(3))

        # 判断买彩票的当天是否可以开奖
        if wk_day in ('Tues', 'Thur', 'Sun'):
            # 每周二，四，日的21:30之后兑奖
            if tm_day in range(21) or (tm_day == 21 and m_day in range(30)):
                print('\nYou can open the prize  after 21:30 today.')
            else:
                print('\nYou can open the prize now.')
                self.open_time = True
        elif wk_day in ('Mon', 'Wed'):
            print('\nYou can open the prize after 21:30 Tomorrow ')
        else:
            print('\nYou can open the prize after 21:30 next Monday')

# ******************中奖号码***********************
    def open_prize(self):
        if self.open_time:
            self.bingo_ball = self.produce_ball()
            print('The number of the bingo ball :\nRed:%s  Blue:%s\nThat is %s\n '
                  % (self.bingo_ball[0], self.bingo_ball[1], self.bingo_ball))

# *****************查看奖励等级**********************
    def prize_level(self):
        if self.bingo_ball:  # 避免None
            same_red = set(self.your_ball[0]) & set(self.bingo_ball[0])
            same_blue = set(self.your_ball[1]) & set(self.bingo_ball[1])
            sum1 = len(same_red)
            sum2 = len(same_blue)
            rb = (sum1, sum2)
            if rb in self.bonus_pool:
                print('\n Congratulations!you get the %s prize' % self.bonus_pool[rb])
            print('\nSorry!Maybe you should buy again!')

# ********************保存**********************
    def save(self):
        time = self.buy_date.strftime('%Y-%m-%d')
        path = 'Double-ball'
        if not os.path.exists(path):
            os.makedirs(path)
        file_path = path + '/' + time+'txt'  # 文件名字
        # for i in range(len(context)):
        f = open(file_path, 'a')
        n1 = str(self.your_ball)
        n2 = str(self.bingo_ball)
        f.write('\nYour ball number:\n\t'+n1)
        if self.bingo_ball:
            f.write('\nBingo ball number:\n\t'+n2)
        else:
            f.write('\nBingo ball number have not been produced.')
        f.write('\nTime:'+self.buy_date.strftime('%a,%Y-%m-%d %H:%M:%S'))
        f.close()

# ********************运行**********************
    def run(self):
        # 买彩票
        self.shop()
        # 生成买家双色球号码
        self.your_ball = self.produce_ball()
        print('\nThe number of the ball you get:\nRed:%s  Blue:%s .\nYour Number: %s'
              % (self.your_ball[0], self.your_ball[1], self.your_ball,))
        print('Shopping Time: %s' % self.buy_date.strftime('%a,%Y-%m-%d %H:%M:%S'))
        # 分析现在可以开奖否
        self.open_date()
        # 开奖
        self.open_prize()
        # 奖励等级
        self.prize_level()
        # 保存
        self.save()


if __name__ == '__main__':
    game_start = Bingo_ball()
    game_start.run()
