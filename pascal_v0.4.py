# In the first row write 1 and move onto the next row
row_1 = [1]
print row_1

# In the second row write 1, 1 and move onto the next row

row_2 = [1, 1]
previous_row = row_2
print previous_row
'''
# In each subsequent row:
# Take the first value from the previous row (column_number) and write this
print "row 3"
column_number = 0
current_row = [previous_row[column_number]]
print(current_row)

# Take the first number (column_number) and the second number (column_number + 1) from the previous
# row and add them together, write this output
current_row = current_row + [previous_row[column_number] + previous_row[(column_number+1)]]
print(current_row)

print"this is here"
print(column_number)

# Give column_number the value of column_number + 1
# Take the next number (column_number) from the previous row, if this is 1 then write 1 and move 
# onto the next row and return to instruction 3a
column_number = 1
print column_number
'''
row_number = 1
while row_number < 10:
	row_number = row_number + 1
	column_number = 0
	current_row = [previous_row[column_number]]

	#current_row = current_row + [previous_row[column_number] + previous_row[(column_number+1)]]
	#column_number = column_number + 1

	# go until the end of the previous row
	# if the next number is bigger than one or if the next number is 
	# while current_row == [1] or previous_row[column_number] > 1:
	# to make the above row simpler ask if you are at the beginning of the row rather than asking if you have a 1
	while column_number == 0 or previous_row[column_number] > 1:
		current_row = current_row + [previous_row[column_number] + previous_row[(column_number+1)]]
		column_number = column_number + 1
		
	current_row = current_row + [previous_row[column_number]];
		
	print(current_row)
	previous_row = current_row


print(row_number)

'''

n = 1
for n in range(10):
		row(n).append([n+1])

		def repeat(pic_word, n):
    for i in range(n):
        pic_word()

n = 5
pascal = 0
for i in range(1,n):
		pascal = pascal + 1

print pascal

# Store all the rows in a list otherwise you will need one variable per row, 
# and you may as well just type the numbers in ;)


'''

# If the next number (column_number) is not 1 then add column_number and the next number (column_number + 1) 
# together
# Give column_number the value of column_number+1 and return to instruction 3d


