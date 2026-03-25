# Question: Return k most frequent elements.

from collections import Counter
import heapq

def topKFrequent(nums, k):
    counts = Counter(nums)
    top_k = heapq.nlargest(k, counts.keys(), key=counts.get)
    return top_k


# SQL: Find numbers appearing at least three times consecutively.

SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
           LEAD(num, 1) OVER (ORDER BY id) AS next1,
           LEAD(num, 2) OVER (ORDER BY id) AS next2
    FROM Logs
) temp
WHERE num = next1 AND num = next2;