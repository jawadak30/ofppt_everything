function correct(){
    // var a=document.getElementById('text');
    // var b="javascript";
    var a=prompt("write javascript: ");
    let c=[];
    for (val in a){
        c=a.split("|");
        alert(c);
    }
    // c=a.split("|");
    // alert(c);
    // if (a==b.toLowerCase() || a==b.toUpperCase() ){
    //     alert("correct");
    // }else {
    //     alert("n'est pas correct");
    // }
}
correct();