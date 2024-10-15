class Solution {
fun canPlaceFlowers(flowerbed: IntArray, n: Int): Boolean {
    var plantedFlowers = 0

    for (i in flowerbed.indices) {
        if (flowerbed[i] == 0) {
            val isLeftEmpty = (i == 0 || flowerbed[i - 1] == 0)
            val isRightEmpty = (i == flowerbed.size - 1 || flowerbed[i + 1] == 0)

            if (isLeftEmpty && isRightEmpty) {
                flowerbed[i] = 1
                plantedFlowers++
                if (plantedFlowers == n) {
                    return true
                }
            }
        }
    }
    return plantedFlowers >= n
}

}