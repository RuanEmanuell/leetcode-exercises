var longestCommonPrefix = function(strs) {
    let longestPrefix = strs[0].split("")

    for(let i = 1; i < strs.length; i++){
        let newLongestPrefix = []

        for(let j = 0; j < strs[i].length; j++){
            if(longestPrefix[j] !== strs[i][j]){
                break;
            }
            newLongestPrefix.push(strs[i][j]);
        }

        if(longestPrefix.length >= newLongestPrefix.length){
            longestPrefix = newLongestPrefix;
        }
    }

    return longestPrefix.join("")
};