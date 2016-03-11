with open("array.txt", "r") as file1:
	copy_of_file1=file1.read().split(",")
file1.close()

Table=[[] for i in range(8)]
c=0

for i in range(8):
	for j in range(8):
		Table[i].append(copy_of_file[c])
		c+=1

print "Your table will rotate by 90,180 and 270 degrees"

New_Table=Table

for k in range(3):
	for i in range(8):
		for j in range(8):
			num=Table[7-j][i]
			New_Table[i][j]=num

	print "Rotate", k+1
	print New_Table
	Table=New_Table
