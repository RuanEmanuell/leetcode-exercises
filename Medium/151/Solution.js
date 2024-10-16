var reverseWords = function(s) {
    let arr = s.split(" ").reverse()
    let str = ""
    for(var i=0; i<arr.length; i++){
        str += arr[i]
        if(i != arr.length - 1) {
            str += " "
        }
    }
    str = str.replace(/ +(?= )/g,'').trim();
    return str
};