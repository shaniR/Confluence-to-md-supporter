import sys, os
import ntpath
#import ptvsd

# 5678 is the default attach port in the VS Code debug configurations
#print("Waiting for debugger attach")
#ptvsd.enable_attach(address=('localhost', 5005), redirect_output=True)
#ptvsd.wait_for_attach()
#breakpoint()


print '-------------------   Post processing started!  -------------------------'

md_source_path = sys.argv[1]
md_files = os.listdir(md_source_path)
md_dest_folder = sys.argv[2]

for f in md_files:

    inCodeBlock = False
    insideMacro = False
    leadingSpaces = 0
    threeQuotes = '```'

    terms = ["!!! tip", "!!! warning", "!!! info", "!!! note"]

    fileName = ntpath.basename(f)
    f = open(md_source_path + f, 'r')
    lines = f.readlines()
    f.close()

    # Formatting content inside the terms above
    for id, currentLine in enumerate(lines):
        if(not insideMacro):
            for term in terms:
                if term in currentLine:
                    insideMacro = True
                    leadingSpaces = len(currentLine) - len(currentLine.lstrip())
                    break
        if (threeQuotes in currentLine):
                #Identify the end of the code block.
                if (not inCodeBlock):
                    inCodeBlock = True
                    leftSpaces = len(currentLine) - len(currentLine.lstrip())
                    # making the start of the code block 4 spaces indented in relative to the macro
                    if (leftSpaces <= leadingSpaces): 
                        leadingSpaces = leftSpaces +4
                    else:
                        leadingSpaces = leftSpaces
                else:
                    inCodeBlock = False
                    string_length=len(currentLine)+leftSpaces    # adding extra spaces
                    currentLine=currentLine.lstrip().rjust(string_length)
                    leftSpaces =0 
                continue 
        if (inCodeBlock or insideMacro):
                string_length=len(currentLine)+leadingSpaces    # adding extra spaces
                currentLine=currentLine.rjust(string_length)
        # reset counters
        if ("TEST" in currentLine):
                leadingSpaces = 0
                inCodeBlock =False
                leftSpaces =0
                insideMacro =False 
        lines[id] = currentLine

fileNameLength = len(fileName)
#Replace _ with - in the file name.
fileName = fileName[1:fileNameLength].replace('_', '-').replace('-.md', '.md')
fileName = fileName[0].lower() + fileName[1:]

fileName = md_dest_folder + fileName

with open(fileName, "wb") as file:
    for item in lines:
        if ("TEST" not in item):
            file.write("%s" % item)

print '-------------------   Post processing completed!  -------------------------'
