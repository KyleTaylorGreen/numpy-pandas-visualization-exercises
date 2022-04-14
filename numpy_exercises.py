import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1) How many negative numbers are there?
print(f"Negative numbers: {len(a[a<0])}") 
# 4 neg numbers


# 2) How many positive numbers are there?
print(f"Positive numbers: {len(a[a>0])}") 
# 5 pos numbers


# 3) How many even positive numbers are there? 
positive = a[(a > 0) & (a % 2 == 0)]
print(f"Even Positive numbers: {len(positive)}") 
# 3 pos even numbers


# 4) If you were to add 3 to each data point, how many positive numbers would there be?
added_three = a + 3
print(f"Positive numbers after adding 3: {len(added_three[added_three > 0])}") 
# 10 pos numbers


# 5) If you squared each number, what would the new mean and standard deviation be?
squared = a ** 2
print(f"New mean: {squared.mean()}   New Std Dev: {squared.std()}")


# 6) A common statistical operation on a dataset is centering. This means to adjust the data
#  such that the mean of the data is 0. This is done by subtracting the mean from each data 
#  point. Center the data set. See this link for more on centering.

centered = a.mean()
centered = a - centered
print(centered)  # centered array
print(centered.sum()/len(centered)) # 0.0

# 7) Calculate the z-score for each data point.
# (smp - mean(smp)) / std(smp)

our_mean = a.mean()
our_std = a.std()
z_score = (a - our_mean)/our_std
print(z_score)

# 8)******************************************************************************************** 

# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a = sum(a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = max(a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = sum(a)/len(a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

product_of_a = 1
for num in a:
    product_of_a *= num

print(product_of_a)

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = [n ** 2 for n in a]
print(squares_of_a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = [n for n in a if n % 2 != 0]
print(odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = [n for n in a if n % 2 == 0]
print(evens_in_a)


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

b = np.array(b)

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**

# original
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
# print(sum_of_b)

# refactored
sum_of_b_numpy = b.sum()
print(sum_of_b_numpy)


# Exercise 2 - refactor the following to use numpy. 
# original
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

# refactored
min_of_b_numpy = b.min()
print(min_of_b_numpy)

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
# original
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

# refactored
max_of_b_numpy = b.max()
print(max_of_b_numpy)


# Exercise 4 - refactor the following using numpy to find the mean of b
# original
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

# refactored
mean_of_b_numpy = b.mean()


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# original
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

# refactored
product_of_b_numpy = b.prod()
print(product_of_b_numpy)
print()

# Exercise 6 - refactor the following to use numpy to find the list of squares 
# original
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

# refactored
squares_of_b_numpy = b ** 2
print(squares_of_b_numpy)
print()


# Exercise 7 - refactor using numpy to determine the odds_in_b
# original
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

# refactored
odds_in_b_numpy = b[b% 2 != 0]
print(odds_in_b_numpy)
print()


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
# original
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

# refactored
evens_in_b_numpy = b[b % 2 == 0]
print(evens_in_b_numpy)
print()


# Exercise 9 - print out the shape of the array b.
print(b.shape) # 2 rows, 3 columns


# Exercise 10 - transpose the array b.
print("\nArray b transposed: ")
print(b.transpose())

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
print("\nArray b as single list of 6 numbers: ")
print(b.reshape(1, 6))


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

print("\nArray b as 6 lists of 1 number: ")
print(b.reshape(6,1))

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c = np.array(c)
print('stats for array c:')
print(f"min: {c.min()}, max: {c.max()}, sum: {c.sum()}, product: {c.prod()}")

# Exercise 2 - Determine the standard deviation of c.
print(f"std dev of c: {c.std()}")


# Exercise 3 - Determine the variance of c.

print(f"Variance of c: {c.var()}")

# Exercise 4 - Print out the shape of the array c

print(f"Shape of array c: {c.shape}")

# Exercise 5 - Transpose c and print out transposed result.
print("c transposed: ")
print(c.transpose())

# Exercise 6 - Get the dot product of the array c with c. 

print(f"Dot product of c * c:\n {np.dot(c,c)}")

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
sum_of_product = (c * c.transpose()).sum()
print(f"The sum of c * c transposed: {sum_of_product}")

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

prod_of_product = (c * c.transpose()).prod()
print(f"The product of c * c transposed: {prod_of_product}")

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)

# Exercise 1 - Find the sine of all the numbers in d

sine_of_d = np.sin(d)
print(f"\nSin values for d: {sine_of_d}")

# Exercise 2 - Find the cosine of all the numbers in d
cosine_of_d = np.cos(d)
print(f"\ncosine values of d: {cosine_of_d}")


# Exercise 3 - Find the tangent of all the numbers in d
tangent_of_d = np.tan(d)
print(f"\nTangent values of d: {tangent_of_d}")


# Exercise 4 - Find all the negative numbers in d
print(f"\nNegative numbers in d: ")
print(d[d<0])


# Exercise 5 - Find all the positive numbers in d
print(f"\npositive numbers of d: ")
print(d[d>0])


# Exercise 6 - Return an array of only the unique numbers in d.
print(f"\nUnique numbers in d:")
print(np.unique(d))


# Exercise 7 - Determine how many unique numbers there are in d.
print(f"\nAmount of Unique # in d:")
print(len(np.unique(d)))


# Exercise 8 - Print out the shape of d.
print(f"\nShape of array d: {d.shape}")

# Exercise 9 - Transpose and then print out the shape of d.
print(f"\nShape of d transposed: {d.transpose().shape}")

# Exercise 10 - Reshape d into an array of 9 x 2
print(f"\nd reshaped in 9 x 2: \n{d.reshape(9,2)}")
