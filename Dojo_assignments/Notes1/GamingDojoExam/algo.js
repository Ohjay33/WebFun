
//---this is my increment function i used to count the number of times the buttons are pressed---//
var counter = 0;
function increment(){
    counter++;
    console.log(counter);
}


function changeImg() {
    var image = document.getElementById('myImg');
    if (image.src.match("images/stonepunk.png")) {  //if the image is already one image, once clicked change to other image//
        image.src = "images/pixel-ninjas-2.png";
    }
    else {
        image.src = "images/stonepunk.png";
    }
}