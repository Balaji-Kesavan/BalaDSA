def runningSum(nums):
    result = [nums[0]]

    for i in range(1, len(nums)):
        result.append(result[i - 1] + nums[i])

    return result


if __name__ == "__main__":
    # Example usage:
    input_nums = [1, 2, 3, 4]
    output_sum = runningSum(input_nums)
    print(f"The running sum of {input_nums} is {output_sum}")

# Answer :
# The running sum of [1, 2, 3, 4] is [1, 3, 6, 10]
#
# test_sum
