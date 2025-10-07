class Solution:
    def find_missing_numbers_hashset(self, nums: List[int]) -> List[int]:
        num_set = set(nums)

    return [i for i in range(1, len(nums) + 1) if i not in num_set]


if __name__ == "__main__":

    input_nums = [1, 6, 4, 3, 8]
    print(find_missing_numbers_hashset(input_nums))
