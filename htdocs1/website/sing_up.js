const form = document.querySelector("form");

form.onsubmit = e => {
    e.preventDefault();
};
function validateemail() {
    function valide () {
        let email = document.getElementById('email').value ;
        let validateemail = /^[a-zA-Z0-9+]+@[a-zA-Z]+\.[a-zA-Z]{2,}$/;
        let v=validateemail.test(email);
        if (v === true ){
            return("true");
        }else{
            return("false");
        }
    }
    alert(valide());
    // console.log(valide());
    function verification_code() {
        let password = document.getElementById('password').value;
        if (password.length <9){
            return ("saisir le code sépérieur à 8 charachtère");
        }
        else{
            return("le code est bien");
        }
    }
    // console.log(verification_code());
    alert(verification_code());
}
