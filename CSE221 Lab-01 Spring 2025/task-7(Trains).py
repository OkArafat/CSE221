import sys
def time_to_minutes(time_str):
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

    train_name = parts[0]  
    departure_time = parts[-1]  
    time_in_minutes = time_to_minutes(departure_time)  

    trains.append((train_name, time_in_minutes, line)) 

trains.sort(key=sorting_key)

for train in trains:
    print(train[2]) 
