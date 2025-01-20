let a=parseInt(prompt("write nombre of numbers: "));
let arr=[];

for (let i=0;i<a;i++) {
    let b=parseInt(prompt("saisir le nombre: "));
    arr.push(b);
}
alert(arr);
let c=parseInt(prompt("saisir le nombre pour l'afficher est-ce qu'il existe: "));
for (val in arr) {
    if (c in arr) {
        console.log("existe");
    }else {
        console.log("n'existes pas ");
    }
}