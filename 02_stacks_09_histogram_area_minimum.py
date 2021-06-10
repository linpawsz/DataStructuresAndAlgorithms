# https://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-set-1/
# Segment tree - need to figure this out first
# you could solve it iteratively but it takes a ton of time O(n^2)
# Messed up - you can't even do iteratively
# - can't even use combinations and figure out what it returns and how to deal with it
# - not using your brain completely
# - come back later

# h = [6, 2, 5, 4, 5, 1, 6]
#      |
#
#
#


from itertools import combinations


def maxhistogramArea(heights):
    area = []
    max_length = len(heights)
    selections = []

    for i in range(1, max_length):
        selection = [j for j in combinations(heights, i)]
        selections.append(selection)

    for j in selections:
        print(j)

    # return max(area)


if __name__ == "__main__":
    h = [6, 2, 5, 4, 5, 1, 6]
    print(maxhistogramArea(h))
