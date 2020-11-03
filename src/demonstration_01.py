"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""
# def two_sum(nums, target): # O(n^2)
#     # Your code here
#     # iterate over the nums indexing with i
#     for i in range(len(nums)):
#         # iterate over the nums indexing with j
#         for j in range(i + 1, len(nums)):
#             # check if nums at the index i + nums at the index of j are equal to target
#             if nums[i] + nums[j] == target:
#                 # return [i, j]
#                 return [i, j]

#     # if we get through the nested loop we can then return 'No two sum found.'
#     return 'No two sum found.'

def two_sum(nums, target): # O(n)
    # create a dictionary to hold our key / value pairs
    my_table = {}
    # iterate over the nums indexing with i
    for i in range(len(nums)): # O(n)
        # give the dictionary a key of nums at the index of i and a value of nums at the index of i
        my_table[nums[i]] = i # O(1)
    # iterate over the nums indexing with i
    for i in range(len(nums)): # O(n)
        # set a compliment to the target minus nums[i]
        compliment = target - nums[i] # O(1)
        # if the compiment is in the dictionary and the value of dictionary at the key of compliment is not equal to i
        if compliment in my_table and my_table[compliment] != i: # O(1)
            # return a list [i, the value of dictionary at the key of compliment]
            return [i, my_table[compliment]] # O(1)

    # if we get through the nested loop we can then return 'No two sum found.'
    return 'No two sum found.'