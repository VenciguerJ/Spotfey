(function(){

    
})
function updateFileName(input) {
    var fileName = input.files[0] ? input.files[0].name : '';
    document.getElementById('file-name').textContent = fileName;
}