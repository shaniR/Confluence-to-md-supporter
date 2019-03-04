import sys,os
import ntpath

EXTRA_SPACES = 4

print '-------------------   Post processing started!  -------------------------'

md_source_path = sys.argv[1]
md_files = os.listdir(md_source_path)
md_dest_folder = sys.argv[2]

for f in md_files:
	
	isFomattingOn = False
	leadingSpaces = 0

	toFormat = False
	toFormatPrevious = False

	terms = ["!!! tip", "!!! warning", "!!! info", "!!! note"]

        fileName = ntpath.basename(f)
	f = open(md_source_path+f, 'r')
	lines = f.readlines()
	f.close()

	for term in terms:
	    for id, currentLine in enumerate(lines):

		if(terms.index(term) == 0):
			if (currentLine.rstrip().lstrip() == "```"):
				leadingSpaces = leadingSpaces - 4
				toFormat = toFormatPrevious
		                toFormat = True
				if(toFormat):
		    			leadingSpaces = 0
	       
		if term in currentLine:
		    toFormat = True
		    EXTRA_SPACES = 0
		    leadingSpaces = len(currentLine) - len(currentLine.lstrip())
		    if(leadingSpaces == 0):
		        leadingSpaces = 4 
		    continue

		if toFormat:
		    currentLine = currentLine.rjust(leadingSpaces + EXTRA_SPACES + len(currentLine))
		    if("TEST" in currentLine):
		        toFormat = False
		        EXTRA_SPACES = 0
		        leadingSpaces = 0

		if(terms.index(term) == 0):
			if "``` " in currentLine:
	       			leadingSpaces = len(currentLine) - len(currentLine.lstrip())
	       			toFormatPrevious = toFormat

		lines[id] = currentLine


        fileName = md_dest_folder+fileName

	with open(fileName, "wb") as file:
	    for item in lines:
		if ("TEST" not in item):
		    file.write("%s" % item)
	
print '-------------------   Post processing completed!  -------------------------'
