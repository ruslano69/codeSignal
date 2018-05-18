function addBorder(picture) {
    var size = picture.length
    var outer = ""
    for(var i = 0; i< size; i++){
        picture[i] = "*" + picture[i] + "*";
    }
    for(var i=0; i<picture[0].length; i++){
        outer+="*";
    }
    
    picture.unshift(outer);
    picture.push(outer);
    
    return picture;
}
