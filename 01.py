# https://adventofcode.com/2022/day/1

nums = [nums.split("\n") for nums in open("input.txt").read().split("\n\n")]
sums = sorted([sum(map(int, x)) for x in nums], reverse=True)

print(sums[0])
print(sum(sums[0:3]))
