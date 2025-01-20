let t=[];
let n=parseInt(prompt("write number of numbers: "));
for (var i=0;i<n;i++){
    let v = parseInt(prompt("write number: "));
    t.push(v);
}
alert(t);
var plusGrand = Math.max(...t);
var plusPetit = Math.min(...t);
alert(plusGrand);
alert(plusPetit);