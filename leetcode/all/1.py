'''
1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
'''
class Solution:
    '''基本的思路，时间复杂度为O(n*n)'''
    def twoSum(self, nums, target):
        for index, val in enumerate(nums):
            temp = target - val
            for i, v in enumerate(nums[index+1:]):
                if v == temp:
                    re = [index, i+index+1]
                    return re
    '''利用字典，时间复杂度为O(n)'''
    def twoSum2(self, nums, target):
        dic = {}
        for index, val in enumerate(nums):
            temp = target - val
            if temp in dic:
                return [index, dic[temp]]
            dic[val] = index
if __name__ == '__main__':
    sln = Solution()
    re = sln.twoSum2([2, 7, 11, 15], 13)
    print(re)
    