import sys
import csv
import json
import time
import math
import numpy as np


def gsk(dsg, k):
    que = []
    temp = []
    answer = []
    for d in dsg.keys():
        for i in dsg[d]:
            if len(i[3]) <= k-1:
                if len(i[3]) < k-1:
                    que.append(i)
                else:
                    temp = [a for a in i[3]]
                    temp.append(i[0])
                    answer.append(temp)

    que.sort(key = lambda q : q[3], reverse = True)
     ### 조합
    for q in que:
        pass
    print(answer, end='\n\n')
    return answer

def ge(dsg, k):
    temp = []
    for d in dsg.keys():
        for i in dsg[d]:
            if len(i[3]) <= k-1:
                temp.append(i[0])
    return temp
#
# def findUnit(ptn):
#     start = time.time()
#     f = open(sys.argv[3],'r')
#     data = json.load(f)
#     gt = time.time()-start
#     ret = []
#     for i in data:
#         if i['ptn'] == int(ptn):
#             ret.append(i['size_unit'])
#             ret.append(i['par'])
#             ret.append(i['cord'])
#             ret.append(gt)
#             return ret
#     f.close()

def cntUnit(ptn):
    f = open(sys.argv[3],'r')
    data = json.load(f)
    for i in data:
        if i['ptn'] == int(ptn):
            cnt = i['size_unit']
            f.close()
            return cnt

def unitCord(ptn):
    temp = {}
    f = open(sys.argv[3],'r')
    data = json.load(f)
    for i in data:
        if i['ptn'] == int(ptn):
            temp[i['ptn']] = i['cord']
            ret = i['par']
    for i in data:
        if i['ptn'] in ret:
            temp[i['ptn']] = i['cord']
    f.close()
    return temp

def createGrid(ptn, unitG):
    f = open(sys.argv[3],'r')
    data = json.load(f)
    cordx = []
    cordy = []
    grid = []
    for u in unitG:
        cordx.append(unitG[u][0])
        cordy.append(unitG[u][1])
    for x in cordx:
        for y in cordy:
            temp = [x]
            temp.append(y)
            grid.append(temp)
    #print((grid))
    f.close()
    return grid

def M(ptn, unitG, k):
    minCord = []
    temp = [[],[]]
    for u in unitG:
        temp[0].append(unitG[u][0])
        temp[1].append(unitG[u][1])
    for t in temp:
        t.sort()
    minCord.append(temp[0][k-1])
    minCord.append(temp[1][k-1])
    if(unitG[ptn][0] < unitG[ptn][1]):
        h1_minD = unitG[ptn][0]
    else:
        h1_minD = unitG[ptn][1]
    idx = 0
    for m in minCord:
        if h1_minD > (unitG[ptn][idx]-m):
            h1_minD = (unitG[ptn][idx]-m)
        idx = idx + 1
    return h1_minD


def createGrid_h1(ptn, unitG, k, lowB):
    f = open(sys.argv[3],'r')
    data = json.load(f)
    cordx = []
    cordy = []
    grid = []
    #print(lowB)
    for u in unitG:
        cordx.append(unitG[u][0])
        cordy.append(unitG[u][1])
    for x in cordx:
        for y in cordy:
            if pow(unitG[ptn][0] - x,2) + pow(unitG[ptn][1] - y,2) <= pow(lowB,2):
                temp = [x]
                temp.append(y)
                grid.append(temp)
    #print((grid))
    f.close()
    return grid

def sch(unitG, grid, k, ptn):
    if(unitG[ptn][0] > unitG[ptn][1]):
        minDist = unitG[ptn][0]
    else:
        minDist = unitG[ptn][1]
    #print(minDist)
    ans = []
    for g in grid:
        cnt = 0
        for u in unitG:
            if g[0] > unitG[u][0] and g[1] > unitG[u][1]:
                cnt = cnt + 1
        if cnt < k:
            tempDist = pow(unitG[ptn][0] - g[0], 2) + pow(unitG[ptn][1] - g[1], 2)
            if tempDist < pow(minDist,2):
                minDist = pow(tempDist,0.5)
                ans[:2] = g[:2]
    print(ans)
    return ans


if __name__ == "__main__":
    f1 = open(sys.argv[1],'r')
    data = json.load(f1)
    f1.close()
    f2 = open('C:\\Users\\Owner\\Desktop\\Result1.csv','w',newline='')
    f3 = open('C:\\Users\\Owner\\Desktop\\Result_time.csv','w',newline='')
    wr = csv.writer(f2)
    wr2 = csv.writer(f3)
    wr.writerow(['Ptn', 'time'])
    wr2.writerow(['try', 'time'])
    elements = ge(data[0],int(sys.argv[2]))

    for idx in range(0,20):
        print("----{}----".format(idx))
        rng = np.random.default_rng()
        tempsampling = rng.choice(1999, size=20, replace=False) + 1
        sampling =  list(set(tempsampling) - set(elements))
        if len(sampling) == 0:
            continue
        tt = 0
        tt1 = 0
        for s in sampling:
            print(s)
            unitG = unitCord(s)
            lowB = M(s, unitG, int(sys.argv[2]))
            start = time.time()
            sch(unitG, createGrid(s, unitG), int(sys.argv[2]), s)
            start2 = time.time()
            sch(unitG, createGrid_h1(s, unitG, int(sys.argv[2]), lowB ), int(sys.argv[2]), s)
            end = time.time()
            tt = tt + start2 - start
            tt1 = tt1 + end - start2
            wr.writerow([s, start2 - start, end - start2])
        #print("")
        wr2.writerow([idx, tt/len(sampling), tt1/len(sampling)])
        print("---- ----")

    f2.close()
    f3.close()
    #for idx in range(1,20):
    #    if idx not in elements:

