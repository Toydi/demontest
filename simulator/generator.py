#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import random
import math

LINE_OF_POINTS = 10
NUM_OF_POINTS = LINE_OF_POINTS**2
MAP_SIZE = 50.0
RECEIVE_POINT_NUM = 15
RECEIVE_THING_NUM = 10

class GENERATOR(object):

    def __init__(self):
        self.x = []
        self.y = []
        self.send = []
        self.receive = []

    def generate_point(self,point_file):
        f = open(point_file,'w') # clean up the file
        f.truncate()
        f.close()

        f = open(point_file,'a')

        example = random.sample(range(NUM_OF_POINTS),RECEIVE_POINT_NUM+1) # random send/receive point ID

        for i in range(NUM_OF_POINTS): # random send num
            if i in example[1:RECEIVE_POINT_NUM+1]:
                receive = random.randint(1,RECEIVE_THING_NUM)
                self.receive.append(receive)
            else:
                self.receive.append(0)

        send = sum(self.receive) # calculate receive num
        for i in range(NUM_OF_POINTS):
            if i==example[0]:
                self.send.append(send)
            else:
                self.send.append(0)

        for i in range(NUM_OF_POINTS):
            x_sand = i % LINE_OF_POINTS + 1 # x
            x = random.uniform(x_sand * MAP_SIZE - 5.0, x_sand * MAP_SIZE + 5.0)
            y_sand = i // LINE_OF_POINTS + 1 # y
            y = random.uniform(y_sand * MAP_SIZE - 5.0, y_sand * MAP_SIZE + 5.0)
            self.x.append(x)
            self.y.append(y)

            result = str(x) + " " + str(y) + " " + str(self.send[i]) + " " + str(self.receive[i])
            f.write(result+"\n")

        f.close()

    def generate_line(self,line_file):
        f = open(line_file, 'w') # clean up the file
        f.truncate()
        f.close()

        f = open(line_file,'a')

        for i in range(NUM_OF_POINTS):
            if i % LINE_OF_POINTS != (LINE_OF_POINTS-1): # start and end in row
                start = i
                end = start + 1
                distance = math.sqrt((self.x[start]-self.x[end])**2+(self.y[start]-self.y[end])**2)
                cost = random.uniform(distance-5.0,distance+5.0)
                f.write(str(start) + " " + str(end) + " " + str(cost) + "\n")
            if i // LINE_OF_POINTS != (LINE_OF_POINTS-1): # start and end in col
                start = i
                end = start + LINE_OF_POINTS
                distance = math.sqrt((self.x[start] - self.x[end]) ** 2 + (self.y[start] - self.y[end]) ** 2)
                cost = random.uniform(distance-5.0,distance+5.0)
                f.write(str(start) + " " + str(end) + " " + str(cost) + "\n")

        f.close()






