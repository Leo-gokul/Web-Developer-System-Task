def three_sum(nums):
    nums.sort()  
    triplets = []
    for i in range(len(nums) - 2):
        # Skip duplicate on 1st value
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # Two-pointer approach
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                triplets.append((nums[i], nums[left], nums[right]))
                # Skip duplicate values for 2nd & 3rd value
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return triplets

def main():
    input_str = input("input:")     # input example Input:-1,0,1,2,-1,-4
    try:        # string to int convertion 
        nums = list(map(int, input_str.split(',')))
    except ValueError:
        print("Invalid input")
        return
    result = three_sum(nums)# Find the unique triplets

    print("Output:", end=" ")
    if result:
        # Format triplets as strings and join them with commas
        result_str = ', '.join(str(triplet) for triplet in result)
        print(f"[{result_str}]", end="")
    else:
        print("No triplet", end="")

if __name__ == "__main__":
    main()
