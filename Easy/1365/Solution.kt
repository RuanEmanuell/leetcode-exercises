class Solution {
    fun smallerNumbersThanCurrent(nums: IntArray): IntArray {
        var minorNumberCountArray = IntArray(nums.size)
        for(i in nums.indices){
           var minorNumberCount = 0
           for(j in nums.indices){
               if(nums[j] < nums[i]) {
                   minorNumberCount++
               }
           }
           minorNumberCountArray[i] = minorNumberCount
        }
        return minorNumberCountArray
    }
}