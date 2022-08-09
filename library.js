const slidesContainer = document.getElementById("slides-container");
const slide = document.querySelector(".slide");
const prevButton = document.getElementById("slide-arrow-prev");
const nextButton = document.getElementById("slide-arrow-next");

const slidesContainer1 = document.getElementById("slides-container1");
const slide1 = document.querySelector(".slide1");
const prevButton1 = document.getElementById("slide-arrow-prev1");
const nextButton1 = document.getElementById("slide-arrow-next1");

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