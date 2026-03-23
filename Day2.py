# Question: Find the length of the longest substring without repeating characters.

def longestsubstring(s):
    char_map = {} # Stores the last seen index of each character
    left = 0
    max_length = 0

    for right in range len(s):
        # If the character is already in the window, move the left pointer
        if s[right] in char_map:
            # We move left to the index after the last occurrence
            left = max(left, char_map[s[right]] + 1)

        # Update/store the last seen index of the character
        char_map[s[right]] = right

        # Calculate window size: right index - left index + 1
        max_length = max(max_length, right - left + 1)

    return max_length



# SQL: Find employees with highest salary in each department.

# SUBQUERY

SELECT e.department, e.firstName, e.salary

FROM employee e

JOIN (
    SELECT department, MAX(salary) as max_salary

    FROM employee
    GROUP BY department
) m ON e.department = m.department AND e.salary = m.max_salary;



# WINDOWS FUNCTION

SELECT department, firstName, salary
FROM (
    SELECT *,
           DENSE_RANK() OVER (
               PARTITION BY department
               ORDER BY salary DESC
           ) AS rnk
    FROM employee
) t
WHERE rnk = 1;