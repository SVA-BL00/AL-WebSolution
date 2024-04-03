let route = 'Scene1.jpg';
let contenedor = document.getElementById("viewer");
let imagen = document.createElement("img");
imagen.src = "../static/img/" + route;
contenedor.appendChild(imagen);

function move(str) {
    console.log(str);
    if (route == 'Scene1.jpg' && str == 'right') {
        route = 'Scene2.jpg';
    }
    if (route == 'Scene2.jpg' && str == 'up') {
        route = 'Scene1.jpg';
    }
    imagen.src = "../static/img/" + route;
}

// Example of triggering the move function when a button is clicked
document.getElementById("nextButton").addEventListener("click", function() {
    move('right');
});

