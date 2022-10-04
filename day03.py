#%%
with open('data/day3.txt') as file:
    paths=[line.strip().split(',') for line in file]
#%%
def get_coordinates_traversed(path):
    travel_path=[(0,0)]
    curr_x=0; curr_y=0
    increase_x=decrease_x=increase_y=decrease_y=False
    for direction in path:
        path_length=int(direction[1:])
        if direction.startswith('R'):            
            increase_x=True #increase x co-ordinates
        elif direction.startswith('L'):
            decrease_x=True #decrease x co-ordinates
        elif direction.startswith('U'):
            increase_y=True # increase y co-ordinates
        elif direction.startswith('D'):
            decrease_y=True # decrease y co-ordinates

        for _ in range(path_length):
            if increase_x:
                curr_x+=1
            elif decrease_x:
                curr_x-=1
            elif increase_y:
                curr_y+=1
            elif decrease_y:
                curr_y-=1
            travel_path.append((curr_x,curr_y))
        increase_x=decrease_x=increase_y=decrease_y=False
    return travel_path

# %%
travel_path1=get_coordinates_traversed(paths[0])
travel_path2=get_coordinates_traversed(paths[1])
# %%
intersection=set(travel_path1).intersection(set(travel_path2))
print(intersection)
intersection=[i for i in intersection if i != (0, 0)]
# %%
fastpath=0
for item in intersection:
    temp_path=travel_path1.index(item)+travel_path2.index(item)
    if not fastpath:
        fastpath=temp_path
    if fastpath>temp_path:
        fastpath=temp_path
print(fastpath)
# %%
