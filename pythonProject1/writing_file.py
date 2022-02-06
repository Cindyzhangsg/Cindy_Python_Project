# This is a sample Python script.
filename = "squared_numbers.txt"
outfile = open(filename, "w")

for number in range(1, 13):
    square = number * number
    outfile.write(str(square) + "\n")

outfile.close()

infile = open(filename, "r")
print(infile.read()[:100])
infile.close()


	With open ('mydata.txt', 'r') as md:
		For line in md:
Print(line)