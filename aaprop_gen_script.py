from amino import extractprop
import sys, random, string

filename = sys.argv[1]
newfilename = sys.argv[2]

# Generate Properties 
file = open(filename, 'r')

properties = []
for line in file:
    properties.append(extractprop(line))

file.close()

# Write to new file 
newfile = open(newfilename, 'w')

for i in range(len(properties)):
    newfile.write(''.join(properties[i][0]))
    newfile.write(',')
    newfile.write(''.join(properties[i][1]))
    newfile.write(',')
    newfile.write(''.join(properties[i][2]))
    newfile.write('\n')

newfile.close()


    
