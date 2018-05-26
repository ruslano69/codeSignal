function sumUpNumbers(inputString) {
    var s = inputString.split(/[^0-9]+/);
    var t = s.map(function(n){ return n != ''?parseInt(n):0  });
    return t.reduce(function(a,b){return a + b});
}
