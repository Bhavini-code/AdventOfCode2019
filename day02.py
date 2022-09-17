#%%
file=open('data/day2.txt','r')
opcode=file.readline().strip().split(',')
opcode=[int(i) for i in opcode]
reset=[i for i in opcode]
file.close()
#%%
def find_output(opcode):
    curr_idx=0
    while(opcode[curr_idx]!=99):

        pos1=opcode[curr_idx+1]
        pos2=opcode[curr_idx+2]
        pos3=opcode[curr_idx+3]

        if (opcode[curr_idx]==1):
            opcode[pos3]=opcode[pos1]+opcode[pos2]
        elif (opcode[curr_idx]==2):
            opcode[pos3]=opcode[pos1]*opcode[pos2]
        curr_idx+=4
        
    return opcode[0]
# %%
for noun in range(100):
    for verb in range(100):
        opcode=[i for i in reset]
        opcode[1]=noun;opcode[2]=verb
        if find_output(opcode) == 19690720:
            print('Answer found. Noun: ', noun, ' and Verb: ',verb)
            break
# %%
