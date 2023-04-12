

document.querySelector('.menu-btn').addEventListener('click', () =>{
    document.querySelector('.nav-menu').classList.toggle('show');
    console.log("CLICK!")
});

var menuItems = document.querySelectorAll('.nav-menu > .iconodesplegable');


ScrollReveal().reveal('.showcase');
ScrollReveal().reveal('.news-cards', { delay: 500});
ScrollReveal().reveal('.cards-banner-one', { delay: 500});
ScrollReveal().reveal('.cards-banner-two', { delay: 500});