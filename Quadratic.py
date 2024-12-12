import cmath

# Input coefficients
a = 1
b = 5
c = 6

# Calculate the discriminant
d = b**2 - (4 * a * c)

# Calculate the roots
sum1 = (-b - cmath.sqrt(d)) / (2 * a)
sum2 = (-b + cmath.sqrt(d)) / (2 * a)

# Print the results in complex format
print("Both quadratic equations are serially: {} and {}".format(sum1, sum2))
