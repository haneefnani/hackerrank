# stu, marks = int(raw_input()), raw_input().split().index("MARKS")
# print (sum([float(raw_input().split()[marks]) for _ in range(stu)]))/ stu

from collections import namedtuple
n, student = int(input()), namedtuple('student', ",".join(list(map(str, input().strip().split()))))
print(sum([float(s.MARKS) for s in [student(*input().strip().split()) for _ in range(n)]]) / n)

