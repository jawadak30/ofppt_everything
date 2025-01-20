const form = document.querySelector("form");

form.onsubmit = e => {
    e.preventDefault();
};
function validation(){
    let id = document.getElementById('id').value;
    let nom = document.getElementById('nom').value;
    let radio = document.getElementById('radio').value;
    let note = document.getElementById('note').value;
    if (id=="" || nom=="" || radio=="" || note==""){
        alert("remplir les champs"); 
    }
}
function ajouter_note(){
    validation();
    let jawad= document.getElementById('jawad');

    var tr= document.createElement('tr');

    var td_id= document.createElement('td');
    td_id.textContent = document.getElementById('id').value;;
    tr.append(td_id);
    jawad.append(tr);

    var td_nom= document.createElement('td');
    td_nom.textContent = document.getElementById('nom').value;
    tr.appendChild(td_nom);
    jawad.appendChild(tr);

    var td_note= document.createElement('td');
    td_note.textContent = document.getElementById('note').value;
    tr.appendChild(td_note);
    jawad.appendChild(tr);

    var td_radio= document.createElement('td');
    // let vv = document.getElementById('radio').value;
    let cc = form.elements["filiere"].value;
    // console.log(cc);

    td_radio.textContent = cc;
    tr.appendChild(td_radio);
    jawad.appendChild(tr);


    let button = document.createElement('td');
    let bu = document.createElement('button');
    bu.textContent = "supprimer";

    bu.setAttribute("id","supprimmerTV");
    bu.setAttribute("onclick","supprimerDuPanier(this)");
    button.appendChild(bu);
    tr.appendChild(button);
    jawad.appendChild(tr);


    // supprimerDuPanier(e);



       // console.log(td_ra.length);
    // for ( val in td_ra) {
    //     console.log(val);
    //     tr.appendChild(td_radio);
    //     tr.append(val);
    //     // jawad.appendChild(tr);
    // }
        // tr.appendChild(td_radio);
        // el.append(element);
        // jawad.appendChild(el);
}
function supprimerDuPanier(e) {
    e.parentNode.parentNode.remove();
}
supprimerDuPanier(e);