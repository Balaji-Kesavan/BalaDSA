def testSum(nums):
    numset = list(set(nums))

    for i in range(1, len(numset)):
        print(numset[i])


# input = [1,3,5,6,2,3]
# output = [4]
# work fine - can be used for revision
def missingnumbers_hashset(nums):
    num_set = set(nums)
    # num_set = [1,3,5,6,2]
    return [i for i in range(1, len(nums) + 1) if i not in num_set]


if __name__ == "__main__":
    input = [1, 4, 2, 3, 4, 5]
    # testSum(input)
    missing_number_input = [1, 4, 5, 7, 2, 3]
    print(missingnumbers_hashset(missing_number_input))
