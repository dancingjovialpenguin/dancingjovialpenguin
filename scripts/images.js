const aboutSectionMainTextDiv = document.getElementById("main-text");
const imagesUl = document.getElementById("images");

let screenWidth = window.innerWidth;

if (screenWidth <= 480) {
  aboutSectionMainTextDiv.insertBefore(
    imagesUl,
    aboutSectionMainTextDiv.children[2]
  );
}
