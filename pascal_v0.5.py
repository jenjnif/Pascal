# In the first row write 1 and move onto the next row
print "row 1"
row_1 = [1]
print row_1

# In the second row write 1, 1 and move onto the next row
print "row 2"
row_2 = [1, 1]
row_prev = row_2
print row_prev

counter = 1 # this was changed to reflect what it actually was, a row number
while counter < 6:
	counter = counter + 1
	n_prev = 0 # 
	row_cur = [row_prev[n_prev]]
	row_cur = row_cur + [row_prev[n_prev] + row_prev[(n_prev+1)]]
	n_prev = 1
	while row_prev[n_prev] > 1: 
		row_cur = row_cur + [row_prev[n_prev] + row_prev[(n_prev+1)]]
		n_prev = n_prev + 1
	else:
		row_cur = row_cur + [row_prev[n_prev]];
		print(row_cur) # marker
		row_prev = row_cur
else: 
	print "else branch" # marker - shows if it went into the else branch
	row_prev = row_cur


print(counter)
