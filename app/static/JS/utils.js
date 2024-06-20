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
