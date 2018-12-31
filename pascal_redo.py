first = [1]

if first == [1]:
    print(first)
    first = [first[1], first[1]]
if first != [1]:
    second = first
    length = len(second)
    print(length)
    for number in range(len(second)):
        if number < len(second):
            line = [second[0], second[0+1]+second[1]]

# print 1
# if the line length is more than one:
    # go through each item until the second from last:
        # adding the current number to the next number until the last number
    # if the last item in a line print 1
