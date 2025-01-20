var telephone = {
    marque:"smartphone",
    prix:1550,
    stock:12,
    ref:"smartphone2022",
        verefication: function() {
            if (this.stock>0){
                return true;
            }else {
                return false;
            }
        }
}
console.log(telephone.marque);
console.log(telephone.verefication());