row_1 = [1]
print row_1
row_2 = [1, 1]
previous_row = row_2
print previous_row

row_number = 1
while row_number < 10:
	row_number = row_number + 1
	column_number = 0
	current_row = [previous_row[column_number]]

	while column_number == 0 or previous_row[column_number] > 1:
		current_row = current_row + [previous_row[column_number] + previous_row[(column_number+1)]]
		column_number = column_number + 1
		
	current_row = current_row + [previous_row[column_number]];
		
	print(current_row)
	previous_row = current_row


print(row_number)
