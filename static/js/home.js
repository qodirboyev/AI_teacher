'use strice'


let auth_section = document.getElementById('auth_section');
auth_section.style.display = 'none';

let icon_i=document.getElementById('icon_i');
function menu(){
    icon_i.style.display = 'none';
    auth_section.style.display = "block"
}


function back_menu(){
    icon_i.style.display = 'block';
    auth_section.style.display = "none"
}