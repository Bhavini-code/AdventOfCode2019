#%%
file=open('data/day5.txt','r')
opcode=file.readline().strip().split(',')
opcode=[int(i) for i in opcode]
file.close()
# %%
##### Run this for part 1 #####
def intcode_computer(opcode, params=0):
    curr_idx=0
    while(opcode[curr_idx]!=99):

        operation=str(opcode[curr_idx]).zfill(5)
        increase_by=0
        index_moved=False
        print(operation)
        
        if operation[-2:]=='03':
            #take input
            opcode[opcode[curr_idx+1]]=params
            increase_by=2

        elif operation[-2:]=='04':
            #post output
            if operation[2]=='1':
                print(opcode[curr_idx+1])
            else:
                print(opcode[opcode[curr_idx+1]])
            increase_by=2


        else:
            #check mode1, mode2, mode3
            if operation[2]=='0':
                #operand 1 in position mode
                pos1=opcode[curr_idx+1]
            else:
                #operand 1 in immediate mode
                pos1=curr_idx+1
            if operation[1]=='0':
                # operand 2 in position mode
                pos2=opcode[curr_idx+2]
            else:
                # operand 2 in immediate mode
                pos2=curr_idx+2
            if operation[0]=='0':
                # answer in position mode
                pos3=opcode[curr_idx+3]
            else:
                # answer in immediate mode
                pos3=curr_idx+3

            increase_by=4
            if (operation[-2:]=='01'):
                opcode[pos3]=opcode[pos1]+opcode[pos2]
            elif (operation[-2:]=='02'):
                opcode[pos3]=opcode[pos1]*opcode[pos2]

        if not index_moved:
            curr_idx+=increase_by
        
    return
intcode_computer(opcode,1)
# %%
#%%
##### Run this for part 2 #####
file=open('data/day5.txt','r')
opcode=file.readline().strip().split(',')
opcode=[int(i) for i in opcode]
file.close()
# %%

def intcode_computer(opcode, params=0):
    curr_idx=0
    while(opcode[curr_idx]!=99):

        #Read instruction in operation
        operation=str(opcode[curr_idx]).zfill(5)
        #initialize variables
        increase_by=0
        index_moved=False
        print(operation)
        
        if operation[-2:]=='03':
            #take input
            opcode[opcode[curr_idx+1]]=params
            increase_by=2

        elif operation[-2:]=='04':
            #post output
            if operation[2]=='1':
                print(opcode[curr_idx+1])
            else:
                print(opcode[opcode[curr_idx+1]])
            increase_by=2

        elif operation[-2:]=='05':
            if operation[2]=='0':
                #operand 1 in position mode
                pos1=opcode[curr_idx+1]
            else:
                #operand 1 in immediate mode
                pos1=curr_idx+1
            if operation[1]=='0':
                # operand 2 in position mode
                pos2=opcode[curr_idx+2]
            else:
                # operand 2 in immediate mode
                pos2=curr_idx+2
            if opcode[pos1]!=0:
                curr_idx=opcode[pos2]
                index_moved=True
            else:
                increase_by=3

        elif operation[-2:]=='06':
            if operation[2]=='0':
                #operand 1 in position mode
                pos1=opcode[curr_idx+1]
            else:
                #operand 1 in immediate mode
                pos1=curr_idx+1
            if operation[1]=='0':
                # operand 2 in position mode
                pos2=opcode[curr_idx+2]
            else:
                # operand 2 in immediate mode
                pos2=curr_idx+2
            if opcode[pos1]==0:
                curr_idx=opcode[pos2]
                index_moved=True
            else:
                increase_by=3

        elif operation[-2:]=='07':
            #check mode1, mode2, mode3
            if operation[2]=='0':
                #operand 1 in position mode
                pos1=opcode[curr_idx+1]
            else:
                #operand 1 in immediate mode
                pos1=curr_idx+1
            if operation[1]=='0':
                # operand 2 in position mode
                pos2=opcode[curr_idx+2]
            else:
                # operand 2 in immediate mode
                pos2=curr_idx+2
            if operation[0]=='0':
                # answer in position mode
                pos3=opcode[curr_idx+3]
            else:
                # answer in immediate mode
                pos3=curr_idx+3
            if opcode[pos1]<opcode[pos2]:
                opcode[pos3]=1
            else:
                opcode[pos3]=0
            increase_by=4

        elif operation[-2:]=='08':
            #check mode1, mode2, mode3
            if operation[2]=='0':
                #operand 1 in position mode
                pos1=opcode[curr_idx+1]
            else:
                #operand 1 in immediate mode
                pos1=curr_idx+1
            if operation[1]=='0':
                # operand 2 in position mode
                pos2=opcode[curr_idx+2]
            else:
                # operand 2 in immediate mode
                pos2=curr_idx+2
            if operation[0]=='0':
                # answer in position mode
                pos3=opcode[curr_idx+3]
            else:
                # answer in immediate mode
                pos3=curr_idx+3
            if opcode[pos1]==opcode[pos2]:
                opcode[pos3]=1
            else:
                opcode[pos3]=0
            increase_by=4    
            
        elif (operation[-2:]=='01') or (operation[-2:]=='02'):
            #check mode1, mode2, mode3
            if operation[2]=='0':
                #operand 1 in position mode
                pos1=opcode[curr_idx+1]
            else:
                #operand 1 in immediate mode
                pos1=curr_idx+1
            if operation[1]=='0':
                # operand 2 in position mode
                pos2=opcode[curr_idx+2]
            else:
                # operand 2 in immediate mode
                pos2=curr_idx+2
            if operation[0]=='0':
                # answer in position mode
                pos3=opcode[curr_idx+3]
            else:
                # answer in immediate mode
                pos3=curr_idx+3

            increase_by=4
            if (operation[-2:]=='01'):
                opcode[pos3]=opcode[pos1]+opcode[pos2]
            elif (operation[-2:]=='02'):
                opcode[pos3]=opcode[pos1]*opcode[pos2]
        else:
            print('Oops. Unknown opcode got : ', operation)

        if not index_moved:
            curr_idx+=increase_by

    return
#%%
intcode_computer(opcode,5)
# %%
