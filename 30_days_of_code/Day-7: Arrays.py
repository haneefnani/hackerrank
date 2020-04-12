n = int(input())

arr = list(map(int, input().rstrip().split()))
arr.reverse()

for num in arr:
    print(num , end=" ")
