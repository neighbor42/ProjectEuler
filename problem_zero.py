# Registration problem
# Calculate the first N odd square numbers

# 1. using range steps
# total = 0
# k = 5
# for i in range(1, k+1, 2):
#     total += (i**2)

# print(total)


# 2. Filtering(modulo)
# total = 0
# k = 5
# for i in range(1, k+1):
#     if i % 2 != 0:
#         total += (i**2)

# print(total)

# 3. function
# def sum_odd_squares(limit):
#     total = 0
#     for i in range(1, limit+1, 2):
#         total += (i**2)
#     return total

# answer1 = sum_odd_squares(5)
# answer2 = sum_odd_squares(10)
# print(answer1)
# print(answer2)

# 4. Pythonic(Brevity)
def sum_odd_squares(limit):
    return sum(i**2 for i in range(1, limit+1, 2))

answer = sum_odd_squares(420000)
print(answer)


"""
- Exponentiation: **
- Modulo: %
    - check for even/odd numbers
    - n % 2 == 0(even)
- Range
    - range(1, n+1, step)
- sum()
    - to replace simple loops for brevity
"""