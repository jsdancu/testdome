def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum

    Error: Duplicate numbers with and without solutions: Correct answer
            Performance test with a large list of numbers: Time limit exceeded
    """
    numbers_dict={}  
    for i, x in enumerate(numbers):
        if x in numbers_dict.keys():
            if 2*x==target_sum:
                return (i, numbers_dict[x])
        else:
            numbers_dict[x]=i

    for i, x in enumerate(numbers):
        y=target_sum-x
        if y in numbers_dict.keys():
            return (i, numbers_dict[y])
        
    return None

def find_two_sum_dummy(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum

    Error: Performance test with a large list of numbers: Time limit exceeded
    """
    i=0
    n=len(numbers)-1
    while i<n:
        j=i+1
        while j<n:
            if numbers[i]+numbers[j]==target_sum:
                return (i, j)
            j+=1
        i+=1
        
    return None

def find_two_sum_chatgpt(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    num_dict = {}
    for i, num in enumerate(numbers):
        complement = target_sum - num
        if complement in num_dict:
            return (num_dict[complement], i)
        num_dict[num] = i
    return None

if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9, 5], 10))