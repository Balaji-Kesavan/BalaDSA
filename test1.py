# input_nums = [5,1,6,8,4]
# output_nums  = [2,3,7]
def find_missing_numbers(nums):
    return [i for i in range(1, max(nums) + 1) if i not in nums]


if __name__ == "__main__":
    input_nums = [5, 1, 6, 8, 4]
    print(find_missing_numbers(input_nums))
