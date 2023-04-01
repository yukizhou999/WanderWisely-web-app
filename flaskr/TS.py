import itertools

#calculate distance bwt 2 POI based on lat/long

def getlocation(POIs_list):
    POIs_dict = {}
    for poi in POIs_list:
        POIs_dict[poi] = database[poi] # get it from database
    return POIs_dict

def distance(POI_1, POI_2):
    return ((POI_1[0] - POI_2[0])**2 + (POI_1[1] - POI_2[1])**2)**0.5

def tsp(POIs_list):
    POIs_dict = getlocation(POIs_list)
    shortest_path = None
    shortest_distance = float('inf')
    for path in itertools.permutations(POIs_dict.keys()):
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += distance(POIs_dict[path[i]], POIs_dict[path[i+1]])
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_path = path
    return shortest_path, shortest_distance

# Example
POIs = ["A", "B", "C"]
database = {"A": (1,3), "B": (4,7), "C": (5,3)}
shortest_path, shortest_distance = tsp(POIs)
print("Shortest path:", shortest_path)
print("Shortest distance:", shortest_distance)