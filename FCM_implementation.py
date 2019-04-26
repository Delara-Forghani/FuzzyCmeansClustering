import matplotlib.pyplot as plt
from Point import *
import random
from math import pow
from scipy.spatial import distance
import numpy as np


class FCM:
    def __init__(self, cluster, iteration):
        self.clusterNum = cluster
        self.iterationNum = iteration
        self.dataList = []
        self.clusterCenters = [None] * self.clusterNum
        self.matrix = []
        self.mExponent = 2
        self.objectiveFunction = 0

    def loadData(self):
        f = open("E:\Computational_intelligence\data.txt", "r")
        if f.mode == 'r':
            content = f.read()
            for i in range(len(content.split("\n")) - 1):
                point = Point(content.split("\n")[i].split(" ")[0], content.split("\n")[i].split(" ")[1])
                self.dataList.append(point)
            # for i in range(len(self.dataList)):
            #    print(self.dataList[i].x + " " + self.dataList[i].y)

    def showData(self):

        for i in range(len(self.dataList)):
            plt.plot(float(self.dataList[i].x),float(self.dataList[i].y), 'o', color='black');
        plt.show()

    def fcmSetup(self):
        temp = random.sample(range(0, len(self.dataList)), len(self.clusterCenters))
        for i in range(len(self.clusterCenters)):
            self.clusterCenters[i] = self.dataList[temp[i]]
        print("********")
        # for i in range(len(self.clusterCenters)):
        #     print(self.clusterCenters[i].x + " " + self.clusterCenters[i].y)

        self.matrix = [[0 for x in range(len(self.dataList))] for y in range(len(self.clusterCenters))]
        for i in range(len(self.dataList)):
            for j in range(len(self.clusterCenters)):
                self.matrix[j][i] = round(random.uniform(0, 1), 2)

       # print(self.matrix)

        # for i in range(0,self.iterationNum):

    def fcmImplement(self):
        print("###########")

        for i in range(self.iterationNum):
            sigma_x = 0
            sigma_y = 0
            denominator = 0
            for i in range(len(self.clusterCenters)):  # calculate cx cy
                for j in range(len(self.dataList)):
                    temp = pow(self.matrix[i][j], self.mExponent)
                    sigma_x += (int(self.dataList[j].x) * temp)
                    sigma_y += (int(self.dataList[j].y) * temp)
                    denominator += temp
                self.clusterCenters[i].x = sigma_x / denominator
                self.clusterCenters[i].y = sigma_y / denominator
                # print(self.clusterCenters[i].x,self.clusterCenters[i].y)

            for i in range(len(self.clusterCenters)):
                total_dst = 0
                dstXiToCj = 0
                for j in range(len(self.dataList)):
                    a = (float(self.dataList[j].x), float(self.dataList[j].y))
                    b = (float(self.clusterCenters[i].x), float(self.clusterCenters[i].y))
                    dst = distance.euclidean(a, b)
                    dstXiToCj = pow(dst, 1 / (self.mExponent - 1))
                    for r in range(len(self.clusterCenters)):
                        c = (float(self.clusterCenters[r].x), float(self.clusterCenters[r].y))
                        if distance.euclidean(a, c) != 0:
                            temp = np.sqrt(1 / distance.euclidean(a, c))
                        final = pow(temp, 2 / (self.mExponent - 1))
                        total_dst += final
                        result = dstXiToCj * total_dst
                    if result != 0:
                        self.matrix[i][j] = round(1 / (result), 3)

            #print(self.matrix)

            for i in range(len(self.clusterCenters)):
                for j in range(len(self.dataList)):
                    a = (int(self.dataList[j].x), int(self.dataList[j].y))
                    b = (float(self.clusterCenters[i].x), float(self.clusterCenters[i].y))
                    dst = distance.euclidean(a, b)
                    temp = pow(self.matrix[i][j], self.mExponent) * dst
                    self.objectiveFunction += temp



    def showCenters(self):
        for i in range(len(self.dataList)):
            plt.plot(float(self.dataList[i].x), float(self.dataList[i].y), 'o', color='black');

        for i in range(len(self.clusterCenters)):
            plt.plot(float(self.clusterCenters[i].x),float(self.clusterCenters[i].y), 'o', color='red');

        plt.show()


if __name__ == '__main__':
    fcm = FCM(4, 10)
    fcm.loadData()
    fcm.fcmSetup()
    fcm.fcmImplement()
    fcm.showCenters()