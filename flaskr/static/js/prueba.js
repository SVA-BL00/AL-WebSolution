let route = 'Scene1.jpg';
let contenedor = document.getElementById("viewer");
let imagen = document.createElement("img");
let right = document.querySelector('#right');
let left = document.querySelector('#left');
let up = document.querySelector('#up');
let down = document.querySelector('#down');
let maria = document.querySelector('#maria')

// Set initial image source
imagen.src = "../static/img/" + route;
contenedor.appendChild(imagen);

// Set initial button opacities
right.style.opacity = 1;
left.style.opacity = 1;
up.style.opacity = 0;
down.style.opacity = 0;
maria.style.opacity = 0;

// Function to handle movements
function move(str) {
    console.log(str);
    if (route == 'Scene1.jpg' && str == 'right') {
        route = 'Scene2.jpg';
        right.style.opacity = 1;
        left.style.opacity = 0;
        up.style.opacity = 0;
        down.style.opacity = 0;
        maria.style.opacity = 1;
    } else if (route == 'Scene1.jpg' && str == 'left') {
        route = 'Scene3.jpg';
        right.style.opacity = 1;
        left.style.opacity = 0;
        up.style.opacity = 0;
        down.style.opacity = 0;
        maria.style.opacity = 0;
    } else if (route == 'Scene2.jpg' && str == 'right') {
        route = 'Scene1.jpg';
        right.style.opacity = 1;
        left.style.opacity = 0;
        up.style.opacity = 0;
        down.style.opacity = 0;
        maria.style.opacity = 0;
    } else if (route == 'Scene3.jpg' && str == 'right') {
        route = 'Scene4.jpg';
        right.style.opacity = 1;
        left.style.opacity = 0;
        up.style.opacity = 0;
        down.style.opacity = 0;
        maria.style.opacity = 0;
    } else if (route == 'Scene3.jpg' && str == 'down') {
        route = 'Scene1.jpg';
        right.style.opacity = 1;
        left.style.opacity = 0;
        up.style.opacity = 0;
        down.style.opacity = 0;
        maria.style.opacity = 0;
    }
    imagen.src = "../static/img/" + route;
}

// Add click event listeners to buttons
right.addEventListener("click", function() {
    move('right');
});

left.addEventListener("click", function() {
    move('left');
});

up.addEventListener("click", function() {
    move('up');
});

down.addEventListener("click", function() {
    move('down');
});
