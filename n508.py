import heapq
num_of_lec=int(input())
event_time=[]
groups_end=[]
for _ in range(num_of_lec):
    line=input().split()
    start,end=line[2].split("-")
    start_hour,start_min=map(int,start.split(":"))
    start_time=start_hour*60+start_min
    end_hour,end_min=map(int,end.split(":"))
    end_time=end_hour*60+end_min
    event_time.append((start_time,end_time))
event_time.sort(key=lambda x: x[0])
for start,end in event_time:
    if groups_end and groups_end[0]<=start:
        heapq.heappop(groups_end)
        heapq.heappush(groups_end,end)
    else:
        heapq.heappush(groups_end,end)
print(len(groups_end))