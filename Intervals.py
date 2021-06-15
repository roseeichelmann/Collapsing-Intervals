import sys

#  File: Intervals.py

#  Description: The aim in this assignment is take a set of intervals and collapse all the overlapping intervals and print the smallest set of non-intersecting intervals in ascending order of the lower end of the interval and then print the intervals in increasing order of the size of the interval. 

#  Student Name: Rose Eichelmann

#  Student UT EID: ree585

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 6-14-21

#  Date Last Modified: 6-14-21

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples(interval_list):
    interval_list.sort()
    i = 0
    while(i < len(interval_list)):
        first_end = interval_list[i][1]
        last_iteration = i == len(interval_list) - 1
        if not last_iteration:
            second_start = interval_list[i + 1][0]
            while second_start < first_end:
                # merge: delete both tuples and add a new one
                interval_list.append((interval_list[i][0], \
                                  max(interval_list[i][1], interval_list[i + 1][1])))
                interval_list.pop(i)
                interval_list.pop(i)
                interval_list.sort()
                last_iteration = i == len(interval_list) - 1
                if last_iteration:
                    break
                first_end = interval_list[i][1]
                second_start = interval_list[i + 1][0]
            i += 1
    interval_list.sort()
    return interval_list


# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
# the interval
# if two intervals have the size then it will sort by the
# lower number in the interval
def sort_by_interval_size(tuples_list):
    return sorted(tuples_list, key = lambda x: x[1] - x[0])


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
    assert merge_tuples([(1, 2)]) == [(1, 2)]
    # write your own test cases
    assert sort_by_interval_size([(1, 3), (4, 5)]) == [(4, 5), (1, 3)]
    # write your own test cases
    return "all test cases passed"


def create_tuples(interval_file):
    '''
    creates a list of tuples given a file containing N intervals
    params:
      interval_file(String): file path
    returns:
      list of tuples    '''
    # read the input file
    interval_list = []
    for i in range(1, len(interval_file)):
        line = interval_file[i]
        first_num, second_num = line.split(" ")
        pair = (int(first_num), int(second_num.strip()))
        interval_list.append(pair)
    return interval_list


def main():
    # open file intervals.in and read the data and create a list of tuples
    interval_file = sys.stdin.readlines()
    interval_list = create_tuples(interval_file)
    # merge the list of tuples
    tuples_list = merge_tuples(interval_list)
    print(tuples_list)
    # sort the list of tuples according to the size of the interval
    print(sort_by_interval_size(tuples_list))
    test_cases()


if __name__ == "__main__":
    main()
