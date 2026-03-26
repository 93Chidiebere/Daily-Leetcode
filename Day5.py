# Question: Return array where each element equals product of others.

def productExceptSelf(nums):
    n = len(nums)
    # 1. Initialize result array
    result = [1] * n
    
    # 2. Left Pass: Calculate prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
        
    # 3. Right Pass: Multiply by suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
        
    return result

# Example: [1, 2, 3, 4] -> [24, 12, 8, 6]


# SQL: Employees Earning More Than Their Managers

SELECT 
    e.name AS Employee
FROM 
    Employee AS e
JOIN 
    Employee AS m ON e.managerId = m.id
WHERE 
    e.salary > m.salary;

