'''
Objective
In this challenge, we go further with Poisson distributions. We recommend reviewing the previous challenge's Tutorial before attempting this problem.

Task
The manager of a industrial plant is planning to buy a machine of either type  or type . For each day’s operation:

The number of repairs, , that machine  needs is a Poisson random variable with mean . The daily cost of operating  is .
The number of repairs, , that machine  needs is a Poisson random variable with mean . The daily cost of operating  is .
Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.

Input Format

A single line comprised of  space-separated values denoting the respective means for  and :

0.88 1.55
If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

There are two lines of output. Your answers must be rounded to a scale of  decimal places (i.e.,  format):

On the first line, print the expected daily cost of machine .
On the second line, print the expected daily cost of machine .
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

means = input()
means = means.split(' ')
mean_a, mean_b = float(means[0]), float(means[1])

def poisson(k, lam):
    return (math.pow(lam, k) * math.pow(math.e, -1 * lam)) / math.factorial(k)

cost_a = lambda x: 160 + 40 * (x ** 2)
cost_b = lambda y: 128 + 40 * (y ** 2)

expected_a = sum([cost_a(x) * poisson(x, mean_a) for x in range(0, 10+1)])
expected_b = sum([cost_b(y) * poisson(y, mean_b) for y in range(0, 10+1)])

print(round(expected_a, 3))
print(round(expected_b, 3))