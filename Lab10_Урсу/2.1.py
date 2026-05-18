def flexible_average(*args):
    nums = [x for x in args if isinstance(x, (int, float))]

    if len(nums) == 0:
        return None

    return sum(nums) / len(nums)
print(flexible_average(10, 20, 30))