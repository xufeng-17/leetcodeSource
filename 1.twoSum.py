def twoSum(nums,target):
  res = {}
  for i in range(0, len(nums) ):
    if res.get(nums[i]) is not None:
      return [res.get(nums[i]),i]
    else:
      res[target - nums[i]] = i

if __name__ == '__main__':
  nums = [3,2,4]
  target = 6
  print(twoSum(nums,target)