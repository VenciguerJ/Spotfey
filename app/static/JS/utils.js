
var $submitRegister = document.querySelector('#js-confirm-register');

$submitRegister.addEventListener('click', uploadToFlask)

function uploadToFlask(){
    this.preventDefault();

    $Registerform = document.querySelector('#js-register-form');
    
    console.log($Registerform.Length);
}