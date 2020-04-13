class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        print(f'nums:{nums}')
        length = len(nums)
        for i in range(length - 2):
            if nums[i]>0: break
            if i > 0 and nums[i] == nums[i - 1]: continue

            l, r = i + 1, length - 1  #[2]
            print(f'i:{i} left :{l},right:{r}')
            while l < r:
              print(f'left :{l},right:{r}')
              total = nums[i] + nums[l] + nums[r]
              print(f'total :{total} and nums[i] : {nums[i]} + nums[l] : {nums[l]} + nums[r] : {nums[r]}' )
              if total < 0:
                l+=1
                print(f'left :{l},right:{r}')
              elif total>0:
                r -= 1
                print(f'left :{l},right:{r}')
              else:
                if [nums[i], nums[l], nums[r]]  not in res:
                  res.append([nums[i], nums[l], nums[r]])
                l+=1
                r -= 1
                print(f'left :{l},right:{r}')
                # print(f'res :{res}')
              # while l < r and nums[l] == nums[l + 1] :
              #   l += 1
              # while l <r and nums[r]==nums[r-1]:
              #   r -= 1

        return res




if __name__ == '__main__':
  problem = Solution()
  nums = [-5, -5, -4, -4, -4, -2, -2, -2, 0, 0, 0, 1, 1, 3, 4, 4]
  print(problem.threeSum(nums))

