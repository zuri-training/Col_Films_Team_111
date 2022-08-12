const slidesContainer = document.getElementById("slides-container");
const slide = document.querySelector(".slide");
const prevButton = document.getElementById("slide-arrow-prev");
const nextButton = document.getElementById("slide-arrow-next");

const slidesContainer1 = document.getElementById("slides-container1");
const slide1 = document.querySelector(".slide1");
const prevButton1 = document.getElementById("slide-arrow-prev1");
const nextButton1 = document.getElementById("slide-arrow-next1");

let libraryDrop = document.getElementById('libraryDrop')
libraryDrop.addEventListener('click', () => {
    let mobileBar = document.querySelector('.mobileBar')
    mobileBar.classList.toggle('active')
})

let dropdown = document.getElementById("dropdown")
dropdown.addEventListener('click', () => {
    let sideBarHeadingListP = document.querySelectorAll('.sideBarHeadingListP')
    let sideBar = document.querySelector('.sideBar')
    sideBar.classList.toggle('active')
    let moviesSection = document.querySelector('.moviesSection')
    moviesSection.classList.toggle('active')
    sideBarHeadingListP.forEach((item) => {
        item.classList.toggle('active')
    })
})

nextButton.addEventListener("click", () => {
    const slideWidth = slide.clientWidth;
    slidesContainer.scrollLeft += slideWidth;
});
   
prevButton.addEventListener("click", () => {
    const slideWidth = slide.clientWidth;
    slidesContainer.scrollLeft -= slideWidth;
});

nextButton1.addEventListener("click", () => {
    const slideWidth = slide1.clientWidth;
    slidesContainer1.scrollLeft += slideWidth;
});
   
prevButton1.addEventListener("click", () => {
    const slideWidth = slide1.clientWidth;
    slidesContainer1.scrollLeft -= slideWidth;
});