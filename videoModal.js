let dropdown = document.getElementById("dropdown")
dropdown.addEventListener('click', () => {
    let sideBarHeadingListP = document.querySelectorAll('.sideBarHeadingListP')
    let sideBar = document.querySelector('.sideBar')
    sideBar.classList.toggle('active')
    sideBarHeadingListP.forEach((item) => {
        item.classList.toggle('active')
    })
})

let libraryDrop = document.getElementById('libraryDrop')
libraryDrop.addEventListener('click', () => {
    let mobileBar = document.querySelector('.mobileBar')
    mobileBar.classList.toggle('active')
})