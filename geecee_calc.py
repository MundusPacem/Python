
i       = 0
tot_GC  = 0.0

seq = raw_input("Enter a sequence: ")

for i in range (len(seq)):
    if seq[i] == "G" or seq[i] == "C":
        tot_GC += 1.0

geecee = (tot_GC/(len(seq)))

print geecee

