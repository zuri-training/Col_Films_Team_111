/* hamburger menu */
let menu = document.getElementById('menu')
let menuBar = document.getElementById('hamburger')
let close = document.getElementById('close-icon')
let menuItems = document.getElementsByClassName('menu-items')

function openNavbar() {
    menu.classList.toggle('active')
}
function closeNavbar() {
    menu.classList.toggle('active')
}

menuBar.addEventListener("click", openNavbar)
close.addEventListener("click", closeNavbar)
