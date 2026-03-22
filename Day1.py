# Question: 
# Given a sorted array of integers and a target,
# return indices of two numbers that add up to the 
# target using constant extra space.

# The Logic
# Place one pointer at the start (left) and one at the end (right).
# Calculate the sum of the elements at these two indices.
# If the sum equals the target, you've found the indices.
# If the sum is less than the target, move the left pointer forward (to increase the sum).
# If the sum is greater than the target, move the right pointer backward (to decrease the sum).

def two_sum(numbers, target):
    left , right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None # if no pair is found
