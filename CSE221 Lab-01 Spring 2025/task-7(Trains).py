import sys
def timetominutes(time_str):
    hours = int(time_str[:2])  
    minutes = int(time_str[3:])  
    return hours * 60 + minutes  

def sorting_key(train):
    return (train[0], -train[1])  

N = int(sys.stdin.readline().strip())  

trains = [] 
for i in range(N):
    line = sys.stdin.readline().strip()  
    parts = line.split()  

    trainname_1 = parts[0]  
    departure_time = parts[-1]  
    time_in_minutes = timetominutes(departure_time)  

    trains.append((trainname_1, time_in_minutes, line)) 

trains.sort(key=sorting_key)

for train in trains:
    print(train[2]) 
