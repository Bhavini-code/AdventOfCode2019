#%%
puzzle_input='372037-905157'
pswd_range=puzzle_input.split('-')
#%%
def find_actual_range(given_range):
    '''Takes in given range strings list and 
    returns actual range applicable as strings'''
    actual_range=[]
    #find lower range
    #loop through numbers from left to right 5 times
    #if the next number is smaller than current number, 
    # replace the trailing numbers to the current number
    # and break out
    for i in range(5):
        actual_range.append([])
        actual_range[0].append(given_range[0][i])
        if given_range[0][i+1]<given_range[0][i]:
            actual_range[0].append(given_range[0][i]*(5-i))
            break
    actual_range[0]="".join(actual_range[0])
    print(actual_range)
    #find upper range
    #loop through numbers from left to right 5 times
    #if the next number is smaller than current number, 
    # reduce the current number by 1 and 
    # replace the rest with 9
    for i in range(5):
        if given_range[1][i+1]<given_range[0][i]:
            actual_range[1].append(str(int(given_range[1][i])-1))
            actual_range[1].append('9'*(5-i))
            break
        actual_range[1].append(given_range[1][i])
    actual_range[1]="".join(actual_range[1])
    print(actual_range)
    return actual_range
actual_range=find_actual_range(pswd_range)
# %%
def is_adjacent_same(possible_password):
    for char in possible_password:
        if char*2 in possible_password:
            return True
    return False
def is_increasing(possible_password):
    for i in range(5):
        if possible_password[i+1]<possible_password[i]:
            return False
    return True
def atleast_one_double(possible_password):
    for char in possible_password:
        if (possible_password.count(char)==2) and (char*2 in possible_password):
            return True
    return False
#%%
total_possible_passwords=0
for possible_password in range(int(actual_range[0]),int(actual_range[1])+1):
    if is_adjacent_same(str(possible_password)) and is_increasing(str(possible_password)) :
        total_possible_passwords+=1
print(total_possible_passwords)

# %%
#for puzzle 2 only
total_possible_passwords=0
for possible_password in range(int(actual_range[0]),int(actual_range[1])+1):
    if atleast_one_double(str(possible_password)) and is_increasing(str(possible_password)) :
        total_possible_passwords+=1
print(total_possible_passwords)
# %%
