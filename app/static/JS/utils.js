<<<<<<< HEAD
//DOM
$switchButton = document.querySelectorAll('.switch-button');
$switchVisibility = document.querySelectorAll('.switch-visibility');
$form = document.querySelectorAll('.default-div');

//Events
for (let i = 0; i < $switchButton.length; i++) {
    $switchButton[i].addEventListener('click', switch_form);
}
window.addEventListener('load', define_hidden);

//functions

function define_hidden(){
    $switchVisibility[1].classList.add('hidden')
    $form[1].classList.add('hidden')
}

function switch_form(event){
    for (let i = 0; i < 2; i++) {
        if($switchVisibility[i].classList.constains('hidden')){
            
        }
        $form
    }
}
=======
//funções gerais da página
//DOM
$fileUpload = document.querySelector("#file-upload");
$switchButton = document.querySelectorAll('.switch-button');
$switchVisibility = document.querySelectorAll('.switch-visibility');
$form = document.querySelectorAll('.default-div');


//Events
$fileUpload.addEventListener('change', updateFileName);
window.addEventListener('load', define_hidden);
for (let i = 0; i < $switchButton.length; i++) {
    $switchButton[i].addEventListener('click', switch_form);
}

//functions
function updateFileName(e) {
    var input = e.target;
    var fileName = input.files[0] ? input.files[0].name : '';
    document.getElementById('file-name').textContent = fileName;
}

function define_hidden(){
    $switchVisibility[1].classList.add('hidden')
    $form[1].classList.add('hidden')
}

function switch_form(){
    for(let i=0;i<2;i++){
        if(!($switchVisibility[i].classList.contains('hidden'))){
            $switchVisibility[i].classList.add('hidden');
            $form[i].classList.add('hidden');
        }
        else{
            $switchVisibility[i].classList.remove('hidden');
            $form[i].classList.remove('hidden');
            switching = false;
        }
    }
}

>>>>>>> 5b6e02677efb2eb2d84964daff6ebf6d266cef28
