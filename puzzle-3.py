import math

#Open input file
file = open('input3.txt')

#Determines end of line
line_length = (len(file.readline()))

total_lines = 321
tree = '#'
count_line = 1
count_trees = 0

#Creates a new file to write the output to
out_file = open('out3.txt', 'w')

#Traverse file to the right
repetitions = math.ceil(total_lines * 50 / line_length)
 
for line in file:
    line = line.strip('\n')
    out_file.write(line * repetitions + '\n')

out_file.close()
new = open('out3.txt', 'r')

#Loops through the file one line at a time counting the number of trees encountered
for line in new:     
    arr = []

    for char in line:
        arr.append(char)

   # if count_line % 2 != 0: #down 2, checks every other line
   if arr[count_line * 7] == tree: #moves across line the specified amount
         count_trees = count_trees + 1 #counts trees encountered

    if count_line == 321: # stop when end of file is reached
        break

    count_line = count_line + 1 #counts number of lines looped through

#Displays the total trees encountered
print(f"Total trees: {count_trees}")

file.close()
new.close()


        
    

