  def permute(self, nums: List[int]) -> List[List[int]]:
      nums.sort()
      results = []
      self.bt(nums, [], set(), results)
      return results

    
  def bt(self, nums, path, seen, results):
      if len(path) == len(nums):
          results.append(path)
          return

      for i in range(len(nums)):
          if nums[i] in seen:
              continue
          seen.add(nums[i])
          self.bt(nums, path + [nums[i]], seen, results)
          seen.remove(nums[i])
