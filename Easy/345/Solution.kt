class Solution {
    fun reverseVowels(s: String): String {
    var vowList = CharArray(s.length)
    var fullStringList = CharArray(s.length)

    var possibleVowels: CharArray = "aeiouAEIOU".toCharArray()

    for (i in s.indices) {
        if (s[i] in possibleVowels) {
        vowList[i] = s[i]
        fullStringList[i] = '_'
        } else {
        fullStringList[i] = s[i]
        }
    }

    var reversedVowList = vowList.toList().reversed().toMutableList()

    var reversedVowString = reversedVowList.joinToString("").replace("\u0000", "")

    reversedVowList = reversedVowString.toMutableList()

    for (i in s.indices) {
        if (fullStringList[i] == '_') {
        fullStringList[i] = reversedVowList.get(0)
        reversedVowList.removeAt(0)
        }
    }


    return String(fullStringList)
    }
}