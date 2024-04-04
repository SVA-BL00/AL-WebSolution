let route = 'Scene1.jpg';
let contenedor = document.getElementById("viewer");
let imagen = document.createElement("img");
let right = document.querySelector('#right');
let left = document.querySelector('#left');
let up = document.querySelector('#up');
let down = document.querySelector('#down');
let maria = document.querySelector('#maria')
imagen.src = "../static/img/" + route;
contenedor.appendChild(imagen);
right.style.opacity = 1;
left.style.opacity = 0;
up.style.opacity = 0;
down.style.opacity = 0;
maria.style.opacity = 0;

function move(str) {
    console.log(str);
    if (route == 'Scene1.jpg' && str == 'right') {
        route = 'Scene2.jpg';
        right.style.opacity = 1;
        left.style.opacity = 0;
        up.style.opacity = 1;
        down.style.opacity = 0;
        maria.style.opacity = 1;
    }
    if (route == 'Scene2.jpg' && str == 'up') {
        route = 'Scene1.jpg';
        right.style.opacity = 1;
        left.style.opacity = 0;
        up.style.opacity = 0;
        down.style.opacity = 0;
        maria.style.opacity = 0;
    }
    imagen.src = "../static/img/" + route;
}

// Example of triggering the move function when a button is clicked
document.getElementById("nextButton").addEventListener("click", function() {
    move('right');
});

