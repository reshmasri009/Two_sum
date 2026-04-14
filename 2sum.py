def two_sum(nums, target):
    nums.sort()  
    
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return nums[left], nums[right]
        
        elif current_sum < target:
            left += 1
        
        else:
            right -= 1
    
    return None



nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

result = two_sum(nums, target)

if result:
    print("Pair found:", result)
else:
    print("No pair found")