function evenDigitsOnly(n) {
    n = n.toString().split("");
    return n.every((element) => { return parseInt(element)%2 === 0; });
}
