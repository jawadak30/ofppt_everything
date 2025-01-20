let post = document.getElementById('add-post');
let users = document.getElementById('users');
let emails = document.getElementById('emails');
let courses = document.getElementById('courses');
post.addEventListener('click' , function(){
})
users.addEventListener('click' , function(){
    let array = ["id","id","id","id","id"];
    let table = document.createElement('table');
    let thead = document.createElement('thead');
    let tr= document.createElement('tr');
    for (let index = 0; index < 5; index++){
        let th = document.createElement('th');
        th.innerText = array[index];
        tr.appendChild(th);
    }
    table.appendChild(thead);
    thead.appendChild(tr);
    document.body.appendChild(table);
    // // console.log("true");
})
emails.addEventListener('click' , function(){

})
courses.addEventListener('click' , function(){

})