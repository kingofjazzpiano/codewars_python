# https://www.codewars.com/kata/5ae62fcf252e66d44d00008e
# Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ()
# In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained

def expression_matter(a, b, c):
    return sorted([a + b + c, (a + b) * c, a * (b + c), a * b * c])[-1]


print(expression_matter(1, 2, 3))
print(expression_matter(3, 4, 5))
print(expression_matter(1, 1, 1))
