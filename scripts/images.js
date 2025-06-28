const sidebarDiv = document.getElementById("sidebar");
const aboutSectionMainTextDiv = document.getElementById("main-text");
const imagesUl = document.getElementById("images");

function placeImages() {
  let screenWidth = window.innerWidth;

  if (screenWidth <= 768) {
    aboutSectionMainTextDiv.insertBefore(
      imagesUl,
      aboutSectionMainTextDiv.children[2]
    );
  } else {
    sidebarDiv.appendChild(imagesUl);
  }
}

placeImages();

window.addEventListener("resize", placeImages);
