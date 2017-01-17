import sys

database = sys.argv[1]
targetseq = sys.argv[2]

# Read entire and store as dictionary, with default value (rank): 0
file = open(database, 'r')

sequences = []
for line in file:
    sequences.append(line)

file.close()

seqbase = dict.fromkeys(sequences, 0)

# Iterate through each letter in target sequence
# If the letter exists in a sequence in the database
#   increment the "rank" value of the sequence
for letter in targetseq:
    for key in seqbase.keys():
        if letter in key:
            seqbase[key] += 1

# Append sequences in database with highest ranks to highsim
highsim = []
threshold = 3
for key in seqbase.keys():
    if seqbase[key] >= threshold:
        highsim.append(key)

print(highsim)
            
