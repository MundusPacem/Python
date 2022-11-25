LINE=80
fp  = open("N315_linear.txt", "r")
fp1 = open("N315_linear.fasta", "w")

line = fp.readline()

line = line.strip()

fp1.write(">N315\n")

LEN=len(line)

i=0

for i in xrange(0,len(line),LINE):

	print line[i:i+LINE]+"\n"
	fp1.write(line[i:i+LINE]+"\n")

	
fp.close()
fp1.close()


