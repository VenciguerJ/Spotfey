
//DOM - Login.html
$fileUpload = document.querySelector("#file-upload");
$switchButton = document.querySelectorAll('.switch-button');
$switchVisibility = document.querySelectorAll('.switch-visibility');
$form = document.querySelectorAll('.default-div');

//DOM - Index.html
$playerButton = document.querySelectorAll('.js-player');
$player = document.querySelector('.music-simple-div');
$closeplayer = document.querySelector('.close-player')

//Events
//login
if($fileUpload){
    $fileUpload.addEventListener('change', updateFileName);
}
window.addEventListener('load', define_hidden);
for (let i = 0; i < $switchButton.length; i++){
    $switchButton[i].addEventListener('click', switch_form);
}

//index
for(let i=0 ; i< $playerButton.length;i++){
    $playerButton[i].addEventListener('click', show_player)
}
$closeplayer.addEventListener('click', function(){
    $player.classList.add('hidden');
})

//functions
function updateFileName(e) {
    var input = e.target;
    var fileName = input.files[0] ? input.files[0].name : '';
    document.getElementById('file-name').textContent = fileName;
}

function define_hidden(){
    if(($switchVisibility.length >= 0) && ($form.length >= 0)){
        $switchVisibility[1].classList.add('hidden')
        $form[1].classList.add('hidden')
    }
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

//funções do player

function show_player(){
    $player.classList.remove('hidden')
}