function sortByHeight(a) {
    var array2 = a;
    array2 = array2.filter((element)=>{
        if(element != -1){
            return element;
        }
    }).sort((a,b)=>{
        return a-b;
    });
    
    var index = 0;
    for(var i = 0; i< a.length; i++){
        if(a[i] != -1){
            a[i] = array2[index];
            index++;
        }
    }
    return a;
}
