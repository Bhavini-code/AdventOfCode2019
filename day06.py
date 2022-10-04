#%%
file=open('data/test.txt','r')
orbits=file.readlines()
file.close()
#%%
orbits=[i.strip().split(')') for i in orbits]
#%%
def find_object(orbits,object):
    for count,item in enumerate(orbits):
        if item[0]==object:
            return count
    return -1

#%%
next_obj='COM'
location=find_object(orbits,next_obj)
temp=[orbits[location][0],orbits[location][1]]
L=[]
L.append(temp)
next_obj=temp[-1]
while (len(orbits)>0):
    print('temp is : ',temp)
    print('L is : ',L)
    orbits.pop(location)
    location=find_object(orbits,next_obj)
    if location>=0:
        temp.extend(orbits[location][1])
        if temp not in L:
            L.append(temp)
        next_obj=temp[-1]
    else:
        temp.pop()
        if temp[-1]=='COM':
            break
        else:
            next_obj=temp[-1]
    
#%%
#%%

orb_dir={}
direct_orbit=0;total_orbit=0
for item in orbits:
    indirect_orbit=0
    if item[0] not in orb_dir:
        #start of a new orbit
        orb_dir[item[0]]=0
        if item[1] in orb_dir:
            orb_dir[item[1]]+=1
        else:
            orb_dir[item[1]]=1
        direct_orbit=1
    else:
        orb_dir[item[0]]+=1
        orb_dir[item[1]]=1
        indirect_orbit+=1;direct_orbit+=1
    sum_orbit=direct_orbit+indirect_orbit
#orb_dir
#%%=[]
L=[];temp_list=[]
for item in orbits:
    if not L:
        temp_list=[item[0], item[1]]
        L.append(temp_list)
    else:
        if item[0] == L[-1][-1]:
            temp_list=L[-1]+[item[1]]
            L.append(temp_list)            
        elif item[0] not in temp_list:
            # find the list with last item in L and assign to templist
            notFound=True
            for i in L:
                if i[-1]==item[0]:
                    notFound=False
                    temp_list=i
                    L.append(temp_list+[item[1]])
            if notFound:
                templist=[item[0],item[1]]
                L.append(temp_list)
    print(L)       
#L
#%%
sum=0
for i in L:
    if len(i)==2:
        sum+=1
    else:
        sum+=len(i)-1
sum
# %%
