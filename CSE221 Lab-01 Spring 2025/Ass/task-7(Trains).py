# You have been recently recruited as the Software Engineer at Jumanji Railway Software System. You have a big task at hand. You will be given 𝑁(1≤𝑁≤100)
#  schedule of the train. The next N line will contain the name of the train and the departure time. See the input format for better understanding.

# Your task is to write a sorting algorithm that will group the trains in the lexicographical order based on the name of the trains. If two or more trains have the same name, then the train with the latest departure time will get prioritized. If there is still a tie, then the train which comes first in the input will come first.

# Input
# The first line will contain an integer 𝑁(1≤𝑁≤100)
# . For the next 𝑁
#  lines, 𝑖𝑡ℎ
#  line will describe 𝑖𝑡ℎ
#  train. Please see the sample input for better understanding.

# Please note that the names of the trains and destinations don't contain any white spaces, and the length of the names and destinations will be at most 100. For example, look at the following description:

# DhumketuExpress will departure for Chittagong at 02:30
# Here, DhumketiExpress is the name of the train Chittagong is the destination, and they don't contain any whitespaces, and their length is less than 100.

# Output
# Print the train description in the sorted order (specified above). Please see the output format for better understanding.




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
