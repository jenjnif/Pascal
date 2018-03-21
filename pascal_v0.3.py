# In the first row write 1 and move onto the next row
print "row 1"
row_1 = [1]
print row_1

# In the second row write 1, 1 and move onto the next row
print "row 2"
row_2 = [1, 1]
row_prev = row_2
print row_prev
'''
# In each subsequent row:
# Take the first value from the previous row (n_prev) and write this
print "row 3"
n_prev = 0
row_cur = [row_prev[n_prev]]
print(row_cur)

# Take the first number (n_prev) and the second number (n_prev + 1) from the previous
# row and add them together, write this output
row_cur = row_cur + [row_prev[n_prev] + row_prev[(n_prev+1)]]
print(row_cur)

print"this is here"
print(n_prev)

# Give n_prev the value of n_prev + 1
# Take the next number (n_prev) from the previous row, if this is 1 then write 1 and move 
# onto the next row and return to instruction 3a
n_prev = 1
print n_prev
'''
counter = 1
while counter < 6:
	print"REPEAT"
	counter = counter + 1
	n_prev = 0
	row_cur = [row_prev[n_prev]]
	print(row_cur)
	print "first index"
	print(row_cur)
	row_cur = row_cur + [row_prev[n_prev] + row_prev[(n_prev+1)]]
	print "first two indexes"
	print(row_cur)
	n_prev = 1
	while row_prev[n_prev] > 1: 
		row_cur = row_cur + [row_prev[n_prev] + row_prev[(n_prev+1)]]
		n_prev = n_prev + 1
		print "while"
	else:
		row_cur = row_cur + [row_prev[n_prev]];
		print "triangle so far"
		print(row_cur)
		row_prev = row_cur
else: 
	print "else branch"
	row_prev = row_cur


print(counter)

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

# If the next number (n_prev) is not 1 then add n_prev and the next number (n_prev + 1) 
# together
# Give n_prev the value of n_prev+1 and return to instruction 3d


