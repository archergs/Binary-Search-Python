# split list
def split_list(lst):
    # divide the number of elements by 2 to get the middle index
    middle_index = len(lst) // 2

    # return the first and second halves
    return lst[:middle_index], lst[middle_index:]

# get list size from user
listSize = int(input("Enter list size (1-...): "))

# create list of user defined length
numList = list(range(listSize))

# get number input from user
num = int(input("Enter a number: "))

while True:
    # split the current number list in two
    first_half, second_half = split_list(numList)

    # if the number of elements is equal to 1, we have an answer
    if len(numList) == 1:
        # if element at 0 is equal to the input number, then it is in the list
        if numList[0] == num:
            print("The number " + str(num) + " is in the list :)")
            break
        # the element at 0 wasnt't equal to the input, so it wasn't in the list
        else:
            print("The number " + str(num) + " is not in the list :(")
            break

    if num > first_half[-1]:
        # num is greater than last element in first half,
        # so it is either in the second half or isn't in the list
        numList = second_half
        print("List Length: " + str(len(numList)))
    else:
        # num is less than or equal to the final element in the
        # first half, so it's either in that half or isn't in the 
        # list
        numList = first_half
        print("List Length: " + str(len(numList)))

