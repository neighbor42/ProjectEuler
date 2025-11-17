# Multiples of 3 or 5
# Find sum of all the multiples of 3 or 5 below 1000


total = 0
n = 10
# 1. Loop
# for i in range(1, n):
#     if i % 3 == 0 or i%5==0:
#         print(i)
#         total += i

# print(total)

# 2. brevity
def sum_multiples(limit):
    return sum(i for i in range(1, limit) if i%3==0 or i%5==0)

print(sum_multiples(10))
print(sum_multiples(1000))
