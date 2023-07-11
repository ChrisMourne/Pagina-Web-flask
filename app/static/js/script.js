// SCRIPTS DE LA PÁGINA EN GENERAL

const bar = document.getElementById('bar')
const close = document.getElementById('close')
const nav = document.getElementById('navbar')

if (bar) {
    bar.addEventListener('click', () => {
        nav.classList.add('active');
    })
}

if (close){
    close.addEventListener('click', () => {
        nav.classList.remove('active');
    })
}

// SCRIPTS DE LA PÁGINA DE PRODUCTO

var MainImg = document.getElementById("MainImg");
var smallimg = document.getElementsByClassName("small-img");
var marcaH = document.getElementById("marcaH")
var precioH = document.getElementById("precioH");
var texto = document.getElementById("textoH")

smallimg[0].onclick = function(){
    MainImg.src = smallimg[0].src;
    marcaH.textContent = "RYZEN RX 6600 XT"
    texto.textContent = "Grande 6600";
    precioH.textContent = "400$";
}
smallimg[1].onclick = function(){
    MainImg.src = smallimg[1].src;
    marcaH.textContent = "MSI RTX 3060"
    texto.textContent = "Grande 3060";
    precioH.textContent = "500$";
}
smallimg[2].onclick = function(){
    MainImg.src = smallimg[2].src;
    marcaH.textContent = "GIGABYTE GTX 1660 SUPER"
    texto.textContent = "Grande 1660";
    precioH.textContent = "300$";
}
smallimg[3].onclick = function(){
    MainImg.src = smallimg[3].src;
    marcaH.textContent = "MSI RTX 4080"
    texto.textContent = "Grande 4080";
    precioH.textContent = "800$";
}


