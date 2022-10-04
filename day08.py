#%%
file=open('data/day8.txt','r')
image=file.readline().strip()
file.close()
#%%
# Reading layer by layer
# Also checking the fewest zero count in this loop in parallel
# Noting down the layer location for later processing
pixel_per_layer=25*6
layers=[]
min_zero_count=pixel_per_layer #all zeroes
for i in range(0,len(image),pixel_per_layer):
    layers.append(image[i:i+pixel_per_layer])
    zero_count=layers[-1].count('0')
    if zero_count<min_zero_count:
        #note down the zero count 
        # and the location in the layers
        min_zero_count=zero_count
        location=len(layers)-1
# %%
# Printing the first answer
print(layers[location])
print('Minimum number of zeroes: ',min_zero_count)
print(layers[location].count('1')*layers[location].count('2'))
# %%
# Creating the output layer
output_layer=[]
for i in range(pixel_per_layer):
    #go through each layer and pick the first pixel that is not '2'
    for j in range(len(layers)):
        transparent=True
        if (layers[j][i]=='0') or (layers[j][i]=='1'):
            output_layer.append(layers[j][i])
            transparent=False
            break
    if transparent:
        output_layer.append('2')
# %%
# Tried with printing the whole matrix, 
# printing with 2 as blanks and printing blanks and zeroes, 
# but it works best and the result is 
# visible only when we print the ones only
count=0
for char in output_layer:
    if (char=='0') or (char=='2'):
        print(' ',end='')
    else:
        print(char,end='')
    count+=1
    if count == 25:
        print('')
        count=0
# %%
