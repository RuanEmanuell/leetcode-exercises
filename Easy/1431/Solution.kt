class Solution {
fun kidsWithCandies(candies: IntArray, extraCandies: Int): List<Boolean> {
        var biggest = 0
        var listResults : ArrayList<Boolean> = ArrayList<Boolean>()
        
        for(i in candies.indices){
            if(candies[i] >= biggest) {
                biggest = candies[i]
            }
        }
        
        for(i in candies.indices){
            if((candies[i] + extraCandies) >= biggest) {
                listResults.add(true)
            } else {
                listResults.add(false)
            }
        }
        return listResults
    }
}