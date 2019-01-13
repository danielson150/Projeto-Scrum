$(document).ready(function () {
    // Códigosm pata inicialização dos frameworks
    $('.parallax').parallax();
    $('.slider').slider();
    $('.tabs').tabs();
    $('.tabs-swipe').tabs({
        swipeable: true,
    });
});

function mostrarChat(){
    document.querySelector('.bate-papo').classList.toggle("mostrar-bate-papo");
}