# https://www.geeksforgeeks.org/next-greater-element/

arr = [4,3,8,1,45,13,24]

sorted_arr = sorted(arr)
last = max(sorted_arr)

# Won't be using stack for this!
for i in range(len(sorted_arr)):
    if sorted_arr[i] == last:
        print("next greater element of: ", last, -1)
    else:
        print("next greater element of: ", sorted_arr[i], sorted_arr[i+1])
