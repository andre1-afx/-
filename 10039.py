import sys

data = sys.stdin.read().split()
idx = 0

S = int(data[idx]); idx += 1              # 有幾組情境

for sc in range(1, S + 1):
    # 第一段：城市
    C = int(data[idx]); idx += 1
    cities = []
    for _ in range(C):
        cities.append(data[idx]); idx += 1

    # 第二段：火車
    T = int(data[idx]); idx += 1
    trains = []                           # 每班車是一個串列，裡面放 (時間, 城市)
    for _ in range(T):
        ti = int(data[idx]); idx += 1     # 這班車停幾站
        stops = []
        for _ in range(ti):
            time = int(data[idx])         # "0949" 轉成整數 949
            city = data[idx + 1]
            idx += 2
            stops.append((time, city))
        trains.append(stops)

    # 第三段：出發時間、起點、終點
    start_time = int(data[idx]); idx += 1
    start = data[idx]; idx += 1
    dest = data[idx]; idx += 1
    
    # 這裡寫兩趟的計算和輸出
    segs=[]
    for stops in trains:
        for j in range(len(stops)-1):
            t1,c1=stops[j]
            t2,c2=stops[j+1]
            segs.append((t1,c1,t2,c2))
    earliest={}
    for city in cities:
        earliest[city]=10000
    earliest[start]=start_time
    segs.sort()
    for t1,c1,t2,c2 in segs:
        if earliest[c1]<=t1:
            earliest[c2]=min(earliest[c2],t2)
    arrive=earliest[dest]
    print(f"Scenario {sc}")
    if arrive==10000:
        print("No connection")
        print()
        continue
    lastest={}
    for city in cities:
        lastest[city]=-1
    lastest[dest]=arrive
    segs.sort(key=lambda s: s[2], reverse=True)
    for t1,c1,t2,c2 in segs:
            if t2<=lastest[c2]:
                lastest[c1]=max(lastest[c1],t1)
    print(f"Departure {lastest[start]:04d} {start}")
    print(f"Arrival   {arrive:04d} {dest}")
    print()    
    
