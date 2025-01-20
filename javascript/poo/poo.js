function telephone(a,b,c,d)  {
    this.nom=a;
    this.prix=b;
    this.stock=c;
    this.ref=d;
    this.verefication=function(){
        if (this.stock>0) {
            return true;
        }else {
            return false;
        }
    }
}
// test 


var t1 = new telephone("smartphone",400,200,"pro1");
var t2 = new telephone("iphone",500,300,"pro2");