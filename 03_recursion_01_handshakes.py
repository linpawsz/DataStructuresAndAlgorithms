# https://www.geeksforgeeks.org/recursive-functions/
# you could just result the summation n*(n-1)/2
# but no - we have to do recursion - base case and then recursive case
# so how did you come up with the base case?
# and how did you come up with the recursive case?


# n = number of people
def total_handshakes(n):
    if n == 1 or n == 2:    # base case - if there's one or two people - how many shakes?
        return 1
    else:                   # recursive case - count handshakes of rest of the people
        return (n-1) + total_handshakes(n-1)


if __name__ == "__main__":
    print(total_handshakes(int(input())))