import string, random

file = open("aminoacids.txt", "w")

amino_acids = 'RKDEQNHSTYCMWAILFVPG'

for i in range(10000):	
    sequence = []
    for i in range(7):
        sequence.append(random.choice(amino_acids))
    file.write(''.join(sequence))
    file.write('\n')

file.close()

