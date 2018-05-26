function fileNaming(names) {
    let s = new Set();
    let nm = names;
    for(let i = 0;i < names.length;i++){
        let j = 0;
        let temp = names[i];
        if(!s.has(temp))
            s.add(temp);
        else
            while(true){
                j++;
                if(!s.has(names[i] + "("+ j.toString() + ")")){
                    temp = names[i] + "("+ j.toString() + ")";
                    s.add(temp);
                    break;
                }
                else
                    temp = names[i] + "("+ j.toString() + ")";
            }
        nm[i] = temp;
    }
    return nm;
}