import sys

id_map = {}
classes = 0

class Node:
    def __init__(self, id, classes_p, depth=0):
        self.id = id
        self.children = []
        self.couple = None
        self.depth = depth
        self.classes = classes_p

    def add_child(self, childID):
        if len(self.children) < 5:
            self.children.append(childID)
            return True
        return False

def check_couple(self_id, couple_id):
    # print("classes: ", id_map[self_id].classes == id_map[couple_id].classes)
    if self_id not in id_map.keys() or couple_id not in id_map.keys():
        return True
    if id_map[couple_id].depth > id_map[self_id].depth:
        return (id_map[couple_id].depth-id_map[self_id].depth) >= 3
    else:
        return (id_map[self_id].depth-id_map[couple_id].depth) >= 3


M = int(sys.stdin.readline())
index = 0
all_ids = sys.stdin.readline().strip().split()
while index < len(all_ids):
    temp_id = int(all_ids[index])
    if index % 2:
        # Child
        prev_id = int(all_ids[index-1])
        id_map[temp_id] = Node(temp_id, id_map[prev_id].classes, id_map[prev_id].depth+1)
        id_map[prev_id].add_child(temp_id)
    else:
        # Parent
        if temp_id not in id_map.keys():
            id_map[temp_id] = Node(temp_id, classes)
            classes += 1
    index += 1
# print(id_map)
N = sys.stdin.readline()
couple_ids = sys.stdin.readline().strip().split()
index = 0
illegal_list = []
while index < len(couple_ids):
    res = check_couple(int(couple_ids[index]), int(couple_ids[index+1]))
    if not res:
        illegal_list.append(int(couple_ids[index]))
        illegal_list.append(int(couple_ids[index+1]))
    # print("couple: {}, {} is {}".format(couple_ids[index], couple_ids[index+1], res))
    index += 2
illegal_list.sort()
result = ""
for i in illegal_list:
    if result:
        result += " "
    result += str(i)
print(result)