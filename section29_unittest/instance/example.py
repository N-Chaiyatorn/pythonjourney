
class MinMaxFinder():
    def minValue(self, nums):
        left_i = 0
        right_i = len(nums) - 1
        seperated_i = (left_i + right_i) // 2
        minimum_value = nums[seperated_i]

        while left_i != right_i:
            if nums[left_i] < nums[seperated_i]:
                minimum_value = min(nums[left_i], minimum_value)
                left_i = seperated_i
            else:
                minimum_value =  min(nums[right_i], nums[seperated_i], minimum_value)
                right_i = seperated_i
                
            seperated_i = (left_i + right_i) // 2

        return minimum_value
    
    def maxValue(self, nums):
        left_i = 0
        right_i = len(nums) - 1
        seperated_i = (left_i + right_i) // 2
        max_value = nums[seperated_i]

        while left_i != seperated_i:
            print(seperated_i)
            if nums[seperated_i] < nums[right_i]:
                max_value = max(max_value, nums[right_i])
                right_i = seperated_i
            else:
                max_value = max(max_value, nums[seperated_i], nums[left_i])
                left_i = seperated_i

            seperated_i = (left_i + right_i) // 2

        return max(max_value, nums[right_i], nums[left_i])
    
s = MinMaxFinder()

nums = input("Type nums list in format x,x,x,x: ").split(",")
nums = [int(n) for n in nums]

print(f"""Find min and max value of  {nums}
          min value is {s.minValue(nums)}
          max value is {s.maxValue(nums)}
       """)


class MultiplyExceptor():
    def multiplyExceptSelf(self, nums):
        multiplyed_nums = []
        total_mul = 1

        for n in nums:
            multiplyed_nums.append(total_mul)
            total_mul *= n

        total_mul = 1

        for i in range(len(nums) - 1,-1,-1):
            multiplyed_nums[i] *= total_mul
            total_mul *= nums[i]

        return multiplyed_nums

s = MultiplyExceptor()
print(s.multiplyExceptSelf([1,-2,3,4]))