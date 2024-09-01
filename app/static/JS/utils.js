                        
//DOM - Login.html  
$fileUpload = document.querySelector("#file-upload");
$imageMusicUpload = document.querySelector("#image-music")
$switchButton = document.querySelectorAll('.switch-button');
$switchVisibility = document.querySelectorAll('.switch-visibility');
$form = document.querySelectorAll('.default-div');

//DOM - Index.html
$showPlayer = document.querySelectorAll('.js-player');
$playerDiv = document.querySelector('.music-simple-div');
$closeplayer = document.querySelector('.close-player');
$player = document.querySelectorAll('.js-start-stop');

// DOM menu
$body = document.querySelector('body')
$menu = document.querySelector('.default-menu');
$menuButton = document.querySelector('.default-menu i');
$menuCard = document.querySelectorAll('.menu-card')
$menuCardText = document.querySelectorAll('.menu-text-card')

//Events
//login
if($imageMusicUpload){
    $imageMusicUpload.addEventListener('change', updateFileName);
}
if($fileUpload){
    $fileUpload.addEventListener('change', updateFileName);
}
window.addEventListener('load', define_hidden);
for (let i = 0; i < $switchButton.length; i++){
    $switchButton[i].addEventListener('click', switch_form);
}

//index
for(let i=0 ; i< $showPlayer.length;i++){
    $showPlayer[i].addEventListener('click', show_player)
}

if($closeplayer){
    $closeplayer.addEventListener('click', function(){
        $playerDiv.classList.add('hidden');
    });
}

for(let i=0;i<$player.length;i++){
    $player[i].addEventListener('click', play_pause)
}

//menu

if($menuButton){
    $menuButton.addEventListener('click', showMenu)
}
if($menu){
    for(var i=0; i< $menuCard.length;i++){
        $menuCard[i].addEventListener('click', menu_redirect);
    } 
}

//functions
function updateFileName(e) {
    var input = e.target;
    var fileName = input.files[0] ? input.files[0].name : '';

    
    if(input == $fileUpload){
        document.getElementById('file-name').textContent = fileName;
    }
    if(input == $imageMusicUpload){
        document.getElementById('image-name').textContent = fileName
    }
}

function define_hidden(){
    if(($switchVisibility.length > 0) && ($form.length > 0)){
        $switchVisibility[1].classList.add('hidden');
        $form[1].classList.add('hidden');
    }

    if($player.length > 0 && $player){
        $player[0].classList.add('hidden');
    }

    if($menuCard.length > 0){
        $menu.classList.add('menu-hidden');
        for(let i=0;i<$menuCard.length; i++){
            // $menuCard[i].classList.add('menu-hidden');
            $menuCardText[i].classList.add('hidden');
        }    
    }
}

function play_pause(){
    for(let i=0;i<$player.length;i++){
        if(!($player[i].classList.contains('hidden'))){
            $player[i].classList.add('hidden');
        }
        else{
            $player[i].classList.remove('hidden');
        }
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

// Funçoes do menu
function showMenu(){

    $menu.classList.contains('menu-hidden') ? $menu.classList.remove('menu-hidden') : $menu.classList.add('menu-hidden');
    
    for(let i=0;i<$menuCard.length;i++){
        if($menuCardText[i].classList.contains('hidden')){
            setTimeout(function(){
                $menuCardText[i].classList.remove('hidden')
            }, 500);
        }
        else{
            $menuCardText[i].classList.add('hidden')
        }
    }
}

function menu_redirect(e){
    const classPrefix = 'js-redirect-';
    console.log(e.target.classList.contains(classPrefix+'register'))
}

//funções do player

function show_player(){
    $playerDiv.classList.remove('hidden')
}