var shuffle = function (nums, n) {
    let result = [];
    let takenNumber = 0;

    for (var i = 0; i < nums.length; i ++) {
        if(i % 2 == 0){
            result.push(nums[takenNumber]); 
            takenNumber++;
        } else {
            result.push(nums[n + i - takenNumber]);
        }
    }

    return result;
};