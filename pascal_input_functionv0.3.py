def pascal():
	create_triangle = input("How many rows would you like to print? Enter a number from 1 to 50.")
	while create_triangle < 1 or create_triangle > 50:
		create_triangle = input("How many rows would you like to print? Enter a number from 1 to 50.")
		



n = 1 # this creates a variable n for the first index
row_number = 1 # this tells you what row to start on
while row_number < 10: # tells you to keep in the loop while the row number is less than 10
	column_number = 0
	while row_number < 3: # while the row numnber is less than 2 stay in this loop
		if row_number == 1:
			current_row = [n] # the current row value is n (which in this example is 1)
			print current_row
			row_number = 1+1
			print row_number
			print "while branch"
		else:
			print "else branch"
			previous_row = current_row # the previous_row takes the value of current_row, which is 1
			current_row = [n, n]
			previous_row = current_row
			row_number = row_number + 1
			print current_row
			print "row number"
			print row_number
	
	current_row = [previous_row[column_number]]

	while column_number == 0 or previous_row[column_number] > n:
		current_row = current_row + [previous_row[column_number] + previous_row[(column_number+1)]]
		column_number = column_number + 1
		
	current_row = current_row + [previous_row[column_number]];
		
	print(current_row)
	previous_row = current_row
	row_number = row_number + 1


print(row_number)

pascal()
