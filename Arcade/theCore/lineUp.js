function lineUp(commands) {
    var temp=commands.split("");
    temp.reverse();
    var sum=0;
    var count=0;
    for(i=0;i<commands.length;i++){
     var letter = temp.pop();
        if(letter=='L'){
         sum=sum-1;
        } else if(letter=='R'){
         sum=sum+1;
        } else if(letter=='A'){
         sum=sum+2;
        }
 
        if(sum%2==0){
         count++;
        }
    }
    return count;
}
