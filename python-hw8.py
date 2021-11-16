with open("input.txt") as inputFile:
	lines = inputFile.readlines()[::-1]
	outputFile = open("output.txt", "w")
	for line in lines:
		outputFile.write(line + "\n")
	outputFile.close()