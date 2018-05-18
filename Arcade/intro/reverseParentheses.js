function reverseParentheses(s) {
    if(s.includes('(')){
        return reverseParentheses(reverseHelper(s));
    }

    return s;
    
}

// secondary function
function reverseHelper(s){
    var regexp = /\(([^()]*)\)/i;
    var subStr = regexp.exec(s)[1];
    
    subStr = subStr.split("").reverse().join("");
    
    return s.replace(regexp, subStr);
}
