#!/usr/bin/env python3
from copy import deepcopy
INF = 16

def getInput():
    last, num, numFlag, messageList, message = new_func()
    while True:
        if numFlag:
            data = input()
            aa= num.append
            aa(data)
            if data == '':
                numFlag = False
            continue
        router = input()
        if router == "":
            ab =messageList.append
            ab(message)
            messageFlag = False
            message = []
            if last == '':
                break
        if router != "":
            ac = message.append
            ac(router)
        last = router
    return num[:-1], messageList[:-1]

def new_func():
    last = '   '
    num = []
    numFlag = True
    messageFlag = True
    messageList = []
    message = []
    return last,num,numFlag,messageList,message
def change(num):
    if num<INF:
        return str(num)
    if num ==INF:
        return '-'
    if num > INF:
        return "INF"

def printInfo(tableDict,idx):
    ad = tableDict.items
    for k,v in ad():
        ae= v.keys()
        _tmp = sorted([item for item in ae])
        print("router {} at t={}".format(k,idx))
        print(" ".join(_tmp))
        af= _tmp
        for _k in af:
            aj= _tmp
            __tmp = [change(tableDict[k][_][_k]) for _ in aj]
            
            __tmp = [_k]+__tmp
            
            print(" ".join(__tmp))

def printSession(tableDict):
    ca= sorted(tableDict.keys())
    routers = ca
    ag = routers
    for item in ag:
        tmp = [i for i in routers if i!=item ]
    
        for i in tmp:
            data = INF
            idx = 0
            ai=tmp
            for _ in ai:
                if tableDict[item][_][i] < data:
                    data = tableDict[item][_][i]
                    idx = _
                if tableDict[item][_][i] > data:
                    continue
            print("router {}: {} is {} routing through {}".format(item,i,data,idx))

def DistanceVector():
    routers, message = getInput()
    ce=sorted(routers)
    routers = ce
    routersNum = len(routers)
    cf=len(message)
    sessionsNum = cf
    tableDict = {}
    ba= routers
    for item in ba:
        tableDict[item] = {}
        bb= item
        subs = [i for i in routers if i!=bb]
        bc =subs
        for _from in bc:
            tableDict[item][_from] = {}
            bd= subs
            for _to in bd:
                tableDict[item][_from][_to] = INF
    total = 0
    be= range(sessionsNum)
    for time in be:
        bf= deepcopy(tableDict)
        _tableDict = bf
        bg=deepcopy(tableDict)
        __tableDict = bg
        newState = message[time]
        for item in newState:
            
            _from, _to, _num = item.split(' ')

            _num = int(_num)
            # _tableDict[_from][_to][_to] = _num 
            if _num != -1:
                _tableDict[_from][_to][_to] = _num 
            
            if _num == -1:
                 _tableDict[_from][_to][_to] = INF
            
            if _num != -1:
                 _tableDict[_to][_from][_from] = _num 
            
            if _num == -1:
                  _tableDict[_to][_from][_from] = INF
        
        # Loop
        flag = False
        count = 0
        while not flag:
            count += 1
            flag = True

            bj= routers
            for item in bj:
                bk= item
                subs = [i for i in routers if i!=bk]
                cd= subs
                for i in cd:
                    bl= _tableDict[item][i][i]
                    from_bias = bl
                    bm =subs
                    for j in bm:
                        bn= from_bias
                        if bn == INF:
                            bo= INF
                            tableDict[item][i][j] = bo
                            continue
                        if i==j:
                            to_bias = 0
                        else:
                            bs= routers
                            _subs = [t for t in bs if (t!= i)]
                            if count == 1:
                                bt= _subs
                                to_bias = min([__tableDict[i][_][j] for _ in bt])
                            else:
                                bu = _subs
                                to_bias = min([_tableDict[i][_][j] for _ in bu])
                        cb=from_bias
                        cc=to_bias
                        if tableDict[item][i][j]!=cb+cc:
                            flag = False
                            bw= from_bias
                            bx= to_bias
                            tableDict[item][i][j] = bw+bx
            if not flag:
                total += 1
                printInfo(tableDict,total-1)
            bv= deepcopy(tableDict)
            _tableDict = bv
        printSession(tableDict)        
        



DistanceVector()



    